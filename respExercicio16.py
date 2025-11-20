# Exercício 16 - Padrão Adapter (Estrutural)

class ProcessadorPagamento:
    def processar_pagamento(self, valor, cartao):
        pass

# Serviço externo (não pode ser modificado)
class PayPalAPI:
    def make_payment(self, amount, credit_card_number):
        return f"PayPal: Processando ${amount} no cartão {credit_card_number}"

# Adapter
class PayPalAdapter(ProcessadorPagamento):
    def __init__(self, paypal_api: PayPalAPI):
        self.paypal = paypal_api

    def processar_pagamento(self, valor, cartao):
        return self.paypal.make_payment(valor, cartao)

# Outro processador interno para demonstração
class ProcessadorPagamentoInterno(ProcessadorPagamento):
    def processar_pagamento(self, valor, cartao):
        return f"Interno: Pagamento de ${valor} processado com o cartão {cartao}"

# Sistema de pagamento
class SistemaPagamento:
    def __init__(self, processador: ProcessadorPagamento):
        self.processador = processador

    def realizar_pagamento(self, valor, cartao):
        resultado = self.processador.processar_pagamento(valor, cartao)
        print(resultado)
        return resultado

# Demonstração
if __name__ == "__main__":
    # Sistema com processador interno
    interno = ProcessadorPagamentoInterno()
    sistema1 = SistemaPagamento(interno)

    # Sistema com PayPal usando Adapter
    paypal = PayPalAPI()
    paypal_adapter = PayPalAdapter(paypal)
    sistema2 = SistemaPagamento(paypal_adapter)

    sistema1.realizar_pagamento(100.0, "1234-5678")
    sistema2.realizar_pagamento(200.0, "8765-4321")