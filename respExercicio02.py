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


aluno1 = Aluno("Maria", "2025001", "Engenharia")

aluno1.adicionar_nota(8.5)
aluno1.adicionar_nota(6.0)
aluno1.adicionar_nota(7.0)

print("Notas:", aluno1.notas)
print("Média:", aluno1.calcular_media())
print("Status:", aluno1.status())