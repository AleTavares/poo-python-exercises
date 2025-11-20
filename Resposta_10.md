# Relatório – Correção dos 7 erros de POO

Durante a análise do código, encontrei 7 problemas relacionados a boas práticas e conceitos de POO. Abaixo explico cada um deles e como resolvi.


## Erro 1 – Nome da classe
A classe estava escrita como `pessoa`, tudo minúsculo.  
Segundo a convenção do Python, nomes de classes começam com letra maiúscula.

**Como corrigi:** mudei para `Pessoa`.

**Conceito:** convenção de nomenclatura e organização do código.


## Erro 2 – Atributo não estava sendo salvo
No construtor tinha `nome = nome`, que não atribui nada ao objeto.

**Como corrigi:** troquei para `self.nome = nome`.

**Conceito:** inicialização correta de atributos usando `self`.


## Erro 3 – Encapsulamento exagerado
O código usava `__cpf`, que cria o mecanismo de "name mangling" sem necessidade. Aqui não era preciso.

**Como corrigi:** deixei como `_cpf`, que já indica atributo protegido.

**Conceito:** encapsulamento adequado.


## Erro 4 – Método sem `self`
O método `apresentar()` estava sem o parâmetro `self`, então ele não funcionaria.

**Como corrigi:** adicionei `self` no método.

**Conceito:** todo método de instância precisa receber `self`.


## Erro 5 – Construtor da classe mãe ignorado
Na classe `Estudante`, o construtor não chamava `super()`, então os atributos de `Pessoa` não eram inicializados.

**Como corrigi:** chamei `super().__init__(nome, idade)`.

**Conceito:** herança + uso correto do super.


## Erro 6 – Possível divisão por zero
O método `calcular_media()` dividia o total das notas pela quantidade. Se não tivesse nenhuma nota, daria erro.

**Como corrigi:** coloquei uma verificação que retorna 0 se não houver notas.

**Conceito:** tratamento de erros e lógica de negócio.


## Erro 7 – Média chamada sem notas
No teste do código, a média era chamada sem o aluno ter nenhuma nota cadastrada.

**Como corrigi:** depois de resolver o erro 6, isso deixou de ser um problema, mas também adicionei notas antes de calcular.

**Conceito:** garantir que o método funcione em todos os cenários.


## Conclusão
Depois de corrigir tudo, o código funciona normalmente e segue melhor os princípios de POO.  
Os erros estavam principalmente em:
- inicialização com `self`
- uso de super()
- nomenclatura
- encapsulamento
- métodos sem parâmetro
- lógica de média