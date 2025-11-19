class Professor:
    def __init__(self, nome, departamento, salario_inicial):
        self.nome = nome
        self.departamento = departamento
        self._salario = 0.0
        self.salario = salario_inicial 

    @property
    def salario(self):
        """Getter: Retorna o valor do salário privado."""
        return self._salario

    @salario.setter
    def salario(self, novo_salario):
        """
        Setter: Define o valor do salário, validando se é positivo.
        Se for inválido, imprime uma mensagem de erro.
        """
        if novo_salario > 0:
            self._salario = novo_salario
        else:
            print("Erro: Salário deve ser um valor positivo!")

if __name__ == "__main__":
    
    
    prof = Professor("Dr. Silva", "Computação", 5000.0)
    print(f"Salário atual: R$ {prof.salario}")

    
    prof.salario = 6000.0
    print(f"Novo salário: R$ {prof.salario}")

    
    prof.salario = -1000.0
    print(f"Salário após tentativa inválida: R$ {prof.salario}")