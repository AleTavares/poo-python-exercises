class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, cargo, salario):
        super().__init__(nome, cpf, data_nascimento)  # chama o construtor da classe Pai
        self.cargo = cargo
        self.salario = salario

    def exibir_dados(self):
        print("=== Dados do Funcionário ===")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R$ {self.salario}")