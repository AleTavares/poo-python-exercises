# Classe que representa apenas os dados do funcionário
class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo


# Classe responsável somente pelos cálculos relacionados a salário
class CalculadoraSalario:
    def calcular_salario_liquido(self, funcionario, descontos):
        return funcionario.salario - descontos


# Classe responsável apenas por gerar relatórios
class GeradorRelatorio:
    def gerar_relatorio(self, funcionario):
        return f"Relatório: {funcionario.nome} - {funcionario.cargo} - R$ {funcionario.salario}"


# Classe responsável pela persistência (salvar no "banco")
class RepositorioFuncionario:
    def salvar(self, funcionario):
        print(f"Salvando {funcionario.nome} no banco de dados...")


if __name__ == "__main__":
    funcionario = Funcionario("Ana Silva", 5000.0, "Desenvolvedora")

    calculadora = CalculadoraSalario()
    gerador = GeradorRelatorio()
    repositorio = RepositorioFuncionario()

    salario_liquido = calculadora.calcular_salario_liquido(funcionario, 500.0)
    relatorio = gerador.gerar_relatorio(funcionario)

    print("Salário líquido:", salario_liquido)
    print(relatorio)
    repositorio.salvar(funcionario)
