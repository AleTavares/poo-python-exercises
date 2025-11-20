#não sei se está certo

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
        print("Codando...")

    def comer(self):
        print("Almoçando...")

    def dormir(self):
        print("Dormindo...")

    def programar(self):
        print("Escrevendo testes...")

class Robo(Trabalhavel, Programavel):
    def trabalhar(self):
        print("Montando peças...")

    def programar(self):
        print("Auto-atualizando firmware...")