from abc import ABC, abstractmethod

# Abstração seguindo o DIP
class ServicoNotificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem: str):
        pass


# Implementações concretas
class EmailService(ServicoNotificacao):
    def enviar(self, mensagem: str):
        print(f"Enviando email: {mensagem}")


class SMSService(ServicoNotificacao):
    def enviar(self, mensagem: str):
        print(f"Enviando SMS: {mensagem}")


class PushService(ServicoNotificacao):
    def enviar(self, mensagem: str):
        print(f"Enviando push: {mensagem}")


# Classe que depende da abstração, não da implementação
class NotificacaoService:
    def __init__(self, servico: ServicoNotificacao):  # Injeção de dependência
        self.servico = servico

    def notificar(self, mensagem: str):
        self.servico.enviar(mensagem)


# Demonstração de uso
if __name__ == "__main__":
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
