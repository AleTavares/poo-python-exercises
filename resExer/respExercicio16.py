class ProcessadorPagamento:
    def processar_pagamento(self, valor, cartao):
        raise NotImplementedError("Implementar na subclasse")


class PayPalAPI:
    def make_payment(self, amount, credit_card_number):
        return f"PayPal: Processando ${amount} no cartão {credit_card_number}"


class PayPalAdapter(ProcessadorPagamento):
    def __init__(self, paypal_api: PayPalAPI):
        self.paypal = paypal_api

    def processar_pagamento(self, valor, cartao):
        return self.paypal.make_payment(valor, cartao)


class ProcessadorPagamentoInterno(ProcessadorPagamento):
    def processar_pagamento(self, valor, cartao):
        return f"Processador interno: Cobrança de R${valor} feita no cartão {cartao}"


class SistemaPagamento:
    def __init__(self, processador: ProcessadorPagamento):
        self.processador = processador

    def realizar_pagamento(self, valor, cartao):
        resultado = self.processador.processar_pagamento(valor, cartao)
        print(resultado)

# Exemplo de uso
if __name__ == "__main__":
    processador_interno = ProcessadorPagamentoInterno()
    sistema1 = SistemaPagamento(processador_interno)

    paypal_api = PayPalAPI()
    paypal_adapter = PayPalAdapter(paypal_api)
    sistema2 = SistemaPagamento(paypal_adapter)

    sistema1.realizar_pagamento(100.0, "1234-5678")
    sistema2.realizar_pagamento(200.0, "8765-4321")