from abc import ABC, abstractmethod


class CalculadorDesconto(ABC):
    """
    Interface/Classe Abstrata que define o método obrigatório para cálculo de desconto.
    """
    @abstractmethod
    def calcular(self, valor: float) -> float:
        """
        Retorna o valor final após a aplicação do desconto.
        """
        pass



class DescontoEstudante(CalculadorDesconto):
    """Implementa 10% de desconto."""
    def calcular(self, valor: float) -> float:
        return valor * 0.90 

class DescontoFuncionario(CalculadorDesconto):
    """Implementa 15% de desconto."""
    def calcular(self, valor: float) -> float:
        return valor * 0.85 

class DescontoVIP(CalculadorDesconto):
    """Implementa 20% de desconto."""
    def calcular(self, valor: float) -> float:
        return valor * 0.80 


class ProcessadorPagamento:
    """
    Processa o pagamento aceitando qualquer objeto que implemente CalculadorDesconto.
    Esta classe não precisa ser modificada quando um novo desconto é criado.
    """
    def processar(self, valor_original: float, calculadora: CalculadorDesconto) -> float:
        """
        Calcula o valor final usando a calculadora de desconto fornecida.
        """
        print(f"Processando pagamento de R$ {valor_original:.2f}...")
        return calculadora.calcular(valor_original)



if __name__ == "__main__":
    pagamento = ProcessadorPagamento()
    valor_original = 1000.0

    desconto_estudante = DescontoEstudante()
    desconto_funcionario = DescontoFuncionario()

    valor_final1 = pagamento.processar(valor_original, desconto_estudante)
    valor_final2 = pagamento.processar(valor_original, desconto_funcionario)

    print(f"\n--- Resultados Iniciais ---")
    print(f"Estudante (10%): R$ {valor_final1:.2f}")
    print(f"Funcionário (15%): R$ {valor_final2:.2f}")

    print("\n" + "=" * 40)
    print("DEMONSTRAÇÃO DO OCP: ADICIONANDO UM NOVO DESCONTO")
    print("=" * 40)


    desconto_vip = DescontoVIP()

    valor_final3 = pagamento.processar(valor_original, desconto_vip)

    print(f"\n--- Novo Resultado (VIP) ---")
    print(f"VIP (20%): R$ {valor_final3:.2f}")