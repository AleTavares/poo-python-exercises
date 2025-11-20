from abc import ABC, abstractmethod

# Classe Abstrata
class Trabalhavel(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def trabalhar(self):
        pass

class Alimentavel(ABC):
    @abstractmethod
    def comer(self):
        pass
      
class Programavel(ABC):
    @abstractmethod
    def programar(self):
        pass
      
class Descansavel(ABC):
    @abstractmethod
    def dormir(self):
        pass


# Classe Específica
class Desenvolvedor(Trabalhavel, Alimentavel, Programavel, Descansavel):
    def trabalhar(self):
        print(f"{self.nome} está trabalhando.")

    def comer(self):
        print(f"{self.nome} está comendo.")

    def programar(self):
        print(f"{self.nome} está programando.")

    def dormir(self):
        print(f"{self.nome} está dormindo.")
        
class Gerente(Trabalhavel, Alimentavel, Descansavel):
    def trabalhar(self):
        print(f"{self.nome} está gerenciando.")

    def comer(self):
        print(f"{self.nome} está comendo.")

    def dormir(self):
        print(f"{self.nome} está dormindo.")

class Robo(Trabalhavel, Programavel):
    def trabalhar(self):
        print(f"{self.nome} está trabalhando.")

    def programar(self):
        print(f"{self.nome} está programando.")

desenvolvedor = Desenvolvedor("Ana")
gerente = Gerente("Carlos")
robo = Robo("R2D2")

# Desenvolvedor faz tudo
desenvolvedor.trabalhar()
desenvolvedor.comer()
desenvolvedor.programar()

# Gerente não programa
gerente.trabalhar()
gerente.comer()

# Robô não come nem dorme
robo.trabalhar()
robo.programar()