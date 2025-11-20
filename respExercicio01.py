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


aluno1 = Aluno ("Renan", 2525, "Analise de Dados")
aluno2 = Aluno ("Cristiano", 3030, "Ciencias de Dados")

disciplina1 = Disciplina ("TI", 1515, "60 horas")
disciplina2 = Disciplina ("Banco de Dados", 2020, "80 horas")



