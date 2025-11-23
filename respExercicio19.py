#Implementar o padrão de projeto Observer para notificação de mudanças de estado.

## Descrição do Exercício
#Crie um sistema de notificações onde múltiplos observadores são notificados quando o estado de um objeto muda.

from abc import ABC, abstractmethod

# Classe Observador (Observer)
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Classe Sujeito (Subject)
class EstacaoMeteorologica:
    def __init__(self):
        self.observers = []
        self.temperatura = None
        self.umidade = None
        self.pressao = None

    def adicionar_observer(self, observer):
        self.observers.append(observer)

    def remover_observer(self, observer):
        self.observers.remove(observer)

    def notificar_observers(self):
        for observer in self.observers:
            observer.update(self.temperatura, self.umidade, self.pressao)

    def definir_medicoes(self, temperatura, umidade, pressao):
        self.temperatura = temperatura
        self.umidade = umidade
        self.pressao = pressao
        self.notificar_observers()

   # Observers Concretos

class DisplayTemperatura(Observer):
    def update(self, temperatura, umidade, pressao):
         print(f"Display Temperatura: {temperatura}°C")

class DisplayUmidade(Observer):
    def update(self, temperatura, umidade, pressao):
        print(f"Display Umidade: {umidade}%")
class DisplayCompleto(Observer):
    def update(self, temperatura, umidade, pressao):
        print(f"Display Completo: {temperatura}°C, {umidade}%, {pressao} hPa")


# Demonstração de uso
if __name__ == "__main__":

    estacao = EstacaoMeteorologica()

    # Criando displays
    display_temp = DisplayTemperatura()
    display_umidade = DisplayUmidade()
    display_completo = DisplayCompleto()

    # Registrando observadores
    estacao.adicionar_observer(display_temp)
    estacao.adicionar_observer(display_umidade)
    estacao.adicionar_observer(display_completo)

    # Mudança de estado
    estacao.definir_medicoes(25.5, 65.0, 1013.2)
    estacao.definir_medicoes(27.0, 70.0, 1015.1)