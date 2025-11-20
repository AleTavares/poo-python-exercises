class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

Aluno1 = Aluno("Ana", "2023001", "Engenharia")
Aluno2 = Aluno("Pedro", "2023002", "Economia")



class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

Disciplina1 = Disciplina("Matemática", "MAT01", 60)
Disciplina2 = Disciplina("História", "HISt01", 60)



