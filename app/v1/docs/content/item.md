---
title: Item
description: A row of content with media, text and actions. Use it for lists, settings and pickers.
description.pt-br: Uma linha com mídia, texto e ações. Serve para listas, ajustes e seletores.
description.es: Una fila con medios, texto y acciones. Sirve para listas, ajustes y selectores.
---

<c-docs.demo-section class="min-h-[350px]">
<c-item variant="outline" class="w-full">
<c-item.media variant="icon">
<c-icon name="search" />
</c-item.media>
<c-item.content>
<c-item.title>Search the docs</c-item.title>
<c-item.description>Find a component by name or description.</c-item.description>
</c-item.content>
<c-item.actions>
<c-button variant="outline" size="sm">Open</c-button>
</c-item.actions>
</c-item>
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add item
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-item variant="outline">
  <c-item.media variant="icon">
    <c-icon name="search" />
  </c-item.media>
  <c-item.content>
    <c-item.title>Title</c-item.title>
    <c-item.description>Description</c-item.description>
  </c-item.content>
  <c-item.actions>
    <c-button variant="outline" size="sm">Open</c-button>
  </c-item.actions>
</c-item>
```

:::en
## Media

`media` boxes the icon by default: `variant="icon"` draws a bordered square
around it, exactly as upstream. Leave the variant out for a bare icon.
:::pt-br
## Mídia

`media` põe o ícone numa caixa por padrão: `variant="icon"` desenha um quadrado
com borda em volta dele, exatamente como no upstream. Deixe a variante de fora
para um ícone sem moldura.
:::

<c-docs.example>
<div class="flex w-full flex-col gap-4">
  <c-item variant="outline">
    <c-item.media>
      <c-icon name="check" class="size-5" />
    </c-item.media>
    <c-item.content>
      <c-item.title>Bare icon</c-item.title>
      <c-item.description>No variant, no box.</c-item.description>
    </c-item.content>
  </c-item>
  <c-item variant="outline">
    <c-item.media variant="icon">
      <c-icon name="check" />
    </c-item.media>
    <c-item.content>
      <c-item.title>Boxed icon</c-item.title>
      <c-item.description>variant="icon", bordered and filled.</c-item.description>
    </c-item.content>
  </c-item>
</div>
</c-docs.example>

:::en
## Examples

### Variants
:::pt-br
## Exemplos

### Variantes
:::

<c-docs.example>
<div class="flex w-full flex-col gap-4">
  <c-item>
    <c-item.content>
      <c-item.title>Default</c-item.title>
      <c-item.description>No background, no border.</c-item.description>
    </c-item.content>
  </c-item>
  <c-item variant="outline">
    <c-item.content>
      <c-item.title>Outline</c-item.title>
      <c-item.description>Bordered on every side.</c-item.description>
    </c-item.content>
  </c-item>
  <c-item variant="muted">
    <c-item.content>
      <c-item.title>Muted</c-item.title>
      <c-item.description>Filled with a muted background.</c-item.description>
    </c-item.content>
  </c-item>
</div>
</c-docs.example>

:::en
### Sizes
:::pt-br
### Tamanhos
:::

<c-docs.example>
<div class="flex w-full flex-col gap-4">
  <c-item variant="outline">
    <c-item.content>
      <c-item.title>Default</c-item.title>
    </c-item.content>
  </c-item>
  <c-item variant="outline" size="sm">
    <c-item.content>
      <c-item.title>Small</c-item.title>
    </c-item.content>
  </c-item>
</div>
</c-docs.example>

:::en
### Group
:::pt-br
### Grupo
:::

<c-docs.example>
<c-item.group class="w-full rounded-md border">
  <c-item>
    <c-item.media variant="icon">
      <c-icon name="check" />
    </c-item.media>
    <c-item.content>
      <c-item.title>Notifications</c-item.title>
      <c-item.description>Get notified when someone replies.</c-item.description>
    </c-item.content>
    <c-item.actions>
      <c-button variant="ghost" size="sm">Edit</c-button>
    </c-item.actions>
  </c-item>
  <c-item.separator />
  <c-item>
    <c-item.media variant="icon">
      <c-icon name="search" />
    </c-item.media>
    <c-item.content>
      <c-item.title>Search history</c-item.title>
      <c-item.description>Keep the last 30 days of searches.</c-item.description>
    </c-item.content>
    <c-item.actions>
      <c-button variant="ghost" size="sm">Edit</c-button>
    </c-item.actions>
  </c-item>
</c-item.group>
</c-docs.example>

:::en
### With an image
:::pt-br
### Com uma imagem
:::

<c-docs.example>
<c-item variant="outline" class="w-full">
  <c-item.media variant="image">
    <img src="https://github.com/mmaachado.png" alt="" />
  </c-item.media>
  <c-item.content>
    <c-item.title>Marcelo Machado</c-item.title>
    <c-item.description>Maintainer of django-shadcn.</c-item.description>
  </c-item.content>
</c-item>
</c-docs.example>

:::en
### Header and footer
:::pt-br
### Cabeçalho e rodapé
:::

<c-docs.example>
<c-item variant="outline" class="w-full">
  <c-item.header>
    <span class="text-xs font-medium text-muted-foreground">PROJECT</span>
    <c-badge variant="secondary">Active</c-badge>
  </c-item.header>
  <c-item.content>
    <c-item.title>django-shadcn</c-item.title>
    <c-item.description>shadcn/ui components for Django templates.</c-item.description>
  </c-item.content>
  <c-item.footer>
    <span class="text-xs text-muted-foreground">Updated today</span>
    <c-button variant="ghost" size="sm">Open</c-button>
  </c-item.footer>
</c-item>
</c-docs.example>
