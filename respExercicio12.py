from abc import ABC, abstractmethod


class Desconto(ABC):

    @abstractmethod
    def calcular(self, valor):
        pass


class DescontoEstudante(Desconto):
    def calcular(self, valor):
        return valor * 0.5   # 50% de desconto


class DescontoFuncionario(Desconto):
    def calcular(self, valor):
        return valor * 0.7   # 30% de desconto


class DescontoVIP(Desconto):
    def calcular(self, valor):
        return valor * 0.2   # 80% de desconto


class CalculadorDesconto:
    def __init__(self, desconto: Desconto):
        self.desconto = desconto

    def aplicar(self, valor):
        return self.desconto.calcular(valor)


class ProcessadorPagamento:
    def __init__(self, desconto: Desconto):
        self.desconto = desconto

    def processar(self, valor):
        return valor - self.desconto.calcular(valor)
