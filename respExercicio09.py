class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self._cpf = None

    def apresentar(self):
        return f"Olá, sou {self.nome}"


class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nota):
        try:
            n = float(nota)
        except (TypeError, ValueError):
            return
        if 0 <= n <= 10:
            self.notas.append(n)

    def calcular_media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)


class Professor(Pessoa):
    def __init__(self, nome, idade, departamento, salario):
        super().__init__(nome, idade)
        self.departamento = departamento
        self.salario = float(salario)

    def apresentar(self):
        return f"Olá, sou o professor {self.nome} do departamento {self.departamento}"