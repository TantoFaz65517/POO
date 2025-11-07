class IndexUI:
    def __init__
        self.__view = View()

    def menu(self):

    while True:
        print("\n--- Sistema de Agendamento ---")
        print("1 - Manter Clientes")
        print("2 - Manter Serviços")
        print("0 - Sair")
        opc = input("Escolha: ")

        if opc == "1":
                self.__view.manter_clientes()
        elif opc == "2":
            self.__view.manter_servicos()
        elif opc == "0":
            break
        else:
            print("Opção inválida.")