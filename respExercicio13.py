class Veiculo:
    def __init__(self, velocidade_max):
        self.velocidade = 0
        self.velocidade_max = velocidade_max

    def acelerar(self):
        nova_velocidade = self.velocidade + 10
        if nova_velocidade > self.velocidade_max:
            self.velocidade = self.velocidade_max
        else:
            self.velocidade = nova_velocidade

    def frear(self):
        nova_velocidade = self.velocidade - 5
        if nova_velocidade < 0:
            self.velocidade = 0
        else:
            self.velocidade = nova_velocidade

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
    def __init__(self, veiculo):
        self.veiculo = veiculo

    def acelerar(self):
        self.veiculo.acelerar()

    def frear(self):
        self.veiculo.frear()

    def mostrar_velocidade(self):
        print(f"Velocidade atual: {self.veiculo.get_velocidade()} km/h")


# Função pedida no exercício
def testar_veiculo(veiculo):
    print(f"Testando {type(veiculo).__name__}")
    veiculo.acelerar()
    veiculo.acelerar()
    print(f"Velocidade: {veiculo.get_velocidade()} km/h")
    veiculo.frear()
    print(f"Velocidade após frear: {veiculo.get_velocidade()} km/h")