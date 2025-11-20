# respExercicio08.py
# Exercício 08 - Método de Classe (@classmethod)

class Departamento:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.professores = []  # Lista de nomes ou objetos Professor (dependendo do uso futuro)

    @classmethod
    def criar_departamento_exatas(cls, nome):
        return cls(nome, "EXA")

    @classmethod
    def criar_departamento_humanas(cls, nome):
        return cls(nome, "HUM")

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def listar_professores(self):
        print(f"=== Professores do Departamento {self.nome} ({self.sigla}) ===")
        if not self.professores:
            print("Nenhum professor cadastrado.")
        else:
            for prof in self.professores:
                print(f"- {prof}")
        print()


# Demonstração de uso (opcional)
if __name__ == "__main__":
    dept_exatas = Departamento.criar_departamento_exatas("Matemática e Computação")
    dept_humanas = Departamento.criar_departamento_humanas("Letras e Filosofia")

    print(f"Departamento: {dept_exatas.nome} - Sigla: {dept_exatas.sigla}")
    print(f"Departamento: {dept_humanas.nome} - Sigla: {dept_humanas.sigla}")
