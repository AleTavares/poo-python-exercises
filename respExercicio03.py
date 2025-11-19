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
        
aluno = Aluno("João Silva", "2023001", "Engenharia de Software")

aluno.adicionar_nota(8)
aluno.adicionar_nota(7)

aluno_media = aluno.calcular_media()

print(f"Média do aluno: {aluno_media:.2f}")
aluno.status()

disciplina = Disciplina("Programação Orientada a Objetos", "CS101", 60)

print(f"Aluno: {aluno.nome}, Matrícula: {aluno.matricula}, Curso: {aluno.curso}")

print(f"Disciplina: {disciplina.nome}, Código: {disciplina.codigo}, Carga Horária: {disciplina.carga_horaria} horas")

prof = Professor("Dr. Carlos", "Ciência da Computação", 5000)
print(f"Salário do professor: R$ {prof.salario:.2f}")
prof.salario = 6000
print(f"Novo salário do professor: R$ {prof.salario:.2f}")
prof.salario = -1000  # Isso levantará um ValueError