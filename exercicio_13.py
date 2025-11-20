class Veiculo:
    def __init__(self):
        self._velocidade = 0

    def acelerar(self):
        self._velocidade += 10

    def frear(self):
        self._velocidade -= 10
        if self._velocidade < 0:
            self._velocidade = 0

    def get_velocidade(self):
        return self._velocidade

class Carro(Veiculo):
    def acelerar(self):
        if self._velocidade < 180:
            self._velocidade += 20

class Bicicleta(Veiculo):
    def acelerar(self):
        if self._velocidade < 50:
            self._velocidade += 5

class Aviao(Veiculo):
    def acelerar(self):
        if self._velocidade < 900:
            self._velocidade += 50

def testar_veiculo(veiculo):
    print(f"Testando {type(veiculo).__name__}")
    veiculo.acelerar()
    veiculo.acelerar()
    print(f"Velocidade: {veiculo.get_velocidade()} km/h")
    veiculo.frear()
    print(f"Velocidade após frear: {veiculo.get_velocidade()} km/h")

carro = Carro()
bicicleta = Bicicleta()
aviao = Aviao()

testar_veiculo(carro)
testar_veiculo(bicicleta)
testar_veiculo(aviao)