class Professor:
    def __init__(self, salario, departamento, nome):
        self.nome = nome
        self.departamento = departamento
        self._salario = salario
    
    @property 
    def salario(self):  
        return self._salario
  
    @salario.setter
    def salario(self, receber_salario):
        if receber_salario < 0:
            raise ValueError("Salário não pode ser negativo.")
        self._salario = receber_salario


prof = Professor(5000.0, "Computação", "Dr. Silva")

print(f"Salário atual: R$ {prof.salario}")

prof.salario = 6000.0 
print(f"Novo salário: R$ {prof.salario}")

try:
    prof.salario = -1000.0
except ValueError as erro:
    print(f"Erro capturado: {erro}")

print(f"Salário após tentativa inválida: R$ {prof.salario}") 