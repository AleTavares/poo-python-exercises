class Professor:
    def __init__(self, nome, departamento, salario):
        self.nome = nome
        self.departamento = departamento
        self._salario = salario  # atributo privado

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_valor):
        if novo_valor > 0:
            self._salario = novo_valor
        else:
            print("Erro: Salário deve ser um valor positivo!")
