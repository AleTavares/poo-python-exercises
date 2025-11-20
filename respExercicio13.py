class Veiculo:
    def __init__(self, velocidade_maxima, incremento=20):
        self._velocidade = 0
        self._velocidade_maxima = velocidade_maxima
        self._incremento = incremento

    def acelerar(self):
        self._velocidade += self._incremento
        if self._velocidade > self._velocidade_maxima:
            self._velocidade = self._velocidade_maxima

    def frear(self):
        self._velocidade -= self._incremento
        if self._velocidade < 0:
            self._velocidade = 0

    def get_velocidade(self):
        return self._velocidade


class Carro(Veiculo):
    def __init__(self):
        super().__init__(velocidade_maxima=180, incremento=20)


class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__(velocidade_maxima=50, incremento=10)


class Aviao(Veiculo):
    def __init__(self):
        super().__init__(velocidade_maxima=900, incremento=200)


class ControladorTrafego:
    def monitorar(self, veiculo: Veiculo):
        veiculo.acelerar()
        veiculo.acelerar()
        return veiculo.get_velocidade()


if __name__ == "__main__":
    def testar_veiculo(veiculo):
        print(f"Testando {type(veiculo).__name__}")
        veiculo.acelerar()
        veiculo.acelerar()
        print(f"Velocidade: {veiculo.get_velocidade()} km/h")
        veiculo.frear()
        print(f"Velocidade após frear: {veiculo.get_velocidade()} km/h\n")

    carro = Carro()
    bicicleta = Bicicleta()
    aviao = Aviao()

    testar_veiculo(carro)
    testar_veiculo(bicicleta)
    testar_veiculo(aviao)