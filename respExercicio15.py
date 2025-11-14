from abc import ABC, abstractmethod

# -----------------------------
# 1. Abstração (DIP aplicado)
# -----------------------------
class ServicoNotificacao(ABC):

    @abstractmethod
    def enviar(self, mensagem):
        pass


# -----------------------------
# 2. Implementações concretas
# -----------------------------
class EmailService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando email: {mensagem}")


class SMSService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")


class PushService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando push: {mensagem}")


# -----------------------------
# 3. Serviço que DEPENDE da abstração (não de implementações)
# -----------------------------
class NotificacaoService:
    def __init__(self, servico: ServicoNotificacao):   # Injeção de dependência
        self.servico = servico

    def notificar(self, mensagem):
        self.servico.enviar(mensagem)


# -----------------------------
# 4. Demonstração de uso
# -----------------------------
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
