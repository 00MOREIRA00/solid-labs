# Princípio da Substituição de Liskov (LSP)

O Princípio da Substituição de Liskov (LSP) é o terceiro princípio dos cinco princípios SOLID da programação orientada a objetos. Ele foi introduzido por Barbara Liskov em 1987.

## Definição

"Se S é um subtipo de T, então os objetos do tipo T podem ser substituídos por objetos do tipo S (ou seja, objetos do tipo S podem substituir objetos do tipo T) sem alterar as propriedades desejáveis do programa."

## Objetivo

O objetivo do LSP é garantir que uma classe derivada possa ser substituída por sua classe base sem que o comportamento do programa seja alterado. Isso significa que as subclasses devem ser capazes de substituir suas superclasses sem que o usuário da classe precise saber a diferença.

## Vantagens

- **Consistência**: Garante que as subclasses mantenham o comportamento esperado da classe base.
- **Reusabilidade**: Facilita a reutilização de código, pois as subclasses podem ser usadas no lugar das superclasses.
- **Manutenção**: Reduz o risco de introduzir erros ao modificar ou estender o código existente.

## Exemplo

Considere as seguintes classes:

```python
class Ave:
    def emitir_som(self):
        return "Som genérico de ave"

class AveQueVoa(Ave):
    def voar(self):
        return "Estou voando!"

class Pato(AveQueVoa):
    pass

class Avestruz(Ave):
    pass
```

Neste exemplo, `Pardal` pode substituir `Passaro` sem problemas, mas `Avestruz` não pode, pois lança uma exceção quando o método `voar` é chamado. Isso viola o LSP, pois `Avestruz` não pode ser substituído por `Passaro` sem alterar o comportamento do programa.

## Outro Exemplo

### Forma Errada

```python
class ContaBancaria:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def sacar(self, valor: float):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente!")
        self.saldo -= valor
        return f"Saque de R${valor:.2f} realizado! Saldo atual: R${self.saldo:.2f}"

class ContaCorrente(ContaBancaria):
    pass  # Herda tudo normalmente

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor: float):
        raise NotImplementedError("Não é permitido saque direto na Conta Poupança!")
```

Neste exemplo, `ContaPoupanca` viola o LSP, pois lança uma exceção quando o método `sacar` é chamado, diferentemente do comportamento esperado da classe base `ContaBancaria`.

### Forma Correta

```python
class Conta:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def get_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"

class ContaComSaque(Conta):
    def sacar(self, valor: float):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente!")
        self.saldo -= valor
        return f"Saque de R${valor:.2f} realizado! Saldo atual: R${self.saldo:.2f}"

class ContaCorrente(ContaComSaque):
    pass  # Pode sacar normalmente

class ContaPoupanca(Conta):
    pass  # Não tem método sacar
```

Neste exemplo, `ContaPoupanca` e `ContaCorrente` seguem o LSP, pois `ContaPoupanca` não implementa o método `sacar`, enquanto `ContaCorrente` herda de `ContaComSaque`, que possui o método `sacar`.

## Como aplicar o LSP

Para aplicar o LSP corretamente, siga estas diretrizes:

1. **Métodos e propriedades da classe base devem ser implementados na classe derivada**: As subclasses devem implementar todos os métodos e propriedades da classe base de maneira consistente.
2. **Não lançar exceções inesperadas**: As subclasses não devem lançar exceções que não são esperadas pela classe base.
3. **Preservar a semântica da classe base**: As subclasses devem manter o comportamento esperado da classe base.

## Conclusão

O Princípio da Substituição de Liskov é essencial para criar sistemas de software consistentes e reutilizáveis. Ao garantir que as subclasses possam substituir suas superclasses sem alterar o comportamento do programa, podemos adicionar novas funcionalidades com segurança e minimizar o risco de introduzir novos bugs.

