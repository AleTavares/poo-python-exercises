class Aluno:
    def __init__(self, nome, matricula, curso, notas):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, notas):
        self.notas.append(float(notas))

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def status(self):
        """Imprime o status do aluno com base na média."""
        media = self.calcular_media()
        if media >= 7.0:            
            print(f"{self.nome} está Aprovado com média {media:.2f}.")
        else:
            print(f"{self.nome} está Reprovado com média {media:.2f}.")


eu_aluno = Aluno("Felipe", 3225014, "ADS", 0)

class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
minha_disciplina = Disciplina("ADS", 134, "4 horas")

eu_aluno.adicionar_nota(8.0)
eu_aluno.adicionar_nota(6.5)
eu_aluno.adicionar_nota(9.0)


print(f"O nome do aluno é {eu_aluno.nome} e sua matrícula é {eu_aluno.matricula}")
print(f"A Disciplina é {minha_disciplina.nome} e sua carga horária é {minha_disciplina.carga_horaria}")

eu_aluno.status()