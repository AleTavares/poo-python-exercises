
class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(float(nota))

    def calcular_media(self):
        if not self.notas:
            return 0.0
        return round(sum(self.notas) / len(self.notas), 2)

    def status(self):
        media = self.calcular_media()
        print("Aprovado" if media >= 7.0 else "Reprovado")
