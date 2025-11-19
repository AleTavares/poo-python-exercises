
class Veiculo:
    def __init__(self, velocidade_maxima):
        self.velocidade_atual = 0
        self.velocidade_maxima = velocidade_maxima

    def acelerar(self, valor):
        nova_velocidade = self.velocidade_atual + valor
        if nova_velocidade > self.velocidade_maxima:
            self.velocidade_atual = self.velocidade_maxima
        else:
            self.velocidade_atual = nova_velocidade

    def frear(self, valor):
        nova_velocidade = self.velocidade_atual - valor
        if nova_velocidade < 0:
            self.velocidade_atual = 0
        else:
            self.velocidade_atual = nova_velocidade

    def get_velocidade(self):
        return self.velocidade_atual

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
    def controlar(self, veiculo: Veiculo):
        veiculo.acelerar(100)
        veiculo.frear(30)
        return veiculo.get_velocidade()
