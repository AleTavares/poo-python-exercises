class Aluno:
    def __init__ (self, nome, matricula, curso, notas=[]):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = notas
        
    def adicionar_nota(self, nota):
        if len(self.notas) >= 2:
            print("Número máximo de notas atingido.")
            self.notas = []
        self.notas.append(nota)
        
    def calcular_media(self):
        print(self.notas)
        return sum(self.notas) / len(self.notas)
      
    def status(self):
        media = self.calcular_media()      
        return "Aprovado" if media >= 7 else "Reprovado"
      
class Disciplina:
    def __init__ (self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

aluno = Aluno("João Silva", "2023001", "Engenharia de Software")

aluno.adicionar_nota(8)
aluno.adicionar_nota(7)

aluno_media = aluno.calcular_media()

print(f"Média do aluno: {aluno_media:.2f}")
aluno.status()

disciplina = Disciplina("Programação Orientada a Objetos", "CS101", 60)

print(f"Aluno: {aluno.nome}, Matrícula: {aluno.matricula}, Curso: {aluno.curso}")

print(f"Disciplina: {disciplina.nome}, Código: {disciplina.codigo}, Carga Horária: {disciplina.carga_horaria} horas")