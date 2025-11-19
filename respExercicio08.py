class Departamento:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.professores = []  # lista de professores

    @classmethod
    def criar_departamento_exatas(cls, nome):
        return cls(nome, "EXA")

    @classmethod
    def criar_departamento_humanas(cls, nome):
        return cls(nome, "HUM")

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def listar_professores(self):
        print(f"=== Professores do Departamento: {self.nome} ===")
        if not self.professores:
            print("Nenhum professor cadastrado.")
        else:
            for prof in self.professores:
                print(f"- {prof}")

           
if __name__ == "__main__":
    dept_exatas = Departamento.criar_departamento_exatas("Matemática e Computação")
    dept_humanas = Departamento.criar_departamento_humanas("Letras e Filosofia")

    print(f"Departamento: {dept_exatas.nome} - Sigla: {dept_exatas.sigla}")
    print(f"Departamento: {dept_humanas.nome} - Sigla: {dept_humanas.sigla}")

    # exemplo adicionando professores
    dept_exatas.adicionar_professor("Dr. Silva")
    dept_exatas.adicionar_professor("Dra. Costa")

    dept_exatas.listar_professores()