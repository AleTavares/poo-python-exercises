class Funcionario:
    """
    Classe responsável apenas por armazenar os dados do funcionário.
    """
    def __init__(self, nome: str, salario: float, cargo: str):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo


class CalculadoraSalario:
    """
    Classe responsável apenas por cálculos relacionados ao salário.
    """
    def calcular_salario_liquido(self, funcionario: Funcionario, descontos: float) -> float:
        return funcionario.salario - descontos


class GeradorRelatorio:
    """
    Classe responsável apenas pela geração de relatórios.
    """
    def gerar_relatorio(self, funcionario: Funcionario) -> str:
        return f"Relatório: {funcionario.nome} - {funcionario.cargo} - R$ {funcionario.salario}"


class RepositorioFuncionario:
    """
    Classe responsável apenas pela persistência de dados.
    """
    def salvar(self, funcionario: Funcionario):
        # Aqui seria feita a lógica de banco de dados
        print(f"Salvando {funcionario.nome} no banco de dados...")


# Demonstração de Uso
if __name__ == "__main__":
    funcionario = Funcionario("Ana Silva", 5000.0, "Desenvolvedora")
    calculadora = CalculadoraSalario()
    gerador = GeradorRelatorio()
    repositorio = RepositorioFuncionario()

    salario_liquido = calculadora.calcular_salario_liquido(funcionario, 500.0)
    relatorio = gerador.gerar_relatorio(funcionario)
    repositorio.salvar(funcionario)

    print("Salário líquido:", salario_liquido)
    print("Relatório:", relatorio)
