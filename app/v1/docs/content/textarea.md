---
title: Textarea
description: Displays a form textarea or a component that looks like a textarea.
description.pt-br: Exibe uma área de texto, ou um componente com cara de área de texto.
description.es: Muestra un área de texto, o un componente con aspecto de área de texto.
---

<c-docs.demo-section class="min-h-[350px]">
<c-textarea placeholder="Type your message here." />
</c-docs.demo-section>

<c-docs.cheat-sheet name="textarea">
<c-textarea placeholder="Type your message here." />
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add textarea
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-textarea placeholder="Type your message here." />
</c-docs.example>

:::en
## Examples

### Disabled
:::pt-br
## Exemplos

### Desabilitado
:::

<c-docs.example>
<c-textarea placeholder="Type your message here." disabled />
</c-docs.example>

:::en
### With Label
:::pt-br
### Com rótulo
:::

<c-docs.example>
<div class="grid w-full gap-1.5">
  <c-label for="message">Your Message</c-label>
  <c-textarea id="message" placeholder="Type your message here." />
</div>
</c-docs.example>

:::en
### With Button
:::pt-br
### Com botão
:::

<c-docs.example>
<div class="grid w-full gap-2">
  <c-textarea placeholder="Type your message here." />
  <c-button type="submit">Send message</c-button>
</div>
</c-docs.example>

:::en
### Invalid

There is no invalid style built in: mark it `aria-invalid="true"` and add a class.
:::pt-br
### Inválido

Não há estilo de inválido embutido: marque com `aria-invalid="true"` e acrescente uma classe.
:::

<c-docs.example>
<c-textarea aria-invalid="true" aria-label="Message" class="max-w-sm aria-invalid:border-destructive">Too short</c-textarea>
</c-docs.example>

:::en
## RTL

The text starts at the start of the field, so under `dir="rtl"` it runs from
the right.

## Accessibility

It is a native `<textarea>`: name it with a `<label>` tied by `for`, or an
`aria-label`. A placeholder is not a label.

## API reference
:::pt-br
## RTL

O texto começa no início do campo, então sob `dir="rtl"` ele corre a partir
da direita.

## Acessibilidade

É um `<textarea>` nativo: dê um nome a ele com um `<label>` ligado por `for`,
ou um `aria-label`. Um placeholder não é um rótulo.

## Referência da API
:::

<c-docs.api-reference name="textarea" />
