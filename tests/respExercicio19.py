from abc import ABC, abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self, temperatura, umidade, pressao):
        pass


class EstacaoMeteorologica:
    def __init__(self):
        self.observers = []
        self.temperatura = None
        self.umidade = None
        self.pressao = None

    def adicionar_observer(self, observer):
        self.observers.append(observer)

    def remover_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notificar_observers(self):
        for obs in self.observers:
            obs.update(self.temperatura, self.umidade, self.pressao)

    def definir_medicoes(self, temperatura, umidade, pressao):
        self.temperatura = temperatura
        self.umidade = umidade
        self.pressao = pressao
        self.notificar_observers()


class DisplayTemperatura(Observer):
    def update(self, temperatura, umidade, pressao):
        print(f"Display Temperatura: {temperatura}°C")


class DisplayUmidade(Observer):
    def update(self, temperatura, umidade, pressao):
        print(f"Display Umidade: {umidade}%")

class DisplayPressao(Observer):
    def update(self, temperatura, umidade, pressao):
        print(f"Display Pressão: {pressao} hpa")

class DisplayCompleto(Observer):
    def update(self, temperatura, umidade, pressao):
        print(
            f"Display Completo: Temp: {temperatura}°C Umidade: {umidade}%  Pressão: {pressao} hPa")


estacao = EstacaoMeteorologica()

display_temp = DisplayTemperatura()
display_umidade = DisplayUmidade()
display_pressao = DisplayPressao()
display_completo = DisplayCompleto()

estacao.adicionar_observer(display_temp)
estacao.adicionar_observer(display_umidade)
estacao.adicionar_observer(display_pressao)
estacao.adicionar_observer(display_completo)

estacao.definir_medicoes(25.5, 65.0, 1013.2)
estacao.definir_medicoes(27.0, 70.0, 1015.1)
