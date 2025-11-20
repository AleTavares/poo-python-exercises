class LigarFuncao:
    def __init__(self, nome):
        self.nome = nome

    def ligar(self):
        print(f"Ligando {self.nome}...")

class Amplificador(LigarFuncao):
    def __init__(self):
        super().__init__("Amplificador")

    def definir_volume(self, volume):
        print(f"Definindo volume do Amplificador para {volume}.")

class DVDPlayer(LigarFuncao):
    def __init__(self):
        super().__init__("DVD Player")

    def reproduzir(self, filme):
        print(f"Reproduzindo filme: {filme}.")

class Projetor(LigarFuncao):
    def __init__(self):
        super().__init__("Projetor")

    def modo_widescreen(self):
        print("Configurando Projetor para modo widescreen.")

class Luzes(LigarFuncao):
    def __init__(self):
        super().__init__("Luzes")

    def diminuir(self, nivel):
        print(f"Diminuindo luzes para o nível {nivel}.")

class PipocaPopper(LigarFuncao):
    def __init__(self):
        super().__init__("Pipoca Popper")

    def fazer_pipoca(self):
        print("Fazendo pipoca.")

class HomeTheaterFacade:
    def __init__(self):
        self.amplificador = Amplificador()
        self.dvd_player = DVDPlayer()
        self.projetor = Projetor()
        self.luzes = Luzes()
        self.pipoca_popper = PipocaPopper()

    def assistir_filme(self, filme):
        print("Preparando para assistir ao filme...")
        self.pipoca_popper.ligar()
        self.pipoca_popper.fazer_pipoca()
        self.luzes.diminuir(10)
        self.projetor.ligar()
        self.projetor.modo_widescreen()
        self.amplificador.ligar()
        self.amplificador.definir_volume(5)
        self.dvd_player.ligar()
        self.dvd_player.reproduzir(filme)
        print("Aproveite o filme!")

    def fim_filme(self):
        print("Desligando o Home Theater...")
        print("Home Theater desligado.")

# Usando o sistema diretamente        
home_theater = HomeTheaterFacade()
home_theater.assistir_filme("Inception")
home_theater.fim_filme()
