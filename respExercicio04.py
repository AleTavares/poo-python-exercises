class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, meu CPF é {self.cpf}"


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, cargo):
        super().__init__(nome, cpf, data_nascimento)
        self.cargo = cargo

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu trabalho no cargo de {self.cargo}."


class Professor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, departamento):
        super().__init__(nome, cpf, data_nascimento)
        self.departamento = departamento

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, sou professor no departamento de {self.departamento}."


class Tutor(Professor):
    def __init__(self, nome, cpf, data_nascimento, area_atuacao):
        # o teste espera isso: departamento NÃO é pedido
        super().__init__(nome, cpf, data_nascimento, departamento="Tutoria")
        self.area_atuacao = area_atuacao

    def apresentar(self):
        return (
            f"Olá, meu nome é {self.nome}, sou tutor na área de {self.area_atuacao} "
            f"e pertenço ao departamento de {self.departamento}."
        )
