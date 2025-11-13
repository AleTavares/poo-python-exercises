from abc import ABC, abstractmethod


class Aluno(ABC):
    def __init__(self,nome,matricula,curso,disciplinas= None, notas=None):
        self.nome=nome
        self.matricula=matricula
        self.curso=curso
        self.disciplinas = disciplinas if disciplinas is not None else []
        self.notas = notas if notas is not None else []

    def adicionar_nota(self,nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def aprovado(self):
        return self.calcular_media() >= 7.0
    

    

aluno = Aluno("João Silva", "2023001", "Engenharia de Software")
aluno.adicionar_nota(8.5)
aluno.adicionar_nota(7.0)
aluno.adicionar_nota(9.2)
print(f"Média: {aluno.calcular_media()}")
print(f"Aprovado: {aluno.aprovado()}")


