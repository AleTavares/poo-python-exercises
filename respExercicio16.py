# Exercício 16 - Padrão Adapter

# Interface esperada pelo sistema
class ProcessadorPagamento:
    def processar_pagamento(self, valor, cartao):
        pass


# Serviço externo (não pode ser modificado)
class PayPalAPI:
    def make_payment(self, amount, credit_card_number):
        return f"PayPal: Processando ${amount} no cartão {credit_card_number}"


# Implementação interna do sistema
class ProcessadorPagamentoInterno(ProcessadorPagamento):
    def processar_pagamento(self, valor, cartao):
        print(f"Interno: Processando pagamento de R$ {valor} no cartão {cartao}")


# Adapter para integrar PayPal com interface esperada
class PayPalAdapter(ProcessadorPagamento):
    def __init__(self, paypal_api: PayPalAPI):
        self.paypal = paypal_api

    def processar_pagamento(self, valor, cartao):
        resposta = self.paypal.make_payment(valor, cartao)
        print(resposta)


# Sistema cliente que usa qualquer ProcessadorPagamento
class SistemaPagamento:
    def __init__(self, processador: ProcessadorPagamento):
        self.processador = processador

    def realizar_pagamento(self, valor, cartao):
        self.processador.processar_pagamento(valor, cartao)


# Demonstração de Uso
if __name__ == "__main__":
    # Sistema com processador interno
    processador_interno = ProcessadorPagamentoInterno()
    sistema1 = SistemaPagamento(processador_interno)

    # Sistema usando o Adapter do PayPal
    paypal_api = PayPalAPI()
    paypal_adapter = PayPalAdapter(paypal_api)
    sistema2 = SistemaPagamento(paypal_adapter)

    # Ambos funcionando da mesma forma
    sistema1.realizar_pagamento(100.0, "1234-5678")
    sistema2.realizar_pagamento(200.0, "8765-4321")
