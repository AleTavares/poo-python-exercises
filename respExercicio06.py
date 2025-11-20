# respExercicio06.py
# Exercício 06 - Composição (Curso "tem um" conjunto de Disciplinas)

# Classe Disciplina (do exercício 1)
class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria


# Classe Curso usando Composição
class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.disciplinas = []  # lista de objetos Disciplina

    def adicionar_disciplina(self, disciplina):
        """Adiciona um objeto Disciplina ao curso."""
        self.disciplinas.append(disciplina)


    def listar_disciplinas(self):
        """Mostra o nome e código de cada disciplina."""
    
        # Preenchimento da lista de disciplinas
        print(f"=== Disciplinas do Curso: {self.nome} ===")        
        for disciplina in self.disciplinas:
            print(f"- {disciplina.nome} ({disciplina.codigo})")
    

    def carga_horaria_total(self):
        """Retorna a soma da carga horária das disciplinas."""
        return sum(d.carga_horaria for d in self.disciplinas)


# Exemplo de Uso
if __name__ == "__main__":
    curso = Curso("Engenharia de Software", "ES001")

    disciplina1 = Disciplina("Programação Orientada a Objetos", "POO001", 60)
    disciplina2 = Disciplina("Banco de Dados", "BD001", 80)

    curso.adicionar_disciplina(disciplina1)
    curso.adicionar_disciplina(disciplina2)

    curso.listar_disciplinas()

    print(f"Carga horária total: {curso.carga_horaria_total()}h")
