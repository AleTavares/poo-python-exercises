class Pessoa:  # CORREÇÃO 1: Nome da classe deve começar com maiúscula
    def __init__(self, nome, idade):
        self.nome = nome  # CORREÇÃO 2: Usar self.nome para criar atributo
        self.idade = idade
        self._cpf = None  # CORREÇÃO 3: Usar underscore simples para atributo protegido
    
    def apresentar(self):  # CORREÇÃO 4: Adicionar self como parâmetro
        return f"Olá, sou {self.nome}"
    
    def definir_cpf(self, cpf):
        """Método para definir o CPF (atributo protegido)"""
        self._cpf = cpf
    
    def obter_cpf(self):
        """Método para obter o CPF"""
        return self._cpf


class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  # CORREÇÃO 5: Usar super() para inicializar classe pai
        self.curso = curso
        self.notas = []
    
    def adicionar_nota(self, nota):
        if nota >= 0 and nota <= 10:
            self.notas.append(nota)
        else:
            print(f"Nota inválida: {nota}. Deve estar entre 0 e 10.")
    
    def calcular_media(self):
        # CORREÇÃO 6: Tratar divisão por zero
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


class Professor(Pessoa):
    def __init__(self, nome, idade, departamento, salario):
        super().__init__(nome, idade)
        self.departamento = departamento
        self.salario = salario
    
    def apresentar(self):
        return f"Olá, sou o professor {self.nome} do departamento {self.departamento}"
    
    def dar_aumento(self, percentual):
        """Aplica um aumento percentual ao salário"""
        self.salario += self.salario * (percentual / 100)


# Testando o código corrigido
if __name__ == "__main__":
    print("="*70)
    print("TESTANDO CÓDIGO CORRIGIDO")
    print("="*70)
    
    # Criando objetos
    estudante = Estudante("João", 20, "Engenharia")
    professor = Professor("Dr. Silva", 45, "Computação", 8000)
    
    # Testando apresentações
    print("\n--- APRESENTAÇÕES ---")
    print(estudante.apresentar())
    print(professor.apresentar())
    
    # Adicionando notas ao estudante
    print("\n--- ADICIONANDO NOTAS ---")
    estudante.adicionar_nota(8.5)
    estudante.adicionar_nota(7.0)
    estudante.adicionar_nota(9.0)
    print(f"Notas adicionadas: {estudante.notas}")
    
    # CORREÇÃO 7: Agora não dá erro mesmo sem notas
    print(f"Média do estudante: {estudante.calcular_media():.2f}")
    
    # Testando com estudante sem notas
    print("\n--- TESTANDO ESTUDANTE SEM NOTAS ---")
    estudante2 = Estudante("Maria", 19, "Computação")
    print(f"Média de {estudante2.nome} (sem notas): {estudante2.calcular_media()}")
    
    # Testando atributo protegido CPF
    print("\n--- TESTANDO CPF (ATRIBUTO PROTEGIDO) ---")
    estudante.definir_cpf("123.456.789-00")
    print(f"CPF de {estudante.nome}: {estudante.obter_cpf()}")
    
    # Testando aumento de salário
    print("\n--- TESTANDO AUMENTO DE SALÁRIO ---")
    print(f"Salário atual de {professor.nome}: R$ {professor.salario:.2f}")
    professor.dar_aumento(10)
    print(f"Salário após aumento de 10%: R$ {professor.salario:.2f}")
    
    # Testando nota inválida
    print("\n--- TESTANDO VALIDAÇÃO DE NOTA ---")
    estudante.adicionar_nota(15)  # Deve mostrar mensagem de erro
    estudante.adicionar_nota(-5)  # Deve mostrar mensagem de erro
    
    # Demonstrando herança
    print("\n--- DEMONSTRANDO HERANÇA ---")
    print(f"Estudante é instância de Pessoa? {isinstance(estudante, Pessoa)}")
    print(f"Professor é instância de Pessoa? {isinstance(professor, Pessoa)}")
    print(f"Estudante é instância de Professor? {isinstance(estudante, Professor)}")
    
    print("\n" + "="*70)
    print("TODOS OS TESTES CONCLUÍDOS COM SUCESSO!")
    print("="*70)