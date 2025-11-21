class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

class CalculadoraSalario:
    def calcular_salario_liquido(self, funcionario, descontos):
        salario_liquido = funcionario.salario - descontos
        return salario_liquido

class GeradorRelatorio:
    def gerar_relatorio(self, funcionario):
        return f"Relatório: {funcionario.nome} - {funcionario.cargo} - R$ {funcionario.salario}"

class RepositorioFuncionario:
    def salvar_no_banco(self, funcionario):
        print(f"Salvando {funcionario.nome} no banco de dados...")

# Testando
funcionario = Funcionario("Ana Silva", 5000.0, "Desenvolvedora")
calculadora = CalculadoraSalario()
gerador = GeradorRelatorio()
repositorio = RepositorioFuncionario()

salario_liquido = calculadora.calcular_salario_liquido(funcionario, 500.0)
relatorio = gerador.gerar_relatorio(funcionario)
repositorio.salvar_no_banco(funcionario)

print(f"Salário líquido: R$ {salario_liquido:.2f}")
print(relatorio)