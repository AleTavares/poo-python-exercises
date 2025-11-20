from abc import ABC, abstractmethod

class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular_frete(self, peso, distancia): pass

class FreteNormal(EstrategiaFrete):
    def calcular_frete(self, peso, distancia):
        return 5.00 + (peso * 2.0) + (distancia * 0.1)

class FreteExpresso(EstrategiaFrete):
    def calcular_frete(self, peso, distancia):
        return 15.00 + (peso * 3.0) + (distancia * 0.2)

class FreteEconomico(EstrategiaFrete):
    def calcular_frete(self, peso, distancia):
        return 2.00 + (peso * 1.0) + (distancia * 0.05)

class CalculadoraFrete:
    def __init__(self, estrategia: EstrategiaFrete):
        self.estrategia = estrategia

    def definir_estrategia(self, estrategia: EstrategiaFrete):
        self.estrategia = estrategia

    def calcular(self, peso, distancia):
        return self.estrategia.calcular_frete(peso, distancia)

peso = 10.0
distancia = 100.0

calculadora = CalculadoraFrete(FreteNormal())
print(f"Frete Normal: R$ {calculadora.calcular(peso, distancia)}")

calculadora.definir_estrategia(FreteExpresso())
print(f"Frete Expresso: R$ {calculadora.calcular(peso, distancia)}")

calculadora.definir_estrategia(FreteEconomico())
print(f"Frete Econômico: R$ {calculadora.calcular(peso, distancia)}")