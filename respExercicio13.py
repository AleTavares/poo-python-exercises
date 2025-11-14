# Exercício 13 - Liskov Substitution Principle (LSP)

# ----------------------------------------
# Classe base Veiculo
# ----------------------------------------
class Veiculo:
    def __init__(self, velocidade_maxima):
        self.velocidade = 0
        self.velocidade_maxima = velocidade_maxima

    def acelerar(self):
        """Aumenta a velocidade em 20 km/h, sem passar da velocidade máxima."""
        nova_velocidade = self.velocidade + 20
        if nova_velocidade <= self.velocidade_maxima:
            self.velocidade = nova_velocidade
        else:
            self.velocidade = self.velocidade_maxima

    def frear(self):
        """Diminui a velocidade em 10 km/h, sem ficar negativa."""
        nova_velocidade = self.velocidade - 10
        if nova_velocidade >= 0:
            self.velocidade = nova_velocidade
        else:
            self.velocidade = 0

    def get_velocidade(self):
        return self.velocidade


# ----------------------------------------
# Subclasses que respeitam LSP
# ----------------------------------------
class Carro(Veiculo):
    def __init__(self):
        super().__init__(velocidade_maxima=180)


class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__(velocidade_maxima=50)


class Aviao(Veiculo):
    def __init__(self):
        super().__init__(velocidade_maxima=900)


# ----------------------------------------
# Classe ControladorTrafego (polimorfismo)
# ----------------------------------------
class ControladorTrafego:
    def testar(self, veiculo: Veiculo):
        print(f"Testando {type(veiculo).__name__}")
        veiculo.acelerar()
        veiculo.acelerar()
        print(f"Velocidade: {veiculo.get_velocidade()} km/h")
        veiculo.frear()
        print(f"Velocidade após frear: {veiculo.get_velocidade()} km/h")
        print("-" * 40)


# ----------------------------------------
# Demonstração de uso
# ----------------------------------------
if __name__ == "__main__":
    carro = Carro()
    bicicleta = Bicicleta()
    aviao = Aviao()

    controlador = ControladorTrafego()

    controlador.testar(carro)
    controlador.testar(bicicleta)
    controlador.testar(aviao)
