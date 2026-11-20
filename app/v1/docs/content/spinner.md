---
title: Spinner
description: An indicator that something is in progress.
description.pt-br: Um indicador de que algo está em andamento.
description.es: Un indicador de que algo está en marcha.
---

<c-docs.demo-section class="min-h-[350px]">
<c-spinner />
</c-docs.demo-section>

<c-docs.cheat-sheet name="spinner">
<c-spinner />
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add spinner
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-spinner />
</c-docs.example>

:::en
It is the lucide `loader-circle` icon with `animate-spin`, already carrying
`role="status"` and an accessible label.

## Examples

### Sizes
:::pt-br
É o ícone `loader-circle` do lucide com `animate-spin`, já levando
`role="status"` e um rótulo acessível.

## Exemplos

### Tamanhos
:::

<c-docs.example>
<div class="flex items-center gap-4">
  <c-spinner class="size-3" />
  <c-spinner />
  <c-spinner class="size-6" />
  <c-spinner class="size-8" />
</div>
</c-docs.example>

:::en
### Inside a button
:::pt-br
### Dentro de um botão
:::

<c-docs.example>
<div class="flex items-center gap-3">
  <c-button disabled>
    <c-spinner />
    Saving
  </c-button>
  <c-button variant="outline" disabled>
    <c-spinner />
    Please wait
  </c-button>
</div>
</c-docs.example>

:::en
### Color
:::pt-br
### Cor
:::

<c-docs.example>
<div class="flex items-center gap-4">
  <c-spinner class="size-6 text-muted-foreground" />
  <c-spinner class="size-6 text-primary" />
  <c-spinner class="size-6 text-destructive" />
</div>
</c-docs.example>

:::en
## API reference
:::pt-br
## Referência da API
:::

<c-docs.api-reference name="spinner" />
