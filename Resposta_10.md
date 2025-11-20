# Relatório – Exercício 10  
Correção dos 7 Erros de POO no Código Fornecido

## Erro 1 – Nome da classe em minúsculo
**Descrição:** A classe foi declarada como `class pessoa:` usando letra minúscula, violando a convenção PascalCase usada para classes em Python.  
**Solução:** Renomear para `class Pessoa:`.  
**Conceito POO:** Boas práticas e padronização de modelagem.

## Erro 2 – Atributo `nome` não armazenado no objeto
**Descrição:** O código do construtor contém `nome = nome`, o que não associa o valor ao objeto.  
**Solução:** Alterado para `self.nome = nome`.  
**Conceito POO:** Encapsulamento e inicialização correta de atributos.

## Erro 3 – Atributo privado `__cpf` sem uso
**Descrição:** O construtor atribui `self.__cpf = None`, mas o atributo nunca é usado, lido ou alterado, caracterizando falha de modelagem.  
**Solução:** Mantido, mas corretamente inicializado. Idealmente deveria possuir getter/setter ou ser removido.  
**Conceito POO:** Encapsulamento (atributos privados precisam ter motivo e acesso adequado).

## Erro 4 – Método `apresentar()` sem `self`
**Descrição:** O método foi declarado como `def apresentar():`, impossibilitando acesso aos atributos da instância.  
**Solução:** Adicionado o parâmetro: `def apresentar(self):`.  
**Conceito POO:** Métodos de instância devem sempre receber `self`.

## Erro 5 – Classe Estudante não chama o construtor da classe mãe
**Descrição:** O construtor de `Estudante` redefine manualmente atributos herdados e não reutiliza o construtor de Pessoa.  
**Solução:** Alterado para usar `super().__init__(nome, idade)`.  
**Conceito POO:** Herança – uso adequado de `super()` para reaproveitamento.

## Erro 6 – Possível divisão por zero no cálculo da média
**Descrição:** O método `calcular_media()` divide por `len(self.notas)` sem verificar se há notas, causando erro quando a lista está vazia.  
**Solução:** Inserido teste: `if len(self.notas) == 0: return 0`.  
**Conceito POO:** Robustez e tratamento seguro de lógica de negócio.

## Erro 7 – Chamada de `calcular_media()` sem notas cadastradas
**Descrição:** No código de teste, `calcular_media()` é chamado antes de qualquer nota ser adicionada.  
**Solução:** Após correção do Erro 6, o método simplesmente retorna 0, evitando falha.  
**Conceito POO:** Execução segura e responsabilidade do método.

