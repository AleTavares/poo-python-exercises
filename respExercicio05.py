# respExercicio05.py
# Exercício 05 - Herança e o Uso de super()

# Classe base
class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


# Classe filha Funcionario, herdando de Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, cargo, salario):
        # Chama o construtor da classe base (Pessoa)
        super().__init__(nome, cpf, data_nascimento)
        # Adiciona os atributos específicos de Funcionario
        self.cargo = cargo
        self.salario = salario

    def exibir_dados(self):
        """Exibe todos os dados do funcionário."""
        print("=== Dados do Funcionário ===")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R$ {self.salario}")


# Exemplo de uso
if __name__ == "__main__":
    funcionario = Funcionario("Ana Costa", "111.222.333-44", "20/03/1988", "Coordenadora", 4500.0)
    funcionario.exibir_dados()
