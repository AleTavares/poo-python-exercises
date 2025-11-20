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
        print(f"Enviando notificação push: {mensagem}")

class NotificacaoService:
    def __init__(self, servico: ServicoNotificacao):
        self.servico = servico  # Injeção de dependência

    def notificar(self, mensagem):
        self.servico.enviar(mensagem)

if __name__ == "__main__":
   
    email_service = EmailService()
    notificacao = NotificacaoService(email_service)
    notificacao.notificar("Mensagem via Email")

    sms_service = SMSService()
    notificacao = NotificacaoService(sms_service)
    notificacao.notificar("Mensagem via SMS")

 
    push_service = PushService()
    notificacao = NotificacaoService(push_service)
    notificacao.notificar("Mensagem via Push")

# Diferentes implementações podem ser injetadas
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