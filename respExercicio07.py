class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas_inscritas = []  # lista de objetos Disciplina

    def listar_disciplinas(self):
        print(f"=== Disciplinas de {self.nome} ===")
        for disc in self.disciplinas_inscritas:
            print(f"- {disc.nome} ({disc.codigo})")


class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.alunos_matriculados = []  # lista de objetos Aluno

    def listar_alunos(self):
        print(f"=== Alunos matriculados em {self.nome} ===")
        for aluno in self.alunos_matriculados:
            print(f"- {aluno.nome} ({aluno.matricula})")


class Secretaria:
    @staticmethod
    def inscrever_aluno(aluno, disciplina):
        # Evita duplicações acidentais
        if disciplina not in aluno.disciplinas_inscritas:
            aluno.disciplinas_inscritas.append(disciplina)

        if aluno not in disciplina.alunos_matriculados:
            disciplina.alunos_matriculados.append(aluno)
