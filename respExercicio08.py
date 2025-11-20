class Departamento:
    def __init__(self, sigla,nome):
        self.sigla = sigla
        self.nome = nome
        self.professores = []

    @classmethod
    def criar_departamento_exatas(cls,nome):
        return  cls (nome, "EXA")
    
    @classmethod
    def criar_departamento_humanas(cls,nome):
        return cls (nome, "EXA")
    
    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def listar_professores(self):
        for professor in self.professores:
            print(professor.nome)


dept_exatas = Departamento.criar_departamento_exatas('Matematica e Computacao')
dept_humanas = Departamento.criar_departamento_humanas("Letras e Filosofia")

print(f"Departamento: {dept_exatas.nome} - Sigla: {dept_exatas.sigla}")
print(f"Departamento: {dept_humanas.nome} - Sigla: {dept_humanas.sigla}")