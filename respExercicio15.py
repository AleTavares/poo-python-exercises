from abc import ABC, abstractmethod


class ServicoNotificacao(ABC):
    """
    Define a interface/contrato que todos os serviços de envio devem seguir.
    """
    @abstractmethod
    def enviar(self, mensagem: str):
        pass



class EmailService(ServicoNotificacao):
    """Implementação concreta de envio por Email."""
    def enviar(self, mensagem: str):
        print(f"Enviando email: {mensagem}")

class SMSService(ServicoNotificacao):
    """Implementação concreta de envio por SMS."""
    def enviar(self, mensagem: str):
        print(f"Enviando SMS: {mensagem}")

class PushService(ServicoNotificacao):
    """Implementação concreta de envio de notificação Push."""
    def enviar(self, mensagem: str):
        print(f"Enviando push: {mensagem}")


class NotificacaoService:

    def __init__(self, servico: ServicoNotificacao):
        
        self._servico_notificacao = servico
    
    def notificar(self, mensagem: str):
        """
        O método notificar usa o método 'enviar' da abstração injetada.
        """
        self._servico_notificacao.enviar(mensagem)


if __name__ == "__main__":
    
   
    email_service = EmailService()
    sms_service = SMSService()
    push_service = PushService()

    mensagem = "Bem-vindo ao sistema!"

    print("--- Injeção de Dependência (DIP) ---")
    
    
    notificador1 = NotificacaoService(email_service)
    notificador1.notificar(mensagem)

   
    notificador2 = NotificacaoService(sms_service)
    notificador2.notificar(mensagem)
    
    
    notificador3 = NotificacaoService(push_service)
    notificador3.notificar(mensagem)
    
    print("-" * 40)
    print("O módulo NotificacaoService (alto nível) funciona de forma idêntica")
    print("com todas as implementações (baixo nível), pois dependem da mesma Abstração.")