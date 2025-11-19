from abc import ABC, abstractmethod

# =====================================
# Abstração (Interface) — DIP aplicado
# =====================================

class ServicoNotificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass


# =====================================
# Implementações concretas
# =====================================

class EmailService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando email: {mensagem}")


class SMSService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")


class PushService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando push: {mensagem}")


# =====================================
# Classe que DEPENDE da abstração
# (injeção de dependência)
# =====================================

class NotificacaoService:
    def __init__(self, servico: ServicoNotificacao):
        self.servico = servico  # DIP: depende da abstração, não da implementação

    def notificar(self, mensagem):
        self.servico.enviar(mensagem)



if __name__ == "__main__":
    email_service = EmailService()
    sms_service = SMSService()
    push_service = PushService()

    # Mesmo código funciona com qualquer serviço
    notificador1 = NotificacaoService(email_service)
    notificador2 = NotificacaoService(sms_service)
    notificador3 = NotificacaoService(push_service)

    mensagem = "Bem-vindo ao sistema!"
    
    notificador1.notificar(mensagem)
    notificador2.notificar(mensagem)
    notificador3.notificar(mensagem)
