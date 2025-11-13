class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def adicionar_nota1(self, nota1):
        nota1 = float(nota1)
        if 0 <= nota1 <= 10:
            self.nota1 = nota1
    
    def adicionar_nota2(self, nota2):
        nota2 = float(nota2)
        if 0 <= nota2 <= 10:
            self.nota2 = nota2

    def media (self):
        media = (self.nota1 + self.nota2) / 2
        return media
        
    def aprovado(self):
        if self.media() >= 7:
            return True
        else:
            return False
        

aluno1 = Aluno("João Silva")
aluno1.adicionar_nota1(8.5)
aluno1.adicionar_nota2(7.0)

aluno2 = Aluno("Maria Santos")
aluno2.adicionar_nota1(6.0)
aluno2.adicionar_nota2(5.5)

print(f"Aluno: {aluno1.nome}, Nota 1: {aluno1.nota1}, Nota 2: {aluno1.nota2}, Média: {aluno1.media()}, Aprovado: {aluno1.aprovado()}")
print(f"Aluno: {aluno2.nome}, Nota 1: {aluno2.nota1}, Nota 2: {aluno2.nota2}, Média: {aluno2.media()}, Aprovado: {aluno2.aprovado()}")
