from abc import ABC
from abc import abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

    @abstractmethod
    def get_velocidade(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 10
        if self.velocidade < 0:
            self.velocidade = 0

    def get_velocidade(self):
        return self.velocidade

class Bicicleta(Veiculo):
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 5

    def frear(self):
        self.velocidade -= 5
        if self.velocidade < 0:
            self.velocidade = 0

    def get_velocidade(self):
        return self.velocidade

class Aviao(Veiculo):
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 50

    def frear(self):
        self.velocidade -= 50
        if self.velocidade < 0:
            self.velocidade = 0

    def get_velocidade(self):
        return self.velocidade


def testar_veiculo(veiculo):
    print(f"Testando {type(veiculo).__name__}")
    veiculo.acelerar()
    veiculo.acelerar()
    print(f"Velocidade: {veiculo.get_velocidade()} km/h")
    veiculo.frear()
    print(f"Velocidade após frear: {veiculo.get_velocidade()} km/h")

# Todos os veículos devem funcionar da mesma forma
carro = Carro()
bicicleta = Bicicleta()
aviao = Aviao()

testar_veiculo(carro)
testar_veiculo(bicicleta)
testar_veiculo(aviao)