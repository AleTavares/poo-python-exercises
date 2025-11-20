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


# Exemplo de uso
if __name__ == "__main__":
    funcionario = Funcionario("João Silva", "123.456.789-00", "01/01/1990", "Secretário")
    tutor = Tutor("Maria Santos", "987.654.321-00", "15/05/1985", "Programação")

    print(funcionario.apresentar())
    print(tutor.apresentar())
    
    print("\n--- Testes adicionais ---")
    
    # Teste com outra instância de Tutor
    tutor2 = Tutor("Carlos Oliveira", "111.222.333-44", "20/03/1992", "Matemática")
    print(tutor2.apresentar())
    
    # Teste com Pessoa (classe base)
    pessoa = Pessoa("Ana Costa", "555.666.777-88", "10/10/1995")
    print(pessoa.apresentar())
    
    # Demonstrando acesso aos atributos específicos
    print(f"\nCargo do funcionário: {funcionario.cargo}")
    print(f"Área de atuação do tutor: {tutor.area_atuacao}")