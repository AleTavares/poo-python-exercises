#Padrão Decorator (Estrutural)
#Crie um sistema de bebidas onde você pode adicionar ingredientes extras usando decorators.

class Bebida:
    def get_descricao(self):
        return self.descricao()
    pass

    def get_preco(self):
        pass
   
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
    

    #decorator base
class BebidaDecorator(Bebida):
    def __init__(self, bebida: Bebida):
        self.bebida = bebida

    def get_descricao(self):
        return self.bebida.get_descricao()
    
    def get_preco(self):
        return self.bebida.get_preco()


    #decorators concretos
class Leite(BebidaDecorator):
    def get_descricao(self):
        return self.bebida.get_descricao() + ", com Leite"
    
    def get_preco(self):
        return self.bebida.get_preco() + 2.00
    
class Acucar(BebidaDecorator):
    def get_descricao(self):
        return self.bebida.get_descricao() + " com Açúcar"
    
    def get_preco(self):
        return self.bebida.get_preco() + 0.50
    
class Chantilly(BebidaDecorator):
    def get_descricao(self):
        return self.bebida.get_descricao() + " com Chantilly"
    
    def get_preco(self):
        return self.bebida.get_preco() + 3.00
    
    #demostração de uso

if __name__ == "__main__":

    # Bebida simples
    cafe = Cafe()
    print(f"{cafe.get_descricao()} - R$ {cafe.get_preco():.2f}")

    # Bebida com decorators
    cafe_com_leite = Leite(cafe)
    print(f"{cafe_com_leite.get_descricao()} - R$ {cafe_com_leite.get_preco():.2f}")

    # Múltiplos decorators
    cafe_especial = Chantilly(Acucar(Leite(Cafe())))
    print(f"{cafe_especial.get_descricao()} - R$ {cafe_especial.get_preco():.2f}")


          




