---
title: Hover Card
description: A preview card that opens when a link is hovered.
description.pt-br: Um cartão de prévia que abre ao passar o mouse num link.
description.es: Una tarjeta de vista previa que abre al pasar el ratón por un enlace.
---

<c-docs.demo-section class="min-h-[350px]">
<c-hover-card>
<c-hover-card.trigger>
<a href="#" class="text-sm font-medium underline underline-offset-4">@mmaachado</a>
</c-hover-card.trigger>
<c-hover-card.content>
<div class="flex gap-4 text-start">
<c-avatar>
<c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
<c-avatar.fallback>MM</c-avatar.fallback>
</c-avatar>
<div class="space-y-1">
<h4 class="text-sm font-semibold">@mmaachado</h4>
<p class="text-sm text-muted-foreground">Maintains this port of shadcn/ui for Django.</p>
</div>
</div>
</c-hover-card.content>
</c-hover-card>
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add hover_card
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-hover-card>
  <c-hover-card.trigger>
    <a href="#" class="text-sm font-medium underline underline-offset-4">Hover this link</a>
  </c-hover-card.trigger>
  <c-hover-card.content>
    <p class="text-sm text-muted-foreground text-start">Enough room for a sentence or two of context.</p>
  </c-hover-card.content>
</c-hover-card>
</c-docs.example>

:::en
The card waits before opening and before closing, so crossing the gap between
the link and the card does not dismiss it. Both delays are attributes:
`open_delay` and `close_delay`, in milliseconds.

## Examples

### Alignment
:::pt-br
O card espera antes de abrir e antes de fechar, então atravessar o espaço entre
o link e o card não o fecha. Os dois atrasos são atributos: `open_delay` e
`close_delay`, em milissegundos.

## Exemplos

### Alinhamento
:::

<c-docs.example>
<div class="flex items-center gap-10">
  <c-hover-card>
    <c-hover-card.trigger><a href="#" class="text-sm underline underline-offset-4">Start</a></c-hover-card.trigger>
    <c-hover-card.content align="start"><p class="text-sm text-muted-foreground">Aligned to the start.</p></c-hover-card.content>
  </c-hover-card>
  <c-hover-card>
    <c-hover-card.trigger><a href="#" class="text-sm underline underline-offset-4">End</a></c-hover-card.trigger>
    <c-hover-card.content align="end"><p class="text-sm text-muted-foreground">Aligned to the end.</p></c-hover-card.content>
  </c-hover-card>
</div>
</c-docs.example>

:::en
### Slower
:::pt-br
### Mais devagar
:::

<c-docs.example>
<c-hover-card open_delay="700" close_delay="300">
  <c-hover-card.trigger><a href="#" class="text-sm underline underline-offset-4">Takes its time</a></c-hover-card.trigger>
  <c-hover-card.content><p class="text-sm text-muted-foreground">Opens after 700ms.</p></c-hover-card.content>
</c-hover-card>
</c-docs.example>

:::en
## Notes

As with the tooltip, `side` and `align` are choices rather than measurements —
there is no portal and no collision detection. On a touch screen there is no
hover, so anything behind a hover card needs to be reachable another way.
:::pt-br
## Observações

Como no tooltip, `side` e `align` são escolhas e não medições — não há portal
nem detecção de colisão. Numa tela de toque não existe hover, então tudo o que
fica atrás de um hover card precisa ser alcançável de outro jeito.
:::

:::en
## API reference
:::pt-br
## Referência da API
:::

<c-docs.api-reference name="hover-card" />
