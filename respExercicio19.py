class Observer:
  def update(self, temperature, humidity, pressure):
    pass

class EstacaoMeteorologica:
  def __init__(self):
    self.observers = []
    self.temperature = 0
    self.humidity = 0
    self.pressure = 0

  def register_observer(self, observer):
    self.observers.append(observer)

  def remove_observer(self, observer):
    self.observers.remove(observer)

  def notify_observers(self):
    for observer in self.observers:
      observer.update(self.temperature, self.humidity, self.pressure)

  def set_measurements(self, temperature, humidity, pressure):
    self.temperature = temperature
    self.humidity = humidity
    self.pressure = pressure
    self.notify_observers()

class DisplayTemperatura(Observer):
  def update(self, temperature, humidity, pressure):
    print(f"Temperatura Atual: {temperature}°C")

class DisplayUmidade(Observer):
  def update(self, temperature, humidity, pressure):
    print(f"Umidade Atual: {humidity}%")

class DisplayCompleto(Observer):
  def update(self, temperature, humidity, pressure):
    print(f"Temperatura: {temperature}°C, Umidade: {humidity}%, Pressão: {pressure} hPa")

if __name__ == "__main__":
  estacao = EstacaoMeteorologica()

  display_temp = DisplayTemperatura()
  display_umid = DisplayUmidade()
  display_completo = DisplayCompleto()

  estacao.register_observer(display_temp)
  estacao.register_observer(display_umid)
  estacao.register_observer(display_completo)

  estacao.set_measurements(25, 65, 1013)
  estacao.set_measurements(28, 70, 1012)