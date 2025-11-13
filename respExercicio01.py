class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mostrar(self):
        print(f'Aluno: {self.nome}, Matricula: {self.matricula}, Curso: {self.curso}')

class  Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

    def mostrar(self):
        print(f'Diciplina: {self.nome}, Codigo: {self.codigo}, Carga horária: {self.carga_horaria}')

aluno1 = Aluno('João Silva', 2023001,'Engenharia de Software')
aluno1.mostrar()
aluno2 = Aluno('Emily', 212251,'ADS')
aluno2.mostrar()

diciplina1 = Disciplina('ADS', 444, '45h')
diciplina1.mostrar()
diciplina2 = Disciplina('Engenharia de Software', 442, '50h')
diciplina2.mostrar()
        

        