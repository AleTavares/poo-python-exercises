from abc import ABC, abstractmethod

class Bebidas(ABC):
    @abstractmethod
    def get_descricao(self):
        pass

    def get_preco(self):
        pass

class BebidaDecorator(Bebidas):
    def __init__(self, bebidas: Bebidas):
        self.bebidas = bebidas
        

class Cafe(Bebidas):
    def get_descricao(self):
        tipo_de_bebida = 'Café'
        return tipo_de_bebida

    def get_preco(self):
        preco = 5.00
        return preco


class Cha(Bebidas):
    def get_descricao(self):
        tipo_de_bebida = 'Chá'
        return tipo_de_bebida

    def get_preco(self):
        preco = 3.00
        return preco
    
class LeiteDecorator(BebidaDecorator):
    def get_descricao(self):
        self.com_leite = self.bebidas.get_descricao() + ' com leite'
        return self.com_leite
    
    def get_preco(self):
        self.preco = self.bebidas.get_preco() + 2
        return self.preco
    
class AcucarDecorator(BebidaDecorator):
    def get_descricao(self):
        self.com_acucar = self.bebidas.get_descricao() + ' com acucar'
        return self.com_acucar
    
    def get_preco(self):
        self.preco = self.bebidas.get_preco() + 0.50
        return self.preco
    
class ChantillyDecorator(BebidaDecorator):
    def get_descricao(self):
        self.com_chantilly = self.bebidas.get_descricao() + ' com chantilly'
        return self.com_chantilly
    
    def get_preco(self):
        self.preco = self.bebidas.get_preco() + 3
        return self.preco

    

        
        
cafe = Cafe()
print(f"{cafe.get_descricao()} - R$ {cafe.get_preco()}")

# Bebida com decorators
cafe_com_leite = LeiteDecorator(cafe)
print(f"{cafe_com_leite.get_descricao()} - R$ {cafe_com_leite.get_preco()}")

# Múltiplos decorators
cafe_especial = LeiteDecorator(AcucarDecorator(ChantillyDecorator(Cafe())))
print(f"{cafe_especial.get_descricao()} - R$ {cafe_especial.get_preco()}")