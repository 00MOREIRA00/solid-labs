# Princípio da Segregação de Interface (ISP)

O Princípio da Segregação de Interface (ISP) é o quarto dos cinco princípios SOLID de design de software orientado a objetos. Ele afirma que os clientes não devem ser forçados a depender de interfaces que não utilizam.

## Definição

"Os clientes não devem ser forçados a depender de interfaces que não utilizam."

## Objetivo

O objetivo do ISP é evitar a criação de interfaces grandes e monolíticas, promovendo a criação de interfaces menores e mais específicas. Isso facilita a implementação e manutenção do código, além de promover a reutilização de componentes.

## Vantagens

- **Modularidade**: Interfaces menores e específicas tornam o sistema mais modular.
- **Facilidade de manutenção**: Reduz o impacto de mudanças, pois as interfaces são menores e mais focadas.
- **Reusabilidade**: Facilita a reutilização de componentes em diferentes contextos.
- **Flexibilidade**: Permite que diferentes clientes implementem apenas as funcionalidades que realmente necessitam.

## Exemplo

Considere uma interface `Trabalhador` que define várias operações:

```python
class Trabalhador:
    def trabalhar(self):
        pass

    def comer(self):
        pass

    def dormir(self):
        pass
```

Para aplicar o ISP, podemos dividir essa interface em interfaces menores e mais específicas:

```python
class Trabalhador:
    def trabalhar(self):
        pass

class Comedor:
    def comer(self):
        pass

class Dorminhoco:
    def dormir(self):
        pass
```

Agora, podemos criar classes que implementam apenas as interfaces necessárias:

```python
class Programador(Trabalhador, Comedor):
    def trabalhar(self):
        return "Programando..."

    def comer(self):
        return "Comendo..."

class Vigia(Trabalhador, Dorminhoco):
    def trabalhar(self):
        return "Vigiando..."

    def dormir(self):
        return "Dormindo..."
```

## Conclusão

O Princípio da Segregação de Interface é essencial para criar sistemas de software modulares e flexíveis. Ao garantir que os clientes não sejam forçados a depender de interfaces que não utilizam, podemos adicionar novas funcionalidades com segurança e minimizar o risco de introduzir novos bugs.

