# respExercicio18.py

class Amplificador:
    def ligar(self):
        print("Ligando amplificador")

    def definir_volume(self, volume):
        print(f"Definindo volume para {volume}")


class DVDPlayer:
    def ligar(self):
        print("Ligando DVD player")

    def reproduzir(self, filme):
        print(f"Reproduzindo {filme}")


class Projetor:
    def ligar(self):
        print("Ligando projetor")

    def modo_widescreen(self):
        print("Modo widescreen ativado")


class Luzes:
    def diminuir(self, nivel):
        print(f"Diminuindo luzes para {nivel}%")


class PipocaPopper:
    def ligar(self):
        print("Ligando pipoqueira")

    def fazer_pipoca(self):
        print("Fazendo pipoca")


# Facade
class HomeTheaterFacade:
    def __init__(self):
        self.amplificador = Amplificador()
        self.dvd = DVDPlayer()
        self.projetor = Projetor()
        self.luzes = Luzes()
        self.pipoca = PipocaPopper()

    def assistir_filme(self, filme):
        print(f"Preparando para assistir {filme}...")
        self.amplificador.ligar()
        self.amplificador.definir_volume(5)
        self.dvd.ligar()
        self.projetor.ligar()
        self.projetor.modo_widescreen()
        self.luzes.diminuir(10)
        self.pipoca.ligar()
        self.pipoca.fazer_pipoca()
        self.dvd.reproduzir(filme)

    def fim_filme(self):
        print("Filme finalizado!")


# Demonstração de uso
if __name__ == "__main__":
    # Uso complexo (sem facade)
    print("--- Uso complexo ---")
    amplificador = Amplificador()
    dvd = DVDPlayer()
    projetor = Projetor()
    luzes = Luzes()
    pipoca = PipocaPopper()

    amplificador.ligar()
    amplificador.definir_volume(5)
    dvd.ligar()
    projetor.ligar()
    projetor.modo_widescreen()
    luzes.diminuir(10)
    pipoca.ligar()
    pipoca.fazer_pipoca()
    dvd.reproduzir("Matrix")

    # Uso simples (com facade)
    print("\n--- Uso com Facade ---")
    home_theater = HomeTheaterFacade()
    home_theater.assistir_filme("Matrix")
    home_theater.fim_filme()
