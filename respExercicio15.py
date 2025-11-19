class NotificacaoService:
    def __init__(self, metodo_notificacao):
        self.metodo_notificacao = metodo_notificacao

    def notificar(self, mensagem):
        self.metodo_notificacao.enviar(mensagem)
        
class EmailService:
    def enviar(self, mensagem):
        print(f"Enviando email com a mensagem: {mensagem}")
        
class SMSService:
    def enviar(self, mensagem):
        print(f"Enviando SMS com a mensagem: {mensagem}")
        
class PushService:
    def enviar(self, mensagem):
        print(f"Enviando notificação push com a mensagem: {mensagem}")

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