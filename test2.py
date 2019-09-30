class View:

    def __init__(self):
        print("informe o que deseja fazer: ")

    def digitar_opcao(self):
        print("digite o que deseja fazer")
        opcao = input()

    def processa_opcao(self):
        Controller.nome_model()
        Controller.instanciar_n_classes(10)



class Controller:

    def nome_model(self):
        m = Model()
        return m.getName()


    def instanciar_n_classes(qtd_classes):
        for i in range(qtd_classes):
            m = Model()


class Model:

    def __init__(self):
        print("instancia de Model")

    def getName(self):
        return "Model"


class Teste:
    def __init__(self):
        pass


v = View()
v.processa_opcao()