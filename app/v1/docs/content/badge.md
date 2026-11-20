---
title: Badge
description: Displays a badge or a component that looks like a badge.
description.pt-br: Exibe um selo, ou um componente com cara de selo.
description.es: Muestra una insignia, o un componente con aspecto de insignia.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="flex flex-wrap items-center justify-center gap-2">
<c-badge>Badge</c-badge>
<c-badge variant="secondary">Secondary</c-badge>
<c-badge variant="destructive">Destructive</c-badge>
<c-badge variant="outline">Outline</c-badge>
</div>
</c-docs.demo-section>

<c-docs.cheat-sheet name="badge">
<c-badge variant="secondary">{{ post.status }}</c-badge>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add badge
```

:::en
## Usage

A badge is a small rounded label for a status, a count or a tag. It renders an
inline `<div>`, needs no JavaScript, and shows whatever you put inside, so a
model field goes straight in.
:::pt-br
## Uso

Um badge é um rótulo pequeno e arredondado para um status, uma contagem ou uma
tag. Ele renderiza uma `<div>` em linha, não precisa de JavaScript e mostra o
que você puser dentro, então um campo do model entra direto.
:::

```html
{% for tag in post.tags.all %}
  <c-badge variant="outline">{{ tag.name }}</c-badge>
{% endfor %}
```

:::en
## Examples

### Variants
:::pt-br
## Exemplos

### Variantes
:::

<c-docs.example>
<div class="flex flex-wrap gap-2">
  <c-badge>Default</c-badge>
  <c-badge variant="secondary">Secondary</c-badge>
  <c-badge variant="destructive">Destructive</c-badge>
  <c-badge variant="outline">Outline</c-badge>
</div>
</c-docs.example>

:::en
### With an icon

The badge does not space or size an icon on its own, so give it `gap-1` and the
icon `size-3`.
:::pt-br
### Com ícone

O badge não espaça nem dimensiona um ícone sozinho, então dê a ele `gap-1` e ao
ícone `size-3`.
:::

<c-docs.example>
<div class="flex flex-wrap gap-2">
  <c-badge variant="secondary" class="gap-1">
    <c-icon name="check" class="size-3" />
    Verified
  </c-badge>
  <c-badge variant="outline" class="gap-1">
    Bookmarks
    <c-icon name="trending-up" class="size-3" />
  </c-badge>
</div>
</c-docs.example>

:::en
### With a spinner
:::pt-br
### Com spinner
:::

<c-docs.example>
<c-badge variant="secondary" class="gap-1">
  <c-spinner class="size-3" />
  Syncing
</c-badge>
</c-docs.example>

:::en
### Link

Wrap the badge in an `<a>` to make it a link. The link takes the focus and the
click; the badge is its look.
:::pt-br
### Link

Envolva o badge num `<a>` para torná-lo um link. O link recebe o foco e o
clique; o badge é a aparência.
:::

<c-docs.example>
<a href="#" class="rounded-full">
  <c-badge variant="outline" class="gap-1">
    Open Source
    <c-icon name="arrow-right" class="size-3" />
  </c-badge>
</a>
</c-docs.example>

:::en
### Custom colors

A colour of your own takes the `!` suffix: the badge already sets a background
and a text colour, and two utilities for the same property are settled by the
compiled stylesheet, not by the order you write them.
:::pt-br
### Cores personalizadas

Uma cor sua pede o sufixo `!`: o badge já define um fundo e uma cor de texto, e
dois utilitários para a mesma propriedade são decididos pela folha de estilo
compilada, não pela ordem em que você os escreve.
:::

<c-docs.example>
<div class="flex flex-wrap gap-2">
  <c-badge class="bg-blue-50! text-blue-700! dark:bg-blue-950! dark:text-blue-300!">Blue</c-badge>
  <c-badge class="bg-green-50! text-green-700! dark:bg-green-950! dark:text-green-300!">Green</c-badge>
  <c-badge class="bg-purple-50! text-purple-700! dark:bg-purple-950! dark:text-purple-300!">Purple</c-badge>
</div>
</c-docs.example>

:::en
## RTL

The padding is the same on both sides, so a badge looks the same under
`dir="rtl"`. An icon stays where the markup puts it, which is the other side.

## Accessibility

A badge is text and is read as text. Colour alone does not say anything to a
screen reader or to someone who cannot tell the variants apart, so the word
inside has to carry the status.

## API reference
:::pt-br
## RTL

O padding é o mesmo dos dois lados, então um badge fica igual sob `dir="rtl"`.
Um ícone fica onde o markup o põe, o que é o outro lado.

## Acessibilidade

Um badge é texto e é lido como texto. A cor sozinha não diz nada a um leitor de
tela nem a quem não distingue as variantes, então a palavra dentro dele tem de
carregar o status.

## Referência da API
:::

<c-docs.api-reference name="badge" />
