# respExercicio03.py
# Exercício 03 - Encapsulamento e Propriedades

class Professor:
    def __init__(self, nome, departamento, salario):
        self.nome = nome
        self.departamento = departamento
        self._salario = salario  # atributo privado (por convenção, começa com _)

    # Getter para o salário
    @property
    def salario(self):
        """Retorna o valor atual do salário."""
        return self._salario

    # Setter para o salário
    @salario.setter
    def salario(self, novo_salario):
        """Define um novo salário, se o valor for positivo."""
        if novo_salario > 0:
            self._salario = novo_salario
        else:
            print("Erro: Salário deve ser um valor positivo!")

    # Método opcional para exibir os dados do professor
    def exibir_informacoes(self):
        print(f"Professor: {self.nome}")
        print(f"Departamento: {self.departamento}")
        print(f"Salário: R$ {self._salario}")


# Exemplo de uso
if __name__ == "__main__":
    prof = Professor("Dr. Silva", "Computação", 5000.0)

    print(f"Salário atual: R$ {prof.salario}")

    prof.salario = 6000.0  # Deve funcionar
    print(f"Novo salário: R$ {prof.salario}")

    prof.salario = -1000.0  # Deve dar erro
    print(f"Salário após tentativa inválida: R$ {prof.salario}")
