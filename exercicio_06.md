   # Exercício 06 - Composição (Relacionamento "Tem Um")

   ## Objetivo
   Praticar o princípio da Composição, onde um objeto é feito de outros objetos.

   ## Descrição do Exercício
   Crie a classe **Curso** que será composta por objetos **Disciplina**.

   ### Requisitos:

   1. Crie a classe **Curso** com atributos:
      - nome
      - codigo
      - disciplinas (lista de objetos Disciplina)

   2. Um **Curso** deve ser composto por uma lista de objetos **Disciplina** (do exercício 1).

   3. Adicione um método `adicionar_disciplina(disciplina)` à classe Curso.

   4. Adicione um método `listar_disciplinas()` que imprima o nome e código de cada disciplina.

   5. Adicione um método `carga_horaria_total()` que retorne a soma da carga horária de todas as disciplinas.

   ## Entrega
   Crie um arquivo chamado `respExercicio06.py` com a implementação das classes e demonstração da composição.

   ## Exemplo de Uso
   ```python
   curso = Curso("Engenharia de Software", "ES001")
   disciplina1 = Disciplina("Programação Orientada a Objetos", "POO001", 60)
   disciplina2 = Disciplina("Banco de Dados", "BD001", 80)

   curso.adicionar_disciplina(disciplina1)
   curso.adicionar_disciplina(disciplina2)
   curso.listar_disciplinas()
   print(f"Carga horária total: {curso.carga_horaria_total()}h")
   ```

   ## Exemplo de Saída Esperada
   ```
   === Disciplinas do Curso: Engenharia de Software ===
   - Programação Orientada a Objetos (POO001)
   - Banco de Dados (BD001)
   Carga horária total: 140h
   ```