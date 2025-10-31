class ServicoDAO:
    def __init__(self,):
        self.__servicos = []
    
    def adicionar(self, Servico: Servico):
        self.__servicos.append(servico)

    def listar(self)
    return self.__servicos

    def buscar_por_codigo(self, codigo: int):
        for s in self.__servicos:
            s.get_codigo() == codigo:
            return s
        return None

    def remover(self, codigo: int):
        servico = self.buscar_por_codigo(codigo)
        if servico:
            self.__servicos.remove(servico)
            return True
        return False
