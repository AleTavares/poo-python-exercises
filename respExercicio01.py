from abc import ABC, abstractmethod


class Aluno(ABC):
    def __init__(self,nome,matricula,curso):
        self.nome=nome
        self.matricula=matricula
        self.curso=curso
        self.disciplinas=[] 

class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria


aluno1 = Aluno("Fernanda Tavares", "A001", "Análise e Desenvolvimento de Sistemas")
aluno2 = Aluno("Lucas Silva", "A002", "Arquitetura de Software")

disciplina1 = Disciplina("Programação Orientada a Objetos", "POO101", 80)
disciplina2 = Disciplina("Banco de Dados", "BD102", 60)


print("= Alunos =")
print(f"Nome: {aluno1.nome}, Matrícula: {aluno1.matricula}, Curso: {aluno1.curso}")
print(f"Nome: {aluno2.nome}, Matrícula: {aluno2.matricula}, Curso: {aluno2.curso}")

print("\n= Disciplinas =")
print(f"Nome: {disciplina1.nome}, Código: {disciplina1.codigo}, Carga Horária: {disciplina1.carga_horaria}h")
print(f"Nome: {disciplina2.nome}, Código: {disciplina2.codigo}, Carga Horária: {disciplina2.carga_horaria}h")