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
    def __init__(self, calculadora):
        self.calculadora = calculadora
        
    def processar(self, valor):
        valor_final = self.calculadora.calcular(valor)
        return valor_final
    
pagamento1 = ProcessadorPagamento(DescontoEstudante())
print(pagamento1.processar(100))   # 90.0

pagamento2 = ProcessadorPagamento(DescontoFuncionario())
print(pagamento2.processar(100))   # 85.0

pagamento3 = ProcessadorPagamento(DescontoVIP())
print(pagamento3.processar(100))   # 80.0