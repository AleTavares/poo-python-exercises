from abc import ABC, abstractmethod

class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular_frete(self, peso, distancia):
        pass

class FreteNormal(EstrategiaFrete):
    def calcular_frete(self, peso, distancia):
        return peso * 2.0 + distancia * 0.1
    
class FreteExpressogit(EstrategiaFrete):
    def calcular_frete(self, peso, distancia):
        return peso * 3.0 + distancia * 0.2

class FreteEconomico(EstrategiaFrete):
    def calcular_frete(self, peso, distancia):
        return peso * 1.0 + distancia * 0.5

class CalculadoraFrete:
    def __init__(self, frete: EstrategiaFrete):
        self.frete = frete

    def calcular(self, peso, distancia):
        return self.frete.calcular_frete(peso, distancia)

    def definir_estrategia(self, nova_estrategia: EstrategiaFrete):
        self.frete = nova_estrategia


peso = 10.0  # kg
distancia = 100.0  # km

calculadora = CalculadoraFrete(FreteNormal())
print(f"Frete Normal: R$ {calculadora.calcular(peso, distancia)}")

calculadora.definir_estrategia(FreteExpresso())
print(f"Frete Expresso: R$ {calculadora.calcular(peso, distancia)}")

calculadora.definir_estrategia(FreteEconomico())
print(f"Frete Econômico: R$ {calculadora.calcular(peso, distancia)}")
