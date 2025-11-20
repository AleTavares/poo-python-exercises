
class EstrategiaFrete:
    def calcular_frete(self, peso, distancia):
        pass

class FreteNormal(EstrategiaFrete):
    def calcular_frete(self, peso, distancia):
        return 5.0 + (peso * 2.0) + (distancia * 0.1)


class FreteExpresso(EstrategiaFrete):
    def calcular_frete(self, peso, distancia):
        return 15.0 + (peso * 3.0) + (distancia * 0.2)


class FreteEconomico(EstrategiaFrete):
    def calcular_frete(self, peso, distancia):
        return 2.0 + (peso * 1.0) + (distancia * 0.05)

class CalculadoraFrete:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def definir_estrategia(self, nova_estrategia):
        self.estrategia = nova_estrategia

    def calcular(self, peso, distancia):
        return self.estrategia.calcular_frete(peso, distancia)



