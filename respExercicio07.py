from abc import ABC


class Aluno(ABC):
    def __init__(self,nome,matricula,curso):
        self.nome=nome
        self.matricula=matricula
        self.curso=curso
        self.disciplinas_inscritas = []

class disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.alunos_matriculados = []