class Amplificador:
    def ligar(self):
        print("Amplificador ligado.")
    
    def definir_volume(self, volume):
        print(f"Volume do amplificador definido para {volume}.")

class DVDPlayer:
    def ligar(self):
        print("DVD Player ligado.")
    
    def reproduzir(self, filme):
        print(f"Reproduzindo o filme: {filme}.")

class Projetor:
    def ligar(self):
        print("Projetor ligado.")
    
    def modo_widescreen(self):
        print("Projetor ajustado para o modo widescreen.")

class Luzes:
    def diminuir(self, nivel):
        print(f"Luzes diminuídas para o nível {nivel}.")

class PipocaPopper:
    def ligar(self):
        print("Pipoqueira ligada.")
    
    def fazer_pipoca(self):
        print("Pipoca sendo preparada.")

class HomeTheaterFacade:
    def __init__(self, amp, dvd, proj, luzes, pipoca):
        self.amp = amp
        self.dvd = dvd
        self.proj = proj
        self.luzes = luzes
        self.pipoca = pipoca

    def assistir_filme(self, filme):
        print("\nPreparando para assistir ao filme...")
        self.pipoca.ligar()
        self.pipoca.fazer_pipoca()
        self.luzes.diminuir(10)
        self.proj.ligar()
        self.proj.modo_widescreen()
        self.amp.ligar()
        self.amp.definir_volume(5)
        self.dvd.ligar()
        self.dvd.reproduzir(filme)
        print("Tudo pronto! Aproveite o filme!\n")

    def fim_filme(self):
        print("\nEncerrando o filme...")
        print("Desligando todos os componentes...")
        print("Filme encerrado. Boa noite!\n")

# Demonstração
if __name__ == "__main__":
    # Criando os componentes
    amp = Amplificador()
    dvd = DVDPlayer()
    proj = Projetor()
    luzes = Luzes()
    pipoca = PipocaPopper()

    # Usando o sistema diretamente
    print("Usando o sistema diretamente:")
    pipoca.ligar()
    pipoca.fazer_pipoca()
    luzes.diminuir(10)
    proj.ligar()
    proj.modo_widescreen()
    amp.ligar()
    amp.definir_volume(5)
    dvd.ligar()
    dvd.reproduzir("O Senhor dos Anéis")

    # Usando a facade
    print("\nUsando a facade:")
    home_theater = HomeTheaterFacade(amp, dvd, proj, luzes, pipoca)
    home_theater.assistir_filme("O Senhor dos Anéis")
    home_theater.fim_filme()

    # Uso complexo (sem facade)
amplificador = Amplificador()
dvd = DVDPlayer()
projetor = Projetor()
luzes = Luzes()
pipoca = PipocaPopper()

# Muitas chamadas necessárias...
amplificador.ligar()
amplificador.definir_volume(5)
dvd.ligar()
# ... etc

# Uso simples (com facade)
home_theater = HomeTheaterFacade()
home_theater.assistir_filme("Matrix")
home_theater.fim_filme()