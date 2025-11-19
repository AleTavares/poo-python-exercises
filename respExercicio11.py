class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo


class CalculadoraSalario:
    def calcular_salario_liquido(self, funcionario: Funcionario, desconto: float) -> float:
        return funcionario.salario - desconto


class GeradorRelatorio:
    def gerar_relatorio(self, funcionario: Funcionario) -> str:
        calculadora = CalculadoraSalario()
        salario_liquido = calculadora.calcular_salario_liquido(funcionario, 0)

        return (
            f"Relatório:\n"
            f"Nome: {funcionario.nome}\n"
            f"Cargo: {funcionario.cargo}\n"
            f"Salário Base: R$ {funcionario.salario:.2f}\n"
            f"Salário Líquido: R$ {salario_liquido:.2f}"
        )


class Banco:
    def salvar_no_banco(self, funcionario: Funcionario):
        print(f"Salvando {funcionario.nome} no banco de dados...")


class RepositorioFuncionario:
    def salvar(self, funcionario: Funcionario):
        print(f"Salvando {funcionario.nome} no repositório...")
