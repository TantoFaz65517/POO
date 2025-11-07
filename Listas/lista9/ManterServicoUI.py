from Servico import Servico


class ManterServicoUI:
    def __init__(self, dao, ServicoDAO):
        self.__dao = dao

    def menu(self):
        while True:
            print("\n--- Cadastro de Serviços ---")
            print("1 - Cadastrar serviço")
            print("2 - Listar Serviços")
            print("3 - Remover Servico")
            print("0 - Voltar")
            opc = input("Escolha: ")

            if opc == "1":
                self.cadastrar_servico()
            elif opc == "2":
                self.listar_servicos()
            elif opc == "3":
                self.remover_servico()
            elif opc == "0":
                break
            else:
                print("Opcão Inválida.")
    
    def cadastrar_servico(self):
        codigo = int(input("codigo do serviço: "))
        descricao = input("descrição: ")
        preco = float(input("preço: R$ "))
        servico = Servico(codigo, descricao, preco)
        self.__dao.adicionar(servico)
        print("✅ Serviço cadastrado com sucesso!")

    def listar_servicos(self):
        print("\nServiços cadastrados:")
        for s in self.__dao.listar():
            print(s)

    def remover_servico(self):
        codigo = int(input("codigo do servico a remover: "))
        if self.__dao.remover(codigo):
            print("serviço removido.")
        else:
            print("servico não encontrado.")