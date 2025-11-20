## Erro 1 – Nome da classe fora da convenção
**Descrição:** A classe foi declarada como `class pessoa`, começando com letra minúscula.  
**Solução:** Renomeada para `class Pessoa`.  
**Conceito POO:** Convenção e boas práticas (legibilidade e padronização).


## Erro 2 – Atributo não atribuído ao objeto
**Descrição:** Dentro do `__init__`, o código fazia `nome = nome`, sem usar `self`.  
**Solução:** Corrigido para `self.nome = nome`.  
**Conceito POO:** Encapsulamento / inicialização correta de atributos.


## Erro 3 – Uso incorreto de atributo privado
**Descrição:** Foi usado `self.__cpf`, mas nunca foi utilizado ou acessado. Além disso, o duplo underscore causa name mangling desnecessário.  
**Solução:** Ajustado para `self._cpf`, que indica atributo protegido.  
**Conceito POO:** Encapsulamento.


## Erro 4 – Método `apresentar()` sem parâmetro `self`
**Descrição:** O método foi declarado como `def apresentar():`, impossibilitando acessar atributos.  
**Solução:** Corrigido para `def apresentar(self):`.  
**Conceito POO:** Estrutura de métodos de instância.


## Erro 5 – Classe filha não chama o construtor da classe Pai
**Descrição:** `Estudante` ignora `super().__init__()` e redefine atributos manualmente.  
**Solução:** Corrigido para `super().__init__(nome, idade)`.  
**Conceito POO:** Herança e uso correto de `super()`.


## Erro 6 – Cálculo de média sem tratar lista vazia
**Descrição:** `sum(self.notas) / len(self.notas)` causava erro quando a lista estava vazia.  
**Solução:** Adicionada verificação:  
```python
if len(self.notas) == 0:
    return 0.0