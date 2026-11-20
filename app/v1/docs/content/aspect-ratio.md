---
title: Aspect Ratio
description: Displays content within a desired ratio.
description.pt-br: Mantém o conteúdo dentro da proporção que você escolher.
description.es: Mantiene el contenido dentro de la proporción que elijas.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="w-[450px]">
            <c-aspect-ratio ratio="16/9" class="overflow-hidden rounded-lg bg-muted">
                <div class="flex size-full items-center justify-center text-sm text-muted-foreground">
                    16 / 9
                </div>
            </c-aspect-ratio>
        </div>
</c-docs.demo-section>

<c-docs.cheat-sheet name="aspect-ratio">
<div class="w-[300px]">
  <c-aspect-ratio ratio="16/9" class="overflow-hidden rounded-lg bg-muted">
    <div class="flex size-full items-center justify-center text-sm text-muted-foreground">
      16 / 9
    </div>
  </c-aspect-ratio>
</div>
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
:::pt-br
## Uso
:::

<c-docs.example>
<div class="w-[300px]">
  <c-aspect-ratio ratio="16/9" class="overflow-hidden rounded-lg bg-muted">
    <div class="flex size-full items-center justify-center text-sm text-muted-foreground">
      16 / 9
    </div>
  </c-aspect-ratio>
</div>
</c-docs.example>

:::en
Radix reserves the space with a padding hack. Here it is the native `aspect-
ratio` CSS property, so `ratio` takes anything the property accepts: `16/9`,
`4/3`, `1.85`. The default is `1/1`.

## Examples

### Square
:::pt-br
O Radix reserva o espaço com um truque de padding. Aqui é a propriedade CSS
nativa `aspect-ratio`, então `ratio` aceita qualquer valor que a propriedade
aceita: `16/9`, `4/3`, `1.85`. O padrão é `1/1`.

## Exemplos

### Quadrado
:::

<c-docs.example>
<div class="w-[200px]">
  <c-aspect-ratio class="overflow-hidden rounded-lg bg-muted">
    <div class="flex size-full items-center justify-center text-sm text-muted-foreground">
      1 / 1
    </div>
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
    <div class="flex size-full items-center justify-center text-sm text-muted-foreground">
      3 / 4
    </div>
  </c-aspect-ratio>
</div>
</c-docs.example>

:::en
## API reference
:::pt-br
## Referência da API
:::

<c-docs.api-reference name="aspect-ratio" />
