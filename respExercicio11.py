class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

class CalculadoraSalario:
    @staticmethod
    def calcular_salario_liquido(funcionario, descontos):
        return funcionario.salario - descontos

class GeradorRelatorio:
    @staticmethod
    def gerar_relatorio(funcionario):
        return f"Relatório: {funcionario.nome} - {funcionario.cargo} - R$ {funcionario.salario}"

class RepositorioFuncionario:
    @staticmethod
    def salvar_no_banco(funcionario):
        print(f"Salvando {funcionario.nome} no banco de dados...")

if __name__ == "__main__":
    funcionario = Funcionario("João", 5000, "Desenvolvedor")

    descontos = 500
    salario_liquido = CalculadoraSalario.calcular_salario_liquido(funcionario, descontos)
    print(f"Salário líquido: R$ {salario_liquido}")

    relatorio = GeradorRelatorio.gerar_relatorio(funcionario)
    print(relatorio)

    RepositorioFuncionario.salvar_no_banco(funcionario)


funcionario = Funcionario("Ana Silva", 5000.0, "Desenvolvedora")
calculadora = CalculadoraSalario()
gerador = GeradorRelatorio()
repositorio = RepositorioFuncionario()

salario_liquido = calculadora.calcular_salario_liquido(funcionario, 500.0)
relatorio = gerador.gerar_relatorio(funcionario)
repositorio.salvar_no_banco(funcionario)