from abc import ABC, abstractmethod


class EstrategiaFrete(ABC):
    """
    Interface comum para todas as estratégias de cálculo de frete.
    """
    @abstractmethod
    def calcular_frete(self, peso: float, distancia: float) -> float:
        pass



class FreteNormal(EstrategiaFrete):
    """
    Estratégia 1: Frete normal.
    Fórmula: R$ 5.00 + (peso * 2.0) + (distancia * 0.1)
    """
    def calcular_frete(self, peso: float, distancia: float) -> float:
        return 5.00 + (peso * 2.0) + (distancia * 0.1)

class FreteExpresso(EstrategiaFrete):
    """
    Estratégia 2: Frete expresso (mais caro, mais rápido).
    Fórmula: R$ 15.00 + (peso * 3.0) + (distancia * 0.2)
    """
    def calcular_frete(self, peso: float, distancia: float) -> float:
        return 15.00 + (peso * 3.0) + (distancia * 0.2)

class FreteEconomico(EstrategiaFrete):
    """
    Estratégia 3: Frete econômico (mais barato, mais lento).
    Fórmula: R$ 2.00 + (peso * 1.0) + (distancia * 0.05)
    """
    def calcular_frete(self, peso: float, distancia: float) -> float:
        return 2.00 + (peso * 1.0) + (distancia * 0.05)


class CalculadoraFrete:
    """
    O Contexto que usa a estratégia atual para calcular o frete.
    """
    def __init__(self, estrategia: EstrategiaFrete):
        self._estrategia = estrategia
    
    def definir_estrategia(self, nova_estrategia: EstrategiaFrete):
        """Permite trocar a estratégia em tempo de execução."""
        self._estrategia = nova_estrategia
    
    def calcular(self, peso: float, distancia: float) -> float:
        """
        Executa o cálculo usando a estratégia configurada (delegação).
        """
        custo = self._estrategia.calcular_frete(peso, distancia)
        
        # Apenas para visualização no console
        nome_estrategia = type(self._estrategia).__name__
        print(f"{nome_estrategia}: R$ {custo:.1f}")
        
        return custo


if __name__ == "__main__":
    peso = 10.0      # kg
    distancia = 100.0  # km

    print("--- Padrão Strategy: Cálculo de Frete ---")
    

    calculadora = CalculadoraFrete(FreteNormal())
    calculadora.calcular(peso, distancia)

    
    calculadora.definir_estrategia(FreteExpresso())
    calculadora.calcular(peso, distancia)

 
    calculadora.definir_estrategia(FreteEconomico())
    calculadora.calcular(peso, distancia)