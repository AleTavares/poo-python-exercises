class Aluno:
    def __init__ (self,nome, matricula,curso):
         self.nome = nome 
         self.matricula = matricula
         self.curso = curso 



class Curso:
    def __int__(self, nome ,matricula,curso):
        self.nome =nome 
        self.matricula = matricula 
        self.curso = curso
    
    def ___str___ ( self ):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Curso: {self.curso}"
    



class Disciplina():
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome 
        self.codigo = codigo 
        self.carga_horaria = carga_horaria
    def __str__ ( self ):
        return f"Nome: {self.nome}, Código: {self.codigo}, Carga Horária: {self.carga_horaria}"  
    
aluno1 = Aluno("João Silva", "2023001", "Engenharia de Software")
aluno2 = Aluno("Maria Oliveira", "2023002", "Ciência da Computação")
diciplina = Disciplina("Programação Orientada a Objetos", "POO101", 60)
diciplina = Disciplina("Estruturas de Dados", "ED202", 45)

print(Aluno)
print(f"nome: {aluno1.nome}, matricula,{aluno1.matricula} curso, {aluno1.curso}")
print(f"nome: {aluno2.nome}, matricula,{aluno2.matricula} curso, {aluno2.curso}")
print(f"Disciplina: {diciplina.nome}, Código: {diciplina.codigo}, Carga Horária: {diciplina.carga_horaria}")
print(f"Disciplina: {diciplina.nome}, Código: {diciplina.codigo}, Carga Horária: {diciplina.carga_horaria}")
      