from abc import ABC, abstractmethod


class ProcessadorPagamento(ABC):
    """
    Interface esperada pelo nosso sistema de pagamento.
    """
    @abstractmethod
    def processar_pagamento(self, valor: float, cartao: str) -> str:
        pass


class ProcessadorPagamentoInterno(ProcessadorPagamento):
    """
    Uma implementação concreta que o sistema já usa (Interface Target).
    """
    def processar_pagamento(self, valor: float, cartao: str) -> str:
        return f"Interno: Processando R$ {valor:.2f} no cartão {cartao[:4]}xxxx"


class PayPalAPI:
    """
    O serviço externo com uma interface incompatível.
    Note a diferença nos nomes dos parâmetros (amount, credit_card_number).
    """
    def make_payment(self, amount: float, credit_card_number: str) -> str:
        return f"PayPal API: Pagamento de R$ {amount:.2f} efetuado com sucesso (Cartão: {credit_card_number[-4:]})"


class PayPalAdapter(ProcessadorPagamento):
    """
    Implementa a interface Target e contém o Adaptee.
    Traduz os métodos do nosso sistema para a API do PayPal.
    """
    def __init__(self, paypal_api: PayPalAPI):
        
        self._paypal_api = paypal_api

    def processar_pagamento(self, valor: float, cartao: str) -> str:
        """
        Adapta a chamada: mapeia 'valor' para 'amount' e 'cartao' para 'credit_card_number',
        e chama o método do PayPalAPI.
        """
        
        
        amount = valor
        credit_card_number = cartao
        
     
        return self._paypal_api.make_payment(amount, credit_card_number)


class SistemaPagamento:
    """
    O Cliente do sistema que aceita qualquer ProcessadorPagamento.
    """
    def __init__(self, processador: ProcessadorPagamento):
        self._processador = processador
    
    def realizar_pagamento(self, valor: float, cartao: str):
        print(f"Sistema Pagamento iniciando transação de R$ {valor:.2f}...")
        
      
        resultado = self._processador.processar_pagamento(valor, cartao)
        
        print(f"Resultado da Transação: {resultado}")
        print("-" * 20)


if __name__ == "__main__":
 
    processador_interno = ProcessadorPagamentoInterno()
    paypal_api = PayPalAPI()
    
    paypal_adapter = PayPalAdapter(paypal_api)

    sistema1 = SistemaPagamento(processador_interno)
    
  
    sistema2 = SistemaPagamento(paypal_adapter)

    print("--- Teste com Processador Interno (Target nativo) ---")
    sistema1.realizar_pagamento(100.0, "1234-5678-9012-3456")
    
    print("--- Teste com PayPal via Adapter ---")
    sistema2.realizar_pagamento(200.0, "8765-4321-0987-6543")