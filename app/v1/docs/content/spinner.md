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
### Badge
:::pt-br
### Badge
:::

<c-docs.example>
<c-badge variant="secondary" class="gap-1">
  <c-spinner class="size-3" />
  Syncing
</c-badge>
</c-docs.example>

:::en
### Input group
:::pt-br
### Input group
:::

<c-docs.example>
<c-input-group class="max-w-xs">
  <c-input-group.input value="mmaachado" aria-label="Username" />
  <c-input-group.addon align="inline-end"><c-spinner /></c-input-group.addon>
</c-input-group>
</c-docs.example>

:::en
## RTL

A spinner turns the same way in every language.

## Accessibility

It carries `role="status"` and `aria-label="Loading"`, so a screen reader
announces it. Pass your own `aria-label` to say what is loading, or in your
language.

## API reference
:::pt-br
## RTL

Um spinner gira para o mesmo lado em qualquer idioma.

## Acessibilidade

Ele leva `role="status"` e `aria-label="Loading"`, então um leitor de tela o
anuncia. Passe o seu `aria-label` para dizer o que está carregando, ou no seu
idioma.

## Referência da API
:::

<c-docs.api-reference name="spinner" />
