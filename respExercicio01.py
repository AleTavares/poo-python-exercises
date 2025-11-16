class aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
  
    class disciplina:
        def __init__(self, nome_disciplina, codigo_disciplina, carga_horaria):
            self.nome_disciplina = nome_disciplina
            self.codigo_disciplina = codigo_disciplina
            self.carga_horaria = carga_horaria
       
        
aluno1 = aluno("Joao Silva", "2023001", "Engenharia de Software")
aluno2 = aluno("Maria Santos", "2023002", "Ciencia da Computacao")
disciplina1 = aluno.disciplina("Programação Orientada a Objetos", "POO101", 60)
disciplina2 = aluno.disciplina("Estruturas de Dados", "ED202", 45)
print(f"Aluno: {aluno1.nome}, Matrícula: {aluno1.matricula}, Curso: {aluno1.curso}")
print(f"Aluno: {aluno2.nome}, Matrícula: {aluno2.matricula}, Curso: {aluno2.curso}")
print(f"Disciplina: {disciplina1.nome_disciplina}, Código: {disciplina1.codigo_disciplina}, Carga Horaria: {disciplina1.carga_horaria} horas")
print(f"Disciplina: {disciplina2.nome_disciplina}, Código: {disciplina2.codigo_disciplina}, Carga Horaria: {disciplina2.carga_horaria} horas")

