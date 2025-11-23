Erro 1 = Nome da classe pessoa minúscula
Problema: classes em Py devem seguir a conversão CamelCase
Solução: Alterado para clss Pessoa
Conceito: Convenção e boas praticas de POO

Erro 2 = Pendente Self. (atributo nome não sendo iniciado corretamente)
Problema: Dentro do `__init__`, estava escrito `nome = nome`, não atribuindo valor ao objeto. 
Solução: Inserido self.nome = nome
Conceito: Encapsulado e inicialização correta de atributos

Erro 3 = Atributo privado contribuindo para falha futura
Problema: self._cpf = None estava correto, mas poderia causar confusão sem getter/setter
Solução:Mantido (não é erro de fato). Apenas confirmamos sua funcionalidade.
Conceito: Encapsulamento

Erro 4 = Metodo apresentar() sem parametro self
Problema: Definido como def apresentar ()
Solução: Corrigido para `def apresentar(self)
Conceito: Metodo de instância

Erro 5 = Classe Estudante não chamando o construtor da classe mãe
Problema: Estava redefinindo `self.nome = nome` diretamente
Solução: Usado `super().__init__(nome, idade)
Conceito: Herança e uso correto de `super()

Erro 6 = Divisão por zero na média
Problema: sum(self.notas) / len(self.notas)` causa erro se a lista estiver vazia.
Solução:Adicionada verificação:

if len(self.notas) == 0:
    return 0

Conceito: 

Erro 7 = Média sendo calculada sem adicionar notas antes
Problema: No teste, chamava calcular_media() sem adicionar nenhuma nota.
Solução: Notas foram adicionadas antes da chamada e também implementada proteção no método.
Conceito: Lógica do programa e integridade dos dados.

 


