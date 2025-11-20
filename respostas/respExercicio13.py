class Veiculo:
    def __init__ (self, velocidade):
        self.velocidade = velocidade
        
    def acelerar(self, velocidade):
        self.velocidade_final = velocidade + 100
        return f"A nova velocidade é: {self.velocidade_final}"
    
    def frear(self, velocidade):
        self.velocidade_final = velocidade - 100
        return f"A nova velocidade é: {self.velocidade_final}"
    
    def get_velocidade(self, velocidade):
        return f"A velocidade atual é: {self.velocidade}"
    
class Carro(Veiculo):
    