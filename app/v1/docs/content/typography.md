---
title: Typography
description: Styles for headings, paragraphs, lists and inline text.
description.pt-br: Estilos para títulos, parágrafos, listas e texto em linha.
description.es: Estilos para títulos, párrafos, listas y texto en línea.
---

<c-docs.demo-section class="min-h-[350px]">

<div class="text-start">
            <c-typography.h2 class="mt-0">The Joke Tax</c-typography.h2>
            <c-typography.p>
                The king's subjects were not amused. They grumbled and complained,
                but the king was firm.
            </c-typography.p>
        </div>
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add typography
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-typography.h1>Taxing Laughter</c-typography.h1>
<c-typography.p>The king thought long and hard.</c-typography.p>
```

:::en
shadcn/ui documents typography as utility classes rather than shipping a
component. There is no per-file equivalent of a `prose` wrapper in a Django
template, so each style is its own subcomponent here. The classes are the
ones from the original page, unchanged.

## Examples

### h1
:::pt-br
O shadcn/ui documenta a tipografia como classes utilitárias em vez de distribuir
um componente. Não há um equivalente por arquivo de um invólucro `prose` num
template Django, então aqui cada estilo é o próprio subcomponente. As classes
são as da página original, sem mudanças.

## Exemplos

### h1
:::

<c-docs.example>
<c-typography.h1>Taxing Laughter: The Joke Tax Chronicles</c-typography.h1>
</c-docs.example>

:::en
### h2
:::pt-br
### h2
:::

<c-docs.example>
<c-typography.h2 class="w-full">The People of the Kingdom</c-typography.h2>
</c-docs.example>

:::en
### h3
:::pt-br
### h3
:::

<c-docs.example>
<c-typography.h3>The Joke Tax</c-typography.h3>
</c-docs.example>

:::en
### h4
:::pt-br
### h4
:::

<c-docs.example>
<c-typography.h4>People stopped telling jokes</c-typography.h4>
</c-docs.example>

:::en
### Paragraph
:::pt-br
### Parágrafo
:::

<c-docs.example>
<c-typography.p>
  The king, seeing how much happier his subjects were, realized the
  error of his ways and repealed the joke tax.
</c-typography.p>
</c-docs.example>

:::en
### Blockquote
:::pt-br
### Citação
:::

<c-docs.example>
<c-typography.blockquote>
  "After all," he said, "everyone enjoys a good joke, so it's only
  fair that they should pay for the privilege."
</c-typography.blockquote>
</c-docs.example>

:::en
### List
:::pt-br
### Lista
:::

<c-docs.example>
<c-typography.list>
  <li>1st level of puns: 5 gold coins</li>
  <li>2nd level of jokes: 10 gold coins</li>
  <li>3rd level of one-liners: 20 gold coins</li>
</c-typography.list>
</c-docs.example>

:::en
### Inline code
:::pt-br
### Código em linha
:::

<c-docs.example>
<c-typography.code>django-cotton</c-typography.code>
</c-docs.example>

:::en
### Lead
:::pt-br
### Lead
:::

<c-docs.example>
<c-typography.lead>
  A modal dialog that interrupts the user with important content and
  expects a response.
</c-typography.lead>
</c-docs.example>

:::en
### Large
:::pt-br
### Large
:::

<c-docs.example>
<c-typography.large>Are you absolutely sure?</c-typography.large>
</c-docs.example>

:::en
### Small
:::pt-br
### Small
:::

<c-docs.example>
<c-typography.small>Email address</c-typography.small>
</c-docs.example>

:::en
### Muted
:::pt-br
### Muted
:::

<c-docs.example>
<c-typography.muted>Enter your email address.</c-typography.muted>
</c-docs.example>
