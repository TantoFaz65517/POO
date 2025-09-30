class Servico:
    def __init__(self, id, descricao: str, valor):
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor
    
    def get_id(self, id):
        self.__id = id

    def get_descricao(self, descricao: str):
        self.__descricao = descricao

    def get_valor(self, valor):
        self.__valor = valor

    def set_id(self):
        return self.__id
    
    def set_descricao(self):
        return self.__descricao
    
    def set_valor(self):
        return self.__valor
    
    def __str__(self):
        return f"identificação {self.__id} \n descrição {self.__descricao} \n valor {self.__valor}"
    
    def to_json(self):
        dic = {"id":self.__id, "descricao":self.__descricao, "fone":self.__valor}
        return dic
    
    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descricao"], dic["valor"])