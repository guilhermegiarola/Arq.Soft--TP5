from View import View
from Calculator import Calculator
import os
import time

class Controller:
    def ctrlMenu(self):
        op = self.view.menu()

        while op != '0':         
            results = self.operation(op)
            self.view.showResults(str(results))
            time.sleep(2)
            os.system('clear')
            
            op = self.view.menu()
        
        self.view.closeProgram()

    def operation(self, op):
        if op == '1':
            first,second = self.view.getValues()
            return self.model.sum(first, second)
        elif op == '2':
            first,second = self.view.getValues()
            return self.model.subtract(first, second)
        elif op == '3':
            first,second = self.view.getValues()
            return self.model.multiply(first, second)
        else:
            return 'notvalid'
    
    def __init__(self):
        self.model = Calculator()
        self.view = View()
    
if __name__ == "__main__":
    main = Controller()
    main.ctrlMenu()