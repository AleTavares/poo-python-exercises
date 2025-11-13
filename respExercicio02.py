class Aluno:
    def __init__ (self,nome, matricula,curso):
         self.nome = nome 
         self.matricula = matricula
         self.curso = curso 

aluno = Aluno("João Silva", "2023001", "Engenharia de Software")
aluno.adicionar_nota(8.5)
aluno.adicionar_nota(7.0)
aluno.adicionar_nota(9.2)
print(f"Média: {aluno.calcular_media()}")
aluno.status()