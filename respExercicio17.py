class Bebida:
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco     
    def get_descricao(self):
        return self.descricao
    def get_preco(self):
        return self.preco 
      
# Decorator base
class Cafe(Bebida):
    def __init__(self):
        super().__init__("Café", 5.0)
        
class Cha(Bebida):
    def __init__(self):
        super().__init__("Chá", 4.0)

# Decorator com decorators
class LeiteDecorator(Bebida):
    def __init__(self, bebida):
        descricao = bebida.get_descricao() + ", Leite"
        preco = bebida.get_preco() + 1.5
        super().__init__(descricao, preco)
        
class AcucarDecorator(Bebida):
    def __init__(self, bebida):
        descricao = bebida.get_descricao() + ", Açúcar"
        preco = bebida.get_preco() + 0.5
        super().__init__(descricao, preco)
        
class ChantillyDecorator(Bebida):
    def __init__(self, bebida):
        descricao = bebida.get_descricao() + ", Chantilly"
        preco = bebida.get_preco() + 2.0
        super().__init__(descricao, preco)
# Bebida simples
cafe = Cafe()
print(f"{cafe.get_descricao()} - R$ {cafe.get_preco()}")

# Bebida com decorators
cafe_com_leite = LeiteDecorator(cafe)
print(f"{cafe_com_leite.get_descricao()} - R$ {cafe_com_leite.get_preco()}")

# Múltiplos decorators
cafe_especial = ChantillyDecorator(AcucarDecorator(LeiteDecorator(Cafe())))
print(f"{cafe_especial.get_descricao()} - R$ {cafe_especial.get_preco()}")