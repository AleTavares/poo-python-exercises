# Exercício 14 - Princípio da Segregação de Interface (ISP)

## Objetivo
#Aplicar o quarto princípio SOLID - Interface Segregation Principle (ISP).

## Descrição do Exercício
#Refatore interfaces "gordas" em interfaces menores e mais específicas.

from abc import ABC, abstractmethod

# Interfaces pequenas e específicas

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

# Classes concretas -------------------------

class Desenvolvedor(Trabalhavel, Alimentavel, Descansavel, Programavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está trabalhando como desenvolvedora.")

    def comer(self):
        print(f"{self.nome} está comendo.")

    def dormir(self):    
        print(f"{self.nome} está dormindo.")

    def programar(self):
        print(f"{self.nome} está programando.")

class Gerente(Trabalhavel, Alimentavel, Descansavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está trabalhando como gerente.")

    def comer(self):
        print(f"{self.nome} está comendo.")

    def dormir(self):
        print(f"{self.nome} está dormindo.")

class Robo(Trabalhavel, Programavel):
    def __init__(self, id_robo):
        self.id_robo = id_robo

    def trabalhar(self):
        print(f"Robo {self.id_robo} está executando tarefas.")

    def programar(self):
        print(f"Robo {self.id_robo} está executando código.")

 # Demonstração de uso ----------------------
if __name__ == "__main__":

    desenvolvedor = Desenvolvedor("Ana")
    gerente = Gerente("Carlos")
    robo = Robo("R202")

    print("----- Desenvolvedor -----")
    desenvolvedor.trabalhar()
    desenvolvedor.comer()
    desenvolvedor.dormir()
    desenvolvedor.programar()

    print("\n----- Gerente -----")
    gerente.trabalhar()
    gerente.comer()     
    gerente.dormir()

    print("\n----- Robo -----")
    robo.trabalhar()
    robo.programar()

  