class Pessoa:  # Erro 1 - OK
    def __init__(self, nome, idade):
        self.nome = nome  # Erro 2 - OK
        self.idade = idade
        self.__cpf = cpf  # Erro 3 - OK
    
    def apresentar():  # Erro 4
        return f"Olá, sou {self.nome}"

class Estudante(Pessoa):
        super().__init__(nome, idade, curso) # Erro 5 - OK
        self.notas = []
    
    def adicionar_nota(self, notas):
        if nota >= 0 and nota <= 10:
            self.notas.append(nota)
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)  # Erro 6 - 

class Professor(Pessoa):
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