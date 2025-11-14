from abc import ABC, abstractmethod

# -----------------------------
# Interfaces específicas (ISP)
# -----------------------------
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


# -----------------------------
# Classes concretas
# -----------------------------
class Desenvolvedor(Trabalhavel, Alimentavel, Descansavel, Programavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está escrevendo código...")

    def comer(self):
        print(f"{self.nome} está comendo para recarregar as energias.")

    def dormir(self):
        print(f"{self.nome} está dormindo depois de um dia de trabalho.")

    def programar(self):
        print(f"{self.nome} está programando em Python.")


class Gerente(Trabalhavel, Alimentavel, Descansavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está em reunião e gerenciando a equipe.")

    def comer(self):
        print(f"{self.nome} está almoçando com o time.")

    def dormir(self):
        print(f"{self.nome} está descansando para o próximo dia de trabalho.")


class Robo(Trabalhavel, Programavel):
    def __init__(self, identificacao):
        self.identificacao = identificacao

    def trabalhar(self):
        print(f"Robô {self.identificacao} está executando tarefas repetitivas.")

    def programar(self):
        print(f"Robô {self.identificacao} está compilando e otimizando código.")


# -----------------------------
# Demonstração de uso
# -----------------------------
if __name__ == "__main__":
    desenvolvedor = Desenvolvedor("Ana")
    gerente = Gerente("Carlos")
    robo = Robo("R2D2")

    # Desenvolvedor faz tudo
    desenvolvedor.trabalhar()
    desenvolvedor.comer()
    desenvolvedor.programar()
    desenvolvedor.dormir()

    print("-----")

    # Gerente não programa
    gerente.trabalhar()
    gerente.comer()
    gerente.dormir()

    print("-----")

    # Robô não come nem dorme
    robo.trabalhar()
    robo.programar()
