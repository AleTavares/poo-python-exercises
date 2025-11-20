class Pessoa:  # Correção do Erro 1
    def __init__(self, nome, idade):
        self.nome = nome  # Correção do Erro 2
        self.idade = idade
        self._cpf = None  # Correção do Erro 3 (encapsulamento adequado)

    def apresentar(self):  # Correção do Erro 4
        return f"Olá, sou {self.nome}"


class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  # Correção do Erro 5
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:  # Correção do Erro 6
            return 0
        return sum(self.notas) / len(self.notas)


class Professor(Pessoa):
    def __init__(self, nome, idade, departamento, salario):
        super().__init__(nome, idade)
        self.departamento = departamento
        self.salario = salario

    def apresentar(self):
        return f"Olá, sou o professor {self.nome} do departamento {self.departamento}"


# Testes
estudante = Estudante("João", 20, "Engenharia")
estudante.adicionar_nota(8)
estudante.adicionar_nota(7)

professor = Professor("Dr. Silva", 45, "Computação", 8000)

print(estudante.apresentar())
print(professor.apresentar())
print(f"Média do estudante: {estudante.calcular_media()}")  # Correção do Erro 7
