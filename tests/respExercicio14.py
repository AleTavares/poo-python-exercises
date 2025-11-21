from abc import ABC, abstractmethod

class Trabalhar(ABC):
    @abstractmethod
    def trabalhar(self):
        ...
    
class Comer(ABC):
    @abstractmethod
    def comer(self):
        ...
    
class Dormir(ABC):
    @abstractmethod
    def dormir(self):
        ...

class Programar(ABC):
    @abstractmethod
    def programar(self):
        ...

class Desenvolvedor(Trabalhar, Comer, Dormir, ProcessLookupError):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f'{self.nome} está trabalhando')

    def comer(self):
        print(f'{self.nome} está comendo')

    def dormir(self):
        print(f'{self.nome} está dormindo')

    def programar(self):
        print(f'{self.nome} está progamando')

class Gerente(Trabalhar, Comer, Dormir, ProcessLookupError):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f'{self.nome} está trabalhando')

    def comer(self):
        print(f'{self.nome} está comendo')

class Robo(Trabalhar, Comer, Dormir, ProcessLookupError):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f'{self.nome} está trabalhando')

    def programar(self):
        print(f'{self.nome} está comendo')


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