
from respExercicio1 import Aluno

class Aluno_nota(Aluno):
    def __init__(self,nome, matricula, curso , notas):
        super().__init__(nome,matricula,curso)
        self.notas = notas

    def adicionar_nota (self, adicionar_nota):
        self.adicionar = adicionar_nota

    def calcular_media (self, calcular_media):
        self.calcular = calcular_media

    def status (self, status):
        self.status= status 
