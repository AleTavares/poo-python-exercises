from abc import ABC, abstractmethod


# Classe abstrata seguindo OCP
class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass


# Tipos de desconto (extensões sem modificar código existente)
class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.90


class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.85


class DescontoVIP(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.80


# Classe que processa pagamentos usando qualquer estratégia de desconto
class ProcessadorPagamento:
    def processar(self, valor, calculadora_desconto: CalculadorDesconto):
        return calculadora_desconto.calcular(valor)


# Demonstração de extensão sem alterar o código existente
# Novo tipo de desconto
class DescontoBlackFriday(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.50


# Demonstração de uso
if __name__ == "__main__":
    pagamento = ProcessadorPagamento()
    valor_original = 1000.0

    desconto_estudante = DescontoEstudante()
    desconto_funcionario = DescontoFuncionario()
    desconto_vip = DescontoVIP()
    desconto_bf = DescontoBlackFriday()  # Novo desconto sem alterar código existente

    print("Estudante:", pagamento.processar(valor_original, desconto_estudante))
    print("Funcionário:", pagamento.processar(valor_original, desconto_funcionario))
    print("VIP:", pagamento.processar(valor_original, desconto_vip))
    print("Black Friday:", pagamento.processar(valor_original, desconto_bf))
    