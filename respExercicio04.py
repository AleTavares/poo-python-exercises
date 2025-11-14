class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def apresentar(self):
        return f"Olá, sou {self.nome}, CPF: {self.cpf}"


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, cargo):
        super().__init__(nome, cpf, data_nascimento)
        self.cargo = cargo


class Tutor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, area_atuacao):
        super().__init__(nome, cpf, data_nascimento)
        self.area_atuacao = area_atuacao

    def apresentar(self):
        return f"Olá, sou {self.nome}, CPF: {self.cpf}, atuo na área de {self.area_atuacao}"
