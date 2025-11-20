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
    

funcionario = Funcionario("João Silva", "123.456.789-00", "01/01/1990", "Secretário")
tutor = Tutor("Maria Santos", "987.654.321-00", "15/05/1985", "Programação")

print(funcionario.apresentar())
print(tutor.apresentar())
    

    