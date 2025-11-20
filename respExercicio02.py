class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = []
    
    def adicionar_nota(self, nota):
        self.notas.append(nota)
    
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0.0
        return sum(self.notas) / len(self.notas)
    
    def status(self):
        media = self.calcular_media()
        if media >= 7.0:
            print("Aprovado")
        else:
            print("Reprovado")



if __name__ == "__main__":
    aluno = Aluno("João Silva", "2023001", "Engenharia de Software")
    aluno.adicionar_nota(8.5)
    aluno.adicionar_nota(7.0)
    aluno.adicionar_nota(9.2)
    print(f"Média: {aluno.calcular_media()}")
    aluno.status()
    
    print("\n--- Teste adicional ---")
    aluno2 = Aluno("Maria Santos", "2023002", "Ciência da Computação")
    aluno2.adicionar_nota(6.5)
    aluno2.adicionar_nota(5.8)
    aluno2.adicionar_nota(6.0)
    print(f"Média: {aluno2.calcular_media():.2f}")
    aluno2.status()