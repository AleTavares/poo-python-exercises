class Pessoa:
    """
    Classe base que representa uma pessoa.
    
    Atributos:
        nome (str): Nome completo da pessoa
        cpf (str): CPF da pessoa
        data_nascimento (str): Data de nascimento da pessoa
    """
    
    def __init__(self, nome, cpf, data_nascimento):
        """
        Inicializa uma nova pessoa.
        
        Args:
            nome (str): Nome completo
            cpf (str): CPF
            data_nascimento (str): Data de nascimento
        """
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
    
    def apresentar(self):
        """
        Retorna uma apresentação básica da pessoa.
        
        Returns:
            str: Mensagem de apresentação
        """
        return f"Olá, sou {self.nome}, CPF: {self.cpf}"


class Funcionario(Pessoa):
    """
    Classe que representa um funcionário, herda de Pessoa.
    
    Atributos adicionais:
        cargo (str): Cargo do funcionário
    """
    
    def __init__(self, nome, cpf, data_nascimento, cargo):
        """
        Inicializa um novo funcionário.
        
        Args:
            nome (str): Nome completo
            cpf (str): CPF
            data_nascimento (str): Data de nascimento
            cargo (str): Cargo do funcionário
        """
        super().__init__(nome, cpf, data_nascimento)
        self.cargo = cargo


class Tutor(Pessoa):
    """
    Classe que representa um tutor, herda de Pessoa.
    
    Atributos adicionais:
        area_atuacao (str): Área de atuação do tutor
    """
    
    def __init__(self, nome, cpf, data_nascimento, area_atuacao):
        """
        Inicializa um novo tutor.
        
        Args:
            nome (str): Nome completo
            cpf (str): CPF
            data_nascimento (str): Data de nascimento
            area_atuacao (str): Área de atuação do tutor
        """
        super().__init__(nome, cpf, data_nascimento)
        self.area_atuacao = area_atuacao
    
    def apresentar(self):
        """
        Retorna uma apresentação do tutor incluindo sua área de atuação.
        Sobrescreve o método da classe base.
        
        Returns:
            str: Mensagem de apresentação com área de atuação
        """
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