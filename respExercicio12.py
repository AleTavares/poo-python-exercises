from abc import ABC, abstractmethod

class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.9

class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.85

class DescontoVIP(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.8

class ProcessadorPagamento:
    def __init__(self, calculador_desconto: CalculadorDesconto):
        self.calculador_desconto = calculador_desconto

    def processar_pagamento(self, valor):
        return self.calculador_desconto.calcular(valor)

class DescontoPromocional(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.75

# Exemplo de uso
desconto_estudante = DescontoEstudante()
processador = ProcessadorPagamento(desconto_estudante)
print(processador.processar_pagamento(100)) 

desconto_promocional = DescontoPromocional()
processador = ProcessadorPagamento(desconto_promocional)
print(processador.processar_pagamento(100)) 