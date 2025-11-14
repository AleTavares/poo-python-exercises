# Exercício 19 - Padrão Observer

from abc import ABC, abstractmethod


# ----------------------------------------
# 1. Interface Observer
# ----------------------------------------
class Observer(ABC):
    @abstractmethod
    def update(self, temperatura, umidade, pressao):
        pass


# ----------------------------------------
# 2. Subject (Estação Meteorológica)
# ----------------------------------------
class EstacaoMeteorologica:
    def __init__(self):
        self.observers = []
        self.temperatura = None
        self.umidade = None
        self.pressao = None

    def adicionar_observer(self, observer: Observer):
        self.observers.append(observer)

    def remover_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notificar_observers(self):
        for obs in self.observers:
            obs.update(self.temperatura, self.umidade, self.pressao)

    def definir_medicoes(self, temperatura, umidade, pressao):
        self.temperatura = temperatura
        self.umidade = umidade
        self.pressao = pressao
        self.notificar_observers()


# ----------------------------------------
# 3. Observadores concretos
# ----------------------------------------
class DisplayTemperatura(Observer):
    def update(self, temperatura, umidade, pressao):
        print(f"Display Temperatura: {temperatura}°C")


class DisplayUmidade(Observer):
    def update(self, temperatura, umidade, pressao):
        print(f"Display Umidade: {umidade}%")


class DisplayCompleto(Observer):
    def update(self, temperatura, umidade, pressao):
        print(f"Display Completo: {temperatura}°C, {umidade}%, {pressao} hPa")


# ----------------------------------------
# 4. Demonstração de uso
# ----------------------------------------
if __name__ == "__main__":
    estacao = EstacaoMeteorologica()

    display_temp = DisplayTemperatura()
    display_umidade = DisplayUmidade()
    display_completo = DisplayCompleto()

    estacao.adicionar_observer(display_temp)
    estacao.adicionar_observer(display_umidade)
    estacao.adicionar_observer(display_completo)

    estacao.definir_medicoes(25.5, 65.0, 1013.2)
    print("---")
    estacao.definir_medicoes(27.0, 70.0, 1015.1)
