from abc import ABC, abstractmethod

class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.90


class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.85

class DescontoVIP(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.80

class ProcessadorPagamento:
    def processar(self, valor, calculadora_desconto: CalculadorDesconto):
        return calculadora_desconto.calcular(valor)


if __name__ == "__main__":
    pagamento = ProcessadorPagamento()
    valor_original = 1000.0

    desconto_estudante = DescontoEstudante()
    desconto_funcionario = DescontoFuncionario()
    desconto_vip = DescontoVIP()

    print("Estudante:", pagamento.processar(valor_original, desconto_estudante))
    print("Funcionário:", pagamento.processar(valor_original, desconto_funcionario))
    print("VIP:", pagamento.processar(valor_original, desconto_vip))

    class DescontoBlackFriday(CalculadorDesconto):
        def calcular(self, valor):
            return valor * 0.50

    desconto_bf = DescontoBlackFriday()
    print("Black Friday:", pagamento.processar(valor_original, desconto_bf))
