
class Observer:
    def update(self, temperatura, umidade, pressao):
        pass

class EstacaoMeteorologica:
    def __init__(self):
        self.observers = []
        self.temperatura = 0
        self.umidade = 0
        self.pressao = 0

    def adicionar_observer(self, observer):
        self.observers.append(observer)

    def remover_observer(self, observer):
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


class DisplayCompleto(Observer):
    def update(self, temperatura, umidade, pressao):
        print(f"Display Completo: {temperatura}°C, {umidade}%, {pressao} hPa")



