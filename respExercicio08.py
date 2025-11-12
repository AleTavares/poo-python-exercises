class Departamento:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.professores = []

    @classmethod
    def criar_departamento_exatas(cls, nome):
        return cls(nome, "EXA")

    @classmethod
    def criar_departamento_humanas(cls, nome):
        return cls(nome, "HUM")

    def adicionar_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)

    def listar_professores(self):
        print(f"Professores do Departamento {self.nome}:")
        for p in self.professores:
            print(f"- {p.nome}")

if __name__ == "__main__":
    class ProfessorSimples:
        def __init__(self, nome):
            self.nome = nome

    dept_exatas = Departamento.criar_departamento_exatas("Matemática e Computação")
    dept_humanas = Departamento.criar_departamento_humanas("Letras e Filosofia")

    prof1 = ProfessorSimples("Dr. Almeida")
    prof2 = ProfessorSimples("Dra. Pereira")

    dept_exatas.adicionar_professor(prof1)
    dept_humanas.adicionar_professor(prof2)

    print(f"Departamento: {dept_exatas.nome} - Sigla: {dept_exatas.sigla}")
    print(f"Departamento: {dept_humanas.nome} - Sigla: {dept_humanas.sigla}")
