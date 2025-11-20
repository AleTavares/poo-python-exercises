# Exercício 15 – Princípio da Inversão de Dependência (DIP)

from abc import ABC, abstractmethod

# Abstração
class ServicoNotificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

# Implementações concretas
class EmailService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando email: {mensagem}")

class SMSService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")

class PushService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando push: {mensagem}")

# NotificacaoService depende da abstração
class NotificacaoService:
    def __init__(self, servico_notificacao: ServicoNotificacao):
        self.servico = servico_notificacao

    def notificar(self, mensagem):
        self.servico.enviar(mensagem)

# Demonstração
if __name__ == "__main__":
    email_service = EmailService()
    sms_service = SMSService()
    push_service = PushService()

    notificador1 = NotificacaoService(email_service)
    notificador2 = NotificacaoService(sms_service)
    notificador3 = NotificacaoService(push_service)

    mensagem = "Bem-vindo ao sistema!"
    notificador1.notificar(mensagem)
    notificador2.notificar(mensagem)
    notificador3.notificar(mensagem)