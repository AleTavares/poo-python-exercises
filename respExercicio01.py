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

    
Aluno1 = Aluno("Luiza", 6325257, "ADS")
Aluno2 = Aluno("Gabriel", 6325256, "Enfermagem")
Disciplina1 = Disciplina("Engenharia de Software", "ADS1", 60)
Disciplina2 = Disciplina("Anatomia Humana", "ENF1", 80)

print(f"Aluno: {Aluno1.nome}, Matrícula: {Aluno1.matricula}, Curso: {Aluno1.curso}")
print(f"Aluno: {Aluno2.nome}, Matrícula: {Aluno2.matricula}, Curso: {Aluno2.curso}")
print(f"Disciplina: {Disciplina1.nome}, Código: {Disciplina1.codigo}, Carga Horária: {Disciplina1.carga_horaria} horas")
print(f"Disciplina: {Disciplina2.nome}, Código: {Disciplina2.codigo}, Carga Horária: {Disciplina2.carga_horaria} horas")