class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = [0,1,2,3,4,5,6,7,8,9,10]  

    def adicionar_nota(self, nota):
        """Adiciona uma nova nota à lista de notas."""
        self.notas.append(nota)

    def calcular_media(self):
        """Calcula e retorna a média das notas do aluno."""
        if len(self.notas) == 0:
            return 0.0  # evita divisão por zero
        media = sum(self.notas) / len(self.notas)
        return round(media, 2)  # arredonda para duas casas decimais

    def status(self):
        """Imprime o status do aluno com base na média."""
        media = self.calcular_media()
        if media >= 7.0:
            print("Aprovado")
        else:
            print("Reprovado")


# Exemplo de uso:
if __name__ == "__main__":
    aluno = Aluno("João Silva", "2023001", "Engenharia de Software")
    aluno.adicionar_nota(8.5)
    aluno.adicionar_nota(7.0)
    aluno.adicionar_nota(9.2)
    print(f"Média: {aluno.calcular_media()}")
    aluno.status()


            
