class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso


class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria


# Exemplos de uso
Aluno1 = Aluno("Joao Silva", "2023001", "Engenharia de Software")
Aluno2 = Aluno("Maria Santos", "2023002", "Ciencia da Computacao")

Disciplina1 = Disciplina("Programação Orientada a Objetos", "POO101", 60)
Disciplina2 = Disciplina("Estruturas de Dados", "ED202", 45)

print(f"Aluno: {Aluno1.nome}, Matrícula: {Aluno1.matricula}, Curso: {Aluno1.curso}")
print(f"Aluno: {Aluno2.nome}, Matrícula: {Aluno2.matricula}, Curso: {Aluno2.curso}")

print(f"Disciplina: {Disciplina1.nome}, Código: {Disciplina1.codigo}, Carga Horaria: {Disciplina1.carga_horaria} horas")
print(f"Disciplina: {Disciplina2.nome}, Código: {Disciplina2.codigo}, Carga Horaria: {Disciplina2.carga_horaria} horas")
