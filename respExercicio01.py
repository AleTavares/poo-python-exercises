class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

eu_aluno = Aluno("Felipe", 3225014, "ADS")

class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
minha_disciplina = Disciplina("ADS", 134, "4 horas")


print(f"O nome do aluno é {eu_aluno.nome} e sua matrícula é {eu_aluno.matricula}")
print(f"A Disciplina é {minha_disciplina.nome} e sua carga horária é {minha_disciplina.carga_horaria}")