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
        print(f"{self.nome} está coordenando o trabalho...")

    def comer(self):
        print(f"{self.nome} está comendo...")

    def dormir(self):
        print(f"{self.nome} está descansando...")


class Robo(Trabalhavel, Programavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está executando tarefas automáticas...")

    def programar(self):
        print(f"{self.nome} está processando código...")

# Exemplo de Uso
if __name__ == "__main__":
    desenvolvedor = Desenvolvedor("Ana")
    gerente = Gerente("Carlos")
    robo = Robo("R2D2")

    desenvolvedor.trabalhar()
    desenvolvedor.comer()
    desenvolvedor.programar()

    print()

    gerente.trabalhar()
    gerente.comer()

    print()

    robo.trabalhar()
    robo.programar()