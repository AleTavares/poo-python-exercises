# SOLID - Liskov Substitution Principle (LSP)

# SOLID - Liskov Substitution Principle (LSP)

class Veiculo:
    def __init__(self, velocidade_maxima):
        self.velocidade = 0
        self.velocidade_maxima = velocidade_maxima

    def acelerar(self):
        if self.velocidade + 20 <= self.velocidade_maxima:
            self.velocidade += 20

    def frear(self):
        if self.velocidade - 10 >= 0:
            self.velocidade -= 10

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
    def testar_veiculo(self, veiculo):
        print(f"Testando {type(veiculo).__name__}")
        veiculo.acelerar()
        veiculo.acelerar()
        print(f"Velocidade: {veiculo.get_velocidade()} km/h")
        veiculo.frear()
        print(f"Velocidade após frear: {veiculo.get_velocidade()} km/h")


if __name__ == "__main__":

    controlador = ControladorTrafego()

    carro = Carro()
    bicicleta = Bicicleta()
    aviao = Aviao()

    controlador.testar_veiculo(carro)
    controlador.testar_veiculo(bicicleta)
    controlador.testar_veiculo(aviao)

