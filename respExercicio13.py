# respExercicio13.py
from abc import ABC

class Veiculo(ABC):
    def __init__(self, velocidade_maxima):
        self.velocidade = 0
        self.velocidade_maxima = velocidade_maxima

    def acelerar(self):
        nova_vel = self.velocidade + 20
        self.velocidade = min(nova_vel, self.velocidade_maxima)

    def frear(self):
        nova_vel = self.velocidade - 10
        self.velocidade = max(nova_vel, 0)

    def get_velocidade(self):
        return self.velocidade


class Carro(Veiculo):
    def __init__(self):
        super().__init__(180)


class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__(50)


class Aviao(Veiculo):
    def __init__(self):
        super().__init__(900)


class ControladorTrafego:
    @staticmethod
    def testar_veiculo(veiculo):
        print(f"Testando {type(veiculo).__name__}")
        veiculo.acelerar()
        veiculo.acelerar()
        print(f"Velocidade: {veiculo.get_velocidade()} km/h")
        veiculo.frear()
        print(f"Velocidade após frear: {veiculo.get_velocidade()} km/h")
        print("-" * 30)


# Para permitir rodar diretamente
if __name__ == "__main__":
    carro = Carro()
    bicicleta = Bicicleta()
    aviao = Aviao()

    ControladorTrafego.testar_veiculo(carro)
    ControladorTrafego.testar_veiculo(bicicleta)
    ControladorTrafego.testar_veiculo(aviao)


