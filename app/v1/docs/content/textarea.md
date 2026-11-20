---
title: Textarea
description: Displays a form textarea or a component that looks like a textarea.
description.pt-br: Exibe uma área de texto, ou um componente com cara de área de texto.
description.es: Muestra un área de texto, o un componente con aspecto de área de texto.
---

<c-docs.demo-section class="min-h-[350px]">
<c-textarea placeholder="Type your message here." />
</c-docs.demo-section>

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

<c-docs.demo-section>
<c-textarea placeholder="Type your message here." />
</c-docs.demo-section>

```html
<c-textarea placeholder="Type your message here." />
```

:::en
## Examples

### Disabled
:::pt-br
## Exemplos

### Desabilitado
:::

<c-docs.demo-section>
<c-textarea placeholder="Type your message here." disabled />
</c-docs.demo-section>

```html
<c-textarea placeholder="Type your message here." disabled />
```

:::en
### With Label
:::pt-br
### Com rótulo
:::

<c-docs.demo-section>

<div class="grid w-full gap-1.5">
    <c-label for="message">Your Message</c-label>
    <c-textarea id="message" placeholder="Type your message here." />
</div>
</c-docs.demo-section>

```html
<div class="grid w-full gap-1.5">
  <c-label for="message">Your Message</c-label>
  <c-textarea id="message" placeholder="Type your message here." />
</div>
```

:::en
### With Button
:::pt-br
### Com botão
:::

<c-docs.demo-section>

<div class="grid w-full gap-2">
    <c-textarea placeholder="Type your message here." />
    <c-button type="submit">Send message</c-button>
</div>
</c-docs.demo-section>

```html
<div class="grid w-full gap-2">
  <c-textarea placeholder="Type your message here." />
  <c-button type="submit">Send message</c-button>
</div>
```
