---
title: Card
description: Displays a card with header, content, and footer.
description.pt-br: Um cartão com cabeçalho, conteúdo e rodapé.
description.es: Una tarjeta con encabezado, contenido y pie.
---

<c-docs.demo-section class="min-h-[350px]">
<c-card class="w-[380px]">
<c-card.header>
<c-card.title>Create project</c-card.title>
<c-card.description>Deploy your new project in one click.</c-card.description>
</c-card.header>
<c-card.content class="space-y-2">
<c-label for="card-demo-name">Name</c-label>
<c-input id="card-demo-name" placeholder="Name of your project" />
</c-card.content>
<c-card.footer class="flex justify-between">
<c-button variant="outline">Cancel</c-button>
<c-button>Create</c-button>
</c-card.footer>
</c-card>
</c-docs.demo-section>

<c-docs.cheat-sheet name="card">
<c-card>
  <c-card.header>
    <c-card.title>{{ project.name }}</c-card.title>
    <c-card.description>{{ project.summary }}</c-card.description>
  </c-card.header>
  <c-card.content>...</c-card.content>
  <c-card.footer>...</c-card.footer>
</c-card>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add card
```

:::en
## Usage

A card is a bordered surface with a header, content and a footer, each its own
part so the spacing between them comes out right. It is markup only. A card
around a form is the common case, with the submit button in the footer:
:::pt-br
## Uso

Um card é uma superfície com borda, cabeçalho, conteúdo e rodapé, cada um uma
parte própria para que o espaço entre eles fique certo. É só markup. Um card em
volta de um formulário é o caso comum, com o botão de enviar no rodapé:
:::

```html
<form method="post">
  {% csrf_token %}
  <c-card>
    <c-card.header>
      <c-card.title>Your profile</c-card.title>
    </c-card.header>
    <c-card.content>{{ form }}</c-card.content>
    <c-card.footer>
      <c-button>Save</c-button>
    </c-card.footer>
  </c-card>
</form>
```

:::en
## Examples

### Spacing

The parts carry their own padding. Spacing inside the content is yours, with
`space-y-*` or a grid.
:::pt-br
## Exemplos

### Espaçamento

As partes trazem o próprio padding. O espaço dentro do conteúdo é seu, com
`space-y-*` ou um grid.
:::

<c-docs.example>
<c-card class="w-[380px]">
  <c-card.header>
    <c-card.title>Notifications</c-card.title>
    <c-card.description>You have 3 unread messages.</c-card.description>
  </c-card.header>
  <c-card.content class="grid gap-3 text-sm">
    <p>Your call has been confirmed.</p>
    <p>You have a new message.</p>
    <p>Your subscription is expiring soon.</p>
  </c-card.content>
  <c-card.footer>
    <c-button class="w-full">Mark all as read</c-button>
  </c-card.footer>
</c-card>
</c-docs.example>

:::en
### Image

An image above the header fills the width when the card clips its corners.
:::pt-br
### Imagem

Uma imagem acima do cabeçalho preenche a largura quando o card corta os
próprios cantos.
:::

<c-docs.example>
<c-card class="w-[320px] overflow-hidden">
  <c-aspect-ratio ratio="16/9" class="bg-muted">
    <img src="https://github.com/mmaachado.png" alt="" class="size-full object-cover" />
  </c-aspect-ratio>
  <c-card.header>
    <c-card.title>Design review</c-card.title>
    <c-card.description>Thursday at 3 pm, with the whole team.</c-card.description>
  </c-card.header>
</c-card>
</c-docs.example>

:::en
## RTL

The parts pad both sides alike and align their text to the start, so a card
mirrors under `dir="rtl"` without anything to change.

## Accessibility

The title is an `<h3>`, so the cards on a page are headings a screen reader
can move between. Where `<h3>` is the wrong level for the page, put the title
text in the heading you need and style it instead. The rest of the card is
plain `<div>`s.

## API reference
:::pt-br
## RTL

As partes têm o mesmo padding dos dois lados e alinham o texto ao início,
então um card espelha sob `dir="rtl"` sem nada para mudar.

## Acessibilidade

O título é um `<h3>`, então os cards de uma página são cabeçalhos entre os
quais um leitor de tela pode passar. Onde `<h3>` é o nível errado para a
página, ponha o texto do título no cabeçalho de que você precisa e estilize-o.
O resto do card são `<div>`s simples.

## Referência da API
:::

<c-docs.api-reference name="card" />

:::en
## Notes

Upstream's card has a `size="sm"` for a denser card. There is no size here;
smaller padding on the parts, such as `p-4`, does the same.
:::pt-br
## Observações

O card do upstream tem um `size="sm"` para um card mais denso. Aqui não há
tamanho; um padding menor nas partes, como `p-4`, faz o mesmo.
:::
