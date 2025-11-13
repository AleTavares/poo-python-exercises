# Exercício 08 - Método de Classe (@classmethod)

## Objetivo

Entender o uso de métodos de classe para criar fábricas de objetos.

## Descrição do Exercício

Crie a classe **Departamento** com métodos de classe para facilitar a criação de objetos.

### Requisitos

1. Crie a classe **Departamento** com atributos:
   - nome
   - sigla
   - professores (lista de professores)

2. Implemente um método de classe `@classmethod` chamado `criar_departamento_exatas(nome)` que automaticamente atribui a sigla como "EXA".

3. Implemente um método de classe `@classmethod` chamado `criar_departamento_humanas(nome)` que automaticamente atribui a sigla como "HUM".

4. Adicione um método `adicionar_professor(professor)` e `listar_professores()`.

5. Use esses métodos para criar dois departamentos distintos.

## Entrega

Crie um arquivo chamado `respExercicio08.py` com a implementação dos métodos de classe.

## Exemplo de Uso

```python
dept_exatas = Departamento.criar_departamento_exatas("Matemática e Computação")
dept_humanas = Departamento.criar_departamento_humanas("Letras e Filosofia")

print(f"Departamento: {dept_exatas.nome} - Sigla: {dept_exatas.sigla}")
print(f"Departamento: {dept_humanas.nome} - Sigla: {dept_humanas.sigla}")
```

## Exemplo de Saída Esperada

```
Departamento: Matemática e Computação - Sigla: EXA
Departamento: Letras e Filosofia - Sigla: HUM
```
