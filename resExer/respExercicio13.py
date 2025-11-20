class Veiculo:
    def __init__(self, velocidade_maxima):
        self._velocidade = 0
        self._velocidade_maxima = velocidade_maxima

    def acelerar(self):
        # Aumenta sempre 20 km/h, mas sem ultrapassar a velocidade máxima
        nova_vel = self._velocidade + 20
        self._velocidade = min(nova_vel, self._velocidade_maxima)

    def frear(self):
        # Sempre reduz 20 km/h, mas não deixa ficar negativo
        nova_vel = self._velocidade - 20
        self._velocidade = max(nova_vel, 0)

    def get_velocidade(self):
        return self._velocidade


class Carro(Veiculo):
    def __init__(self):
        super().__init__(velocidade_maxima=180)


class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__(velocidade_maxima=50)


class Aviao(Veiculo):
    def __init__(self):
        super().__init__(velocidade_maxima=900)


class ControladorTrafego:
    def testar(self, veiculo):
        print(f"Testando {type(veiculo).__name__}")
        veiculo.acelerar()
        veiculo.acelerar()
        print(f"Velocidade: {veiculo.get_velocidade()} km/h")
        veiculo.frear()
        print(f"Velocidade após frear: {veiculo.get_velocidade()} km/h")
        print("-" * 40)


# Exemplo de uso
if __name__ == "__main__":
    carro = Carro()
    bicicleta = Bicicleta()
    aviao = Aviao()

    controlador = ControladorTrafego()
    controlador.testar(carro)
    controlador.testar(bicicleta)
    controlador.testar(aviao)