# Exercício 15 - Princípio da Inversão de Dependência (DIP)

## Objetivo
#Aplicar o quinto princípio SOLID - Dependency Inversion Principle (DIP).

## Descrição do Exercício
#Refatore código que depende de implementações concretas para depender de abstrações.


from abc import ABC, abstractmethod 


#abstração
class ServicoNotificacao(ABC):
    @abstractmethod
    def enviar (self, mensagem):
        pass

    #concretas

class EmailService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando email com a mensagem: {mensagem}")

class SMSService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando SMS com a mensagem: {mensagem}")

class PushService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando notificação push com a mensagem: {mensagem}")

#Alta camada de depende da abstraçã, não da implementação concreta

class NotificadorService:
    def __init__(self, servico: ServicoNotificacao):
        self.servico = servico #injeção de dependência

    def notificar(self, mensagem):
        self.servico.enviar(mensagem)

        #demonstração
if __name__ == "__main__":
    email_service = EmailService()
    sms_service = SMSService()
    push_service = PushService()

    notificador_email = NotificadorService(email_service)
    notificador_sms = NotificadorService(sms_service)
    notificador_push = NotificadorService(push_service)

    mensagem = "Bem-vindo ao sistema!"

    notificador_email.notificar(mensagem)
    notificador_sms.notificar(mensagem)
    notificador_push.notificar(mensagem)
