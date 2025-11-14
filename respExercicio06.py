class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria


class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.disciplinas = []  # lista de objetos Disciplina

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def listar_disciplinas(self):
        print(f"=== Disciplinas do Curso: {self.nome} ===")
        for disc in self.disciplinas:
            print(f"- {disc.nome} ({disc.codigo})")

    def carga_horaria_total(self):
        return sum(d.carga_horaria for d in self.disciplinas)
