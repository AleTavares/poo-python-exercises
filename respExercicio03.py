class Professor:
 
    def __init__(self, nome, departamento, salario):
 
        self.nome = nome
        self.departamento = departamento
        self._salario = salario if salario > 0 else 0.0
        
        if salario <= 0:
            print("Erro: Salário inicial deve ser um valor positivo! Definido como R$ 0.0")
    
    @property
    def salario(self):

        return self._salario
    
    @salario.setter
    def salario(self, valor):
 
        if valor > 0:
            self._salario = valor
        else:
            print("Erro: Salário deve ser um valor positivo!")
    
    def apresentar(self):
     
        return f"Professor(a) {self.nome} - Departamento: {self.departamento} - Salário: R$ {self._salario:.2f}"


# Exemplo de uso
if __name__ == "__main__":
    prof = Professor("Dr. Silva", "Computação", 5000.0)
    print(f"Salário atual: R$ {prof.salario}")
    
    prof.salario = 6000.0  # Deve funcionar
    print(f"Novo salário: R$ {prof.salario}")
    
    prof.salario = -1000.0  # Deve dar erro
    print(f"Salário após tentativa inválida: R$ {prof.salario}")
    
    print("\n--- Testes adicionais ---")
    
   
    print(prof.apresentar())
    
   
    prof2 = Professor("Dra. Santos", "Matemática", 7500.0)
    print(f"\n{prof2.apresentar()}")
    
    
    print()
    prof3 = Professor("Dr. Costa", "Física", -500.0)
    print(f"Salário do Prof. Costa: R$ {prof3.salario}")
    
   
    prof.salario = 0
    print(f"Salário após tentar definir zero: R$ {prof.salario}")
    
 
    print(f"\nAcesso direto ao atributo privado (NÃO RECOMENDADO): {prof._salario}")