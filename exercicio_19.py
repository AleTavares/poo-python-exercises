from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temp, umid, pressao): pass

class EstacaoMeteorologica:
    def __init__(self):
        self.observers = []
        self.temp = 0
        self.umid = 0
        self.pressao = 0

    def adicionar_observer(self, observer):
        self.observers.append(observer)

    def remover_observer(self, observer):
        self.observers.remove(observer)

    def notificar_observers(self):
        for observer in self.observers:
            observer.update(self.temp, self.umid, self.pressao)

    def definir_medicoes(self, temp, umid, pressao):
        self.temp = temp
        self.umid = umid
        self.pressao = pressao
        self.notificar_observers()

class DisplayTemperatura(Observer):
    def update(self, temp, umid, pressao):
        print(f"Display Temperatura: {temp}°C")

class DisplayUmidade(Observer):
    def update(self, temp, umid, pressao):
        print(f"Display Umidade: {umid}%")

class DisplayCompleto(Observer):
    def update(self, temp, umid, pressao):
        print(f"Display Completo: {temp}°C, {umid}%, {pressao} hPa")

estacao = EstacaoMeteorologica()
display_temp = DisplayTemperatura()
display_umidade = DisplayUmidade()
display_completo = DisplayCompleto()

estacao.adicionar_observer(display_temp)
estacao.adicionar_observer(display_umidade)
estacao.adicionar_observer(display_completo)

estacao.definir_medicoes(25.5, 65.0, 1013.2)
estacao.definir_medicoes(27.0, 70.0, 1015.1)