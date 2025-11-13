from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, CPF, data_nascimento=None):
        self.nome = nome
        self.CPF = CPF
        self.data_nascimento = None

    def apresentar(self):
        return f"Nome: {self.nome}, CPF: {self.CPF}"
    
class Funcionario(Pessoa):
    def __init__(self, nome, CPF,cargo, data_nascimento=None):
        super().__init__(nome, CPF, data_nascimento)
        self.cargo = cargo

    
class Tutor(Pessoa):
    def __init__(self, nome, CPF, area_atuacao, data_nascimento=None):
        super().__init__(nome, CPF, data_nascimento)
        self.area_atuacao = area_atuacao
        def apresentar(self):
            return (f" Área de Atuação: {self.area_atuacao}")