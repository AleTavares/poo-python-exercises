class Aluno:
    def __init__ (self, nome, matricula, curso, notas=[], disciplinas_inscritas: list = []):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = notas
        self.disciplinas_inscritas = disciplinas_inscritas
        
    def adicionar_nota(self, nota):
        if len(self.notas) >= 2:
            print("Número máximo de notas atingido.")
            self.notas = []
        self.notas.append(nota)
        
    def calcular_media(self):
        print(self.notas)
        return sum(self.notas) / len(self.notas)
      
    def status(self):
        media = self.calcular_media()      
        return "Aprovado" if media >= 7 else "Reprovado"
      
    def listar_disciplinas(self):
        print("Disciplinas inscritas:\n")
        for disciplina in self.disciplinas_inscritas:
            print(f"Disciplina: {disciplina.nome}, Código: {disciplina.codigo}")
            
    def apresentar(self):
      return f"Olá, sou o aluno {self.nome} e estudo no curso {self.curso}."
      
class Disciplina:
    def __init__ (self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.alunos_matriculados = []
      
    def listar_alunos(self):
        print("Alunos inscritos na disciplina:\n")
        for aluno in self.alunos_matriculados:
            print(f"Aluno: {aluno.nome}, Matrícula: {aluno.matricula}")

class Professor:
    def __init__ (self, nome, departamento, salario):
        self.nome = nome
        self.departamento = departamento
        self._salario = salario
        
    @property
    def salario(self):
        return self._salario
      
    @salario.setter
    def salario(self, novo_salario):
        if novo_salario > 0: 
          self._salario = novo_salario
        else:
          print("Salário deve ser positivo.")
    
    def apresentar(self):
      return f"Olá, sou o professor {self.nome} do departamento de {self.departamento}."
          
class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        
    def apresentar(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}"
        
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, cargo, salario):
        super().__init__(nome, cpf, data_nascimento)
        self.cargo = cargo
        self.salario = salario
    def apresentar(self):
        return f"=== Dados do Funcionário ===\nNome: {self.nome}\nCPF: {self.cpf}\nData de Nascimento: {self.data_nascimento}\nCargo: {self.cargo}\nSalário: R$ {self.salario:.2f}"

class Tutor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, area_atuacao):
        super().__init__(nome, cpf, data_nascimento)
        self.area_atuacao = area_atuacao
    def apresentar(self):
        print(f"=== Dados do Tutor ===\nNome: {self.nome}\nCPF: {self.cpf}\nData de Nascimento: {self.data_nascimento}\nÁrea de Atuação: {self.area_atuacao}")
      
class Curso:
    def __init__ (self, nome, codigo, disciplinas: list[Disciplina] = []):
      self.nome = nome
      self.codigo = codigo
      self.disciplinas = disciplinas
      
    def adicionar_disciplina(self, disciplina: Disciplina):
      if len(self.disciplinas) >= 2:
        self.disciplinas = []
      self.disciplinas.append(disciplina)
    
    def listar_disciplinas(self):
      for disciplina in self.disciplinas:
        print(f"Disciplina: {disciplina.nome}\nCódigo: {disciplina.codigo}")
        
    def carga_horaria_total(self):
      total = sum(disciplina.carga_horaria for disciplina in self.disciplinas)
      return total
        
class Secretaria:        
    def inscrever_aluno(aluno: Aluno, disciplina: Disciplina):
        aluno.disciplinas_inscritas.append(disciplina)
        disciplina.alunos_matriculados.append(aluno)
        print(f"Aluno {aluno.nome} inscrito na disciplina {disciplina.nome}.")
        
class Departamento:
    def __init__(self, nome, sigla, professores: list[Professor] = []):
        self.nome = nome
        self.sigla = sigla
        self.professores: list[Professor] = professores
        
    @classmethod
    def criar_departamento_exatas(self, nome):
        dept = Departamento(nome, "EXA")
        dept.sigla = "EXA"
        return dept
      
    @classmethod
    def criar_departamento_humanas(self, nome):
        dept = Departamento(nome, "HUM")
        dept.sigla = "HUM"
        return dept
    
    def adicionar_professor(self, professor: Professor):
        self.professores.append(professor)
    
    def listar_professores(self):
        for professor in self.professores:
            print(f"Professor: {professor.nome}, Departamento: {professor.departamento}")
        
# Testando as classes criadas
aluno = Aluno("João Silva", "2023001", "Engenharia de Software")

aluno.adicionar_nota(8)
aluno.adicionar_nota(7)

aluno_media = aluno.calcular_media()

print(f"Média do aluno: {aluno_media:.2f}")
aluno.status()

disciplina = Disciplina("Programação Orientada a Objetos", "CS101", 60)

print(f"Aluno: {aluno.nome}, Matrícula: {aluno.matricula}, Curso: {aluno.curso}")

print(f"Disciplina: {disciplina.nome}, Código: {disciplina. codigo}, Carga Horária: {disciplina.carga_horaria} horas")

#---------------------------------------------------
prof = Professor("Dr. Carlos", "Ciência da Computação", 5000)
print(f"Salário do professor: R$ {prof.salario:.2f}")
prof.salario = 6000
print(f"Novo salário do professor: R$ {prof.salario:.2f}")
prof.salario = -1000


#---------------------------------------------------
funcionario = Funcionario("Ana Souza", "123.456.789-00", "15/04/1985", "Gerente", 7000)
print(funcionario.apresentar())

tutor = Tutor("Carlos Pereira", "987.654.321-00", "22/09/1990", "Matemática")
print(tutor.apresentar())


#---------------------------------------------------
curso = Curso("Engenharia de Software", "ES101")
disc1 = Disciplina("Programação", "CS101", 60)
disc2 = Disciplina("Banco de Dados", "CS102", 80)
curso.adicionar_disciplina(disc1)
curso.adicionar_disciplina(disc2)
curso.listar_disciplinas()
total_carga = curso.carga_horaria_total()
print(f"Carga horária total do curso: {total_carga} horas")

#---------------------------------------------------
aluno1 = Aluno("Maria Oliveira", "2023002", "Engenharia de Software")
aluno2 = Aluno("Pedro Santos", "2023003", "Engenharia de Software")
disciplina1 = Disciplina("Estruturas de Dados", "CS201", 70)
disciplina2 = Disciplina("Redes de Computadores", "CS202", 50)
Secretaria.inscrever_aluno(aluno1, disciplina1)
Secretaria.inscrever_aluno(aluno1, disciplina2)
Secretaria.inscrever_aluno(aluno2, disciplina1)
aluno1.listar_disciplinas()
disciplina1.listar_alunos()
disciplina2.listar_alunos()

#---------------------------------------------------
dept_exatas = Departamento.criar_departamento_exatas("Departamento de Ciências Exatas")
dept_humanas = Departamento.criar_departamento_humanas("Departamento de Ciências Humanas")

print(f"Departamento: {dept_exatas.nome}, Sigla: {dept_exatas.sigla}")
print(f"Departamento: {dept_humanas.nome}, Sigla: {dept_humanas.sigla}")

#---------------------------------------------------
pessoas = [
    Aluno("João Silva", "2023001", "Engenharia de Software"),
    Professor("Dr. Maria", "Computação", 8000),
    Funcionario("Carlos Santos", "123.456.789-00", "01/01/1980", "Secretário", 7000),
]

for pessoa in pessoas:
    print(pessoa.apresentar())