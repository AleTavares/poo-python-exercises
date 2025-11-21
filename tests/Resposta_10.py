class Pessoa:  # Erro 1
    def __init__(self, nome, idade, cpf = None):
        self.nome = nome  # Erro 2
        self.idade = idade
        self.__cpf = cpf # Erro 3
    
    def apresentar(self):  # Erro 4
        return f"Olá, sou {self.nome}"

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade, cpf = None)
        self.curso = curso
        self.notas = []
    
    def adicionar_nota(self, nota):
        if nota >= 0 and nota <= 10:
            self.notas.append(nota)
    
    def calcular_media(self):
        if not self.notas:
            return 0
        media = sum(self.notas) / len(self.notas) 
        return media
        

class Professor(Pessoa):
    def __init__(self, nome, idade, departamento, salario):
        super().__init__(nome, idade, cpf = None)
        self.departamento = departamento
        self.salario = salario
    
    def apresentar(self):
        return f"Olá, sou o professor {self.nome} do departamento {self.departamento}"

# Testando o código
estudante = Estudante("João", 20, "Engenharia")
professor = Professor("Dr. Silva", 45, "Computação", 8000)

print(estudante.apresentar())
print(professor.apresentar())
estudante.adicionar_nota(7.5)
estudante.adicionar_nota(8.0)
estudante.adicionar_nota(9.5)
estudante.adicionar_nota(8.5)
print(f"Média do estudante: {estudante.calcular_media()}")  # Erro 7