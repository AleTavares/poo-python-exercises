class Aluno:
  def __init__(self, nome, matricula, curso):
    self.nome = nome
    self.matricula = matricula
    self.curso = curso
    self.notas = []

  def adicionar_nota(self, notas):
    self.notas.append(notas)

  def calcular_media(self, media, notas):
    self.notas = notas
    self.media = media
    if len(self.notas):
      media = notas
      return 0
    else: 
      media = notas
      return sum(self.notas) / len(self.notas)
  
  def status(self, notas):
