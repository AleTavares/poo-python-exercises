from abc import ABC, abstractmethod

# Classe Abstrata seguindo OCP
class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass


# Implementações dos descontos (abertos para extensão)
class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.90  # 10% de desconto


class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.85  # 15% de desconto


class DescontoVIP(CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.80  # 20% de desconto


# Classe que usa qualquer calculadora de desconto
class ProcessadorPagamento:
    def processar(self, valor: float, calculadora: CalculadorDesconto) -> float:
        return calculadora.calcular(valor)


# Demonstração de uso
if __name__ == "__main__":
    pagamento = ProcessadorPagamento()
    valor_original = 1000.0

    # Tipos de desconto existentes
    desconto_estudante = DescontoEstudante()
    desconto_funcionario = DescontoFuncionario()
    desconto_vip = DescontoVIP()

    print("Estudante:", pagamento.processar(valor_original, desconto_estudante))
    print("Funcionário:", pagamento.processar(valor_original, desconto_funcionario))
    print("VIP:", pagamento.processar(valor_original, desconto_vip))

    # Demonstração de como adicionar novo desconto SEM modificar código existente

    class DescontoNatal(CalculadorDesconto):  # Novo tipo de desconto
        def calcular(self, valor: float) -> float:
            return valor * 0.75  # 25% de desconto

    desconto_natal = DescontoNatal()
    print("Natal:", pagamento.processar(valor_original, desconto_natal))
