Relatório dos 7 Erros - Exercício 10
Erro 1: Classe com nome em minúscula
Problema: class pessoa: deveria ser class Pessoa:

Solução: Renomear para class Pessoa:
Conceito POO: Convenção de nomenclatura - classes em Python devem usar PascalCase
Erro 2: Atribuição sem self
Problema: nome = nome ao invés de self.nome = nome

Solução: Alterar para self.nome = nome
Conceito POO: Encapsulamento - o atributo não era armazenado na instância
Erro 3: Atributo privado sem inicialização adequada
Problema: self.__cpf = None sem parâmetro no __init__

Solução: Adicionar parâmetro cpf=None na assinatura do método
Conceito POO: Encapsulamento - atributos privados devem ser inicializados corretamente
Erro 4: Método sem parâmetro self
Problema: def apresentar(): está faltando self

Solução: Alterar para def apresentar(self):
Conceito POO: Métodos de instância sempre precisam do parâmetro self
Erro 5: Não usar super() na herança
Problema: Estudante não chama super().__init__(), duplicando código

Solução: Usar super().__init__(nome, idade, cpf=None) para herdar inicialização da classe pai
Conceito POO: Herança - reutilizar código da classe pai evita duplicação
Erro 6: Divisão por zero
Problema: calcular_media() divide por zero quando self.notas está vazio

Solução: Adicionar verificação if not self.notas: return 0
Conceito POO: Tratamento de exceções e validação de dados
Erro 7: Teste com estudante sem notas
Problema: print(estudante.calcular_media()) sem adicionar notas causa erro

Solução: Adicionar notas com estudante.adicionar_nota() antes de calcular
Conceito POO: Lógica de negócio - estado do objeto deve ser válido antes de operações
