class Aluno:
    def __init__(self,nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso


class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria        


aluno1 = Aluno("Thiago",6325304,"Analise e Desenvolvimento de Sistemas")
aluno2 = Aluno("Ana",6325305,"Odontologia")


disciplina1 = Disciplina("POO","Analise e Desenvolvimento de Sistemas","60h")
disciplina2 = Disciplina("Anatomia","Odontologia","80h")    

