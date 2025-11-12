class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def apresentar(self):
        return f"Olá, sou o aluno {self.nome} e estudo no curso {self.curso}."


class Professor:
    def __init__(self, nome, departamento, salario):
        self.nome = nome
        self.departamento = departamento
        self.salario = salario

    def apresentar(self):
        return f"Olá, sou o professor {self.nome} e leciono no departamento {self.departamento}."


class Funcionario:
    def __init__(self, nome, cpf, data_nascimento, cargo, salario):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.cargo = cargo
        self.salario = salario

    def apresentar(self):
        return f"Olá, sou o funcionário {self.nome} e meu cargo é {self.cargo}."
