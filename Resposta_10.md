# Relatório: Erros encontrados e correções - Exercício 10

Abaixo estão os 7 erros identificados no código fornecido, a solução aplicada e o princípio de POO envolvido.

---

**Erro 1**: Nome da classe em minúsculas

- Descrição: A classe foi declarada como `class pessoa:` (nome em minúsculas). Pela convenção do Python e boas práticas de POO, nomes de classes devem usar PascalCase.
- Solução: Renomeada para `class Pessoa:`.
- Conceito POO: Convenção de nomenclatura / legibilidade.

---

**Erro 2**: Atributo `nome` não atribuído ao objeto

- Descrição: No construtor foi usado `nome = nome` (atribuição local), em vez de `self.nome = nome`. Isso não cria o atributo de instância.
- Solução: Corrigido para `self.nome = nome` no `__init__` de `Pessoa`.
- Conceito POO: Encapsulamento / inicialização de atributos de instância.

---

**Erro 3**: Uso incorreto / falta de inicialização do atributo `__cpf`

- Descrição: Existia uma referência solta a `self.__cpf` no construtor (ou em algumas versões faltava a atribuição). Esse uso sem atribuição provoca `AttributeError` ou é ambíguo.
- Solução: Inicializar o atributo privado corretamente: `self.__cpf = None`.
- Conceito POO: Encapsulamento / atributos privados (name mangling). Inicialização correta de estado do objeto.

---

**Erro 4**: Método `apresentar` sem parâmetro `self`

- Descrição: O método foi definido como `def apresentar():`, sem o parâmetro `self`, tornando impossível acessar `self.nome` dentro do método.
- Solução: Alterado para `def apresentar(self):` e uso de `self.nome` para compor a string.
- Conceito POO: Métodos de instância devem aceitar `self` como primeiro parâmetro.

---

**Erro 5**: Inicialização incorreta na subclasse `Estudante`

- Descrição: A classe `Estudante` atribuía manualmente `self.nome = nome` e `self.idade = idade` invés de reutilizar o construtor da superclasse, perdendo lógica de inicialização e manutenção.
- Solução: Usar `super().__init__(nome, idade)` dentro de `Estudante.__init__` para reaproveitar a inicialização da classe `Pessoa`.
- Conceito POO: Herança e reutilização de construtores com `super()`.

---

**Erro 6**: Cálculo de média sem tratamento de casos especiais

- Descrição: O cálculo `sum(self.notas) / len(self.notas)` assume que `self.notas` não está vazia; quando lista vazia, causa `ZeroDivisionError`.
- Solução parcial/relacionada: implementar verificação antes da divisão (feito na solução final abaixo).
- Conceito POO / Lógica: Validação de estado do objeto e tratamento de exceções.

---

**Erro 7**: Chamada de `calcular_media` com lista de notas vazia

- Descrição: O teste no final do script chama `estudante.calcular_media()` sem ter adicionado nenhuma nota, resultando em `ZeroDivisionError` no código original.
- Solução: Implementar proteção dentro de `calcular_media` para retornar `0.0` quando `self.notas` estiver vazia. Assim, a chamada é segura e o programa não levanta exceção inesperada. A implementação atual em `Resposta_10.py` é:

```python
    def calcular_media(self):
        # Evita divisão por zero quando não há notas registradas
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)
```

- Conceito POO / Lógica: Validação de estado do objeto; tratamento de entradas inválidas / ausência de dados.

---

## Observações sobre outras escolhas de design

- O atributo `__cpf` foi mantido como privado (com double-underscore). Isso aplica name-mangling no Python e é adequado se a intenção for tornar o acesso direto mais difícil. Alternativamente, pode-se usar um único underscore (`_cpf`) ou implementar getters/setters para controlar acesso.
- Ao retornar `0.0` para `calcular_media` quando não há notas, optamos por um comportamento seguro e previsível. Outra alternativa seria lançar uma exceção explícita (`ValueError`) para forçar o chamador a validar a existência de notas antes de pedir a média. A escolha depende do comportamento esperado pela aplicação.

---

## Resultado do teste

Rodando o script `Resposta_10.py` após as correções, a saída é similar a:

```
Olá, sou João
Olá, sou o professor Dr. Silva do departamento Computação
Média do estudante: 0.0
```

Isso indica que o programa não produz exceções ao calcular a média quando não há notas (resultado `0.0`).

---

Arquivos entregues:

- `Resposta_10.py` (corrigido)
- `Resposta_10.md` (este relatório)
