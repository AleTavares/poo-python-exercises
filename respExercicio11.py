class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

class calcular_salario:
        def calcular_salario_liquido(self, funcionario,descontos):
             return funcionario.salario -descontos
        

class Gerador_relatorio:
    def gerar_relatorio(self, funcionario, salario_liquido):
        return f"Funcionário: {funcionario.nome}\nCargo: {funcionario.cargo}\nSalário Líquido: R$ {salario_liquido:.2f}"
    
        
class RepositorioFuncionario:
    def salvar(self, funcionario):
        print(f"Salvando {funcionario.nome} no banco de dados...")

funcionario = Funcionario("Ana Silva", 5000.0, "Desenvolvedora")
calculadora = calcular_salario()
gerador = Gerador_relatorio()
repositorio = RepositorioFuncionario()

salario_liquido = calculadora.calcular_salario_liquido(funcionario, 500.0)
relatorio = gerador.gerar_relatorio(funcionario, salario_liquido)
repositorio.salvar(funcionario)