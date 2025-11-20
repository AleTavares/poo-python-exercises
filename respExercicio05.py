class Pessoa:
    def __init__(self, nome, CPF, data_nascimento):
        self.nome = nome
        self.CPF = CPF
        self.data_nascimento = data_nascimento

    def apresentar(self):
        return f"Nome: {self.nome}, CPF: {self.CPF}"


class Funcionario(Pessoa):
    def __init__(self, nome, CPF, data_nascimento, cargo, salario):
        super().__init__(nome, CPF, data_nascimento) 
        self.cargo = cargo
        self.salario = salario 

    def apresentar(self):
        return f"Nome: {self.nome}, CPF: {self.CPF}"

    def exibir_dados(self):
        return (
            f"Nome: {self.nome}\n"
            f"CPF: {self.CPF}\n"
            f"Data de Nascimento: {self.data_nascimento}\n"
            f"Cargo: {self.cargo}\n"
            f"Salário: R$ {self.salario:.2f}"
        )

    

funcionario = Funcionario("Ana Costa", "111.222.333-44", "20/03/1988", "Coordenadora", 4500.0)
funcionario.exibir_dados()
