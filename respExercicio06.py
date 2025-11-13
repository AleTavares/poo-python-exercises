class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.Disciplinas = []

def adicionar_disciplina(self, disciplina):
    self.Disciplinas.append(disciplina)

def listar_disciplinas(self):
    print(f"=== Disciplinas do Curso: {self.nome} ===")
    for disc in self.disciplinas:
        print(f"- {disc.nome} ({disc.codigo})")

def carga_horaria_total(self):
    total = sum(disc.carga_horaria for disc in self.disciplinas)
    return total 


curso = Curso("Engenharia de Software", "ES101")


disciplina1 = Disciplina("Programação Orientada a Objetos", "POO001", 60)
disciplina2 = Disciplina("Banco de Dados", "BD001", 80)

curso.adicionar_disciplina(disciplina1)
curso.adicionar_disciplina(disciplina2)

curso.listar_disciplinas()
print(f"Carga Horaria total: {curso.carga_horaria_total()}h")