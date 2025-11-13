class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Curso: {self.curso}")

    def exibir_dados(self):
        aluno1 = ("João Silva", 2023001, "Engenharia de Software")
        aluno2 = ("Maria Santos", 2023002, "Ciência da Computação")

class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

    def exibir_dados(self):
        aluno1 = ("Programação Orientada a Objetos", POO001, "60h")
        aluno2 = ("Banco de Dados", BD001, "80h")
    