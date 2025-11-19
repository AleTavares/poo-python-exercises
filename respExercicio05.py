class Aluno:
    def __init__ (self, nome, matricula, curso, notas=[]):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = notas
        
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
      
class Disciplina:
    def __init__ (self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

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
    def exibir_dados(self):
        print(f"=== Dados do Funcionário ===\nNome: {self.nome}\nCPF: {self.cpf}\nData de Nascimento: {self.data_nascimento}\nCargo: {self.cargo}\nSalário: R$ {self.salario:.2f}")

class Tutor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, area_atuacao):
        super().__init__(nome, cpf, data_nascimento)
        self.area_atuacao = area_atuacao
    def apresentar(self):
        print(f"=== Dados do Tutor ===\nNome: {self.nome}\nCPF: {self.cpf}\nData de Nascimento: {self.data_nascimento}\nÁrea de Atuação: {self.area_atuacao}")
      

        
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
funcionario.exibir_dados()

tutor = Tutor("Carlos Pereira", "987.654.321-00", "22/09/1990", "Matemática")
print(tutor.apresentar())


#---------------------------------------------------
