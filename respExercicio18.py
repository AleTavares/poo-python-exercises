#Implementar o padrão de projeto Facade para simplificar uma interface complexa.

## Descrição do Exercício#
#Crie uma facade para simplificar o uso de um sistema complexo de home theater.

class Amplificador:
    def ligar(self):
      print("Amplificador ligado.")

    def definir_volume(self, volume):
      print(f"Volume definido para {volume}.")  


    def desligar(self):
      print("Amplificador desligado.")

class DVDPlayer:
    def ligar(self):
      print("DVD Player ligado.")

    def reproduzir(self, filme):
      print(f"Reproduzindo filme: {filme}")

    def parar(self):
      print("DVD Player parado.")

    def desligar(self):
        print("DVD Player desligado.")

    
class Projetor:
    def ligar(self):
      print("Projetor ligado.")

    def modo_widescreen(self):
      print("Projetor em modo widescreen.")

    def desligar(self):
      print("Projetor desligado.")

class Luzes:
    def aumentar(self, nivel): 
       print(f"Luzes aumentadas para {nivel}%.")

    def diminuir(self, nivel): 
       print(f"Luzes diminuídas para {nivel}%.")

class PipocaPopper:
    def ligar(self): 
       print("Pipoca Popper ligado.")

    def fazer_pipoca(self): 
       print("Fazendo pipoca...")

#Facade

class HomeTheaterFacade:
    def __init__(self):
        self.amp = Amplificador()
        self.dvd = DVDPlayer()
        self.proj = Projetor()
        self.luzes = Luzes()
        self.pipoca = PipocaPopper()

    def assistir_filme(self, filme):
        print("Preparando para assistir ao filme...")

        self.pipoca.ligar()
        self.pipoca.fazer_pipoca()

        self.luzes.diminuir(10)

        self.proj.ligar()
        self.proj.modo_widescreen()

        self.amp.ligar()
        self.amp.definir_volume(5)
        
        self.dvd.ligar()
        self.dvd.reproduzir(filme)

        print("Aproveite o filme!")

    def fim_filme(self):
        print("Desligando o home theater...")

        self.amp.desligar()
        self.dvd.parar()
        self.dvd.desligar()
        self.proj.desligar()
        self.luzes.aumentar(100)

        print("Home theater desligado.")

#Uso da Facade
if __name__ == "__main__":
    home_theater = HomeTheaterFacade()
    home_theater.assistir_filme("Matrix")
    home_theater.fim_filme()
  





