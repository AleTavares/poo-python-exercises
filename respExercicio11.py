class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        
class CalculadoraSalario:
    def calcular_salario_liquido(self, funcionario:Funcionario, descontos):
        return funcionario.salario - descontos
      
class GeradorRelatorio:
    def gerar_relatorio(self, funcionario:Funcionario):
        return f"Relatório do Funcionário:\nNome: {funcionario.nome}\nCargo: {funcionario.cargo}\nSalário: {funcionario.salario}"
      
class RepositorioFuncionario:
    def salvar(self, funcionario:Funcionario):
        print(f"Funcionário {funcionario.nome} salvo no repositório.")
        
if __name__ == "__main__": 
  funcionario = Funcionario("Ana Silva", 5000.0, "Desenvolvedora")
  calculadora = CalculadoraSalario()
  gerador = GeradorRelatorio()
  repositorio = RepositorioFuncionario()

  salario_liquido = calculadora.calcular_salario_liquido(funcionario, 500.0)
  relatorio = gerador.gerar_relatorio(funcionario)
  repositorio.salvar(funcionario)