class CalculadorDesconto:
    def calcular(self, valor):
        pass

#Tipos de Desconto

class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.90
    
class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.85
    
class DescontoVIP(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.80
    
#Aceita qualquer objeto que implemente CalculadorDesconto:

class ProcessadorPagamento:

    def __init__(self, calculador_desconto: CalculadorDesconto):
        self.calculador_desconto = calculador_desconto

    def processar(self, valor):
        return self.calculador_desconto.calcular(valor)

#Demonstração do uso

valor = 100

p1 = ProcessadorPagamento(DescontoEstudante())
print("Estudante:", p1.processar(valor))

p2 = ProcessadorPagamento(DescontoFuncionario())
print("Funcionário:", p2.processar(valor))

p3 = ProcessadorPagamento(DescontoVIP())
print("VIP:", p3.processar(valor))

# Adicionando um novo tipo de desconto sem modificar código existente

class DescontoAniversario(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.70
    
p4 = ProcessadorPagamento(DescontoAniversario())
print("Aniversário:", p4.processar(100))
