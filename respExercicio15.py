from abc import ABC, abstractmethod

class ServicoNotificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

class EmailService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando email: {mensagem}")


class SMSService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")


class PushService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando push: {mensagem}")

class NotificacaoService:
    def __init__(self, servico: ServicoNotificacao):
        self.servico = servico  # depende da abstração

    def notificar(self, mensagem):
        self.servico.enviar(mensagem)



