from abc import ABC, abstractmethod

# Interfaces específicas seguindo ISP
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


# Classes concretas
class Desenvolvedor(Trabalhavel, Alimentavel, Descansavel, Programavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está trabalhando...")

    def comer(self):
        print(f"{self.nome} está comendo...")

    def dormir(self):
        print(f"{self.nome} está dormindo...")

    def programar(self):
        print(f"{self.nome} está programando...")


class Gerente(Trabalhavel, Alimentavel, Descansavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está gerenciando a equipe...")

    def comer(self):
        print(f"{self.nome} está comendo...")

    def dormir(self):
        print(f"{self.nome} está descansando...")


class Robo(Trabalhavel, Programavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está executando tarefas...")

    def programar(self):
        print(f"{self.nome} está rodando scripts de programação...")


# Demonstração de uso
if __name__ == "__main__":
    desenvolvedor = Desenvolvedor("Ana")
    gerente = Gerente("Carlos")
    robo = Robo("R2D2")

    desenvolvedor.trabalhar()
    desenvolvedor.comer()
    desenvolvedor.programar()

    gerente.trabalhar()
    gerente.comer()

    robo.trabalhar()
    robo.programar()