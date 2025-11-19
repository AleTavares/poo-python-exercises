
class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo


class CalculadoraSalario:
    def calcular_salario_liquido(self, funcionario, descontos):
        """Calcula o salário líquido de um funcionário."""
        return funcionario.salario - descontos


class GeradorRelatorio:
    def gerar_relatorio(self, funcionario):
        """Gera um relatório de apresentação do funcionário."""
        return f"Relatório: {funcionario.nome} - {funcionario.cargo} - Salário Bruto: R$ {funcionario.salario:.2f}"


class RepositorioFuncionario:
    def salvar(self, funcionario):
        """Simula a persistência do objeto Funcionario no banco de dados."""
        print(f"Persistência: Salvando {funcionario.nome} ({funcionario.cargo}) no repositório de dados.")
    
    def buscar(self, nome):
        """Simula a busca de um funcionário."""
        print(f"Persistência: Buscando funcionário {nome}...")
        # Simulação de retorno
        return Funcionario(nome, 4000.0, "Analista Júnior")

if __name__ == "__main__":
    
 
    funcionario = Funcionario("Ana Silva", 5000.0, "Desenvolvedora")
    
   
    calculadora = CalculadoraSalario()
    gerador = GeradorRelatorio()
    repositorio = RepositorioFuncionario()
    


    print("--- Demonstração do SRP ---")
    
   
    descontos = 500.0
    salario_liquido = calculadora.calcular_salario_liquido(funcionario, descontos)
    print(f"Cálculo: Salário Bruto: R$ {funcionario.salario:.2f}, Descontos: R$ {descontos:.2f}")
    print(f"Cálculo: Salário Líquido: R$ {salario_liquido:.2f}")
    
    print("-" * 25)

   
    relatorio = gerador.gerar_relatorio(funcionario)
    print(f"Relatório: {relatorio}")
    
    print("-" * 25)

   
    repositorio.salvar(funcionario)