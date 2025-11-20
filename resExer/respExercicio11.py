class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

class CalculadoraSalario:
    def calcular_salario_liquido(self, salario, descontos):
        return salario - descontos

class GeradorRelatorio:
    def gerar(self, funcionario):
        return f"Relatório: {funcionario.nome} - {funcionario.cargo} - R$ {funcionario.salario}"

class RepositorioFuncionario:
    def salvar(self, funcionario):
        print(f"Salvando {funcionario.nome} no banco de dados...")

# Exemplo de uso das classes
func = Funcionario("João", 5000, "Desenvolvedor")

calc = CalculadoraSalario()
salario_liquido = calc.calcular_salario_liquido(func.salario, descontos=800)
print("Salário líquido:", salario_liquido)

relatorio = GeradorRelatorio()
print(relatorio.gerar(func))

repo = RepositorioFuncionario()
repo.salvar(func)