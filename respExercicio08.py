class Departamento:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.professores = []  

    
    @classmethod
    def criar_departamento_exatas(cls, nome):
        """Cria um departamento de Exatas com a sigla 'EXA'."""
        return cls(nome, "EXA") 

    
    @classmethod
    def criar_departamento_humanas(cls, nome):
        """Cria um departamento de Humanas com a sigla 'HUM'."""
        return cls(nome, "HUM") 

    
    def adicionar_professor(self, professor):
        self.professores.append(professor)
        print(f"Professor(a) {professor.nome} adicionado(a) ao departamento de {self.nome}.")

    def listar_professores(self):
        print(f"\n--- Professores do Depto. {self.nome} ({self.sigla}) ---")
        if not self.professores:
            print("Nenhum professor registrado.")
            return
        for prof in self.professores:
            print(f"- {prof.nome} ({prof.departamento})")


class Professor:
    def __init__(self, nome, departamento):
        self.nome = nome
        self.departamento = departamento

if __name__ == "__main__":
    
    
    dept_exatas = Departamento.criar_departamento_exatas("Matemática e Computação")
    dept_humanas = Departamento.criar_departamento_humanas("Letras e Filosofia")

    
    print(f"Departamento: {dept_exatas.nome} - Sigla: {dept_exatas.sigla}")
    print(f"Departamento: {dept_humanas.nome} - Sigla: {dept_humanas.sigla}")

    print("-" * 30)

   
    prof_mat = Professor("Dr. Alan Turing", "Computação")
    prof_lit = Professor("Dra. Clarice Lispector", "Literatura")
    
    dept_exatas.adicionar_professor(prof_mat)
    dept_humanas.adicionar_professor(prof_lit)
    
    dept_exatas.listar_professores()
    dept_humanas.listar_professores()