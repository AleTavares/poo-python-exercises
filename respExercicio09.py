class Pessoa:
    """Classe base que representa uma pessoa (opcional, mas demonstra hierarquia)"""
    
    def __init__(self, nome):
        self.nome = nome
    
    def apresentar(self):
        """Método que será sobrescrito nas subclasses (polimorfismo)"""
        return f"Olá, sou {self.nome}."


class Aluno(Pessoa):
    """Classe que representa um aluno"""
    
    def __init__(self, nome, matricula, curso):
        super().__init__(nome)
        self.matricula = matricula
        self.curso = curso
        self.disciplinas_inscritas = []
    
    def apresentar(self):
        """Implementação específica do método apresentar para Aluno"""
        return f"Olá, sou o aluno {self.nome} e estudo no curso {self.curso}."
    
    def __str__(self):
        return f"Aluno: {self.nome} - Matrícula: {self.matricula} - Curso: {self.curso}"


class Professor(Pessoa):
    """Classe que representa um professor"""
    
    def __init__(self, nome, departamento, salario):
        super().__init__(nome)
        self.departamento = departamento
        self.salario = salario
        self.disciplinas_lecionadas = []
    
    def apresentar(self):
        """Implementação específica do método apresentar para Professor"""
        return f"Olá, sou o professor {self.nome} e leciono no departamento {self.departamento}."
    
    def lecionar_disciplina(self, disciplina):
        """Adiciona uma disciplina que o professor leciona"""
        if disciplina not in self.disciplinas_lecionadas:
            self.disciplinas_lecionadas.append(disciplina)
    
    def __str__(self):
        return f"Professor: {self.nome} - Departamento: {self.departamento}"


class Funcionario(Pessoa):
    """Classe que representa um funcionário"""
    
    def __init__(self, nome, cpf, data_nascimento, cargo, salario):
        super().__init__(nome)
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.cargo = cargo
        self.salario = salario
    
    def apresentar(self):
        """Implementação específica do método apresentar para Funcionario"""
        return f"Olá, sou o funcionário {self.nome} e meu cargo é {self.cargo}."
    
    def __str__(self):
        return f"Funcionário: {self.nome} - Cargo: {self.cargo} - CPF: {self.cpf}"


class Coordenador(Professor):
    """Classe que representa um coordenador (herda de Professor)"""
    
    def __init__(self, nome, departamento, salario, curso_coordenado):
        super().__init__(nome, departamento, salario)
        self.curso_coordenado = curso_coordenado
    
    def apresentar(self):
        """Implementação específica do método apresentar para Coordenador"""
        return f"Olá, sou o professor {self.nome}, leciono no departamento {self.departamento} e coordeno o curso de {self.curso_coordenado}."
    
    def __str__(self):
        return f"Coordenador: {self.nome} - Curso: {self.curso_coordenado}"


def exibir_apresentacoes(pessoas):
    """
    Função que demonstra polimorfismo:
    Recebe uma lista de diferentes objetos e chama o método apresentar() de cada um
    """
    print("\n" + "="*70)
    print("APRESENTAÇÕES (DEMONSTRAÇÃO DE POLIMORFISMO)")
    print("="*70 + "\n")
    
    for i, pessoa in enumerate(pessoas, 1):
        print(f"{i}. {pessoa.apresentar()}")


def processar_pessoas_polimorficamente(pessoas):
    """
    Demonstra como diferentes objetos respondem ao mesmo método de formas diferentes
    """
    print("\n" + "="*70)
    print("PROCESSAMENTO POLIMÓRFICO")
    print("="*70 + "\n")
    
    for pessoa in pessoas:
        # O método apresentar() é chamado, mas cada classe responde diferentemente
        apresentacao = pessoa.apresentar()
        
        # Podemos processar todos os objetos da mesma forma
        print(f"→ {apresentacao}")
        
        # Verificando o tipo de forma dinâmica
        if isinstance(pessoa, Aluno):
            print(f"  ℹ️  Este é um estudante da matrícula {pessoa.matricula}")
        elif isinstance(pessoa, Coordenador):
            print(f"  ℹ️  Este coordenador ganha R$ {pessoa.salario:.2f}")
        elif isinstance(pessoa, Professor):
            print(f"  ℹ️  Este professor ganha R$ {pessoa.salario:.2f}")
        elif isinstance(pessoa, Funcionario):
            print(f"  ℹ️  CPF: {pessoa.cpf}")
        print()


# Demonstração do uso das classes e polimorfismo
if __name__ == "__main__":
    print("="*70)
    print("SISTEMA UNIVERSITÁRIO - DEMONSTRAÇÃO DE POLIMORFISMO")
    print("="*70)
    
    # Criando objetos de diferentes classes
    print("\n--- CRIANDO PESSOAS ---")
    
    aluno1 = Aluno("João Silva", "2023001", "Engenharia de Software")
    aluno2 = Aluno("Ana Paula", "2023002", "Ciência da Computação")
    aluno3 = Aluno("Carlos Eduardo", "2023003", "Sistemas de Informação")
    
    professor1 = Professor("Dr. Maria Santos", "Computação", 8000.0)
    professor2 = Professor("Dr. Pedro Oliveira", "Matemática", 7500.0)
    
    funcionario1 = Funcionario("Carlos Santos", "123.456.789-00", "01/01/1980", "Secretário", 3000.0)
    funcionario2 = Funcionario("Juliana Costa", "987.654.321-00", "15/05/1985", "Bibliotecária", 3500.0)
    
    coordenador1 = Coordenador("Dra. Fernanda Lima", "Engenharia", 9000.0, "Engenharia de Software")
    
    print("✓ 8 pessoas criadas no sistema")
    
    # Lista polimórfica: contém objetos de diferentes classes
    pessoas = [
        aluno1,
        professor1,
        funcionario1,
        aluno2,
        coordenador1,
        funcionario2,
        professor2,
        aluno3
    ]
    
    # Demonstração 1: Chamada simples e direta do polimorfismo
    exibir_apresentacoes(pessoas)
    
    # Demonstração 2: Processamento mais complexo
    processar_pessoas_polimorficamente(pessoas)
    
    # Demonstração 3: Iteração simples (conforme exemplo do exercício)
    print("\n" + "="*70)
    print("EXEMPLO BÁSICO DO EXERCÍCIO")
    print("="*70 + "\n")
    
    pessoas_exemplo = [
        Aluno("João Silva", "2023001", "Engenharia de Software"),
        Professor("Dr. Maria", "Computação", 8000.0),
        Funcionario("Carlos Santos", "123.456.789-00", "01/01/1980", "Secretário", 3000.0)
    ]
    
    for pessoa in pessoas_exemplo:
        print(pessoa.apresentar())
    
    # Estatísticas
    print("\n" + "="*70)
    print("ESTATÍSTICAS")
    print("="*70)
    
    total_alunos = sum(1 for p in pessoas if isinstance(p, Aluno))
    total_professores = sum(1 for p in pessoas if isinstance(p, Professor) and not isinstance(p, Coordenador))
    total_coordenadores = sum(1 for p in pessoas if isinstance(p, Coordenador))
    total_funcionarios = sum(1 for p in pessoas if isinstance(p, Funcionario))
    
    print(f"\nTotal de alunos: {total_alunos}")
    print(f"Total de professores: {total_professores}")
    print(f"Total de coordenadores: {total_coordenadores}")
    print(f"Total de funcionários: {total_funcionarios}")
    print(f"Total geral de pessoas: {len(pessoas)}")
    
    print("\n" + "="*70)
    print("POLIMORFISMO EXPLICADO:")
    print("Todas as classes têm o método 'apresentar()', mas cada uma")
    print("implementa de forma diferente. Isso é POLIMORFISMO!")
    print("="*70)
