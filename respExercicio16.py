from abc import ABC, abstractmethod

class ProcessadorPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor, cartao):
        pass


class PayPalAPI:
    def make_payment(self, valor, cartao):
        return f"Pagamento de R${valor} realizado via PayPal com o cartão {cartao}."


class PayPalAdapter(ProcessadorPagamento):
    def __init__(self, paypal_api):
        self.paypal_api = paypal_api

    def processar_pagamento(self, valor, cartao):
        return self.paypal_api.make_payment(valor, cartao)


class SistemaPagamento:
    def __init__(self, processador_pagamento):
        self.processador_pagamento = processador_pagamento

    def realizar_pagamento(self, valor, cartao):
        return self.processador_pagamento.processar_pagamento(valor, cartao)


if __name__ == "__main__":
    
    paypal_api = PayPalAPI()

    
    paypal_adapter = PayPalAdapter(paypal_api)

    
    sistema = SistemaPagamento(paypal_adapter)
    resultado = sistema.realizar_pagamento(100, "1234-5678-9876-5432")
    print(resultado)


