from abc import ABC, abstractmethod


class Aluno(ABC):
    def __init__(self,nome,matricula,curso):
        self.nome=nome
        self.matricula=matricula
        self.curso=curso
        self.disciplinas=[] 
    
    def apresentar(self):
        apresentacao = f"Ola sou o aluno {self.nome}, e estudo o curso de {self.curso}"
        return apresentacao

class Professor(ABC):
    def __init__(self, nome, departamento, salario):
        self._nome = nome
        self._departamento = departamento
        self._salario = salario

    def apresentar(self):
        apresentacao = f" Olá, sou o professor{self._nome}, e leciono no departamento {self._departamento}"
        return apresentacao

class Funcionario(Professor):
    def __init__(self, nome, CPF, data_nascimento, cargo, salario):
        self.cargo = cargo
        self.salario = salario 
        self.nome= nome 

    def apresentar(self):
        apresentacao = f"Olá, sou o funcionário {self.nome},e meu cargo é {self.cargo} "
        return apresentacao



pessoas = [
    Aluno("João Silva", "2023001", "Engenharia de Software"),
    Professor("Maria", "Computação", 8000.0),
    Funcionario("Carlos Santos", "123.456.789-00", "01/01/1980", "Secretário", 3000.0)
]

for pessoa in pessoas:
    print(pessoa.apresentar())
    