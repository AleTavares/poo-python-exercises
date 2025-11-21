class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas_inscritas = []

    def listar_disciplinas(self):
        for d in self.disciplinas_inscritas:
            print(d.nome)

class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.alunos_matriculados = []

    def listar_alunos(self):
        for a in self.alunos_matriculados:
            print(f"{a.nome} ({a.curso})")

class Secretaria:
    @staticmethod
    def inscrever_aluno(aluno, disciplina):
        disciplina.alunos_matriculados.append(aluno)
        aluno.disciplinas_inscritas.append(disciplina)

aluno1 = Aluno("João Silva", "2023001", "Engenharia de Software")
aluno2 = Aluno("Maria Santos", "2023002", "Ciência da Computação")
disciplina1 = Disciplina("POO", "POO001", 60)
disciplina2 = Disciplina("Banco de Dados", "BD001", 80)

secretaria = Secretaria()
secretaria.inscrever_aluno(aluno1, disciplina1)
secretaria.inscrever_aluno(aluno1, disciplina2)
secretaria.inscrever_aluno(aluno2, disciplina1)


aluno1.listar_disciplinas()
disciplina1.listar_alunos()