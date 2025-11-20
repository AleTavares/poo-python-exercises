import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

aluno1 = Aluno("Maria Silva", "2021001", "Engenharia de Software")
aluno2 = Aluno("João Souza", "2021002", "Matemática")

disciplina1 = Disciplina("Programação", "CS101", 60)
disciplina2 = Disciplina("Matemática Discreta", "MAT101", 45)

print(f"Aluno: {aluno1.nome}, Matrícula: {aluno1.matricula}, Curso: {aluno1.curso}")
print(f"Aluno: {aluno2.nome}, Matrícula: {aluno2.matricula}, Curso: {aluno2.curso}")

print(f"Disciplina: {disciplina1.nome}, Código: {disciplina1.codigo}, Carga Horária: {disciplina1.carga_horaria} horas")
print(f"Disciplina: {disciplina2.nome}, Código: {disciplina2.codigo}, Carga Horária: {disciplina2.carga_horaria} horas")
