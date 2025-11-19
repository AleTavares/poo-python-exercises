class Departamento:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.professores = []

        
    @classmethod
    def criar_departamento_exatas(cls, nome):
        sigla = 'EXA'
        return cls(nome, sigla)

    @classmethod
    def criar_departamento_humanas(cls, nome):
        sigla = 'HUM'
        return cls(nome, sigla)

    def adicionar_professor(self, professor):
        self.professores.append(professor)

dept_exatas = Departamento.criar_departamento_exatas("Matemática e Computação")
dept_humanas = Departamento.criar_departamento_humanas("Letras e Filosofia")

print(f"Departamento: {dept_exatas.nome} - Sigla: {dept_exatas.sigla}")
print(f"Departamento: {dept_humanas.nome} - Sigla: {dept_humanas.sigla}")