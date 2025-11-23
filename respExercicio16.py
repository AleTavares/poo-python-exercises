class ProcessadorPagamento:
    def processar_pagamento(self, valor, cartao):
        pass
class PayPalAPI:
    def make_payment(self, amount, credit_card_number):
        return f"PayPal: Processando ${amount} no cartão {credit_card_number}"
    
    #crie o adaptador
class PayPalAdapter(ProcessadorPagamento):
    def __init__(self, paypal_api):
        self.paypal_api = paypal_api

    def processar_pagamento(self, valor, cartao):
        return self.paypal_api.make_payment(valor, cartao)
    
#Processador de pagamento interno (exemplo)

class ProcessadorPagamentoInterno(ProcessadorPagamento):
    def processar_pagamento(self, valor, cartao):
        return f"Sistema Interno: Processando ${valor} no cartão {cartao}"
    
#qualquer processador de pagamento pode ser usado aqui
class SistemaPagamento:
    def __init__(self, processador: ProcessadorPagamento):
        self.processador = processador

    def realizar_pagamento(self, valor, cartao):
        resultado = self.processador.processar_pagamento(valor, cartao)
        print(resultado)

if __name__ == "__main__":
 
#uso
# Sistema funciona com interface padrão
 processador_interno = ProcessadorPagamentoInterno()
 sistema1 = SistemaPagamento(processador_interno)


# Adapter permite usar PayPal com a mesma interface
 paypal_api = PayPalAPI()
 paypal_adapter = PayPalAdapter(paypal_api)
 sistema2 = SistemaPagamento(paypal_adapter)


# Ambos funcionam da mesma forma
 sistema1.realizar_pagamento(100.0, "1234-5678")
 sistema2.realizar_pagamento(200.0, "8765-4321")

 


