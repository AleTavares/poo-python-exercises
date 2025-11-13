    ## Classe Aluno ##

class Aluno:
    def __init__(self, nome, matricula, curso, notas):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, notas):
        self.notas.append(float(notas))

    def calcular_media(self):
        if len(self.notas) == 0:
          return 0.0
        return sum(self.notas) / len(self.notas)

    def status(self):
        """Imprime o status do aluno com base na média."""
        media = self.calcular_media()
        if media >= 7.0:            
            print(f"{self.nome} está Aprovado com média {media:.2f}.")
        else:
            print(f"{self.nome} está Reprovado com média {media:.2f}.")


eu_aluno = Aluno("Felipe", 3225014, "ADS", 0)


    ## Classe Disciplina ##


class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

minha_disciplina = Disciplina("ADS", 134, "4 horas")


    ## Classe Professor ##

class Professor:
    def __init__(self, nome, departamento, _salario):
        self.nome = nome
        self.departamento = departamento
        self._salario = _salario

    @property
    def salario(self):
        """Retorna o salário atual do professor."""
        return self._salario

prof = Professor("Dr. Silva", "Computação", 5000.0)



print(f"Salário atual: R$ {prof._salario}")
prof._salario = 6000.0  # Deve funcionar
print(f"Novo salário: R$ {prof._salario}")
prof._salario = -1000.0  # Deve dar erro
print(f"Salário após tentativa inválida: R$ {prof._salario}")
