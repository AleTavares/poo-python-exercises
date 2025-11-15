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
        
aluno1 = Aluno('João Silva', 2023001, 'Engenharia de Software')
aluno1.adicionar_nota(3)
aluno1.adicionar_nota(3)
aluno1.adicionar_nota(3)
media = aluno1.calcular_media()
print(aluno1.media)
aluno1.status()



