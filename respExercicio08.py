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
        self.professores.append(professor)

    def listar_professores(self):
       print(f"=== Professores do departamento {self.nome}: ===")
       for p in self.professores:
         print(f"- {p}") 






    
if __name__ == "__main__":
    depto_exatas = Departamento.criar_departamento_exatas("Matemática e Computação")
    depto_humanas = Departamento.criar_departamento_humanas("Letras e Filosofia")

    print(f"Departamento: {depto_exatas.nome}, Sigla: {depto_exatas.sigla}")
    print(f"Departamento: {depto_humanas.nome}, Sigla: {depto_humanas.sigla}")

    depto_exatas.adicionar_professor("João Silva")
    depto_exatas.adicionar_professor("Ana Costa")

    depto_exatas.listar_professores()
                
                
    
                
                    

            