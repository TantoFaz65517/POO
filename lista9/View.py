class View:
    def __init__(self):
        self.__servico_dao = ServicoDAO()

    def manter_servicos(self):
        ui = ManterServicoUI(self.__servico_dao)
        ui.menu()