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

    def apresentar_funcionario(self):
        info_pessoa = super().apresentar()
        return f"{info_pessoa}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}" 
    
f1 = funcionario("Maria Souza", "987.654.321-00", "15/05/1985", 3500.00, "Analista")

class tutor(funcionario):
    def __init__(self, nome, cpf, data_nascimento, salario, cargo, area_atucacao):
        super().__init__(nome, cpf, data_nascimento, salario, cargo)
        self.area_area_atucacao =area_atucacao

    def apresentar_tutor(self):
        info_funcionario = super().apresentar_funcionario()
        return f"{info_funcionario}, Disciplina: {self.area_area_atucacao}"
    
t1 = tutor("Carlos Pereira", "555.666.777-88", "20/10/1980", 4500.00, "Tutor", "Matemática")

print(p1.apresentar())
print(f1.apresentar_funcionario())
print(t1.apresentar_tutor())