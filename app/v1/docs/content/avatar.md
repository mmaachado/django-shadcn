---
title: Avatar
description: An image element with a fallback for representing the user.
description.pt-br: Uma imagem com fallback para representar o usuário.
description.es: Una imagen con alternativa para representar al usuario.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="flex items-center gap-4">
<c-avatar>
<c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
<c-avatar.fallback>MM</c-avatar.fallback>
</c-avatar>
<c-avatar>
<c-avatar.fallback>CN</c-avatar.fallback>
</c-avatar>
</div>
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add avatar
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-avatar>
  <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
  <c-avatar.fallback>MM</c-avatar.fallback>
</c-avatar>
</c-docs.example>

:::en
Radix hides the fallback once the image loads. Here the image is stacked on top
of the fallback instead, and removes itself on `error` so the initials show
through. Both are always in the markup.

That last part is one Alpine attribute on the image, with its own `x-data`.
Without Alpine the avatar still works, but a broken source leaves the browser's
broken-image glyph over the fallback.

## Examples

### Sizes
:::pt-br
O Radix esconde o fallback quando a imagem carrega. Aqui a imagem fica empilhada
sobre o fallback, e se remove no `error` para que as iniciais apareçam por
baixo. Os dois estão sempre no markup.

Essa última parte é um atributo do Alpine na imagem, com o próprio `x-data`.
Sem o Alpine o avatar continua funcionando, mas uma origem quebrada deixa o
ícone de imagem quebrada do navegador por cima do fallback.

## Exemplos

### Tamanhos
:::

<c-docs.example>
<div class="flex items-center gap-4">
  <c-avatar size="sm">
    <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
    <c-avatar.fallback>MM</c-avatar.fallback>
  </c-avatar>
  <c-avatar>
    <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
    <c-avatar.fallback>MM</c-avatar.fallback>
  </c-avatar>
  <c-avatar size="lg">
    <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
    <c-avatar.fallback>MM</c-avatar.fallback>
  </c-avatar>
</div>
</c-docs.example>

:::en
### Fallback
:::pt-br
### Fallback
:::

<c-docs.example>
<c-avatar>
  <c-avatar.image src="/does-not-exist.png" alt="" />
  <c-avatar.fallback>CN</c-avatar.fallback>
</c-avatar>
</c-docs.example>

:::en
### Badge
:::pt-br
### Badge
:::

<c-docs.example>
<div class="flex items-center gap-4">
  <c-avatar>
    <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
    <c-avatar.fallback>MM</c-avatar.fallback>
    <c-avatar.badge class="bg-emerald-500!" />
  </c-avatar>
  <c-avatar size="lg">
    <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
    <c-avatar.fallback>MM</c-avatar.fallback>
    <c-avatar.badge class="bg-emerald-500!" />
  </c-avatar>
</div>
</c-docs.example>

:::en
### Group
:::pt-br
### Grupo
:::

<c-docs.example>
<c-avatar.group>
  <c-avatar>
    <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
    <c-avatar.fallback>MM</c-avatar.fallback>
  </c-avatar>
  <c-avatar>
    <c-avatar.image src="https://github.com/SarthakJariwala.png" alt="@SarthakJariwala" />
    <c-avatar.fallback>SJ</c-avatar.fallback>
  </c-avatar>
  <c-avatar>
    <c-avatar.image src="https://github.com/shadcn.png" alt="@shadcn" />
    <c-avatar.fallback>SH</c-avatar.fallback>
  </c-avatar>
  <c-avatar.group-count>+3</c-avatar.group-count>
</c-avatar.group>
</c-docs.example>

:::en
## Notes

The badge defaults to `bg-primary`. Colouring it takes the `!` suffix —
`bg-emerald-500!` — because two background utilities on the same element are
decided by their order in the compiled stylesheet, not by the order you wrote
them. Tailwind sorts them by name, so `bg-primary` lands after
`bg-emerald-500` and wins.

The rule holds for any class of yours that collides with one the component
already sets. It applies to every component here, not just this one.
:::pt-br
## Observações

O badge usa `bg-primary` por padrão. Colori-lo pede o sufixo `!` —
`bg-emerald-500!` — porque dois utilitários de fundo no mesmo elemento são
decididos pela ordem na folha de estilo compilada, não pela ordem em que você os
escreveu. O Tailwind os ordena pelo nome, então `bg-primary` fica depois de
`bg-emerald-500` e vence.

A regra vale para qualquer classe sua que colida com uma que o componente já
define. Ela se aplica a todos os componentes daqui, não só a este.
:::
