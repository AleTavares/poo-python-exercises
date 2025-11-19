class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def apresentar(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}"

class Disciplina: 
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []
        self.carga_horaria = 0

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        return [aluno.apresentar() for aluno in self.alunos]    
    def definir_carga_horaria(self, horas):
        self.carga_horaria = horas

