---
title: Skeleton
description: Use to show a placeholder while content is loading.
description.pt-br: Um espaço reservado enquanto o conteúdo carrega.
description.es: Un espacio reservado mientras el contenido carga.
---

<c-docs.demo-section class="min-h-[350px]">

<div class="flex items-center gap-4">
            <c-skeleton class="size-12 rounded-full" />
            <div class="space-y-2">
                <c-skeleton class="h-4 w-[250px]" />
                <c-skeleton class="h-4 w-[200px]" />
            </div>
        </div>
</c-docs.demo-section>

<c-docs.cheat-sheet name="skeleton">
<c-skeleton class="h-4 w-[250px]" />
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add skeleton
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example background="bg-background">
<c-skeleton class="h-4 w-[250px]" />
</c-docs.example>

:::en
The component ships no dimensions of its own. Give it the size and shape of
whatever it stands in for.

It fills with `bg-accent`, which is the same value as `bg-muted` in the
default palette. The demos below sit on the page background so the shapes
stay visible.

## Examples

### Card
:::pt-br
O componente não traz dimensões próprias. Dê a ele o tamanho e a forma do que
quer que ele esteja substituindo.

Ele é preenchido com `bg-accent`, que tem o mesmo valor de `bg-muted` na paleta
padrão. As demos abaixo ficam sobre o fundo da página para que as formas
continuem visíveis.

## Exemplos

### Card
:::

<c-docs.example background="bg-background">
<div class="flex flex-col gap-3">
  <c-skeleton class="h-[125px] w-[250px] rounded-xl" />
  <div class="space-y-2">
    <c-skeleton class="h-4 w-[250px]" />
    <c-skeleton class="h-4 w-[200px]" />
  </div>
</div>
</c-docs.example>

:::en
### Avatar and text
:::pt-br
### Avatar e texto
:::

<c-docs.example background="bg-background">
<div class="flex items-center gap-4">
  <c-skeleton class="size-12 rounded-full" />
  <div class="space-y-2">
    <c-skeleton class="h-4 w-[250px]" />
    <c-skeleton class="h-4 w-[200px]" />
  </div>
</div>
</c-docs.example>

:::en
### Standing in for a card
:::pt-br
### No lugar de um card
:::

<c-docs.example background="bg-background">
<c-card class="w-[320px]">
  <c-card.header>
    <c-skeleton class="h-5 w-[160px]" />
    <c-skeleton class="h-4 w-[220px]" />
  </c-card.header>
  <c-card.content class="space-y-2">
    <c-skeleton class="h-4 w-full" />
    <c-skeleton class="h-4 w-[80%]" />
  </c-card.content>
  <c-card.footer>
    <c-skeleton class="h-9 w-[100px] rounded-md" />
  </c-card.footer>
</c-card>
</c-docs.example>

:::en
### Table

A few rows of bars stand in for a table that is still loading.
:::pt-br
### Tabela

Algumas linhas de barras ficam no lugar de uma tabela que ainda está carregando.
:::

<c-docs.example>
<div class="w-full max-w-md space-y-3" aria-busy="true">
  {% for row in "123" %}
    <div class="flex gap-4">
      <c-skeleton class="h-4 w-1/4" />
      <c-skeleton class="h-4 w-1/2" />
      <c-skeleton class="h-4 w-1/4" />
    </div>
  {% endfor %}
</div>
</c-docs.example>

:::en
## RTL

A skeleton is shapes, so under `dir="rtl"` it mirrors with whatever layout
you give it.

## Accessibility

The shapes are empty and silent. Mark the region that is loading
`aria-busy="true"` while the skeleton stands in, and swap in the content when
it arrives.

## API reference
:::pt-br
## RTL

Um skeleton são formas, então sob `dir="rtl"` ele espelha com o layout que
você der a ele.

## Acessibilidade

As formas são vazias e silenciosas. Marque a região que está carregando com
`aria-busy="true"` enquanto o skeleton ocupa o lugar, e troque pelo conteúdo
quando ele chegar.

## Referência da API
:::

<c-docs.api-reference name="skeleton" />
