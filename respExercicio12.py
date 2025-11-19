from abc import ABC, abstractmethod

# -------------------------------------------
# Classe abstrata (aberta para extensão)
# -------------------------------------------

class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass


# -------------------------------------------
# Tipos de desconto (novas classes não exigem modificar código existente)
# -------------------------------------------

class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.90  # 10% de desconto


class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.85  # 15% de desconto


class DescontoVIP(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.80  # 20% de desconto


# Exemplo de extensão sem modificar código existente
class DescontoBlackFriday(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.50  # 50% de desconto


# -------------------------------------------
# Classe que processa pagamentos usando QUALQUER desconto
# -------------------------------------------

class ProcessadorPagamento:
    def processar(self, valor, calculador_desconto: CalculadorDesconto):
        return calculador_desconto.calcular(valor)


# -------------------------------------------
# Exemplo de uso
# -------------------------------------------

if __name__ == "__main__":
    pagamento = ProcessadorPagamento()
    valor_original = 1000.0

    desconto_estudante = DescontoEstudante()
    desconto_funcionario = DescontoFuncionario()

    valor_final1 = pagamento.processar(valor_original, desconto_estudante)
    valor_final2 = pagamento.processar(valor_original, desconto_funcionario)

    print(f"Estudante: R$ {valor_final1}")
    print(f"Funcionário: R$ {valor_final2}")