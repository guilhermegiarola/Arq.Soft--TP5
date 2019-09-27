import ast
import os
import time

class ReconhecedorMVC:
    tree = None
    modelList = []
    viewList = []
    controllerList = []

    def menu(self):
        op = '0'
        while op != '4':
            os.system('clear')
            print("Reconhecedor MVC v1.0")
            print("     1 - Reconhecer Model")
            print("     2 - Reconhecer View")
            print("     3 - Reconhecer Controller")
            print("     4 - Finalizar Programa")
            op = input()
            if op == '1':
                print("Insira o nome do arquivo: ")
                name = input()
                if self.isModel(name):
                    print("O arquivo " + name + " corresponde à implementação de um Model.")
                    time.sleep(5)
                else:
                    print("O arquivo " + name + " não corresponde à implementação de um Model.")
                    time.sleep(5)
            elif op == '2':
                print("Insira o nome do arquivo: ")
                name = input()
                if self.isView(name):
                    print("O arquivo " + name + " corresponde à implementação de uma View.")
                    time.sleep(5)
                else:
                    print("O arquivo " + name + " não corresponde à implementação de uma View.")
                    time.sleep(5)
            elif op == '3':
                print("Insira o nome do arquivo: ")
                name = input()
                if self.isController(name):
                    print("O arquivo " + name + " corresponde à implementação de um Controller.")
                    time.sleep(5)
                else:
                    print("O arquivo " + name + " não corresponde à implementação de um Controller.")
                    time.sleep(5)
            elif op == '4':
                print("Finalizando programa.")
            else:
                print("Opção inválida.")
                time.sleep(1)

    def isModel(self, archive):
        with open(archive, "r") as analisedCode:
            self.tree = ast.parse(analisedCode.read())
            for node in ast.walk(self.tree):
                if isinstance(node, ast.Name):
                    if node.id == 'print':
                        return False
                elif isinstance(node, ast.ImportFrom):
                        return False
        return True
                
        
    
    def isView(self, archive):
        with open(archive, "r") as analisedCode:
            self.tree = ast.parse(analisedCode.read())
            for node in ast.walk(self.tree):
                    if isinstance(node, ast.Name):
                        if node.id == 'print':
                            return True
        return False
    
    def isController(self, archive):
        with open(archive, "r") as analisedCode:
            self.tree = ast.parse(analisedCode.read())
            for node in ast.walk(self.tree):
                if isinstance(node, ast.ImportFrom):
                    return True
        return False
                

if __name__ == "__main__":
    main = ReconhecedorMVC()
    main.menu()

