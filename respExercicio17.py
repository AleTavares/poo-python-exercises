from abc import ABC, abstractmethod

# Interface base
class Bebida(ABC):
    @abstractmethod
    def get_descricao(self) -> str:
        pass

    @abstractmethod
    def get_preco(self) -> float:
        pass

# Bebidas concretas
class Cafe(Bebida):
    def get_descricao(self) -> str:
        return "Café"

    def get_preco(self) -> float:
        return 5.00

class Cha(Bebida):
    def get_descricao(self) -> str:
        return "Chá"

    def get_preco(self) -> float:
        return 3.00

# Decorator base
class BebidaDecorator(Bebida):
    def __init__(self, bebida: Bebida):
        self._bebida = bebida

    def get_descricao(self) -> str:
        return self._bebida.get_descricao()

    def get_preco(self) -> float:
        return self._bebida.get_preco()

# Decorators concretos
class LeiteDecorator(BebidaDecorator):
    def get_descricao(self) -> str:
        return self._bebida.get_descricao() + " com Leite"

    def get_preco(self) -> float:
        return self._bebida.get_preco() + 2.00

class AcucarDecorator(BebidaDecorator):
    def get_descricao(self) -> str:
        return self._bebida.get_descricao() + " com Açúcar"

    def get_preco(self) -> float:
        return self._bebida.get_preco() + 0.50

class ChantillyDecorator(BebidaDecorator):
    def get_descricao(self) -> str:
        return self._bebida.get_descricao() + " com Chantilly"

    def get_preco(self) -> float:
        return self._bebida.get_preco() + 3.00

# Demonstração de uso
if __name__ == "__main__":
    # Bebida simples
    cafe = Cafe()
    print(f"{cafe.get_descricao()} - R$ {cafe.get_preco()}")

    # Bebida com decorator
    cafe_com_leite = LeiteDecorator(cafe)
    print(f"{cafe_com_leite.get_descricao()} - R$ {cafe_com_leite.get_preco()}")

    # Múltiplos decorators
    cafe_especial = ChantillyDecorator(AcucarDecorator(LeiteDecorator(Cafe())))
    print(f"{cafe_especial.get_descricao()} - R$ {cafe_especial.get_preco()}")
