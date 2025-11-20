class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
  
    class Disciplina:
        def __init__(self, nome_disciplina, codigo_disciplina, carga_horaria):
            self.nome_disciplina = nome_disciplina
            self.codigo_disciplina = codigo_disciplina
            self.carga_horaria = carga_horaria
       
        
Aluno1 = Aluno("Joao Silva", "2023001", "Engenharia de Software")
Aluno2 = Aluno("Maria Santos", "2023002", "Ciencia da Computacao")
Disciplina1 = Aluno.Disciplina("Programação Orientada a Objetos", "POO101", 60)
Disciplina2 = Aluno.Disciplina("Estruturas de Dados", "ED202", 45)
print(f"Aluno: {Aluno1.nome}, Matrícula: {Aluno1.matricula}, Curso: {Aluno1.curso}")
print(f"Aluno: {Aluno2.nome}, Matrícula: {Aluno2.matricula}, Curso: {Aluno2.curso}")
print(f"Disciplina: {Disciplina1.nome_disciplina}, Código: {Disciplina1.codigo_disciplina}, Carga Horaria: {Disciplina1.carga_horaria} horas")
print(f"Disciplina: {Disciplina2.nome_disciplina}, Código: {Disciplina2.codigo_disciplina}, Carga Horaria: {Disciplina2.carga_horaria} horas")

