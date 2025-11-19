class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def status(self):
        media = self.calcular_media()
        if media >= 7.0:
            print("Aprovado")
        else:
            print("Reprovado")

    def __str__(self):
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}, Curso: {self.curso}, Notas: {self.notas}"

if __name__ == "__main__":
    aluno = Aluno("João Silva", "2023001", "Engenharia de Software")
    
    aluno.adicionar_nota(8.5)
    aluno.adicionar_nota(7.0)
    aluno.adicionar_nota(9.2)
    
 
    media_formatada = f"{aluno.calcular_media():.2f}"
    print(f"Média: {media_formatada}")
    aluno.status()
    
    print("-" * 20)
    
  
    aluno_b = Aluno("Pedro Mendes", "2023003", "Análise de Sistemas")
    aluno_b.adicionar_nota(5.0)
    aluno_b.adicionar_nota(6.5)
    print(f"Média: {aluno_b.calcular_media():.2f}")
    aluno_b.status()