class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def apresentar():
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos!")

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, idade, cargo):
        super().__init__(nome, cpf, idade)
        self.cargo = cargo


class Tutor(Pessoa):
    def __init__(self, nome, cpf, idade, area_atuacao):
        super().__init__(nome, cpf, idade) 
        self.area_atuacao = area_atuacao

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos! Atuo na área de {self.area_atuacao}")

tutor = Tutor("Cleiton", 12345678911, 40, "Automobilismo")

tutor.apresentar()
