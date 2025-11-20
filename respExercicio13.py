# Exercício 13 - LSP

class Veiculo:
    def __init__(self, velocidade_maxima: int):
        self._velocidade = 0
        self._velocidade_maxima = velocidade_maxima

    def acelerar(self):
        if self._velocidade + 20 <= self._velocidade_maxima:
            self._velocidade += 20
        else:
            self._velocidade = self._velocidade_maxima

    def frear(self):
        if self._velocidade - 10 >= 0:
            self._velocidade -= 10
        else:
            self._velocidade = 0

    def get_velocidade(self):
        return self._velocidade


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
    def monitorar(self, veiculo: Veiculo):
        print(f"Monitorando {type(veiculo).__name__}")
        veiculo.acelerar()
        veiculo.acelerar()
        print(f"Velocidade atual: {veiculo.get_velocidade()} km/h")
        veiculo.frear()
        print(f"Após frear: {veiculo.get_velocidade()} km/h")


# Demonstração de uso
if __name__ == "__main__":
    carro = Carro()
    bicicleta = Bicicleta()
    aviao = Aviao()

    controlador = ControladorTrafego()

    controlador.monitorar(carro)
    controlador.monitorar(bicicleta)
    controlador.monitorar(aviao)
