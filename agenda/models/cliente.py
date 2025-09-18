class Cliente:
    def __init__(self, id, nome, email, fone):
        self.set_ide(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - 
        {self.__fone}"