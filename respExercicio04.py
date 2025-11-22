class Pessoa:
  def __init__(self, nome, cpf, data_nascimento):
    self.nome = nome
    self.cpf = cpf
    self.data_nascimento = data_nascimento
  
  def apresentar(self):
    return f"Olá, meu nome é {self.nome}."
  

class Funcionario(Pessoa):
  def __init__(self, nome, cpf, data_nascimento, cargo):
    self.nome = nome
    self.cpf = cpf
    self.data_nascimento = data_nascimento
    self.cargo = cargo

  

class Tutor(Pessoa):
  def __init__(self, nome, cpf, data_nascimento, area_atuacao):
    self.nome = nome
    self.cpf = cpf
    self.data_nascimento = data_nascimento
    self.area_atuacao = area_atuacao

  def apresentar(self):
   return f"Olá, meu nome é {self.nome} sou da área de {self.area_atuacao}."

funcionario = Funcionario("João Silva", "123.456.789-00", "01/01/1990", "Secretário")
tutor = Tutor("Maria Santos", "987.654.321-00", "15/05/1985", "Programação")

print(funcionario.apresentar())
print(tutor.apresentar())