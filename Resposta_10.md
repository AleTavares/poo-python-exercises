# Relatório – Jogo dos 7 Erros de POO
## Autor: José Henrique Teixeira Luiz

---

## Erro 1 – Nome da classe fora da convenção
**Problema:** A classe foi escrita como `class pessoa` (minúsculo).  
**Solução:** Alterado para `class Pessoa:` seguindo PEP8.  
**Conceito violado:** Nomenclatura e boas práticas de classe.

---

## Erro 2 – Atributo não inicializado corretamente
**Problema:** No construtor: `nome = nome` — isso não atribui ao objeto.  
**Solução:** Corrigido para `self.nome = nome`.  
**Conceito violado:** Inicialização de atributos de instância.

---

## Erro 3 – Encapsulamento inconsistente
**Problema:** Usado `__cpf` (duplo underline), dificultando acesso e podendo gerar name mangling desnecessário.  
**Solução:** Alterado para `_cpf`, seguindo a convenção de atributo protegido.  
**Conceito violado:** Encapsulamento.

---

## Erro 4 – Método sem parâmetro `self`
**Problema:** O método `apresentar()` não possuía `self`.  
**Solução:** Corrigido para `def apresentar(self):`.  
**Conceito violado:** Métodos de instância.

---

## Erro 5 – Construtor de Estudante ignorando herança
**Problema:** A classe Estudante inicializava `nome` e `idade` diretamente, quebrando a reutilização do construtor da classe base.  
**Solução:** Adicionado `super().__init__(nome, idade)`.  
**Conceito violado:** Herança e uso correto de super().

---

## Erro 6 – Possível divisão por zero ao calcular a média
**Problema:** `len(self.notas)` pode ser 0, gerando erro.  
**Solução:** Adicionada verificação: retorna 0 caso não haja notas.  
**Conceito violado:** Tratamento de exceções / lógica de negócio.

---

## Erro 7 – Média chamada antes de adicionar notas
**Problema:** No teste final, `calcular_media()` era chamado sem notas → erro de divisão.  
**Solução:** No script final, adicionadas notas antes do cálculo.  
**Conceito violado:** Lógica de negócio e consistência do estado do objeto.

---

# Resultado Final
Todos os 7 erros foram identificados e corrigidos.  
O código agora funciona corretamente, respeitando princípios de:

- Encapsulamento  
- Herança  
- Construtores  
- Polimorfismo básico  
- Boas práticas Python (PEP8)  
