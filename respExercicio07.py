class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas_inscritas = []  

    def listar_disciplinas(self):
        print(f"\n=== Disciplinas em que {self.nome} está inscrito ===")
        if not self.disciplinas_inscritas:
            print("Nenhuma disciplina inscrita.")
        else:
            for d in self.disciplinas_inscritas:
                print(f"{d.nome} ({d.codigo})")


class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.alunos_matriculados = []  

    def listar_alunos(self):
        print(f"\n=== Alunos matriculados em {self.nome} ===")
        if not self.alunos_matriculados:
            print("Nenhum aluno matriculado.")
        else:
            for aluno in self.alunos_matriculados:
                print(f"{aluno.nome} ({aluno.matricula})")


class Secretaria:

    @staticmethod
    def inscrever_aluno(aluno, disciplina):
        if disciplina not in aluno.disciplinas_inscritas:
            aluno.disciplinas_inscritas.append(disciplina)

        if aluno not in disciplina.alunos_matriculados:
            disciplina.alunos_matriculados.append(aluno)