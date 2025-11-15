class Professor 
    def __init__(self, salario, nome, departamento ):
        self.nome = nome
        self.departamento = departamento
        self._salario = salario
    
    #Getter
    def obter_salario(self):
        return self._salario 
        