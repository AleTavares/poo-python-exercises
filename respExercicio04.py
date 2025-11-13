# respExercicio04.py
# Exercício 04 - Herança Simples (Especialização)

# Classe base (superclasse)
class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def apresentar(self):
        """Retorna uma apresentação básica da pessoa."""
        return f"Olá, sou {self.nome}, CPF: {self.cpf}"


# Classe derivada (subclasse) Funcionario
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, cargo):
        # Reaproveita o construtor da classe base
        super().__init__(nome, cpf, data_nascimento)
        self.cargo = cargo


# Classe derivada (subclasse) Tutor
class Tutor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, area_atuacao):
        super().__init__(nome, cpf, data_nascimento)
        self.area_atua  cao = area_atuacao

    # Sobrescrita (override) do método apresentar
    def apresentar(self):
        """Retorna uma apresentação personalizada para o Tutor."""
        return f"Olá, sou {self.nome}, CPF: {self.cpf}, atuo na área de {self.area_atuacao}"


# Exemplo de uso
if __name__ == "__main__":
    funcionario = Funcionario("João Silva", "123.456.789-00", "01/01/1990", "Secretário")
    tutor = Tutor("Maria Santos", "987.654.321-00", "15/05/1985", "Programação")

    print(funcionario.apresentar())
    print(tutor.apresentar())
