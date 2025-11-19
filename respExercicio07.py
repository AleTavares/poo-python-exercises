class Aluno:
    """Classe que representa um aluno"""
    
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas_inscritas = []
    
    def listar_disciplinas(self):
        """Lista todas as disciplinas em que o aluno está inscrito"""
        print(f"\n=== Disciplinas de {self.nome} ({self.matricula}) ===")
        if not self.disciplinas_inscritas:
            print("Nenhuma disciplina inscrita.")
        else:
            for disciplina in self.disciplinas_inscritas:
                print(f"- {disciplina.nome} ({disciplina.codigo}) - {disciplina.carga_horaria}h")
            total = sum(d.carga_horaria for d in self.disciplinas_inscritas)
            print(f"Total de carga horária: {total}h")
    
    def __str__(self):
        return f"{self.nome} ({self.matricula}) - {self.curso}"


class Disciplina:
    """Classe que representa uma disciplina"""
    
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.alunos_matriculados = []
    
    def listar_alunos(self):
        """Lista todos os alunos matriculados na disciplina"""
        print(f"\n=== Alunos matriculados em {self.nome} ({self.codigo}) ===")
        if not self.alunos_matriculados:
            print("Nenhum aluno matriculado.")
        else:
            for i, aluno in enumerate(self.alunos_matriculados, 1):
                print(f"{i}. {aluno.nome} ({aluno.matricula}) - {aluno.curso}")
            print(f"Total de alunos: {len(self.alunos_matriculados)}")
    
    def __str__(self):
        return f"{self.nome} ({self.codigo}) - {self.carga_horaria}h"


class Secretaria:
    """Classe responsável por gerenciar inscrições"""
    
    @staticmethod
    def inscrever_aluno(aluno, disciplina):
        """
        Inscreve um aluno em uma disciplina (relacionamento muitos-para-muitos)
        """
        if not isinstance(aluno, Aluno):
            print("Erro: O primeiro parâmetro deve ser um objeto Aluno")
            return False
        
        if not isinstance(disciplina, Disciplina):
            print("Erro: O segundo parâmetro deve ser um objeto Disciplina")
            return False
        
        # Verifica se o aluno já está inscrito na disciplina
        if disciplina in aluno.disciplinas_inscritas:
            print(f"Aviso: {aluno.nome} já está inscrito em {disciplina.nome}")
            return False
        
        # Adiciona a disciplina à lista do aluno
        aluno.disciplinas_inscritas.append(disciplina)
        
        # Adiciona o aluno à lista da disciplina
        disciplina.alunos_matriculados.append(aluno)
        
        print(f"✓ {aluno.nome} foi inscrito em {disciplina.nome}")
        return True
    
    @staticmethod
    def cancelar_inscricao(aluno, disciplina):
        """Remove a inscrição de um aluno em uma disciplina"""
        if disciplina in aluno.disciplinas_inscritas:
            aluno.disciplinas_inscritas.remove(disciplina)
            disciplina.alunos_matriculados.remove(aluno)
            print(f"✓ Inscrição de {aluno.nome} em {disciplina.nome} cancelada")
            return True
        else:
            print(f"Aviso: {aluno.nome} não está inscrito em {disciplina.nome}")
            return False
    
    @staticmethod
    def relatorio_geral(alunos, disciplinas):
        """Gera um relatório geral de alunos e disciplinas"""
        print("\n" + "="*60)
        print("RELATÓRIO GERAL DO SISTEMA")
        print("="*60)
        
        print(f"\nTotal de alunos: {len(alunos)}")
        print(f"Total de disciplinas: {len(disciplinas)}")
        
        total_inscricoes = sum(len(a.disciplinas_inscritas) for a in alunos)
        print(f"Total de inscrições: {total_inscricoes}")


# Demonstração do uso das classes
if __name__ == "__main__":
    print("="*60)
    print("SISTEMA DE GESTÃO ACADÊMICA")
    print("="*60)
    
    # Criando alunos
    aluno1 = Aluno("João Silva", "2023001", "Engenharia de Software")
    aluno2 = Aluno("Maria Santos", "2023002", "Ciência da Computação")
    aluno3 = Aluno("Pedro Oliveira", "2023003", "Engenharia de Software")
    
    # Criando disciplinas
    disciplina1 = Disciplina("Programação Orientada a Objetos", "POO001", 60)
    disciplina2 = Disciplina("Banco de Dados", "BD001", 80)
    disciplina3 = Disciplina("Estruturas de Dados", "ED001", 80)
    
    print("\n--- REALIZANDO INSCRIÇÕES ---")
    # Inscrevendo alunos nas disciplinas
    Secretaria.inscrever_aluno(aluno1, disciplina1)
    Secretaria.inscrever_aluno(aluno1, disciplina2)
    Secretaria.inscrever_aluno(aluno2, disciplina1)
    Secretaria.inscrever_aluno(aluno2, disciplina3)
    Secretaria.inscrever_aluno(aluno3, disciplina1)
    Secretaria.inscrever_aluno(aluno3, disciplina2)
    Secretaria.inscrever_aluno(aluno3, disciplina3)
    
    # Tentando inscrever novamente (deve avisar que já está inscrito)
    print("\n--- TESTANDO DUPLICAÇÃO ---")
    Secretaria.inscrever_aluno(aluno1, disciplina1)
    
    # Listando disciplinas de cada aluno
    print("\n" + "="*60)
    aluno1.listar_disciplinas()
    aluno2.listar_disciplinas()
    aluno3.listar_disciplinas()
    
    # Listando alunos de cada disciplina
    print("\n" + "="*60)
    disciplina1.listar_alunos()
    disciplina2.listar_alunos()
    disciplina3.listar_alunos()
    
    # Cancelando uma inscrição
    print("\n" + "="*60)
    print("--- CANCELANDO INSCRIÇÃO ---")
    Secretaria.cancelar_inscricao(aluno1, disciplina2)
    
    # Verificando após cancelamento
    aluno1.listar_disciplinas()
    disciplina2.listar_alunos()
    
    # Relatório geral
    todos_alunos = [aluno1, aluno2, aluno3]
    todas_disciplinas = [disciplina1, disciplina2, disciplina3]
    Secretaria.relatorio_geral(todos_alunos, todas_disciplinas)
    
    print("\n" + "="*60)