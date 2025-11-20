class Departamento:
    def __init__(self, nome, sigla, professores):
        self.nome = nome
        self.sigla = sigla
        self.professores = professores

    @classmethod
    def criar_departamento_exatas(cls, nome):
        return cls(nome, "EXA", [])

    @classmethod
    def criar_departamento_humanas(cls, nome):
        return cls(nome, "HUM", [])

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def listar_professores(self):
        return self.professores


dept_exatas = Departamento.criar_departamento_exatas("Matemática e Computação")
dept_humanas = Departamento.criar_departamento_humanas("Letras e Filosofia")

dept_exatas.adicionar_professor("Professor A")
dept_humanas.adicionar_professor("Professor B")

print(f"Departamento: {dept_exatas.nome} - Sigla: {dept_exatas.sigla} - Professores: {dept_exatas.listar_professores()}")
print(f"Departamento: {dept_humanas.nome} - Sigla: {dept_humanas.sigla} - Professores: {dept_humanas.listar_professores()}")