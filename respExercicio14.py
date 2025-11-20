from abc import ABC, abstractmethod

# Interfaces específicas seguindo o ISP

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
        print(f"{self.nome} está trabalhando no código...")

    def comer(self):
        print(f"{self.nome} está comendo...")

    def dormir(self):
        print(f"{self.nome} está dormindo...")

    def programar(self):
        print(f"{self.nome} está programando uma nova funcionalidade...")


class Gerente(Trabalhavel, Alimentavel, Descansavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está organizando tarefas...")

    def comer(self):
        print(f"{self.nome} está comendo...")

    def dormir(self):
        print(f"{self.nome} está descansando...")


class Robo(Trabalhavel, Programavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está executando tarefas repetitivas...")

    def programar(self):
        print(f"{self.nome} está processando algoritmos...")


# Demonstração de uso
if __name__ == "__main__":
    desenvolvedor = Desenvolvedor("Ana")
    gerente = Gerente("Carlos")
    robo = Robo("R2D2")

    # Desenvolvedor faz tudo
    desenvolvedor.trabalhar()
    desenvolvedor.comer()
    desenvolvedor.programar()
    desenvolvedor.dormir()

    print()

    # Gerente não programa
    gerente.trabalhar()
    gerente.comer()
    gerente.dormir()

    print()

    # Robô não come nem dorme
    robo.trabalhar()
    robo.programar()


        