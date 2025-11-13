# respExercicio01.py
# Exercício 01 - Modelagem Básica de Entidades

# Classe Aluno
class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

# Classe Disciplina
class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria


# Instanciando dois objetos da classe Aluno
aluno1 = Aluno("João Silva", "2023001", "Engenharia de Software")
aluno2 = Aluno("Maria Santos", "2023002", "Ciência da Computação")

# Instanciando dois objetos da classe Disciplina
disciplina1 = Disciplina("Programação Orientada a Objetos", "POO001", 60)
disciplina2 = Disciplina("Banco de Dados", "BD001", 80)

# Exibindo as informações
print(f"Aluno: {aluno1.nome}, Matrícula: {aluno1.matricula}, Curso: {aluno1.curso}")
print(f"Aluno: {aluno2.nome}, Matrícula: {aluno2.matricula}, Curso: {aluno2.curso}")
print(f"Disciplina: {disciplina1.nome}, Código: {disciplina1.codigo}, Carga Horária: {disciplina1.carga_horaria}h")
print(f"Disciplina: {disciplina2.nome}, Código: {disciplina2.codigo}, Carga Horária: {disciplina2.carga_horaria}h")
