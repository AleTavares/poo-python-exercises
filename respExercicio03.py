class Professor:
    def __init__(self,nome, departamento,salario):
        self.nome =nome
        self.departamento = departamento
        self._salario = salario 


    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome (self, valor):
        self._nome =valor

    @property
    def departamento(self):
        return self._departamento
    
    @departamento.setter
    def departamento(self, valor):
        self._departamento = valor


    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, valor):
        if valor > 0:
            self._salario = valor
        else:
            print("Erro: Salário deve ser um valor positivo!")


prof = Professor ("Dr. Silva", "Matemática", 5000.0)
print(f" salario atual: {prof.salario}")
prof.salario = 6000.0