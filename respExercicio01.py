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

aluno1 = Aluno("João Silva", "2023001", "Engenharia de Software")
aluno2 = Aluno("Maria Oliveira", "2023002", "Ciência da Computação")

disciplina1 = Disciplina("Programação I", "CS101", 60)
disciplina2 = Disciplina("Matemática Discreta", "MA101", 45)

print(f"Aluno: {aluno1.nome}, Matrícula: {aluno1.matricula}, Curso: {aluno1.curso}")
print(f"Aluno: {aluno2.nome}, Matrícula: {aluno2.matricula}, Curso: {aluno2.curso}")


   

