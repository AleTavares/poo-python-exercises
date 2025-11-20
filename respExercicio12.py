from abc import ABC, abstractmethod

class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular_desconto(self, valor: float) -> float:
        pass
class DescontoEstudante(CalculadorDesconto):
    def calcular_desconto(self, valor: float) -> float:
        return valor * 0.1 # 10%  para estudantes 
    
class DescontoFuncionario(CalculadorDesconto):
    def calcular_desconto(self, valor: float) -> float:
        return valor * 0.15 # 15% para funcionários

class DescontoVIP(CalculadorDesconto):
    def calcular_desconto(self, valor: float) -> float:
        return valor * 0.2 # 20% para convidados

class ProcessadorPagamento:
    def processar(self, valor: float, desconto: CalculadorDesconto) -> float:
        valor_com_desconto = valor - desconto.calcular_desconto(valor)
        return valor_com_desconto
    
if __name__ == "__main__":
    valor_original = 100.0

    processador = ProcessadorPagamento()

    desconto_estudante = DescontoEstudante()
    valor_final_estudante = processador.processar(valor_original, desconto_estudante)
    print(f"Valor final para estudante: R$ {valor_final_estudante}")

    desconto_funcionario = DescontoFuncionario()
    valor_final_funcionario = processador.processar(valor_original, desconto_funcionario)
    print(f"Valor final para funcionário: R$ {valor_final_funcionario}")

    desconto_vip = DescontoVIP()
    valor_final_vip = processador.processar(valor_original, desconto_vip)
    print(f"Valor final para VIP: R$ {valor_final_vip}")
    