class Professor:
    def __init__(self, nome, departamento, salario):
        self.nome = nome
        self.departamento = departamento
        self._salario = float(salario)

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_salario):
        try:
            novo_salario = float(novo_salario)
        except (TypeError, ValueError):
            print("Erro: Salário deve ser um valor positivo!")
            return
        if novo_salario > 0:
            self._salario = novo_salario
        else:
            print("Erro: Salário deve ser um valor positivo!")
