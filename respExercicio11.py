# 1. Classe Funcionario (Dados do Funcionário)
class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    def get_cargo(self):
        return self.cargo

# 2. Classe CalculadoraSalario (Cálculo de Salário Líquido)
class CalculadoraSalario:
    @staticmethod
    def calcular_salario_liquido(funcionario, descontos):
        return funcionario.get_salario() - descontos

# 3. Classe GeradorRelatorio (Geração de Relatórios)
class GeradorRelatorio:
    @staticmethod
    def gerar_relatorio(funcionario):
        return f"Relatório: {funcionario.get_nome()} - {funcionario.get_cargo()} - R$ {funcionario.get_salario()}"

# 4. Classe RepositorioFuncionario (Persistência de Dados)
class RepositorioFuncionario:
    @staticmethod
    def salvar_no_banco(funcionario):
        print(f"Salvando {funcionario.get_nome()} no banco de dados...")