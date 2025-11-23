from abc import ABC, abstractmethod


class Desconto(ABC):

    @abstractmethod
    def calcular(self, valor):
        pass


class DescontoEstudante(Desconto):
    def calcular(self, valor):
        return valor * 0.9


class DescontoFuncionario(Desconto):
    def calcular(self, valor):
        return valor * 0.85


class DescontoVIP(Desconto):
    def calcular(self, valor):
        return valor * 0.8   # 80% de desconto


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
