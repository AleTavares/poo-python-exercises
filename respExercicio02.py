class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(float(nota))

    def calcular_media(self):
        self.media = sum(self.notas) / len(self.notas)
        return self.media

    def status(self):
        if self.media > 7:
            print('aprovado')
        else:
            print('reprovado')

    
aluno = Aluno("João Silva", 2023001, "Engenharia de Software")
aluno.adicionar_nota(2)
aluno.adicionar_nota(3)
aluno.adicionar_nota(4)
media = aluno.calcular_media()
aluno.status()
print(f"Média do aluno {aluno.nome}: {media}")