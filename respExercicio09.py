class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        
    def apresentar(self):
        return (
            f"Olá, meu nome é {self.nome}, "
            f"sou aluno do curso de {self.curso} "
            f"e minha matrícula é {self.matricula}."
        )


class Professor:
    def __init__(self, nome, departamento, salario):
        self.nome = nome
        self.departamento = departamento
        self.salario = salario
        
    def apresentar(self):
        return (
            f"Olá, meu nome é {self.nome}, "
            f"sou professor e trabalho no departamento de {self.departamento}."
        )
    

class Funcionario:
    def __init__(self, nome, cpf, data_nascimento, setor, salario):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.setor = setor
        self.salario = salario
            
    def apresentar(self):
        return (
            f"Olá, meu nome é {self.nome}, "
            f"sou funcionário e trabalho no setor de {self.setor}."
        )


# Demonstração de polimorfismo
if __name__ == "__main__":
    pessoas = [
        Aluno("João Silva", "2023001", "Engenharia de Software"),
        Professor("Dr. Maria", "Computação", 8000.0),
        Funcionario("Carlos Santos", "123.456.789-00", "01/01/1980", "Secretaria", 3000.0)
    ]

    for pessoa in pessoas:
        print(pessoa.apresentar())


#dúvidas?????

#aluno = aluno("João Silva", "2023001", "Engenharia de Software")
#professor = professor("Dr. Maria", "Computação")
#funcionario = funcionario("Carlos Santos", "Recursos Humanos")

 # apresentações
#print(aluno.apresentar())
#print(professor.apresentar())
#print(funcionario.apresentar())