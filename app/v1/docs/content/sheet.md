---
title: Sheet
description: Display content that complements the main content of the screen.
description.pt-br: Mostra conteúdo que complementa o principal, vindo de uma das bordas.
description.es: Muestra contenido que complementa al principal, entrando desde un borde.
---

<c-docs.demo-section class="min-h-[350px]">
<c-sheet>
<c-sheet.trigger>
<c-button variant="outline">Open</c-button>
</c-sheet.trigger>
<c-sheet.content>
<c-sheet.header>
<c-sheet.title>Edit profile</c-sheet.title>
<c-sheet.description>Make changes to your profile here.</c-sheet.description>
</c-sheet.header>
</c-sheet.content>
</c-sheet>
</c-docs.demo-section>

<c-docs.cheat-sheet name="sheet">
<c-sheet>
  <c-sheet.trigger>
    <c-button variant="outline">Open</c-button>
  </c-sheet.trigger>
  <c-sheet.content side="right">
    <c-sheet.header>
      <c-sheet.title>Filters</c-sheet.title>
    </c-sheet.header>
  </c-sheet.content>
</c-sheet>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add sheet
```

:::en
## Usage

A panel that slides in from an edge of the screen over a backdrop. The trigger
opens it, and the close button, Escape and a click on the backdrop close it.
It is Alpine state, so without JavaScript it never opens.

A sheet holds what does not need a page of its own: the filters of a list, a
cart, a short form. A form inside posts like any other:
:::pt-br
## Uso

Um painel que desliza a partir de uma borda da tela por cima de um fundo
escurecido. O trigger o abre, e o botão de fechar, o Escape e um clique no
fundo o fecham. É estado do Alpine, então sem JavaScript ele nunca abre.

Um sheet guarda o que não precisa de uma página própria: os filtros de uma
lista, um carrinho, um formulário curto. Um formulário dentro dele envia como
qualquer outro:
:::

```html
<c-sheet>
  <c-sheet.trigger><c-button variant="outline">Filters</c-button></c-sheet.trigger>
  <c-sheet.content>
    <form method="get">
      <c-sheet.header><c-sheet.title>Filters</c-sheet.title></c-sheet.header>
      {{ filter_form }}
      <c-button>Apply</c-button>
    </form>
  </c-sheet.content>
</c-sheet>
```

:::en
## Examples

### Side

`side` takes `right`, the default, `left`, `top` or `bottom`.
:::pt-br
## Exemplos

### Lado

O `side` aceita `right`, o padrão, `left`, `top` ou `bottom`.
:::

<c-docs.example>
<div class="grid grid-cols-2 gap-2">
  <c-sheet>
    <c-sheet.trigger><c-button variant="outline" class="w-full">Left</c-button></c-sheet.trigger>
    <c-sheet.content side="left">
      <c-sheet.header>
        <c-sheet.title>From the left</c-sheet.title>
        <c-sheet.description>For navigation.</c-sheet.description>
      </c-sheet.header>
    </c-sheet.content>
  </c-sheet>
  <c-sheet>
    <c-sheet.trigger><c-button variant="outline" class="w-full">Bottom</c-button></c-sheet.trigger>
    <c-sheet.content side="bottom">
      <c-sheet.header>
        <c-sheet.title>From the bottom</c-sheet.title>
        <c-sheet.description>For a quick action on a phone.</c-sheet.description>
      </c-sheet.header>
    </c-sheet.content>
  </c-sheet>
</div>
</c-docs.example>

:::en
### Size

A width of your own replaces the default `w-3/4 max-w-sm`.
:::pt-br
### Tamanho

Uma largura sua substitui o `w-3/4 max-w-sm` padrão.
:::

<c-docs.example>
<c-sheet>
  <c-sheet.trigger><c-button variant="outline">Wide sheet</c-button></c-sheet.trigger>
  <c-sheet.content class="w-[400px] sm:w-[540px]">
    <c-sheet.header>
      <c-sheet.title>A wider sheet</c-sheet.title>
      <c-sheet.description>Room for a table or a longer form.</c-sheet.description>
    </c-sheet.header>
  </c-sheet.content>
</c-sheet>
</c-docs.example>

:::en
## RTL

`side` names a side of the screen, so a sheet from the right stays on the right
under `dir="rtl"`. Its contents follow the text, and the close button sits in
the end corner.

## Accessibility

The content is a `role="dialog"` with `aria-modal="true"`, and Escape closes
it. Opening it moves focus to its first focusable element, the close button,
which is labelled "Close". Tab and Shift+Tab cycle through what is inside and never reach the page
behind, and closing it returns focus to the element that opened it.

## API reference
:::pt-br
## RTL

O `side` nomeia um lado da tela, então um sheet da direita continua à direita
sob `dir="rtl"`. O conteúdo acompanha o texto, e o botão de fechar fica no
canto do fim.

## Acessibilidade

O conteúdo é um `role="dialog"` com `aria-modal="true"`, e o Escape o fecha.
Abri-lo leva o foco ao primeiro elemento focável, o botão de fechar, que tem o
rótulo "Close". O Tab e o Shift+Tab passam pelo que está dentro e nunca chegam à página de
trás, e fechá-lo devolve o foco ao elemento que o abriu.

## Referência da API
:::

<c-docs.api-reference name="sheet" />

:::en
## Notes

The close button is always there; upstream's no-close-button example has no
counterpart.
:::pt-br
## Observações

O botão de fechar está sempre ali; o exemplo sem botão de fechar do upstream
não tem equivalente.
:::
