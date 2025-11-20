class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria


class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.disciplinas = []  

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def listar_disciplinas(self):
        print(f"=== Disciplinas do Curso: {self.nome} ===")
        for d in self.disciplinas:
            print(f"{d.nome} ({d.codigo})")

    def carga_horaria_total(self):
        total = sum(d.carga_horaria for d in self.disciplinas)
        return total



curso = Curso("Engenharia de Software", "ES001")

disciplina1 = Disciplina("Programação Orientada a Objetos", "POO001", 60)
disciplina2 = Disciplina("Banco de Dados", "BD001", 80)

curso.adicionar_disciplina(disciplina1)
curso.adicionar_disciplina(disciplina2)

curso.listar_disciplinas()
print(f"Carga horária total: {curso.carga_horaria_total()}h")