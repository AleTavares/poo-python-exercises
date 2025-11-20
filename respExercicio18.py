# Exercício 18 - Padrão Facade (Estrutural)

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
        print("Ativando modo widescreen")

class Luzes:
    def diminuir(self, nivel):
        print(f"Diminuindo luzes para {nivel}%")

class PipocaPopper:
    def ligar(self):
        print("Ligando pipoqueira")

    def fazer_pipoca(self):
        print("Fazendo pipoca")


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
        self.luzes.diminuir(10)
        self.pipoca.ligar()
        self.pipoca.fazer_pipoca()
        self.dvd.reproduzir(filme)

    def fim_filme(self):
        print("Filme finalizado!")


# Demonstração de uso direto (sem facade)
if __name__ == "__main__":
    print("--- Uso complexo sem Facade ---")
    amplificador = Amplificador()
    dvd = DVDPlayer()
    projetor = Projetor()
    luzes = Luzes()
    pipoca = PipocaPopper()

    amplificador.ligar()
    amplificador.definir_volume(5)
    dvd.ligar()
    projetor.ligar()
    luzes.diminuir(10)
    pipoca.ligar()
    pipoca.fazer_pipoca()
    dvd.reproduzir("Matrix")

    print("\n--- Uso simples com Facade ---")
    home = HomeTheaterFacade()
    home.assistir_filme("Matrix")
    home.fim_filme()