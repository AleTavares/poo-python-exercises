from abc import ABC, abstractmethod

class Bebida(ABC):

    @abstractmethod
    def get_descricao(self):
        pass

    @abstractmethod
    def get_preco(self):
        pass
class Cafe(Bebida):

    def get_descricao(self):
        return "Café"

    def get_preco(self):
        return 5.0
    
class Cha(Bebida):

    def get_descricao(self):
        return "Chá"

    def get_preco(self):
        return 3.0
    
class AdicionalDecorator(Bebida):
    def __init__(self, bebida):
        self.bebida = bebida

    def get_descricao(self):
        return self().get_descricao()
    
    def get_preco(self):
        return self.bebida.get_preco()

class LeiteDecorator(AdicionalDecorator):
    def get_descricao(self):
        return self.bebida.get_descricao() + " com Leite"

    def get_preco(self):
        return self.bebida.get_preco() + 2.00


class AcucarDecorator(AdicionalDecorator):
    def get_descricao(self):
        return self.bebida.get_descricao() + " com Açúcar"

    def get_preco(self):
        return self.bebida.get_preco() + 0.50


class ChantillyDecorator(AdicionalDecorator):
    def get_descricao(self):
        return self.bebida.get_descricao() + " com Chantilly"

    def get_preco(self):
        return self.bebida.get_preco() + 3.00

# Bebida simples
cafe = Cafe()
print(f"{cafe.get_descricao()} - R$ {cafe.get_preco()}")

# Bebida com decorators
cafe_com_leite = LeiteDecorator(cafe)
print(f"{cafe_com_leite.get_descricao()} - R$ {cafe_com_leite.get_preco()}")

# Múltiplos decorators
cafe_especial = ChantillyDecorator(AcucarDecorator(LeiteDecorator(Cafe())))
print(f"{cafe_especial.get_descricao()} - R$ {cafe_especial.get_preco()}")