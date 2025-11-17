from abc import ABC

class disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria


class curso:
    def __init__(self, nome, codigo, diciplina):
        self.nome = nome
        self.codigo = codigo
        self.diciplina = diciplina

    def adicionar_diciplina(self, diciplina):
        self.diciplina.append(diciplina)

    def listar_diciplinas(self):
        for diciplina in self.diciplina:
            print(diciplina.nome)

    def carga_horaria_total(self):
        total = sum(diciplina.carga_horaria for diciplina in self.diciplina)
        return total

