class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

aluno1 = Aluno("Pedro", "6325", "ADS")

disciplina1 =Disciplina("Matematica", "MATH101", 120)
  