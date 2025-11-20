
class ProcessadorPagamento:
    def processar_pagamento(self, valor, cartao):
        pass


class ProcessadorPagamentoInterno(ProcessadorPagamento):
    def processar_pagamento(self, valor, cartao):
        return f"Pagamento interno de R${valor} realizado no cartão {cartao}"


class PayPalAPI:
    def make_payment(self, amount, credit_card_number):
        return f"PayPal: Processando ${amount} no cartão {credit_card_number}"

class PayPalAdapter(ProcessadorPagamento):
    def __init__(self, paypal_api):
        self.paypal_api = paypal_api

    def processar_pagamento(self, valor, cartao):
        return self.paypal_api.make_payment(valor, cartao)

class SistemaPagamento:
    def __init__(self, processador):
        self.processador = processador

    def realizar_pagamento(self, valor, cartao):
        resultado = self.processador.processar_pagamento(valor, cartao)
        print(resultado)


