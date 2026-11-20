---
title: Link
description: An anchor styled like the link variant of a button.
description.pt-br: Uma âncora com o estilo da variante link do botão.
description.es: Un ancla con el estilo de la variante link del botón.
---

<c-docs.demo-section class="min-h-[350px]">
<c-a href="#">Link</c-a>
</c-docs.demo-section>

<c-docs.cheat-sheet name="a">
<c-a href="{% url 'home' %}">Link</c-a>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add a
```

:::en
## Usage

`<c-a>` renders an `<a>`, named after the element. Upstream this is the `link`
variant of the button put on an anchor, so it takes the button's sizes and no
`variant`.

Every attribute reaches the `<a>`: `href` takes Django's `url` tag like any
template, and `target`, `rel` and `download` work as usual. It is a plain
link, so it needs no JavaScript.
:::pt-br
## Uso

O `<c-a>` renderiza um `<a>`, e leva o nome do elemento. No upstream isto é a
variante `link` do botão posta numa âncora, então ele aceita os tamanhos do
botão e nenhum `variant`.

Todo atributo chega ao `<a>`: o `href` aceita a tag `url` do Django como
qualquer template, e `target`, `rel` e `download` funcionam como sempre. É um
link comum, então não precisa de JavaScript.
:::

```html
<c-a href="{% url 'post-detail' post.pk %}">Read more</c-a>
```

:::en
## Examples

### Sizes
:::pt-br
## Exemplos

### Tamanhos
:::

<c-docs.example>
<div class="flex flex-wrap items-center gap-4">
  <c-a href="#" size="xs">Extra small</c-a>
  <c-a href="#" size="sm">Small</c-a>
  <c-a href="#">Default</c-a>
  <c-a href="#" size="lg">Large</c-a>
</div>
</c-docs.example>

:::en
### With an icon
:::pt-br
### Com ícone
:::

<c-docs.example>
<c-a href="#">
  Documentation
  <c-icon name="chevron-right" />
</c-a>
</c-docs.example>

:::en
### External

A link that opens a new tab should say so with `rel="noopener noreferrer"`,
which also keeps the new page from reaching back into yours.
:::pt-br
### Externo

Um link que abre uma aba nova deve levar `rel="noopener noreferrer"`, o que
também impede a página nova de alcançar a sua.
:::

<c-docs.example>
<c-a href="https://ui.shadcn.com" target="_blank" rel="noopener noreferrer">
  shadcn/ui
</c-a>
</c-docs.example>

:::en
## RTL

The link has no side of its own. An icon stays where the markup puts it, which
under `dir="rtl"` is the other side, and an arrow does not turn by itself: add
`rtl:rotate-180` to one that points the way the text runs.

## Accessibility

It is a native `<a>` with an `href`: it takes focus, follows on Enter and is
announced as a link. Without an `href` it is neither focusable nor announced,
so always give it one. The underline shows on hover, so the text itself has
to say where the link goes.

## API reference
:::pt-br
## RTL

O link não tem um lado próprio. Um ícone fica onde o markup o põe, o que sob
`dir="rtl"` é o outro lado, e uma seta não se vira sozinha: acrescente
`rtl:rotate-180` a uma que aponte no sentido do texto.

## Acessibilidade

É um `<a>` nativo com `href`: recebe foco, segue o link com Enter e é anunciado
como link. Sem `href` ele não recebe foco nem é anunciado, então sempre dê um a
ele. O sublinhado aparece no hover, então o próprio texto tem de dizer para
onde o link vai.

## Referência da API
:::

<c-docs.api-reference name="a" />

:::en
## Notes

There is no link that looks like a solid button: `<c-button>` always renders a
`<button>`, and an `href` on it does nothing. Put the button's classes, from
`templates/cotton/button/index.html`, on an `<a>` for that.
:::pt-br
## Observações

Não há um link com cara de botão sólido: o `<c-button>` sempre renderiza um
`<button>`, e um `href` nele não faz nada. Para isso, ponha as classes do botão,
de `templates/cotton/button/index.html`, num `<a>`.
:::
