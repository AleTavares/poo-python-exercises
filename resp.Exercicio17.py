from abc import ABC, abstractmethod


class Bebida(ABC):
    """
    Interface base que define o contrato para todas as bebidas e decorators.
    """
    @abstractmethod
    def get_descricao(self) -> str:
        pass

    @abstractmethod
    def get_preco(self) -> float:
        pass

class Cafe(Bebida):
    """
    Componente concreto: Café.
    """
    def get_descricao(self) -> str:
        return "Café"

    def get_preco(self) -> float:
        return 5.00

class Cha(Bebida):
    """
    Componente concreto: Chá.
    """
    def get_descricao(self) -> str:
        return "Chá"

    def get_preco(self) -> float:
        return 3.00


class BebidaDecorator(Bebida, ABC):
    """
    Classe abstrata que serve como base para todos os decorators.
    Contém a referência à bebida que será decorada.
    """
    def __init__(self, bebida: Bebida):
        self._bebida = bebida

    @abstractmethod
    def get_descricao(self) -> str:
        
        pass

    @abstractmethod
    def get_preco(self) -> float:
        
        pass



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


if __name__ == "__main__":
    
    print("--- Padrão Decorator: Sistema de Bebidas ---")
    
   
    cafe = Cafe()
    print(f"Bebida Simples: {cafe.get_descricao()} - R$ {cafe.get_preco():.1f}")
    
    print("-" * 30)

  
    cafe_com_leite = LeiteDecorator(cafe)
    print(f"Com um Decorator: {cafe_com_leite.get_descricao()} - R$ {cafe_com_leite.get_preco():.1f}")
    
    print("-" * 30)


    cafe_especial = ChantillyDecorator(AcucarDecorator(LeiteDecorator(Cafe())))
    
  
    print(f"Composição de Decorators:")
    print(f"Descrição: {cafe_especial.get_descricao()}")
    print(f"Preço: R$ {cafe_especial.get_preco():.1f}")
    
    print("-" * 30)
    
    
    cha_simples = AcucarDecorator(Cha())
   
    print(f"Chá com Açúcar: {cha_simples.get_descricao()} - R$ {cha_simples.get_preco():.1f}")