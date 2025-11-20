from abc import ABC, abstractmethod

class CalculadorDesconto():
    @abstractmethod
    def aplicar_desconto(self, valor: float) -> float:
        pass
      
class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.9  # 20% de desconto para estudantes

class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.85  # 15% de desconto para funcionários
      
class DescontoVIP(CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.8  # 20% de desconto para clientes VIP

class ProcessadorPagamento:
    def processar(self, valor: float, estrategia_desconto) -> float:
        return estrategia_desconto.calcular(valor)

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