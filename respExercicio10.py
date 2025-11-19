class Pessoa:  # Corrigido Erro 1
    def __init__(self, nome, idade):
        self.nome = nome  # Corrigido Erro 2
        self.idade = idade
    
    def apresentar(self):  # Corrigido Erro 4
        return f"Olá, sou {self.nome}"

class Estudante(Pessoa):  # Corrigido Erro 1
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  # Corrigido Erro 5
        self.curso = curso
        self.notas = []
    
    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
    
    def calcular_media(self):
        if self.notas:  # Corrigido Erro 6
            return sum(self.notas) / len(self.notas)
        return 0.0
class Professor(Pessoa):  # Corrigido Erro 1
    def __init__(self, nome, idade, departamento, salario):
        super().__init__(nome, idade)
        self.departamento = departamento
        self.salario = salario
    
    def apresentar(self):
        return f"Olá, sou o professor {self.nome} do departamento {self.departamento}"

# Testando o código
estudante = Estudante("João", 20, "Engenharia")
professor = Professor("Dr. Silva", 45, "Computação", 8000)

print(estudante.apresentar())
print(professor.apresentar())
print(f"Média do estudante: {estudante.calcular_media()}")  # Erro 7