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
    
    Atributos herdados:
        nome (str): Nome completo
        cpf (str): CPF
        data_nascimento (str): Data de nascimento
    
    Atributos próprios:
        cargo (str): Cargo do funcionário
        salario (float): Salário do funcionário
    """
    
    def __init__(self, nome, cpf, data_nascimento, cargo, salario):
        """
        Inicializa um novo funcionário utilizando super() para herdar atributos.
        
        Args:
            nome (str): Nome completo
            cpf (str): CPF
            data_nascimento (str): Data de nascimento
            cargo (str): Cargo do funcionário
            salario (float): Salário do funcionário
        """
        # Utiliza super() para inicializar atributos da classe pai
        super().__init__(nome, cpf, data_nascimento)
        
        # Inicializa atributos próprios da classe Funcionario
        self.cargo = cargo
        self.salario = salario
    
    def exibir_dados(self):
        """
        Exibe todos os dados do funcionário (herdados e próprios).
        """
        print("=== Dados do Funcionário ===")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R$ {self.salario}")
    
    def dar_aumento(self, percentual):
        """
        Aplica um aumento percentual ao salário do funcionário.
        
        Args:
            percentual (float): Percentual de aumento (ex: 10 para 10%)
        """
        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        print(f"Aumento de {percentual}% aplicado. Novo salário: R$ {self.salario:.2f}")


# Exemplo de uso
if __name__ == "__main__":
    funcionario = Funcionario("Ana Costa", "111.222.333-44", "20/03/1988", "Coordenadora", 4500.0)
    funcionario.exibir_dados()
    
    print("\n--- Testes adicionais ---")
    
    # Teste do método herdado apresentar()
    print(f"\n{funcionario.apresentar()}")
    
    # Teste de aumento de salário
    print()
    funcionario.dar_aumento(10)
    
    # Exibir dados após o aumento
    print()
    funcionario.exibir_dados()
    
    # Criando outro funcionário
    print("\n" + "="*40 + "\n")
    funcionario2 = Funcionario("Carlos Silva", "555.666.777-88", "15/07/1990", "Analista", 3500.0)
    funcionario2.exibir_dados()
    
    # Demonstrando que super() inicializou corretamente os atributos herdados
    print("\n--- Verificação de Atributos ---")
    print(f"Atributos herdados: nome={funcionario.nome}, cpf={funcionario.cpf}, data_nascimento={funcionario.data_nascimento}")
    print(f"Atributos próprios: cargo={funcionario.cargo}, salario={funcionario.salario}")