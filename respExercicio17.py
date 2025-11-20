
class Bebida:
    def get_descricao(self):
        pass

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

class BebidaDecorator(Bebida):
    def __init__(self, bebida):
        self.bebida = bebida

    def get_descricao(self):
        return self.bebida.get_descricao()

    def get_preco(self):
        return self.bebida.get_preco()

class LeiteDecorator(BebidaDecorator):
    def get_descricao(self):
        return self.bebida.get_descricao() + " com Leite"

    def get_preco(self):
        return self.bebida.get_preco() + 2.0


class AcucarDecorator(BebidaDecorator):
    def get_descricao(self):
        return self.bebida.get_descricao() + " com Açúcar"

    def get_preco(self):
        return self.bebida.get_preco() + 0.5


class ChantillyDecorator(BebidaDecorator):
    def get_descricao(self):
        return self.bebida.get_descricao() + " com Chantilly"

    def get_preco(self):
        return self.bebida.get_preco() + 3.0



