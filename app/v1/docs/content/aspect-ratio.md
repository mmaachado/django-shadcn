---
title: Aspect Ratio
description: Displays content within a desired ratio.
description.pt-br: Mantém o conteúdo dentro da proporção que você escolher.
description.es: Mantiene el contenido dentro de la proporción que elijas.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="w-[450px]">
<c-aspect-ratio ratio="16/9" class="overflow-hidden rounded-lg bg-muted">
<div class="flex size-full items-center justify-center text-sm text-muted-foreground">16 / 9</div>
</c-aspect-ratio>
</div>
</c-docs.demo-section>

<c-docs.cheat-sheet name="aspect-ratio">
<c-aspect-ratio ratio="16/9">
  <img src="{{ photo.url }}" alt="{{ photo.title }}" class="size-full object-cover" />
</c-aspect-ratio>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add aspect_ratio
```

:::en
## Usage

The box takes the width it is given and the height that `ratio` works out
from it. Radix reserves the space with a padding hack; here it is the native
`aspect-ratio` property, so `ratio` takes anything the property accepts,
`16/9`, `4/3` or `1.85`. The default is `1/1`.

It is CSS only. The space is held before an image arrives, so the page does
not jump when it loads, with or without JavaScript. Give the image
`size-full object-cover` to fill the box.
:::pt-br
## Uso

A caixa pega a largura que recebe e a altura que o `ratio` calcula a partir
dela. O Radix reserva o espaço com um truque de padding; aqui é a propriedade
nativa `aspect-ratio`, então `ratio` aceita qualquer valor que ela aceita,
`16/9`, `4/3` ou `1.85`. O padrão é `1/1`.

É só CSS. O espaço fica reservado antes de a imagem chegar, então a página não
pula quando ela carrega, com ou sem JavaScript. Dê à imagem
`size-full object-cover` para preencher a caixa.
:::

<c-docs.example>
<div class="w-[300px]">
  <c-aspect-ratio ratio="16/9" class="overflow-hidden rounded-lg bg-muted">
    <div class="flex size-full items-center justify-center text-sm text-muted-foreground">16 / 9</div>
  </c-aspect-ratio>
</div>
</c-docs.example>

:::en
## Examples

### Square
:::pt-br
## Exemplos

### Quadrado
:::

<c-docs.example>
<div class="w-[200px]">
  <c-aspect-ratio class="overflow-hidden rounded-lg bg-muted">
    <div class="flex size-full items-center justify-center text-sm text-muted-foreground">1 / 1</div>
  </c-aspect-ratio>
</div>
</c-docs.example>

:::en
### Portrait
:::pt-br
### Retrato
:::

<c-docs.example>
<div class="w-[200px]">
  <c-aspect-ratio ratio="3/4" class="overflow-hidden rounded-lg bg-muted">
    <div class="flex size-full items-center justify-center text-sm text-muted-foreground">3 / 4</div>
  </c-aspect-ratio>
</div>
</c-docs.example>

:::en
## RTL

A ratio has no direction. The box looks the same under `dir="rtl"`.

## Accessibility

The box is a plain `<div>` and adds nothing for assistive technology. What is
inside carries the meaning: an image needs its `alt`.

## API reference
:::pt-br
## RTL

Uma proporção não tem direção. A caixa fica igual sob `dir="rtl"`.

## Acessibilidade

A caixa é uma `<div>` simples e não acrescenta nada para as tecnologias
assistivas. O que está dentro carrega o significado: uma imagem precisa do
`alt`.

## Referência da API
:::

<c-docs.api-reference name="aspect-ratio" />
