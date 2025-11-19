 #Interface esperada pelo sistema
class ProcessadorPagamento:
    def processar_pagamento(self, valor, cartao):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")


# Serviço externo (NÃO pode ser modificado)
class PayPalAPI:
    def make_payment(self, amount, credit_card_number):
        return f"PayPal: Processando ${amount} no cartão {credit_card_number}"


# Processador interno padrão do sistema
class ProcessadorPagamentoInterno(ProcessadorPagamento):
    def processar_pagamento(self, valor, cartao):
        return f"Sistema Interno: Pagamento de R${valor} processado no cartão {cartao}"


# ADAPTER — converte PayPalAPI para a interface esperada
class PayPalAdapter(ProcessadorPagamento):
    def __init__(self, paypal_api: PayPalAPI):
        self.paypal_api = paypal_api

    def processar_pagamento(self, valor, cartao):
        # Converte chamada local para chamada do serviço externo
        return self.paypal_api.make_payment(valor, cartao)


# Sistema que usa qualquer processador com interface padrão
class SistemaPagamento:
    def __init__(self, processador: ProcessadorPagamento):
        self.processador = processador

    def realizar_pagamento(self, valor, cartao):
        resultado = self.processador.processar_pagamento(valor, cartao)
        print(resultado)


if __name__ == "__main__":
    # Sistema com processador interno
    processador_interno = ProcessadorPagamentoInterno()
    sistema1 = SistemaPagamento(processador_interno)

    # Sistema com PayPal via Adapter
    paypal_api = PayPalAPI()
    paypal_adapter = PayPalAdapter(paypal_api)
    sistema2 = SistemaPagamento(paypal_adapter)

    # Testando pagamentos
    sistema1.realizar_pagamento(100.0, "1234-5678")
    sistema2.realizar_pagamento(200.0, "8765-4321")