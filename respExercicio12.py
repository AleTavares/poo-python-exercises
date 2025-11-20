from abc import ABC, abstractmethod

class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass

class Desconto_Estudante(CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.90

class Desconto_Funcionario (CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.85
    
class Desconto_Vip (CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.80
    
class Processador_Pagamento:
    def __init__(self, calculador_desconto):
        self.calculador_desconto = calculador_desconto

    def processar(self, valor):
        return self.calculador_desconto.calcular(valor)
    


pagamento = Processador_Pagamento(None)
valor_original = 100.0

desconto_estudante = Desconto_Estudante()
desconto_funcionario = Desconto_Funcionario()

pagamento_estudante = Processador_Pagamento(desconto_estudante)
pagamento_funcionario = Processador_Pagamento(desconto_funcionario)

print(f"Estudante: R$ {pagamento_estudante.processar(valor_original)}")
print(f"Funcionário: R$ {pagamento_funcionario.processar(valor_original)}")