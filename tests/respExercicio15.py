from abc import ABC, abstractmethod

class ServicoNotificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        ...

class EmailService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando email: {mensagem}")

class SMSService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")

class PushService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando Push: {mensagem}")

class NotificacaoService:
    def __init__(self, servico: ServicoNotificacao):
        self.servico = servico
    
    def notificar(self, mensagem):
        self.servico.enviar(mensagem)


email_service = EmailService()
sms_service = SMSService()
push_service = PushService()

# Mesmo código cliente funciona com qualquer implementação
notificador1 = NotificacaoService(email_service)
notificador2 = NotificacaoService(sms_service)
notificador3 = NotificacaoService(push_service)

mensagem = "Bem-vindo ao sistema!"
notificador1.notificar(mensagem)
notificador2.notificar(mensagem)
notificador3.notificar(mensagem)