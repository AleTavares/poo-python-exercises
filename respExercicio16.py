# Exercício 16 - Padrão Adapter

# ----------------------------------------
# 1. Interface esperada pelo sistema
# ----------------------------------------
class ProcessadorPagamento:
    def processar_pagamento(self, valor, cartao):
        pass


# ----------------------------------------
# 2. Serviço externo (não pode ser alterado)
# ----------------------------------------
class PayPalAPI:
    def make_payment(self, amount, credit_card_number):
        return f"PayPal: Processando ${amount} no cartão {credit_card_number}"


# ----------------------------------------
# 3. Adapter para integrar o PayPal ao sistema
# ----------------------------------------
class PayPalAdapter(ProcessadorPagamento):
    def __init__(self, paypal_api: PayPalAPI):
        self.paypal_api = paypal_api

    def processar_pagamento(self, valor, cartao):
        # Adapta o método esperado pelo sistema para o método da API externa
        return self.paypal_api.make_payment(valor, cartao)


# ----------------------------------------
# 4. Outro processador interno (exemplo opcional)
# ----------------------------------------
class ProcessadorPagamentoInterno(ProcessadorPagamento):
    def processar_pagamento(self, valor, cartao):
        return f"Pagamento interno: R${valor} processado no cartão {cartao}"


# ----------------------------------------
# 5. Sistema que usa QUALQUER processador de pagamento
# ----------------------------------------
class SistemaPagamento:
    def __init__(self, processador: ProcessadorPagamento):
        self.processador = processador

    def realizar_pagamento(self, valor, cartao):
        resultado = self.processador.processar_pagamento(valor, cartao)
        print(resultado)


# ----------------------------------------
# Demonstração de uso
# ----------------------------------------
if __name__ == "__main__":
    # Processador interno
    processador_interno = ProcessadorPagamentoInterno()
    sistema1 = SistemaPagamento(processador_interno)
    sistema1.realizar_pagamento(100.0, "1234-5678")

    # Integrando PayPal usando Adapter
    paypal_api = PayPalAPI()
    paypal_adapter = PayPalAdapter(paypal_api)
    sistema2 = SistemaPagamento(paypal_adapter)
    sistema2.realizar_pagamento(200.0, "8765-4321")
