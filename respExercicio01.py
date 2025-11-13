

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
    
    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, minha matricula é {self.matricula} e estudo no curso de {self.curso}."

class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

    def apresentar(self):
        return f"Disciplina: {self.nome}, Código: {self.codigo} e Carga Horária: {self.carga_horaria}."

#criando os objetos
aluno1 = Aluno ("Danielle", 6325179, "Análise e Desenvolvimento de Sistemas")
aluno2 = Aluno ("Bruno", 6325874, "Engenharia")

disciplina1 = Disciplina ("Análise e Desenvolvimento de Sistemas", "POO001", "60h")
discuplina2 = Disciplina ("Engenharia", "POO002", "100h")

#apresentação
print(aluno1.apresentar())
print(aluno2.apresentar())

print(disciplina1.apresentar())
print(discuplina2.apresentar())