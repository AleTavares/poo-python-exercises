class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
    
class Disciplina:
    def __init__(self, nome_disciplina, codigo, carga_horaria):
        self.nome_disciplina = nome_disciplina
        self.codigo = codigo
        self.carga_horaria = carga_horaria

aluno_a = Aluno("Matheus", "101", "Análise e Desenvolvimento de Sistemas")
print(f"Aluno cadastrado: {aluno_a.nome}, matricula: {aluno_a.matricula}, curso: {aluno_a.curso}")

disciplina_a = Disciplina("Engenharia de Software", "ENG02", "50h")
print(f"Nome da disciplina: {disciplina_a.nome_disciplina}, codigo: {disciplina_a.codigo},carga horária: {disciplina_a.carga_horaria}")
    
    