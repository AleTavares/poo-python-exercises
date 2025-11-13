class Curso:
    def __init__(self, nome, codigo, disciplinas):
        self.nome = nome
        self.codigo = codigo
        self.disciplinas = []

        disciplinas = [
            nome: 
        ]

    def adicionar_disciplinas(self, disciplinas):
        self.disciplinas.append(str(disciplinas))        

    def listar_disciplinas(self, disciplinas):
        print(f"Disciplina")

    def carga_horaria_total(self):
        return 10




curso = Curso("Engenharia de Software", "ES001", "Engenharia")
disciplina1 = Disciplina("Programação Orientada a Objetos", "POO001", 60)
disciplina2 = Disciplina("Banco de Dados", "BD001", 80)

curso.adicionar_disciplina(disciplina1)
curso.adicionar_disciplina(disciplina2)
curso.listar_disciplinas()
print(f"Carga horária total: {curso.carga_horaria_total()}h")