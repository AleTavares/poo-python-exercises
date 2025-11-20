class Pessoa: # pessoa minuscula = Pessoa maiuscula
    def __init__(self, nome, idade):
        self.nome = nome  # pendente self.
        self.idade = idade
        self.cpf = None  # self.cpf = privado, não foi declarado no init, ficando como futuro atributo

    def apresentar(self):  # self):
        return f"Olá, sou {self.nome}"


class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  # nao precisa informar self.nome= nome
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nota):
        if nota >= 0 and nota <= 10:
            self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


class Professor(Pessoa):
    def __init__(self, nome, idade, departamento, salario):
        super().__init__(nome, idade)
        self.departamento = departamento
        self.salario = salario

    def apresentar(self):
        return f"Ola, sou o professor {self.nome} do departamento {self.departamento}"


if __name__ == "__main__":
    estudante = Estudante("Joao", 20, "Engenharia")
    professor = Professor("Dr. Silva", 45, "Computacao", 8000)

print(estudante.apresentar())
print(professor.apresentar())
estudante.adicionar_nota(8)
estudante.adicionar_nota(10)
print(f"Média do estudante: {estudante.calcular_media()}")

print(f"Salário do professor: {professor.salario}")
