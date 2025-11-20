class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

class CalculadoraSalario:
  def calcular_salario_liquido(self, funcionario, descontos):
        return funcionario.salario - descontos
  
class GeradorRelatorio:
    def gerar_relatorio(self, funcionario):
        return f"Relatório: {funcionario.nome} - {funcionario.cargo} - R$ {funcionario.salario}"
    
class Repositoriofuncionario:
    def salvar(self, funcionario):
        print(f"Salvando {funcionario.nome} no banco de dados...")

calculadora = CalculadoraSalario()
gerador = GeradorRelatorio()
calculadora = CalculadoraSalario()
gerador = GeradorRelatorio()
repositorio = Repositoriofuncionario()

funcionario = Funcionario("Ana Silva", 5000, "Desenvolvedor")

salario_liquido = calculadora.calcular_salario_liquido(funcionario, 500)
relatorio = gerador.gerar_relatorio(funcionario)
repositorio.salvar(funcionario)
print(relatorio)