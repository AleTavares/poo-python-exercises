class Veiculo:
    def __init__(self):
        self.velocidade_atual = 0

    def acelerar(self):
        self.velocidade_atual = 0
        return self.velocidade_atual

    def frear(self):
        ...

    def get_velocidade(self):
       self.velocidade_atual = 0
       return self.velocidade_atual

class Carro(Veiculo):
    def acelerar(self):
        velocidade_max = 100
        if self.velocidade_atual < velocidade_max:
            self.velocidade_atual =  self.velocidade_atual + 20

    def frear(self):
        if self.velocidade_atual > 0:
            self.velocidade_atual = self.velocidade_atual - 20
        
    def get_velocidade(self):
        self.velocidade = self.velocidade_atual
        return self.velocidade
        
    

class Bicicleta(Veiculo):
    def acelerar(self):
        velocidade_max = 50
        if self.velocidade_atual < velocidade_max:
            self.velocidade_atual =  self.velocidade_atual + 10

    def frear(self):
        if self.velocidade_atual > 0:
            self.velocidade_atual = self.velocidade_atual - 10

    def get_velocidade(self):
        self.velocidade = self.velocidade_atual
        return self.velocidade

class Aviao(Veiculo):
    def acelerar(self):
        velocidade_max = 900
        if self.velocidade_atual < velocidade_max:
            self.velocidade_atual =  self.velocidade_atual + 300

    def frear(self):
        if self.velocidade_atual > 0:
            self.velocidade_atual = self.velocidade_atual - 300

    def get_velocidade(self):
        self.velocidade = self.velocidade_atual
        return self.velocidade

class ControladorTrafego:
    def testar_veiculo(self, veiculo):
        print(f"Testando {type(veiculo).__name__}")
        veiculo.acelerar()
        veiculo.acelerar()
        print(f"Velocidade: {veiculo.get_velocidade()} km/h")
        veiculo.frear()
        print(f"Velocidade após frear: {veiculo.get_velocidade()} km/h")

carro = Carro()
bicicleta = Bicicleta()
aviao = Aviao()

trafego = ControladorTrafego()

trafego.testar_veiculo(carro)
trafego.testar_veiculo(bicicleta)
trafego.testar_veiculo(aviao)
