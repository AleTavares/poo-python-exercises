from abc import ABC, abstractmethod


class Professor(ABC):
    def __init__(self, nome, departamento, salario):
        self._nome = nome
        self._departamento = departamento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

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
        valor = float(valor)
        if valor <= 0:
         raise ValueError("Salário não pode ser negativo.")
        self._salario = valor



prof = Professor("Dr. Silva", "Computação", 5000.0)
print(f"Salário atual: R$ {prof.salario}")
prof.salario = 6000.0  