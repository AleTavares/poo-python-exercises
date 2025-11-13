class pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def apresentar(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}"
        
p1 = pessoa("João Silva", "123.456.789-00", "01/01/1990")


class funcionario(pessoa):
    def __init__(self, nome, cpf, data_nascimento, salario, cargo):
        super().__init__(nome, cpf, data_nascimento)
        self.salario = salario
        self.cargo = cargo

f1 = funcionario("Maria Souza", "987.654.321-00", "15/05/1985", 5000.00, "Analista de Sistemas")

class exibir_dados():
    print(p1.apresentar())
    print(f"Salário: {f1.salario}, Cargo: {f1.cargo}")
    print(f1.apresentar())
