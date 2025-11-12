class Professor:
    def __init__(self, nome, departamento, salario):
        self.nome = nome
        self.departamento = departamento
        self._salario = None
        self.salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_salario):
        try:
            novo_salario = float(novo_salario)
            if novo_salario > 0:
                self._salario = novo_salario
            else:
                print("Salário deve ser um valor positivo.")
        except (ValueError, TypeError):
            print("Salário deve ser um número válido.")

if __name__ == "__main__":
    prof = Professor("Dr. Silva", "Computação", 5000.0)
    print(f"Salário atual: R$ {prof.salario}")
    prof.salario = 6000.0  # Deve funcionar
    print(f"Novo salário: R$ {prof.salario}")
    prof.salario = -1000.0  # Deve dar erro
    print(f"Salário após tentativa inválida: R$ {prof.salario}")        