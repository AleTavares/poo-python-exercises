class Aluno:
    def __init__(self,nome,matricula,curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, notas: float):
        try:
            notas = float(notas)
            self.notas.append(notas)
        except ValueError:
            print("Nota inválida. Por favor, insira um número.")

    def calcular_media(self):
        if not self.notas:
            return 0.0                
        media = sum(self.notas) / len(self.notas)
        return round(media, 2)
    
    def status(self):
        media = self.calcular_media()
        if media >= 7.0:
            return "Aprovado"
        else:
            return "Reprovado"
        
if __name__ == "__main__":
    aluno = Aluno("João Silva", "2023001", "Engenharia de Software")
    aluno.adicionar_nota(8.5)
    aluno.adicionar_nota(7.0)
    aluno.adicionar_nota(9.2)
    print(f"Média: {aluno.calcular_media()}")
    aluno.status()        