class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas_inscritas = []  # lista de objetos Disciplina

    def listar_disciplinas(self):
        print(f"=== Disciplinas de {self.nome} ===")
        for d in self.disciplinas_inscritas:
            print(f"- {d.nome} ({d.codigo})")
        if not self.disciplinas_inscritas:
            print("Nenhuma disciplina inscrita.")


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
        if not self.alunos_matriculados:
            print("Nenhum aluno matriculado.")


class Secretaria:
    @staticmethod
    def inscrever_aluno(aluno, disciplina):
        # evita duplicação
        if disciplina not in aluno.disciplinas_inscritas:
            aluno.disciplinas_inscritas.append(disciplina)
        
        if aluno not in disciplina.alunos_matriculados:
            disciplina.alunos_matriculados.append(aluno)

if __name__ == "__main__":
    aluno1 = Aluno("João Silva", "2023001", "Engenharia de Software")
    aluno2 = Aluno("Maria Santos", "2023002", "Ciência da Computação")

    disciplina1 = Disciplina("POO", "POO001", 60)
    disciplina2 = Disciplina("Banco de Dados", "BD001", 80)

    Secretaria.inscrever_aluno(aluno1, disciplina1)
    Secretaria.inscrever_aluno(aluno1, disciplina2)
    Secretaria.inscrever_aluno(aluno2, disciplina1)

    aluno1.listar_disciplinas()
    disciplina1.listar_alunos()
