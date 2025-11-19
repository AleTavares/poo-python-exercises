class Professor:
    """Classe que representa um professor"""
    
    def __init__(self, nome, matricula, titulacao):
        self.nome = nome
        self.matricula = matricula
        self.titulacao = titulacao
    
    def __str__(self):
        return f"Prof. {self.nome} ({self.titulacao}) - Mat: {self.matricula}"


class Departamento:
    """Classe que representa um departamento universitário"""
    
    # Atributo de classe para contar departamentos criados
    total_departamentos = 0
    
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.professores = []
        Departamento.total_departamentos += 1
    
    @classmethod
    def criar_departamento_exatas(cls, nome):
        """
        Método de classe (factory method) para criar departamento de Exatas
        """
        return cls(nome, "EXA")
    
    @classmethod
    def criar_departamento_humanas(cls, nome):
        """
        Método de classe (factory method) para criar departamento de Humanas
        """
        return cls(nome, "HUM")
    
    @classmethod
    def criar_departamento_biologicas(cls, nome):
        """
        Método de classe (factory method) para criar departamento de Biológicas
        """
        return cls(nome, "BIO")
    
    @classmethod
    def criar_departamento_saude(cls, nome):
        """
        Método de classe (factory method) para criar departamento de Saúde
        """
        return cls(nome, "SAU")
    
    @classmethod
    def criar_departamento_personalizado(cls, nome, sigla):
        """
        Método de classe para criar departamento com sigla personalizada
        """
        return cls(nome, sigla)
    
    @classmethod
    def total_de_departamentos(cls):
        """
        Método de classe que retorna o total de departamentos criados
        """
        return cls.total_departamentos
    
    def adicionar_professor(self, professor):
        """Adiciona um professor ao departamento"""
        if not isinstance(professor, Professor):
            print("Erro: O objeto deve ser uma instância de Professor")
            return False
        
        if professor in self.professores:
            print(f"Aviso: {professor.nome} já está no departamento")
            return False
        
        self.professores.append(professor)
        print(f"✓ Professor {professor.nome} adicionado ao departamento {self.sigla}")
        return True
    
    def remover_professor(self, professor):
        """Remove um professor do departamento"""
        if professor in self.professores:
            self.professores.remove(professor)
            print(f"✓ Professor {professor.nome} removido do departamento {self.sigla}")
            return True
        else:
            print(f"Aviso: Professor não encontrado no departamento")
            return False
    
    def listar_professores(self):
        """Lista todos os professores do departamento"""
        print(f"\n=== Professores do Departamento {self.sigla} ===")
        print(f"Departamento: {self.nome}")
        if not self.professores:
            print("Nenhum professor cadastrado.")
        else:
            for i, professor in enumerate(self.professores, 1):
                print(f"{i}. {professor}")
            print(f"Total de professores: {len(self.professores)}")
    
    def quantidade_professores(self):
        """Retorna a quantidade de professores no departamento"""
        return len(self.professores)
    
    def __str__(self):
        return f"Departamento: {self.nome} ({self.sigla}) - {len(self.professores)} professores"


# Demonstração do uso das classes
if __name__ == "__main__":
    print("="*70)
    print("SISTEMA DE GESTÃO DE DEPARTAMENTOS UNIVERSITÁRIOS")
    print("="*70)
    
    # Criando departamentos usando métodos de classe (Factory Methods)
    print("\n--- CRIANDO DEPARTAMENTOS ---")
    dept_exatas = Departamento.criar_departamento_exatas("Matemática e Computação")
    dept_humanas = Departamento.criar_departamento_humanas("Letras e Filosofia")
    dept_biologicas = Departamento.criar_departamento_biologicas("Ciências Biológicas")
    dept_saude = Departamento.criar_departamento_saude("Medicina e Enfermagem")
    
    print(f"\nDepartamento: {dept_exatas.nome} - Sigla: {dept_exatas.sigla}")
    print(f"Departamento: {dept_humanas.nome} - Sigla: {dept_humanas.sigla}")
    print(f"Departamento: {dept_biologicas.nome} - Sigla: {dept_biologicas.sigla}")
    print(f"Departamento: {dept_saude.nome} - Sigla: {dept_saude.sigla}")
    
    # Criando professores
    print("\n" + "="*70)
    print("--- CRIANDO PROFESSORES ---")
    prof1 = Professor("Dr. Carlos Silva", "P001", "Doutor")
    prof2 = Professor("Dra. Ana Paula", "P002", "Doutora")
    prof3 = Professor("Dr. João Santos", "P003", "Mestre")
    prof4 = Professor("Dra. Maria Oliveira", "P004", "Doutora")
    prof5 = Professor("Dr. Pedro Costa", "P005", "Doutor")
    prof6 = Professor("Dra. Julia Ferreira", "P006", "Mestre")
    
    # Adicionando professores aos departamentos
    print("\n--- ALOCANDO PROFESSORES NOS DEPARTAMENTOS ---")
    dept_exatas.adicionar_professor(prof1)
    dept_exatas.adicionar_professor(prof2)
    dept_exatas.adicionar_professor(prof3)
    
    dept_humanas.adicionar_professor(prof4)
    dept_humanas.adicionar_professor(prof5)
    
    dept_biologicas.adicionar_professor(prof6)
    
    # Testando duplicação
    print("\n--- TESTANDO DUPLICAÇÃO ---")
    dept_exatas.adicionar_professor(prof1)
    
    # Listando professores de cada departamento
    print("\n" + "="*70)
    dept_exatas.listar_professores()
    dept_humanas.listar_professores()
    dept_biologicas.listar_professores()
    dept_saude.listar_professores()
    
    # Removendo um professor
    print("\n" + "="*70)
    print("--- REMOVENDO PROFESSOR ---")
    dept_exatas.remover_professor(prof3)
    dept_exatas.listar_professores()
    
    # Usando método de classe para criar departamento personalizado
    print("\n" + "="*70)
    print("--- CRIANDO DEPARTAMENTO PERSONALIZADO ---")
    dept_engenharia = Departamento.criar_departamento_personalizado(
        "Engenharias", "ENG"
    )
    print(f"Departamento: {dept_engenharia.nome} - Sigla: {dept_engenharia.sigla}")
    
    # Estatísticas gerais usando método de classe
    print("\n" + "="*70)
    print("--- ESTATÍSTICAS GERAIS ---")
    print(f"Total de departamentos criados: {Departamento.total_de_departamentos()}")
    
    # Resumo de todos os departamentos
    print("\n--- RESUMO DE DEPARTAMENTOS ---")
    departamentos = [dept_exatas, dept_humanas, dept_biologicas, dept_saude, dept_engenharia]
    for dept in departamentos:
        print(dept)
    
    total_professores = sum(d.quantidade_professores() for d in departamentos)
    print(f"\nTotal de professores em todos os departamentos: {total_professores}")
    
    print("\n" + "="*70)