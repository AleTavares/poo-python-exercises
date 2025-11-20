class Professor:
    def __init__(self, nome: str, departamento: str, salario: float):
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

    def exibir_informacoes(self):
        return f"Professor: {self.nome}, Departamento: {self.departamento}, Salário: R$ {self._salario:.2f}"

if __name__ == "__main__":
    professor = Professor("Dr. Silva", "Computacao", 5000.00)
    print(f"salario atual: {professor.salario}")
    professor.salario = 6000.00  
    print(f"novo salario: {professor.salario}")
    professor.salario = -1000.00
    print(f"salario apos tentativa invalida: {professor.salario}")


    

       