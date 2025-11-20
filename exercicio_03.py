class Professor:
    def __init__(self, nome, departamento, salario):
        self.nome = nome
        self.departamento = departamento
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor > 0:
            self._salario = valor
        else:
            print("Erro: Salário deve ser um valor positivo!")

prof = Professor("Dr. Silva", "Computação", 5000.0)
print(f"Salário atual: R$ {prof.salario}")

prof.salario = 6000.0
print(f"Novo salário: R$ {prof.salario}")

prof.salario = -1000.0
print(f"Salário após tentativa inválida: R$ {prof.salario}")