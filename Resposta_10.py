
class Pessoa:  
    def __init__(self, nome, idade):
        self.nome = nome  
        self.idade = idade
        self._cpf = None  

    def apresentar(self):
        return f"Olá, sou {self.nome}"


class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:  
            return 0.0
        return sum(self.notas) / len(self.notas)


class Professor(Pessoa):
    def __init__(self, nome, idade, departamento, salario):
        super().__init__(nome, idade)
        self.departamento = departamento
        self.salario = salario

    def apresentar(self):
        return f"Olá, sou o professor {self.nome} do departamento {self.departamento}"



if __name__ == "__main__":
    estudante = Estudante("João", 20, "Engenharia")
    professor = Professor("Dr. Silva", 45, "Computação", 8000)

    
    estudante.adicionar_nota(8.5)
    estudante.adicionar_nota(9.0)
    estudante.adicionar_nota(7.5)

    print(estudante.apresentar())
    print(professor.apresentar())
    print(f"Média do estudante: {estudante.calcular_media():.2f}") 
