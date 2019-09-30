import ast
import os
import time

class ReconhecedorMVC:
    tree = None
    classList = []
    mapClassCalls = {}
    mapCallMethods = {}


    def menu(self, archive):
        with open(archive, "r") as analisedCode:
            self.tree = ast.parse(analisedCode.read())
            self.recognizeMVC()

    def recognizeMVC(self):
        self.listClasses(self.tree)
        for Class in self.classList:
            self.mapMethods(Class)
        self.mapCalls()
        hasView, nameView = self.recognizeView()
        if hasView:
            hasController, nameController = self.recognizeModel(nameView)
            print("Classe View implementada pela classe:" + nameView)
            print("Classe Controller implementada pela classe: " + nameController)


    def listClasses(self, tree):
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                self.classList.append(node)
    
    def mapMethods(self, Class):
        className = Class.name
        for method in Class.body:
            if isinstance(method, ast.FunctionDef):
                if className not in self.mapClassCalls:
                    self.mapClassCalls[className] = [method.name]
                else:
                    self.mapClassCalls[className].append(method.name)
    
    def mapCalls(self):
        for node in self.classList:
            for method in node.body:
                if isinstance(method, ast.FunctionDef):
                    for calls in method.body:
                        try:
                            methodName = calls.value.func.attr
                            local, className = self.verifyExternal(methodName, node.name)
                            if not local:
                                if className not in self.mapCallMethods:
                                    self.mapCallMethods[node.name] = [className]
                                else:
                                    self.mapCallMethods[node.name].append(className)
                        except:
                            continue
        if node.name not in self.mapCallMethods:
            self.mapCallMethods[node.name] = ""
    
    def verifyExternal(self, methodName, className):
        if methodName in self.mapClassCalls[className]:
            return True, " "
        else:
            name = " "
            for node in self.mapClassCalls.keys():
                if methodName in self.mapClassCalls[node] and node != className:
                    name = node
            return False, name
    
    def recognizeView(self):
        isView = True
        for className in self.mapCallMethods.keys():
            for calls in self.mapCallMethods.keys():
                if len(self.mapCallMethods[calls]) > 1:
                    if className in self.mapCallMethods[calls]:
                        isView = False
            if isView:
                if self.checkUserInterface(className):
                    return isView, className
        if not isView:
            return isView, " "
    
    def checkUserInterface(self, viewClass):
        for className in self.classList:
            if viewClass == className.name:
                for element in className.body:
                    if isinstance(element, ast.FunctionDef):
                        for info in element.body:
                            try:
                                if info.value.func.id == "input":
                                    return True
                            except:
                                continue
        return False
    
    def recognizeModel(self, nameView):
        for className in self.mapClassCalls[nameView]:
            if nameView not in self.mapClassCalls[className]:
                for model in self.mapClassCalls[className]:
                    if len(self.mapClassCalls[model]) == 0:
                        print("Classe Model implementada pela classe: " + model)
                        return True, className
        return False, " "
    
    def recognizeController(self):
        pass

main = ReconhecedorMVC()
archive = input()
main.menu(archive)

