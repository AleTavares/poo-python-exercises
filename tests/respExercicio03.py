class Professor:
    def __init__(self, nome, departamento, salario):
        self.nome = nome
        self.departamento = departamento
        self._salario = salario

    @property
    def obter_salario(self):
        return self._salario
    
    @obter_salario.setter
    def obter_salario(self, novo_salario):
        if novo_salario > 0:
            self._salario = novo_salario
        else:
            print('Salario não pode ser menor que0')

    def aumentar_salario(self, valor):
        if valor > 0:
            self._salario += valor
        else:
            print('O aumento não pode ser menor ou igual a zero')

prof = Professor("Dr. Silva", "Computação", 5000.0)
print(f"Salário atual: R$ {prof.obter_salario}")
prof.obter_salario = 6000.0  # Deve funcionar
print(f"Novo salário: R$ {prof.obter_salario}")
prof.obter_salario= -1000.0  # Deve dar erro
print(f"Salário após tentativa inválida: R$ {prof.obter_salario}")

