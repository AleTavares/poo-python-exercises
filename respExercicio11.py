class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

class CalculadoraSalario:
    def calcular_salario_liquido(self, funcionario, descontos):
        return funcionario.salario - descontos
    
class GeradorRelatorio:
    def gerar(self, funcionario):
        return f"Relatório: {funcionario.nome} - {funcionario.cargo} - R$ {funcionario.salario}"
    
class RepositorioFuncionario:
    def salvar(self, funcionario):
        print(f"Salvando {funcionario.nome} no banco de dados...")

# Criando um funcionário
func = Funcionario("Maria", 5000, "Engenheira de Software")

# Calculando salário
calc = CalculadoraSalario()
salario_liquido = calc.calcular_salario_liquido(func, descontos=500)

# Gerando relatório
relatorio = GeradorRelatorio().gerar(func)

# Salvando funcionário
repo = RepositorioFuncionario()
repo.salvar(func)

print("Salário líquido:", salario_liquido)
print(relatorio)