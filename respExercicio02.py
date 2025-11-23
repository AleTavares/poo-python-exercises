class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def status(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"

alunoTeste = Aluno("Carlos Silva", "2023003", "Matemática")
alunoTeste.adicionar_nota(8)
alunoTeste.adicionar_nota(7)
alunoTeste.adicionar_nota(9)
print(f"Média: {alunoTeste.calcular_media()}")
print(f"Status: {alunoTeste.status()}")






        

    
  
