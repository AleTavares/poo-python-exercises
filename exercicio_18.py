class Amplificador:
    def ligar(self): print("Ligando amplificador")
    def definir_volume(self, vol): print(f"Definindo volume para {vol}")
    def desligar(self): print("Desligando amplificador")

class DVDPlayer:
    def ligar(self): print("Ligando DVD player")
    def reproduzir(self, filme): print(f"Reproduzindo {filme}")
    def desligar(self): print("Desligando DVD player")

class Projetor:
    def ligar(self): print("Ligando projetor")
    def modo_widescreen(self): print("Modo widescreen ativado")
    def desligar(self): print("Desligando projetor")

class Luzes:
    def diminuir(self, nivel): print(f"Diminuindo luzes para {nivel}%")
    def ligar(self): print("Luzes ligadas")

class PipocaPopper:
    def ligar(self): print("Ligando pipoqueira")
    def fazer_pipoca(self): print("Fazendo pipoca")
    def desligar(self): print("Desligando pipoqueira")

class HomeTheaterFacade:
    def __init__(self):
        self.amp = Amplificador()
        self.dvd = DVDPlayer()
        self.projetor = Projetor()
        self.luzes = Luzes()
        self.pipoca = PipocaPopper()

    def assistir_filme(self, filme):
        print(f"Preparando para assistir {filme}...")
        self.luzes.diminuir(10)
        self.pipoca.ligar()
        self.pipoca.fazer_pipoca()
        self.amp.ligar()
        self.amp.definir_volume(5)
        self.projetor.ligar()
        self.projetor.modo_widescreen()
        self.dvd.ligar()
        self.dvd.reproduzir(filme)

    def fim_filme(self):
        print("Filme finalizado!")
        self.pipoca.desligar()
        self.amp.desligar()
        self.projetor.desligar()
        self.dvd.desligar()
        self.luzes.ligar()

home_theater = HomeTheaterFacade()
home_theater.assistir_filme("Matrix")
print("-" * 20)
home_theater.fim_filme()