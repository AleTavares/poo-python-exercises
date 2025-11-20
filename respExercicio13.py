# Implementação seguindo o Princípio da Substituição de Liskov (LSP)

class Veiculo:
    def __init__(self, velocidade_maxima):
        self.velocidade = 0
        self.velocidade_maxima = velocidade_maxima

    def acelerar(self):
        # Aumenta 20 km/h por aceleração, respeitando velocidade máxima
        nova_velocidade = self.velocidade + 20
        self.velocidade = min(nova_velocidade, self.velocidade_maxima)

    def frear(self):
        # Diminui 20 km/h por frenagem, sem ir abaixo de zero
        nova_velocidade = self.velocidade - 20
        self.velocidade = max(nova_velocidade, 0)

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


# Controlador de tráfego que funciona com qualquer veículo
class ControladorTrafego:
    def monitorar(self, veiculo: Veiculo):
        print(f"Monitorando {type(veiculo).__name__}")
        print(f"Velocidade atual: {veiculo.get_velocidade()} km/h")


# Demonstração de uso
if __name__ == "__main__":
    def testar_veiculo(veiculo):
        print(f"Testando {type(veiculo).__name__}")
        veiculo.acelerar()
        veiculo.acelerar()
        print(f"Velocidade: {veiculo.get_velocidade()} km/h")
        veiculo.frear()
        print(f"Velocidade após frear: {veiculo.get_velocidade()} km/h")
        print()

    carro = Carro()
    bicicleta = Bicicleta()
    aviao = Aviao()

    testar_veiculo(carro)
    testar_veiculo(bicicleta)
    testar_veiculo(aviao)