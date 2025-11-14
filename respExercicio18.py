# Exercício 18 - Padrão Facade

# ----------------------------------------
# 1. Subsistemas complexos
# ----------------------------------------
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


# ----------------------------------------
# 2. Facade que simplifica o uso do sistema
# ----------------------------------------
class HomeTheaterFacade:
    def __init__(self):
        self.amplificador = Amplificador()
        self.dvd = DVDPlayer()
        self.projetor = Projetor()
        self.luzes = Luzes()
        self.pipoqueira = PipocaPopper()

    def assistir_filme(self, filme):
        print(f"\nPreparando para assistir {filme}...")

        self.pipoqueira.ligar()
        self.pipoqueira.fazer_pipoca()

        self.luzes.diminuir(10)

        self.projetor.ligar()
        self.projetor.modo_widescreen()

        self.amplificador.ligar()
        self.amplificador.definir_volume(5)

        self.dvd.ligar()
        self.dvd.reproduzir(filme)

    def fim_filme(self):
        print("\nFilme finalizado!")
        print("Desligando sistema...")
        # Poderia colocar mais lógica aqui (desligar cada componente)


# ----------------------------------------
# 3. Demonstração de uso
# ----------------------------------------
if __name__ == "__main__":
    # Uso complexo (sem Facade)
    print("=== Uso sem Facade ===")
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

    # Uso com Facade
    print("\n=== Uso com Facade ===")
    home = HomeTheaterFacade()
    home.assistir_filme("Matrix")
    home.fim_filme()
