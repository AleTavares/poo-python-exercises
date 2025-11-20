class pessoa (): 
    def __init__(self, nome, idade, cpf):
        self.nome = nome 
        self.idade = idade
        self.cpf = cpf
    
    def apresentar(self): 
        return f"Olá, sou {self.nome}"
    
class estudante(pessoa):
    def __init__(self, nome, idade, curso,cpf):
        super().__init__(nome, idade, cpf) 
        self.curso = curso
        self.notas = []
        
    
    def adicionar_nota(self, nota):
        if nota >= 0 and nota <= 10:
            self.notas.append(nota)
    
    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)  

class professor(pessoa):
    def __init__(self, nome, idade, departamento, salario,cpf):
        super().__init__(nome, idade,cpf)
        self.departamento = departamento
        self.salario = salario
    
    def apresentar(self):
        return f"Olá, sou o professor {self.nome} do departamento {self.departamento}"

estudante = estudante("João", 20, "123.456.789-00", "Engenharia")
professor = professor("Dr. Silva", 45, "987.654.321-00", "Computação", 8000)

print(estudante.apresentar())
print(professor.apresentar())
print(f"Média do estudante: {estudante.calcular_media()}")