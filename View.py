import os

class View:
    def menu(self):
        os.system('clear')
        print("Calculadora v.1!")
        print("Escolha sua operação: ")
        print("     1 - Adição")
        print("     2 - Subtração")    
        print("     3 - Multiplicação")
        print("     0 - Sair")
        aux = input()
        return aux
    
    def getValues(self):
        print("Digite os valores a serem calculados: ")
        first = input()
        second = input()
        return first, second
    
    def showResults(self, result):
        if(result == 'notvalid'):
            print("Valor invalido")
        else:
            print("O valor calculado foi:" + result)
    
    def closeProgram(self):
        print("Finalizando programa.")