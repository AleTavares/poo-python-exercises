class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.disciplinas = []
    
    def adicionar_disciplina(self, disciplinas):
        self.disciplinas.append(disciplinas)

    def listar_disciplinas(self):
        for i in self.disciplinas:
            print(f"{i.nome} - ({i.codigo})")

    def carga_horaria_total(self):
        total = sum( i.carga_horaria for i in self.disciplinas)
        return  total

class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        

curso = Curso("Engenharia de Software", "ES001")
disciplina1 = Disciplina("Programação Orientada a Objetos", "POO001", 60)
disciplina2 = Disciplina("Banco de Dados", "BD001", 80)

curso.adicionar_disciplina(disciplina1)
curso.adicionar_disciplina(disciplina2)
curso.listar_disciplinas()
print(f"Carga horária total: {curso.carga_horaria_total()}h")