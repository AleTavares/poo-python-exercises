class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def apresentar(self):
       return f"Olá, meu nome é {self.nome}, meu CPF é {self.cpf}"


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, cargo):
        super().__init__(nome, cpf, data_nascimento)
        self.cargo = cargo


class Tutor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, atuacao):
        super().__init__(nome, cpf, data_nascimento)
        self.atuacao = atuacao

    def apresentar(self):
        super().apresentar()
        return f"Olá, meu nome é {self.nome}, meu CPF é {self.cpf} e sou tutor na área de {self.atuacao}."

# Testando as classes com polimorfismo

f1 = Funcionario("João Silva", "123.456.789-00", "01/01/1990", "Secretário")
t1 = Tutor("Maria Santos", "987.654.321-00", "15/05/1985", "Programação")

print(f1.apresentar())
print(t1.apresentar())
        