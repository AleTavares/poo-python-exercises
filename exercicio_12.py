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
    def processar(self, valor, calculador_desconto):
        return calculador_desconto.calcular(valor)

pagamento = ProcessadorPagamento()
valor_original = 1000.0

desconto_estudante = DescontoEstudante()
desconto_funcionario = DescontoFuncionario()

valor_final1 = pagamento.processar(valor_original, desconto_estudante)
valor_final2 = pagamento.processar(valor_original, desconto_funcionario)

print(f"Estudante: R$ {valor_final1}")
print(f"Funcionário: R$ {valor_final2}")