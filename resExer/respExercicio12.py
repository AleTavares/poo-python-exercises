from abc import ABC, abstractmethod

class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.90  # 10% de desconto

class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.85  # 15% de desconto

class DescontoVIP(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.80  # 20% de desconto

class ProcessadorPagamento:
    def __init__(self, calculadora_desconto: CalculadorDesconto):
        self.calculadora_desconto = calculadora_desconto
    
    def processar(self, valor):
        return self.calculadora_desconto.calcular(valor)
    
# Exemplo de uso das classes
valor = 1000

processador = ProcessadorPagamento(DescontoEstudante())
print("Estudante paga:", processador.processar(valor))

processador = ProcessadorPagamento(DescontoFuncionario())
print("Funcionário paga:", processador.processar(valor))

processador = ProcessadorPagamento(DescontoVIP())
print("VIP paga:", processador.processar(valor))

# Demonstração 
class DescontoBlackFriday(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.50

processador = ProcessadorPagamento(DescontoBlackFriday())
print("Black Friday:", processador.processar(1000))
