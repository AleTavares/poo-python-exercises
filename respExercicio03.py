class Professor:
    def __init__(self, nome, departamento, salario):
        self.nome = nome
        self.departamento = departamento
        self._salario = salario  

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario > 0:
            self._salario = novo_salario
        else:
            print("Erro: Salário deve ser um valor positivo")
