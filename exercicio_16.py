class ProcessadorPagamento:
    def processar_pagamento(self, valor, cartao):
        print(f"Pagamento padrão de ${valor} no cartão {cartao}")

class PayPalAPI:
    def make_payment(self, amount, credit_card_number):
        return f"PayPal: Processando ${amount} no cartão {credit_card_number}"

class PayPalAdapter(ProcessadorPagamento):
    def __init__(self, paypal_api):
        self.paypal_api = paypal_api

    def processar_pagamento(self, valor, cartao):
        print(self.paypal_api.make_payment(valor, cartao))

class SistemaPagamento:
    def __init__(self, processador):
        self.processador = processador

    def realizar_pagamento(self, valor, cartao):
        self.processador.processar_pagamento(valor, cartao)

processador_interno = ProcessadorPagamento()
sistema1 = SistemaPagamento(processador_interno)

paypal_api = PayPalAPI()
paypal_adapter = PayPalAdapter(paypal_api)
sistema2 = SistemaPagamento(paypal_adapter)

sistema1.realizar_pagamento(100.0, "1234-5678")
sistema2.realizar_pagamento(200.0, "8765-4321")