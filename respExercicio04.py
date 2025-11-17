class Pessoa:
    def __init__(self, nome, CPF, data_nascimento):
        self.nome = nome
        self.CPF = CPF
        self.data_nascimento = data_nascimento

    def apresentar(self):
        return f"Nome: {self.nome}, CPF: {self.CPF}"
    
class Funcionario(Pessoa):
    def __init__(self, nome, CPF, data_nascimento, cargo):
        super().__init__(nome, CPF, data_nascimento)
        self.cargo = cargo

    def apresentar(self):
        return f"Nome: {self.nome}, CPF: {self.CPF}"

    
class Tutor(Pessoa):
    def __init__(self, nome, CPF, data_nascimento, area_atuacao):
        super().__init__(nome, CPF, data_nascimento)
        self.area_atuacao = area_atuacao

    def apresentar(self):
            return (f" Área de Atuação: {self.area_atuacao}")