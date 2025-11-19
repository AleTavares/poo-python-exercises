class Veiculo:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 10

    def get_velocidade(self):
        return self.velocidade


class Carro(Veiculo):
    def acelerar(self):
        if self.velocidade + 10 <= 180:
            self.velocidade += 10
        else:
            self.velocidade = 180


class Bicicleta(Veiculo):
    def acelerar(self):
        if self.velocidade + 10 <= 50:
            self.velocidade += 10
        else:
            self.velocidade = 50


class Aviao(Veiculo):
    def acelerar(self):
        if self.velocidade + 10 <= 900:
            self.velocidade += 10
        else:
            self.velocidade = 900


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
