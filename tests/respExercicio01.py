class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
    
    def apresentar(self):
        print ( f"Aluno: {self.nome}, Matrícula: {self.matricula}, Curso: {self.curso}")



class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

    def apresentar(self):
        print ( f"Disciplina: {self.nome}, codigo: {self.codigo}, carga horaria: {self.carga_horaria}")

aluno1 = Aluno('João Silva', 2023001, 'Engenharia de Software')
aluno1.apresentar()

disciplina1 = Disciplina('Programação Orientada a Objetos', 'POO001', '60h')
disciplina1.apresentar()
    


 