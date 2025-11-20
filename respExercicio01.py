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

aluno = Aluno("João Silva", "2023001", "Engenharia de Software")
disciplina = Disciplina("Programação Orientada a Objetos", "CS101", 60)

print(f"Aluno: {aluno.nome}, Matrícula: {aluno.matricula}, Curso: {aluno.curso}")

print(f"Disciplina: {disciplina.nome}, Código: {disciplina.codigo}, Carga Horária: {disciplina.carga_horaria} horas")