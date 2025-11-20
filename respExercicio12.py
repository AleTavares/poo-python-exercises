from abc import ABC, abstractmethod

# 1. Classe abstrata CalculadorDesconto
class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass

# 2. Implementação de diferentes tipos de desconto
class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.10  # 10% de desconto

class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.15  # 15% de desconto

class DescontoVIP(CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.20  # 20% de desconto

# 3. Classe ProcessadorPagamento
class ProcessadorPagamento:
    def processar(self, valor_original: float, desconto: CalculadorDesconto) -> float:
        valor_desconto = desconto.calcular(valor_original)
        return valor_original - valor_desconto