from abc import ABC, abstractmethod

# --------------------------------------------
# Classe Abstrata (OCP: aberta para extensão)
# --------------------------------------------
class CalculadorDesconto(ABC):

    @abstractmethod
    def calcular(self, valor):
        pass


# --------------------------------------------
# Implementações concretas (sem modificar código existente)
# --------------------------------------------
class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.90  # 10% de desconto


class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.85  # 15% de desconto


class DescontoVIP(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.80  # 20% de desconto


# --------------------------------------------
# Classe que usa qualquer desconto (OCP aplicado)
# --------------------------------------------
class ProcessadorPagamento:
    def processar(self, valor, calculador: CalculadorDesconto):
        return calculador.calcular(valor)


# --------------------------------------------
# Demonstração de uso
# --------------------------------------------
if __name__ == "__main__":

    pagamento = ProcessadorPagamento()
    valor_original = 1000.0

    desconto_estudante = DescontoEstudante()
    desconto_funcionario = DescontoFuncionario()
    desconto_vip = DescontoVIP()

    print("=== Valores com Desconto ===")
    print(f"Estudante: R$ {pagamento.processar(valor_original, desconto_estudante):.2f}")
    print(f"Funcionário: R$ {pagamento.processar(valor_original, desconto_funcionario):.2f}")
    print(f"VIP: R$ {pagamento.processar(valor_original, desconto_vip):.2f}")

    # --------------------------------------------
    # Exemplo de EXTENSÃO (novo desconto)
    # sem modificar código existente
    # --------------------------------------------
    class DescontoBlackFriday(CalculadorDesconto):
        def calcular(self, valor):
            return valor * 0.50  # 50% OFF

    desconto_bf = DescontoBlackFriday()
    print(f"Black Friday: R$ {pagamento.processar(valor_original, desconto_bf):.2f}")
