class Aluno:
    def __init__ (self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        
class Disciplina:
    def __init__ (self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        
A1 = Aluno("Maria", 123456789, "Matemática")
A2 = Aluno("João", 987654321, "Geografia")
D1 = Disciplina("Matemática", 1, 24)
D2 = Disciplina("Geografia", 2, 12)

lista_alunos = [A1, A2]
lista_disciplinas = [D1, D2]

for aluno in lista_alunos:
    print(f"Aluno: {aluno.nome}, Matrícula: {aluno.matricula}, Curso: {aluno.curso}")

for disciplina in lista_disciplinas:
    print(f"Disciplina: {disciplina.nome}, Código: {disciplina.codigo}, Carga Horária: {disciplina.carga_horaria}")