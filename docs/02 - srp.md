
# Single Responsibility Principle (SRP)

O Princípio da Responsabilidade Única (SRP) é o primeiro dos cinco princípios SOLID de design de software orientado a objetos. Ele afirma que uma classe deve ter apenas uma razão para mudar, ou seja, deve ter uma única responsabilidade ou propósito.

## Definição

"Uma classe deve ter um, e somente um, motivo para mudar."

## Objetivo

O objetivo do SRP é garantir que uma classe seja coesa e que suas responsabilidades sejam claramente definidas. Isso facilita a manutenção e evolução do código, pois mudanças em uma responsabilidade não afetam outras responsabilidades.

## Vantagens

- **Manutenção facilitada**: Com responsabilidades bem definidas, é mais fácil localizar e corrigir problemas no código.
- **Reusabilidade**: Classes com uma única responsabilidade são mais fáceis de reutilizar em diferentes contextos.
- **Testabilidade**: Classes coesas são mais fáceis de testar, pois têm menos dependências e cenários de teste mais simples.
- **Legibilidade**: Código organizado de acordo com o SRP é mais fácil de entender e seguir, facilitando a colaboração entre desenvolvedores.

## Exemplo

Considere uma classe `Relatorio` que tem duas responsabilidades: gerar o conteúdo do relatório e enviá-lo por email.

```python
class Relatorio:
    def gerar_conteudo(self):
        # Lógica para gerar o conteúdo do relatório
        pass

    def enviar_por_email(self, destinatario):
        # Lógica para enviar o relatório por email
        pass
```

Para aplicar o SRP, podemos dividir essa classe em duas classes distintas, cada uma com uma única responsabilidade:

```python
class GeradorDeRelatorio:
    def gerar_conteudo(self):
        # Lógica para gerar o conteúdo do relatório
        pass

class EnviadorDeEmail:
    def enviar_por_email(self, destinatario, conteudo):
        # Lógica para enviar o relatório por email
        pass
```

Agora, cada classe tem uma única responsabilidade, tornando o código mais coeso e fácil de manter.

## Conclusão

O Princípio da Responsabilidade Única é fundamental para criar software de alta qualidade. Ao garantir que cada classe tenha uma única responsabilidade, podemos criar sistemas mais compreensíveis, flexíveis e de fácil manutenção.
