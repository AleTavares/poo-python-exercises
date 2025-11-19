class EstrategiaFrete:
    def calcular_frete(self, peso, distancia):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

class FreteNormal(EstrategiaFrete):
    def calcular_frete(self, peso, distancia):
        return (peso * 2) + (distancia * 0.1)  + 5 # Exemplo de cálculo para frete normal
    
class FreteExpresso(EstrategiaFrete):
    def calcular_frete(self, peso, distancia):
        return (peso * 3) + (distancia * 0.2) + 15 # Exemplo de cálculo para frete expresso
  
class FreteEconomico(EstrategiaFrete):
    def calcular_frete(self, peso, distancia):
        return (peso * 1.0) + (distancia * 0.05) + 2  # Exemplo de cálculo para frete econômico
  
class CalculadoraFrete:
    def __init__(self, estrategia: EstrategiaFrete):
        self.estrategia = estrategia
      
    def definir_estrategia(self, estrategia: EstrategiaFrete):
        self.estrategia = estrategia

    def calcular(self, peso, distancia):
        return self.estrategia.calcular_frete(peso, distancia)
  
# Exemplo de uso
if __name__ == "__main__":
    peso = 10  # em kg
    distancia = 100  # em km

    calculadora = CalculadoraFrete(FreteNormal())
    print("Frete Normal: R$ ", calculadora.calcular(peso, distancia))

    calculadora.definir_estrategia(FreteExpresso())
    print("Frete Expresso: R$ ", calculadora.calcular(peso, distancia))

    calculadora.definir_estrategia(FreteEconomico())
    print("Frete Econômico: R$ ", calculadora.calcular(peso, distancia))