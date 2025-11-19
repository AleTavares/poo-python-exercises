

class Amplificador:
    def ligar(self): 
        print("Ligando amplificador")
    def desligar(self):
        print("Desligando amplificador")
    def definir_volume(self, volume): 
        print(f"Definindo volume para {volume}")

class DVDPlayer:
    def ligar(self): 
        print("Ligando DVD player")
    def desligar(self):
        print("Desligando DVD player")
    def reproduzir(self, filme): 
        print(f"Reproduzindo {filme}")
    def ejetar(self):
        print("Ejetando DVD")

class Projetor:
    def ligar(self): 
        print("Ligando projetor")
    def desligar(self):
        print("Desligando projetor")
    def modo_widescreen(self): 
        print("Definindo modo widescreen (16:9)")

class Luzes:
    def ligar(self):
        print("Ligando luzes")
    def diminuir(self, nivel): 
        print(f"Diminuindo luzes para {nivel}%")
    def apagar(self):
        print("Apagando luzes")

class PipocaPopper:
    def ligar(self): 
        print("Ligando pipoqueira")
    def desligar(self):
        print("Desligando pipoqueira")
    def fazer_pipoca(self): 
        print("Fazendo pipoca")



class HomeTheaterFacade:
    """
    Facade que simplifica a interface do subsistema de home theater.
    """
    def __init__(self):
        # Referência a todos os componentes do subsistema
        self.amplificador = Amplificador()
        self.dvd = DVDPlayer()
        self.projetor = Projetor()
        self.luzes = Luzes()
        self.pipoca = PipocaPopper()
    
    def assistir_filme(self, filme):
        """
        Método de alto nível que configura todo o sistema para assistir ao filme.
        """
        print(f"\nPreparando para assistir {filme}...")
        
       
        self.luzes.diminuir(10)
        self.pipoca.ligar()
        self.pipoca.fazer_pipoca()
        self.projetor.ligar()
        self.projetor.modo_widescreen()
        self.amplificador.ligar()
        self.amplificador.definir_volume(5)
        self.dvd.ligar()
        self.dvd.reproduzir(filme)
    
    def fim_filme(self):
        """
        Método de alto nível que desliga todos os componentes.
        """
        print("\nFilme finalizado! Desligando o sistema...")
        
    
        self.pipoca.desligar()
        self.luzes.ligar()
        self.dvd.ejetar()
        self.dvd.desligar()
        self.amplificador.desligar()
        self.projetor.desligar()


if __name__ == "__main__":
    


    print("--- Uso Simples (COM Facade) ---")
    
   
    home_theater = HomeTheaterFacade()
    

    home_theater.assistir_filme("Matrix")
 
    home_theater.fim_filme()