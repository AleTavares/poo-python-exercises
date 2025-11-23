from abc import ABC, abstractmethod

class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass


class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.90  # 10%


class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.85  # 15%


class DescontoVIP(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.80  # 20%


class ProcessadorPagamento:
    def processar(self, valor, estrategia: CalculadorDesconto):
        return estrategia.calcular(valor)


# Demonstração de extensão sem modificar código existente
class DescontoNetshoes(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.75  # 25%


if __name__ == "__main__":
    pagamento = ProcessadorPagamento()
    valor_original = 1000.0

    print("Estudante:", pagamento.processar(valor_original, DescontoEstudante()))
    print("Funcionário:", pagamento.processar(valor_original, DescontoFuncionario()))
    print("VIP:", pagamento.processar(valor_original, DescontoVIP()))
    print("Netshoes:", pagamento.processar(valor_original, DescontoNetshoes()))
