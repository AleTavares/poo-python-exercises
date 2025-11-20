class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        
class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

aluno1 = Aluno("João Silva", "2023001", "Engenharia de Software")
aluno2 = Aluno("Maria Santos", "2023002", "Ciência da Computação")
aluno3 = Aluno("Feliciano Pinto", "2023003", "computação")

disciplina1 = Disciplina("Programação I", "CS101", 60)
disciplina2 = Disciplina("Cálculo I", "MA101", 80)
disciplina3 = Disciplina("computadoria", "CS101", 60)

print(f"Aluno: {aluno1.nome}, Matrícula: {aluno1.matricula},Curso: {aluno1.curso}" ", " f"Disciplina: {disciplina1.nome}, Código: {disciplina1.codigo}, Carga Horária: {disciplina1.carga_horaria}")
print(f"Aluno: {aluno2.nome}, Matrícula: {aluno2.matricula}, Curso: {aluno2.curso}" ", " f"Disciplina: {disciplina2.nome}, Código: {disciplina2.codigo}, Carga Horária: {disciplina2.carga_horaria}")
print(f"Aluno: {aluno3.nome}, Matrícula: {aluno3.matricula}, Curso: {aluno3.curso}" ", " f"Disciplina: {disciplina3.nome}, Código: {disciplina3.codigo}, Carga Horária: {disciplina3.carga_horaria}")            
