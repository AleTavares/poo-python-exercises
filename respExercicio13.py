from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, aceleracao_passo: int, desaceleracao_passo: int, max_velocidade: int):
        self._velocidade = 0
        self._aceleracao_passo = aceleracao_passo
        self._desaceleracao_passo = desaceleracao_passo
        self._max_velocidade = max_velocidade

    def acelerar(self):
        """Aumenta a velocidade dentro do limite máximo do veículo."""
        self._velocidade = min(self._velocidade + self._aceleracao_passo, self._max_velocidade)

    def frear(self):
        """Diminui a velocidade, garantindo que não seja negativa."""
        self._velocidade = max(self._velocidade - self._desaceleracao_passo, 0)

    def get_velocidade(self):
        """Retorna a velocidade atual."""
        return self._velocidade



class Carro(Veiculo):

    def __init__(self):
        super().__init__(aceleracao_passo=20, desaceleracao_passo=20, max_velocidade=180)

class Bicicleta(Veiculo):
   
    def __init__(self):
        super().__init__(aceleracao_passo=10, desaceleracao_passo=10, max_velocidade=50)

class Aviao(Veiculo):
   
    def __init__(self):
        super().__init__(aceleracao_passo=100, desaceleracao_passo=50, max_velocidade=900)
    
    
    def decolar(self):
        print("Aeronave decolando...")


def controlador_trafego(veiculo: Veiculo):
    """
    Função que usa qualquer objeto Veiculo sem saber seu tipo específico.
    Isso é possível graças ao LSP.
    """
    print(f"\nTeste do Controlador: {type(veiculo).__name__}")
    
    veiculo.acelerar()
    veiculo.acelerar()
    
    print(f"Velocidade após 2x Acelerar: {veiculo.get_velocidade()} km/h")
    
    veiculo.frear()
    
    print(f"Velocidade após 1x Frear: {veiculo.get_velocidade()} km/h")
    
  
    if isinstance(veiculo, Aviao):
        veiculo.decolar()


if __name__ == "__main__":
    
    carro = Carro()
    bicicleta = Bicicleta()
    aviao = Aviao()

    controlador_trafego(carro)
    controlador_trafego(bicicleta)
    controlador_trafego(aviao)