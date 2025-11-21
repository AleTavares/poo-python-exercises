class Amplificador:
    def ligar(self):
        print("Ligando amplificador")

    def definir_volume(self, volume):
        print(f'Definindo volume para {volume}%')

class DVDPlayer:
    def ligar(self):
        print('Ligando DVD player')

    def reproduzir(self, filme):
        print(f"Reproduzindo {filme}")


class Projetor:
    def ligar(self):
        print("ligando projetor")

    def modo_widescreen(self): 
        pass
        

class Luzes:
    def diminuir(self, nivel):
        print(f"Diminuindo luzes para {nivel}%")

class PipocaPopper:
    def ligar(self):
        print("Ligando pipoqueira")

    def fazer_pipoca(self):
        print('Fazendo pipoca')

class HomeTheaterFacade:
    def __init__(self, filme, volume, nivel):
        self.filme = filme
        self.volume = volume
        self.nivel = nivel 
        self.amplificador = Amplificador()
        self.dvd = DVDPlayer()
        self.projetor = Projetor()
        self.luzes = Luzes()
        self.pipoca = PipocaPopper()

    def assistir_filme(self):
        print(f"Preparando para assistir {self.filme}...")
        self.amplificador.ligar()
        self.amplificador.definir_volume(self.volume)
        self.dvd.ligar()
        self.projetor.ligar()
        self.luzes.diminuir(self.nivel)
        self.pipoca.ligar()
        self.pipoca.fazer_pipoca()
        self.dvd.reproduzir(self.filme)

    def fim_filme(self):
        print("Filme finalizado!")


home = HomeTheaterFacade('matrix', 5, 10)
home.assistir_filme()

# Preparando para assistir Matrix...
# Ligando amplificador
# Definindo volume para 5
# Ligando DVD player
# Ligando projetor
# Diminuindo luzes para 10%
# Ligando pipoqueira
# Fazendo pipoca
# Reproduzindo Matrix
# Filme finalizado!