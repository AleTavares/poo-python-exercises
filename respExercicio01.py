class aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

class disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

aluno1 = aluno("Emar Cristian", "6325192", "analise e desenvolvimento de sistemas")
disciplina1 = disciplina("Engenharia de Software", "1POO00", 60)

aluno2 = aluno("Joao Silva", "1234567", "sistemas de informacao")
disciplina2 = disciplina("Banco de Dados", "1POO00", 80)

print("aluno 1:")
print(f"Nome:{aluno1.nome}")
print(f"Matricula:{aluno1.matricula}")
print(f"Curso:{aluno1.curso}")

print("\ndisciplina 1:")
print(f"Nome:{disciplina1.nome}")
print(f"Codigo:{disciplina1.codigo}")
print(f"Carga Horaria:{disciplina1.carga_horaria}")

print("\naluno 2:")
print(f"Nome:{aluno2.nome}")
print(f"Matricula:{aluno2.matricula}")
print(f"Curso:{aluno2.curso}")

print("\ndisciplina 2:")
print(f"Nome:{disciplina2.nome}")
print(f"Codigo:{disciplina2.codigo}")
print(f"Carga Horaria:{disciplina2.carga_horaria}")