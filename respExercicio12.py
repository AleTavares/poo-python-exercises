from abc import ABC, abstractmethod

# Classe Funcionario: Responsável apenas por armazenar os dados do funcionário
class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

# Classe CalculadoraSalario: Responsável pelos cálculos relacionados ao salário
class CalculadoraSalario:
    @staticmethod
    def calcular_salario_liquido(funcionario, descontos):
        return funcionario.salario - descontos

# Classe GeradorRelatorio: Responsável pela geração de relatórios
class GeradorRelatorio:
    @staticmethod
    def gerar_relatorio(funcionario):
        return f"Relatório: {funcionario.nome} - {funcionario.cargo} - R$ {funcionario.salario:.2f}"

# Classe RepositorioFuncionario: Responsável pela persistência de dados
class RepositorioFuncionario:
    @staticmethod
    def salvar(funcionario):
        print(f"Salvando {funcionario.nome} no banco de dados...")

# Classe abstrata para cálculo de descontos
class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        """Método abstrato para calcular o desconto"""
        pass

# Implementação de diferentes tipos de desconto
class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.9  # 10% de desconto

class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.85  # 15% de desconto

# Classe para processar pagamentos com diferentes descontos
class ProcessadorPagamento:
    def processar(self, valor, calculador_desconto):
        return calculador_desconto.calcular(valor)

# Exemplo de Uso
if __name__ == "__main__":
    # Uso do sistema
    pagamento = ProcessadorPagamento()
    valor_original = 1000.0

    # Diferentes tipos de desconto
    desconto_estudante = DescontoEstudante()
    desconto_funcionario = DescontoFuncionario()

    # Processando pagamentos com diferentes descontos
    valor_final1 = pagamento.processar(valor_original, desconto_estudante)
    valor_final2 = pagamento.processar(valor_original, desconto_funcionario)

    # Exibindo os resultados
    print(f"Estudante: R$ {valor_final1:.2f}")
    print(f"Funcionário: R$ {valor_final2:.2f}")