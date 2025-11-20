class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        
    def apresentar(self):
            return f"Olá, meu nome é {self.nome}, minha matrícula é {self.matricula}."

class Professor:
    def __init__(self, nome, departamento, salario):
        self.nome = nome
        self.departamento = departamento
        self.salario = salario
        
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu trabalho no departamento de {self.departamento}."
    
class Funcionario:
        def __init__(self, nome, cpf, data_nascimento, setor, salario):
            self.nome = nome
            self.cpf = cpf
            self.data_nascimento = data_nascimento
            self.salario = salario
            self.setor = setor
            
        def apresentar(self):
            return f"Olá, meu nome é {self.nome} e eu trabalho no setor de {self.setor}."
        
      #criando objetos

        
pessoas = [
    Aluno("João Silva", "2023001", "Engenharia de Software"),
    Professor("Dr. Maria", "Computação", 8000.0),
    Funcionario("Carlos Santos", "123.456.789-00", "01/01/1980", "Secretário", 3000.0)
]

   # polimorfismo
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