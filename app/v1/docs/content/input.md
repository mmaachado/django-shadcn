---
title: Input
description: Displays a form input field or a component that looks like an input field.
description.pt-br: Exibe um campo de formulário, ou um componente com cara de campo.
description.es: Muestra un campo de formulario, o un componente con aspecto de campo.
---

<c-docs.demo-section class="min-h-[350px]">
<c-input type="email" placeholder="Email" />
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add input
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-input type="email" placeholder="Email" />
</c-docs.example>

:::en
## Examples

### Default
:::pt-br
## Exemplos

### Padrão
:::

<c-docs.example>
<c-input type="email" placeholder="Email" />
</c-docs.example>

:::en
### File
:::pt-br
### Arquivo
:::

<c-docs.example>
<c-input type="file" id="picture" />
</c-docs.example>

:::en
### Disabled
:::pt-br
### Desabilitado
:::

<c-docs.example>
<c-input type="email" placeholder="Email" disabled />
</c-docs.example>

:::en
### With Label
:::pt-br
### Com rótulo
:::

<c-docs.example>
<div class="grid w-full max-w-sm items-center gap-1.5">
  <c-label for="email">Email</c-label>
  <c-input type="email" placeholder="you@example.com" />
</div>
</c-docs.example>

:::en
### With Button
:::pt-br
### Com botão
:::

<c-docs.example>
<div class="flex w-full max-w-sm items-center space-x-2">
  <c-input type="email" placeholder="you@example.com" />
  <c-button type="submit">Subscribe</c-button>
</div>
</c-docs.example>

:::en
## API reference
:::pt-br
## Referência da API
:::

<c-docs.api-reference name="input" />
