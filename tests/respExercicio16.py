from abc import ABC, abstractmethod
class ProcessadorPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor, cartao):
        pass

class PayPalAPI:
    def make_payment(self, amount, credit_card_number):
        return f"PayPal: Processando ${amount} no cartão {credit_card_number}"
    
class PayPalAdapter(ProcessadorPagamento):
    def __init__(self, api):
        self.api = api

    def processar_pagamento(self, valor, cartao):
        resultado = self.api.make_payment(valor, cartao)
        return resultado

class SistemaPagamento:
    def __init__(self, pagamento: ProcessadorPagamento):
        self.pagamento = pagamento

    def realizar_pagamento(self, valor, cartao):
        print(self.pagamento.processar_pagamento(valor, cartao))



# Sistema funciona com interface padrão
# # processador_interno = ProcessadorPagamentoInterno()
# sistema1 = SistemaPagamento(processador_interno)

# Adapter permite usar PayPal com a mesma interface
paypal_api = PayPalAPI()
paypal_adapter = PayPalAdapter(paypal_api)
sistema2 = SistemaPagamento(paypal_adapter)

# # Ambos funcionam da mesma forma
# sistema1.realizar_pagamento(100.0, "1234-5678")
sistema2.realizar_pagamento(200.0, "8765-4321")