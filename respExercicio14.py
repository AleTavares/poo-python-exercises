from abc import ABC, abstractmethod

class Trabalhavel(ABC):
    @abstractmethod
    def trabalhar(self):
        pass

class Alimentavel(ABC):
    @abstractmethod
    def comer(self):
        pass

class Descansavel(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Programavel(ABC):
    @abstractmethod
    def programar(self):
        pass

class Desenvolvedor(Trabalhavel, Alimentavel, Descansavel, Programavel):
    def trabalhar(self):
        print("Desenvolvedor está trabalhando.")

    def comer(self):
        print("Desenvolvedor está comendo.")

    def dormir(self):
        print("Desenvolvedor está dormindo.")

    def programar(self):
        print("Desenvolvedor está programando.")

class Gerente(Trabalhavel, Alimentavel, Descansavel):
    def trabalhar(self):
        print("Gerente está trabalhando.")

    def comer(self):
        print("Gerente está comendo.")

    def dormir(self):
        print("Gerente está dormindo.")

class Robo(Trabalhavel, Programavel):
    def trabalhar(self):
        print("Robo está trabalhando.")

    def programar(self):
        print("Robo está programando.")

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