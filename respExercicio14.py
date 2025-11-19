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
        print(f"{self.nome}: Desenvolvedor trabalhando em tarefas.")

    def comer(self):
        print(f"{self.nome}: Desenvolvedor fazendo pausa para o almoço.")

    def dormir(self):
        print(f"{self.nome}: Desenvolvedor descansando após um longo dia.")

    def programar(self):
        print(f"{self.nome}: Desenvolvedor programando o sistema.")


class Gerente(Trabalhavel, Alimentavel, Descansavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome}: Gerente em reuniões e planejamentos.")

    def comer(self):
        print(f"{self.nome}: Gerente fazendo pausa para o lanche.")

    def dormir(self):
        print(f"{self.nome}: Gerente indo dormir para estar pronto amanhã.")


class Robo(Trabalhavel, Programavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome}: Robô executando tarefas automatizadas.")

    def programar(self):
     
        print(f"{self.nome}: Robô atualizando seu firmware (Programando).")

if __name__ == "__main__":
    
    desenvolvedor = Desenvolvedor("Ana")
    gerente = Gerente("Carlos")
    robo = Robo("R2D2")

    print("=== Desenvolvedor (Todas as Interfaces) ===")
    desenvolvedor.trabalhar()
    desenvolvedor.comer()
    desenvolvedor.dormir()
    desenvolvedor.programar()

    print("\n=== Gerente (Sem Programar) ===")
    gerente.trabalhar()
    gerente.comer()
  
    gerente.dormir()

    print("\n=== Robô (Sem Comer/Dormir) ===")
    robo.trabalhar()
    robo.programar()
   