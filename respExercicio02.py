class Aluno:
    def __init__(self, nome, matricula, curso, notas):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = notas if notas is not None else[]

    def adicionar_nota(self, nota):
        self.notas.append(nota)
    
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0.0
        return sum(self.notas) / len(self.notas)
    
    def status(self):
        media = self.calcular_media()
        if media >= 7.0:
            print("Aprovado")
        else:
            print("Reprovado")

aluno = Aluno("João Silva", "2023001", "Engenharia de Software")
aluno.adicionar_nota(8.5)
aluno.adicionar_nota(7.0)
aluno.adicionar_nota(9.2)

print(f"Média: {aluno.calcular_media()}")
aluno.status()
 