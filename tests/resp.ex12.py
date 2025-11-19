from abc import ABC

class CalculadorDesconto(ABC):
    def calcular(self):
        pass


class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor_original):
         valor = valor_original * 0.90
         return valor

class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor_original):
        valor = valor_original * 0.85
        return valor 

class DescontoVIP(CalculadorDesconto):
    def calcular(self, valor_original):
         valor = valor_original * 0.80
         return valor


class ProcessadorPagamento(CalculadorDesconto):
    def processar(self, valor, desconto: CalculadorDesconto):
        valor_desconto = desconto.calcular(valor)
        return valor_desconto
        



# Uso do sistema
pagamento = ProcessadorPagamento()
valor_original = 1000.0

# Diferentes tipos de desconto
desconto_estudante = DescontoEstudante()
desconto_funcionario = DescontoFuncionario()

valor_final1 = pagamento.processar(valor_original, desconto_estudante)
valor_final2 = pagamento.processar(valor_original, desconto_funcionario)

print(f"Estudante: R$ {valor_final1}")
print(f"Funcionário: R$ {valor_final2}")