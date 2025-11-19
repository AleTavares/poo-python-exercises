

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def __str__(self):
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}, Curso: {self.curso}"

class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

    def __str__(self):
        return f"Disciplina: {self.nome}, Código: {self.codigo}, Carga Horária: {self.carga_horaria}h"

if __name__ == "__main__":
    
   
    aluno1 = Aluno("João Silva", "2023001", "Engenharia de Software")
    aluno2 = Aluno("Maria Santos", "2023002", "Ciência da Computação")

   
    disciplina1 = Disciplina("Programação Orientada a Objetos", "POO001", 60)
    disciplina2 = Disciplina("Banco de Dados", "BD001", 80)

    
    print(aluno1)
    print(aluno2)
    print(disciplina1)
    print(disciplina2)