# Exercício 05 - Herança e o Uso de super()

## Objetivo

Entender e utilizar a função super() no construtor da classe filha.

## Descrição do Exercício

Aprimore a classe **Funcionario** do exercício 4 utilizando corretamente a função `super()`.

### Requisitos

1. No construtor (`__init__`) de **Funcionario**, utilize `super().__init__(...)` para inicializar os atributos herdados de **Pessoa**.

2. Adicione um atributo adicional `salario` à classe Funcionario.

3. Crie um método `exibir_dados()` que mostre todos os dados do funcionário.

4. Crie um objeto Funcionario e garanta que todos os atributos (herdados e próprios) foram inicializados corretamente.

## Entrega

Crie um arquivo chamado `respExercicio05.py` com a implementação aprimorada usando `super()`.

## Exemplo de Uso

```python
funcionario = Funcionario("Ana Costa", "111.222.333-44", "20/03/1988", "Coordenadora", 4500.0)
funcionario.exibir_dados()
```

## Exemplo de Saída Esperada

```
=== Dados do Funcionário ===
Nome: Ana Costa
CPF: 111.222.333-44
Data de Nascimento: 20/03/1988
Cargo: Coordenadora
Salário: R$ 4500.0
```
