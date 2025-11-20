class professor():
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

    def salario_professor(self, _salario, departamento):
        self.salario = _salario
        self.departamento = departamento

        if _salario > 1:
            print(f"Professor: {self.nome}, Disciplina: {self.disciplina}, Salário: R${self.salario}, Departamento: {self.departamento}")
        else:
            print("Salário inválido. O valor deve ser positivo.")

professor1 = professor("Carlos Eduardo", "Matemática")
professor1.salario_professor(4500, "Ciências Exatas")

