class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso



class  Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

Aluno1 = Aluno("Joao", "2023001", "Engenharia")
Aluno2 = Aluno("Maria", "2023002", "Ciencia da Computacao")

Disciplina1 = Disciplina("Programação Orientada a Objetos", "POO001", 60)
Disciplina2 =  Disciplina("Banco de Dados", "BD001", 80)

print(Aluno1.nome + Aluno1.matricula + Aluno1.curso)
print(Aluno2.nome + Aluno2.matricula +  Aluno2.curso)

print(Disciplina1.nome + Disciplina1.codigo + str(Disciplina1.carga_horaria))
print(Disciplina2.nome + Disciplina2.codigo + str(Disciplina2.carga_horaria))


    

