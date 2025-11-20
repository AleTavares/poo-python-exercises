#  Exercício 10 — Jogo dos 7 Erros de POO em Python

##  Relatório de Correções

### **Erro 1 — Nome da classe**
- **Erro:** `class pessoa:` (nome iniciado com letra minúscula)
- **Solução:** Alterado para `class Pessoa:`
- **Conceito POO:** Convenção de nomenclatura (as classes devem iniciar com letra maiúscula — *PascalCase*).

---

### **Erro 2 — Atributo não associado ao objeto**
- **Erro:** `nome = nome` (não usava `self`)
- **Solução:** Corrigido para `self.nome = nome`
- **Conceito POO:** Encapsulamento — os atributos devem pertencer à instância (`self`).

---

### **Erro 3 — Encapsulamento incorreto**
- **Erro:** `self.__cpf = None` (uso de *duplo underscore* sem necessidade)
- **Solução:** Corrigido para `self._cpf = None` (protegido, não privado)
- **Conceito POO:** Encapsulamento — uso correto de *protected attributes* (`_atributo`).

---

### **Erro 4 — Método sem parâmetro self**
- **Erro:** `def apresentar():`
- **Solução:** Corrigido para `def apresentar(self):`
- **Conceito POO:** Definição de métodos de instância — todo método precisa de `self` como primeiro parâmetro.

---

### **Erro 5 — Herança sem uso de super()**
- **Erro:** `self.nome = nome` e `self.idade = idade` dentro de `Estudante.__init__`
- **Solução:** Corrigido para `super().__init__(nome, idade)`
- **Conceito POO:** Herança — uso correto de `super()` para inicializar a classe pai.

---

### **Erro 6 — Divisão por zero**
- **Erro:** `return sum(self.notas) / len(self.notas)` (sem verificar se há notas)
- **Solução:** Adicionado teste:
  ```python
  if len(self.notas) == 0:
      return 0.0
