class Disciplina:
    
    
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
    
    def __str__(self):
        return f"{self.nome} ({self.codigo}) - {self.carga_horaria}h"


class Curso:
    """Classe que representa um curso composto por disciplinas"""
    
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.disciplinas = []
    
    def adicionar_disciplina(self, disciplina):
        """Adiciona uma disciplina ao curso"""
        if isinstance(disciplina, Disciplina):
            self.disciplinas.append(disciplina)
        else:
            print("Erro: O objeto deve ser uma instância de Disciplina")
    
    def listar_disciplinas(self):
        """Lista todas as disciplinas do curso"""
        print(f"\n=== Disciplinas do Curso: {self.nome} ===")
        if not self.disciplinas:
            print("Nenhuma disciplina cadastrada.")
        else:
            for disciplina in self.disciplinas:
                print(f"- {disciplina.nome} ({disciplina.codigo})")
    
    def carga_horaria_total(self):
        """Retorna a carga horária total do curso"""
        total = sum(disciplina.carga_horaria for disciplina in self.disciplinas)
        return total
    
    def __str__(self):
        return f"Curso: {self.nome} ({self.codigo}) - {len(self.disciplinas)} disciplinas"



if __name__ == "__main__":
    # Criando o curso
    curso = Curso("Engenharia de Software", "ES001")
    
   
    disciplina1 = Disciplina("Programação Orientada a Objetos", "POO001", 60)
    disciplina2 = Disciplina("Banco de Dados", "BD001", 80)
    disciplina3 = Disciplina("Engenharia de Requisitos", "ER001", 40)
    
   
    curso.adicionar_disciplina(disciplina1)
    curso.adicionar_disciplina(disciplina2)
    curso.adicionar_disciplina(disciplina3)
    
   
    curso.listar_disciplinas()
    
  
    print(f"Carga horária total: {curso.carga_horaria_total()}h")
    
    print("\n" + "="*50)
    print(curso)

    print("\n" + "="*50)
    curso2 = Curso("Ciência da Computação", "CC001")
    disciplina4 = Disciplina("Estruturas de Dados", "ED001", 80)
    disciplina5 = Disciplina("Algoritmos", "ALG001", 60)
    
    curso2.adicionar_disciplina(disciplina4)
    curso2.adicionar_disciplina(disciplina5)
    curso2.listar_disciplinas()
    print(f"Carga horária total: {curso2.carga_horaria_total()}h")