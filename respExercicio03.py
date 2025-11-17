class Professor:
    """
    Classe que representa um professor com encapsulamento de salário.
    
    Atributos:
        nome (str): Nome do professor
        departamento (str): Departamento ao qual pertence
        _salario (float): Salário do professor (privado)
    """
    
    def __init__(self, nome, departamento, salario):
        """
        Inicializa um novo professor.
        
        Args:
            nome (str): Nome do professor
            departamento (str): Departamento
            salario (float): Salário inicial (deve ser positivo)
        """
        self.nome = nome
        self.departamento = departamento
        self._salario = salario if salario > 0 else 0.0
        
        if salario <= 0:
            print("Erro: Salário inicial deve ser um valor positivo! Definido como R$ 0.0")
    
    @property
    def salario(self):
        """
        Getter para o atributo salário.
        
        Returns:
            float: Valor do salário atual
        """
        return self._salario
    
    @salario.setter
    def salario(self, valor):
        """
        Setter para o atributo salário com validação.
        Só permite valores positivos.
        
        Args:
            valor (float): Novo valor do salário
        """
        if valor > 0:
            self._salario = valor
        else:
            print("Erro: Salário deve ser um valor positivo!")
    
    def apresentar(self):
        """
        Retorna informações do professor.
        
        Returns:
            str: Apresentação do professor
        """
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
    
    # Teste com apresentação
    print(prof.apresentar())
    
    # Teste com outro professor
    prof2 = Professor("Dra. Santos", "Matemática", 7500.0)
    print(f"\n{prof2.apresentar()}")
    
    # Teste tentando criar professor com salário negativo
    print()
    prof3 = Professor("Dr. Costa", "Física", -500.0)
    print(f"Salário do Prof. Costa: R$ {prof3.salario}")
    
    # Teste com valores zerados
    print()
    prof.salario = 0
    print(f"Salário após tentar definir zero: R$ {prof.salario}")
    
    # Demonstrando que não é possível acessar diretamente _salario
    # (embora tecnicamente seja possível em Python, é uma convenção não fazer)
    print(f"\nAcesso direto ao atributo privado (NÃO RECOMENDADO): {prof._salario}")