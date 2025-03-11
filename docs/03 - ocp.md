
# Open/Closed Principle (OCP)

O Princípio do Aberto/Fechado (OCP) é o segundo dos cinco princípios SOLID de design de software orientado a objetos. Ele afirma que entidades de software (classes, módulos, funções, etc.) devem estar abertas para extensão, mas fechadas para modificação.

## Definição

"Entidades de software devem estar abertas para extensão, mas fechadas para modificação."

## Objetivo

O objetivo do OCP é permitir que o comportamento de uma entidade de software possa ser estendido sem alterar seu código-fonte original. Isso promove a reutilização de código e minimiza o risco de introduzir novos bugs em um sistema existente.

## Vantagens

- **Extensibilidade**: Permite adicionar novas funcionalidades sem alterar o código existente.
- **Manutenção facilitada**: Reduz o risco de introduzir erros ao modificar código existente.
- **Reusabilidade**: Facilita a reutilização de componentes de software em diferentes contextos.
- **Flexibilidade**: Torna o sistema mais adaptável a mudanças e novos requisitos.

## Exemplo

Considere uma classe `CalculadoraDeDesconto` que calcula descontos para diferentes tipos de clientes.

```python
class CalculadoraDeDesconto:
    def calcular(self, tipo_cliente, valor):
        if tipo_cliente == "regular":
            return valor * 0.1
        elif tipo_cliente == "vip":
            return valor * 0.2
        else:
            return 0
```

Para aplicar o OCP, podemos usar o polimorfismo para permitir a extensão do comportamento sem modificar a classe original:

```python
class CalculadoraDeDesconto:
    def calcular(self, cliente, valor):
        return cliente.calcular_desconto(valor)

class ClienteRegular:
    def calcular_desconto(self, valor):
        return valor * 0.1

class ClienteVIP:
    def calcular_desconto(self, valor):
        return valor * 0.2
```

Agora, podemos adicionar novos tipos de clientes sem modificar a classe `CalculadoraDeDesconto`.

## Conclusão

O Princípio do Aberto/Fechado é essencial para criar sistemas de software flexíveis e extensíveis. Ao garantir que entidades de software estejam abertas para extensão, mas fechadas para modificação, podemos adicionar novas funcionalidades com segurança e minimizar o risco de introduzir novos bugs.
