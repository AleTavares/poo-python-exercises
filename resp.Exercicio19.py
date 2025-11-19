from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Interface comum para todos os observadores (displays).
    """
    @abstractmethod
    def update(self, temperatura: float, umidade: float, pressao: float):
        pass


class EstacaoMeteorologica:
    """
    O Subject (Assunto) que gerencia os dados meteorológicos e notifica os displays.
    """
    def __init__(self):
        self._observers = []
        self._temperatura = 0.0
        self._umidade = 0.0
        self._pressao = 0.0
        print("Estação Meteorológica Inicializada.")

    def adicionar_observer(self, observer: Observer):
        """Adiciona um observador à lista."""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"-> Observer adicionado: {type(observer).__name__}")

    def remover_observer(self, observer: Observer):
        """Remove um observador da lista."""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"-> Observer removido: {type(observer).__name__}")
    
    def notificar_observers(self):
        """Notifica todos os observadores sobre a mudança de estado."""
        print("\n--- NOTIFICANDO OBSERVERS ---")
        for observer in self._observers:
            observer.update(self._temperatura, self._umidade, self._pressao)

    def definir_medicoes(self, temperatura: float, umidade: float, pressao: float):
        """
        Define novas medições e dispara a notificação.
        Esta é a mudança de estado que os observadores esperam.
        """
        self._temperatura = temperatura
        self._umidade = umidade
        self._pressao = pressao
        self.notificar_observers()




class DisplayTemperatura(Observer):
    """Observador que exibe apenas a temperatura."""
    def update(self, temperatura: float, umidade: float, pressao: float):
        print(f"Display Temperatura: {temperatura}°C")

class DisplayUmidade(Observer):
    """Observador que exibe apenas a umidade."""
    def update(self, temperatura: float, umidade: float, pressao: float):
        print(f"Display Umidade: {umidade}%")

class DisplayCompleto(Observer):
    """Observador que exibe todos os dados."""
    def update(self, temperatura: float, umidade: float, pressao: float):
        print(f"Display Completo: {temperatura}°C, {umidade}%, {pressao} hPa")



if __name__ == "__main__":
    estacao = EstacaoMeteorologica()

   
    display_temp = DisplayTemperatura()
    display_umidade = DisplayUmidade()
    display_completo = DisplayCompleto()

   
    estacao.adicionar_observer(display_temp)
    estacao.adicionar_observer(display_umidade)
    estacao.adicionar_observer(display_completo)

   
    print("\n======================================")
    print("MUDANÇA 1: Dados da Tarde")
    print("======================================")
    estacao.definir_medicoes(25.5, 65.0, 1013.2)

    print("\n======================================")
    print("MUDANÇA 2: Dados da Noite")
    print("======================================")
    estacao.definir_medicoes(27.0, 70.0, 1015.1)

  
    estacao.remover_observer(display_umidade)

   
    print("\n======================================")
    print("MUDANÇA 3: Após remover Display Umidade")
    print("======================================")
    estacao.definir_medicoes(22.0, 80.0, 1010.0)