from datetime import datetime
class paciente:
    def __init__(self, nome: str, cpf: str, telefone: str, nascimento: datetime):
        self.__nome = nome 
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento #datetime

    def set_nome(self):
        return self.__nome
    
    def set_cpf(self):
        return self.__cpf

    def set_telefone(self):
        return self.__telefone

    def set_nascimento(self):
        return self.__nascimento
    
    def get_nome(self, nome: str):
        self.__nome = nome

    def get_cpf(self, cpf: str):
        self.__cpf = cpf

    def get_telefone(self, telefone: str):
        self.__telefone = telefone

    def get_nascimento(self, nascimento: str):
        self.__nascimento = nascimento


    def Idade(self) -> str:
        hoje = datetime.today()
        anos = hoje.year - self.__nascimento.year
        mese = hoje.month - self.__nascimento.month
        if idade == mese < 0:
            anos-= 1
            meses += 12
        return f"{anos} anos e {meses} meses"
        
    def __str__(self) -> str:
        return (f"Paciente: {self.__nome}, CPF: {self.__cpf}, "
            f"Telefone: {self.__telefone} \n, Idade: {self.idade('%d/%m/%Y')}")
    