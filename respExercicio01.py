class Aluno:
  def __init__(self, nome, matricula, curso):
    self.nome = nome
    self.matricula = matricula
    self.curso = curso
  
  def obter_informacoes(self):
    return f"Aluno: {self.nome}, Matrícula: {self.matricula}, Curso: {self.curso}"

class Disciplina:
  def __init__(self, nome, codigo, carga_horaria):
    self.nome = nome
    self.codigo = codigo
    self.carga_horaria = carga_horaria

  def obter_informacoes(self): 
    return f"Disciplina: {self.nome}, Código: {self.codigo}, Carga Horária: {self.carga_horaria} horas"
    
Aluno1 = Aluno("Luiza", 6325257, "ADS")
Aluno2 = Aluno("Gabriel", 6325256, "Enfermagem")
Disciplina1 = Disciplina("Engenharia de Software", "ADS1", 60)
Disciplina2 = Disciplina("Anatomia Humana", "ENF1", 80)

print(Aluno1.obter_informacoes())
print(Aluno2.obter_informacoes())
print(Disciplina1.obter_informacoes())
print(Disciplina2.obter_informacoes())