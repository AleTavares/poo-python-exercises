class Bebida:
    def get_descricao(self):
        raise NotImplementedError()

    def get_preco(self):
        raise NotImplementedError()

class Cafe(Bebida):
    def get_descricao(self):
        return "Café"

    def get_preco(self):
        return 5.00

class Cha(Bebida):
    def get_descricao(self):
        return "Chá"

    def get_preco(self):
        return 3.00

class BebidaDecorator(Bebida):
    def __init__(self, bebida: Bebida):
        self.bebida = bebida

    def get_descricao(self):
        return self.bebida.get_descricao()

    def get_preco(self):
        return self.bebida.get_preco()

class LeiteDecorator(BebidaDecorator):
    def get_descricao(self):
        return self.bebida.get_descricao() + " com Leite"

    def get_preco(self):
        return self.bebida.get_preco() + 2.00

class AcucarDecorator(BebidaDecorator):
    def get_descricao(self):
        return self.bebida.get_descricao() + " com Açúcar"

    def get_preco(self):
        return self.bebida.get_preco() + 0.50

class ChantillyDecorator(BebidaDecorator):
    def get_descricao(self):
        return self.bebida.get_descricao() + " com Chantilly"

    def get_preco(self):
        return self.bebida.get_preco() + 3.00

# Exemplo de uso
if __name__ == "__main__":
    cafe = Cafe()
    print(f"{cafe.get_descricao()} - R$ {cafe.get_preco()}")

    cafe_com_leite = LeiteDecorator(cafe)
    print(f"{cafe_com_leite.get_descricao()} - R$ {cafe_com_leite.get_preco()}")

    cafe_especial = ChantillyDecorator(
                        AcucarDecorator(
                            LeiteDecorator(
                                Cafe()
                            )
                        )
                    )
    print(f"{cafe_especial.get_descricao()} - R$ {cafe_especial.get_preco()}")