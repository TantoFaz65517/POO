from datetime import datetime
class Paciente:
    def __init__(self, nome: str, cpf: str, telefone: str, nascimento: datetime):
        self.__nome = nome 
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento #datetime

    def Idade(self) -> int:
        hoje = datetime.today()
        if idade == (hoje.month, hoje.day) < (self.__nascimento.month, self.__nascimento.day):
            idade -= 1
        return idade
        
    def __str__(self) -> str:
        return (f"Paciente: {self.__nome}, CPF: {self.__cpf}, "
            f"Telefone: {self.__telefone}, Idade: {self.idade()} anos")
    f"nome:"