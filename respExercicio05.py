class Pessoa:
  def __init__(self, nome, cpf, data_nascimento):
    self.nome = nome
    self.cpf = cpf
    self.data_nascimento = data_nascimento
  
  def apresentar(self):
    return f"Olá, meu nome é {self.nome}."
  

class Funcionario(Pessoa):
  def __init__(self, nome, cpf, data_nascimento, cargo, salario):
    super().__init__(nome, cpf, data_nascimento)
    self.cargo = cargo
    self.salario = salario
  def exibir_dados(self):
    return f"=== Dados do Funcionário === Nome: Ana Costa CPF: 111.222.333-44 Data de Nascimento: 20/03/1988 Cargo: Coordenadora Salário: R$ 4500.0```."