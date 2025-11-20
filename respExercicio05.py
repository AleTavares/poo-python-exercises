class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def apresentar(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}"


class Funcionario(Pessoa):   
    def __init__(self, nome, cpf, data_nascimento, cargo, salario):
        super().__init__(nome, cpf, data_nascimento)
        self.cargo = cargo
        self._salario = salario 

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, valor):
        if valor > 0:
            self._salario = valor
        else:
            print("Erro: Salário deve ser positivo!")

    def apresentar(self):
        return f"Nome {self.nome}, Cargo: {self.cargo}"
    
    def exibir_dados(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}, Cargo: {self.cargo}, Salário: R$ {self._salario}"
    
funcionario = Funcionario("Ana Costa", "111.222.333-44", "20/03/1988", "Coordenadora", 4500.0)
print(funcionario.exibir_dados())