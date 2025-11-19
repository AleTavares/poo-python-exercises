from abc import ABC, abstractmethod

# ============================
# Interfaces específicas (ISP)
# ============================

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


# ============================
# Classes concretas
# ============================

class Desenvolvedor(Trabalhavel, Alimentavel, Descansavel, Programavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está trabalhando em código...")

    def comer(self):
        print(f"{self.nome} está comendo para recuperar energia.")

    def dormir(self):
        print(f"{self.nome} está dormindo após um longo dia de programação.")

    def programar(self):
        print(f"{self.nome} está programando um novo recurso!")


class Gerente(Trabalhavel, Alimentavel, Descansavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está coordenando a equipe.")

    def comer(self):
        print(f"{self.nome} está almoçando com clientes.")

    def dormir(self):
        print(f"{self.nome} está descansando para liderar melhor amanhã.")


class Robo(Trabalhavel, Programavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está executando tarefas automatizadas.")

    def programar(self):
        print(f"{self.nome} está rodando algoritmos de programação.")
        

if __name__ == "__main__":
    desenvolvedor = Desenvolvedor("Ana")
    gerente = Gerente("Carlos")
    robo = Robo("R2D2")

    # Desenvolvedor faz tudo
    desenvolvedor.trabalhar()
    desenvolvedor.comer()
    desenvolvedor.programar()

    print()

    # Gerente não programa
    gerente.trabalhar()
    gerente.comer()

    print()

    # Robô não come nem dorme
    robo.trabalhar()
    robo.programar()
