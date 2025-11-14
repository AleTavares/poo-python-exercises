# Exercício 11 - Princípio da Responsabilidade Única (SRP)


# -----------------------------
# Classe 1 - Dados do funcionário
# -----------------------------
class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo


# -----------------------------
# Classe 2 - Cálculos de salário
# -----------------------------
class CalculadoraSalario:
    def calcular_salario_liquido(self, funcionario, descontos):
        return funcionario.salario - descontos


# -----------------------------
# Classe 3 - Geração de relatórios
# -----------------------------
class GeradorRelatorio:
    def gerar_relatorio(self, funcionario):
        return (
            f"Relatório do Funcionário:\n"
            f"Nome: {funcionario.nome}\n"
            f"Cargo: {funcionario.cargo}\n"
            f"Salário Bruto: R$ {funcionario.salario:.2f}"
        )


# -----------------------------
