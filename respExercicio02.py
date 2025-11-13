class Aluno:
    def __init__(self, nome, matricula, curso,):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = [] #lista de notas, começa vazia

    def adicionar_nota(self, nota): #Adicionar um novo valor à lista interna de notas.
        self.notas.append(nota) #Adicionar a nota à lista de notas.

    def calcular_media(self): 
        if not self.notas: #Verifica se a lista de notas está vazia.
            return 0 
        return sum(self.notas) / len(self.notas) #'sum(self.notas)' soma os valores, 'len(self.notas)' conta quantos são.
    
    def matricular_em(self, disciplina): #Adicionar uma disciplina à lista de disciplinas que o aluno cursa.
        self.disciplina.append(disciplina)

class Disciplina: 
    def __init__(self, nome_disciplina, codigo, carga_horaria):
        self.nome_disciplina = nome_disciplina
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.alunos_matriculados = [] #lista de alunos matriculados, começa vazia
    
    def matricular_aluno(self, aluno): #Adicionar um aluno à lista interna de alunos matriculados.
        self.alunos_matriculados.append(aluno) #Adicionar o aluno à lista de alunos matriculados.