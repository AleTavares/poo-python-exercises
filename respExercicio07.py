class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas_inscritas = []

    def listar_disciplinas(self):
        return [disciplina.nome for disciplina in self.disciplinas_inscritas]


class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.alunos_matriculados = []

    def listar_alunos(self):
        return [aluno.nome for aluno in self.alunos_matriculados]


class Secretaria:
    @staticmethod
    def inscrever_aluno(aluno, disciplina):
        disciplina.alunos_matriculados.append(aluno)
        aluno.disciplinas_inscritas.append(disciplina)

    @staticmethod
    def listar_disciplinas_aluno(aluno):
        return aluno.disciplinas_inscritas

    @staticmethod
    def listar_alunos_disciplina(disciplina):
        return disciplina.alunos_matriculados
            

aluno1 = Aluno("João Silva", "2023001", "Engenharia de Software")
aluno2 = Aluno("Maria Santos", "2023002", "Ciência da Computação")
disciplina1 = Disciplina("POO", "POO001", 60)
disciplina2 = Disciplina("Banco de Dados", "BD001", 80)

Secretaria.inscrever_aluno(aluno1, disciplina1)
Secretaria.inscrever_aluno(aluno1, disciplina2)
Secretaria.inscrever_aluno(aluno2, disciplina1)

aluno1.listar_disciplinas()
disciplina1.listar_alunos()


print("Disciplinas do aluno João Silva:", aluno1.listar_disciplinas())
print("Alunos matriculados na disciplina POO:", disciplina1.listar_alunos())
