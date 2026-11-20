---
title: Accordion
description: A vertically stacked set of interactive headings that each reveal a section of content.
description.pt-br: Cabeçalhos empilhados que revelam, cada um, uma seção de conteúdo.
description.es: Encabezados apilados que revelan, cada uno, una sección de contenido.
---

<c-docs.demo-section class="min-h-[350px]">
<c-accordion type="single" collapsible="true" class="w-full max-w-md">
<c-accordion.item value="item-1">
<c-accordion.trigger value="item-1">Is it for Django?</c-accordion.trigger>
<c-accordion.content value="item-1">Yes. Every component is a django-cotton template.</c-accordion.content>
</c-accordion.item>
<c-accordion.item value="item-2">
<c-accordion.trigger value="item-2">Is it styled?</c-accordion.trigger>
<c-accordion.content value="item-2">Yes. It matches the other components in this library.</c-accordion.content>
</c-accordion.item>
<c-accordion.item value="item-3">
<c-accordion.trigger value="item-3">Is it animated?</c-accordion.trigger>
<c-accordion.content value="item-3">Yes, through Alpine's collapse plugin.</c-accordion.content>
</c-accordion.item>
</c-accordion>
</c-docs.demo-section>

<c-docs.cheat-sheet name="accordion">
<c-accordion type="single" collapsible="true">
  <c-accordion.item value="shipping">
    <c-accordion.trigger value="shipping">Shipping</c-accordion.trigger>
    <c-accordion.content value="shipping">Orders leave within two days.</c-accordion.content>
  </c-accordion.item>
</c-accordion>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add accordion
```

:::en
The panels open and close through Alpine and animate through its collapse
plugin, `@alpinejs/collapse`, which Alpine's core does not include. `add`
names it at the end of the run. Load it before Alpine:
:::pt-br
Os painéis abrem e fecham pelo Alpine e animam pelo plugin collapse dele, o
`@alpinejs/collapse`, que o núcleo do Alpine não traz. O `add` o cita no fim da
execução. Carregue-o antes do Alpine:
:::

```html
<script src="{% static 'js/collapse.min.js' %}" defer></script>
<script src="{% static 'js/alpine.min.js' %}" defer></script>
```

:::en
## Usage

Each item, its trigger and its content carry the same `value`: that is how a
trigger finds its panel without an id. Loop over a queryset and use the pk.

`type="single"` keeps one item open at a time, and `collapsible="true"` lets the
open one close again. `type="multiple"` opens them independently. `open` takes
a JSON object of the values that start open.

Without JavaScript the panels stay closed and cannot be opened, so do not put
anything there that a reader must see.
:::pt-br
## Uso

Cada item, o trigger e o conteúdo dele levam o mesmo `value`: é assim que um
trigger encontra o painel sem um id. Percorra um queryset e use o pk.

`type="single"` mantém um item aberto por vez, e `collapsible="true"` deixa o
aberto fechar de novo. `type="multiple"` abre cada um por conta própria. `open`
aceita um objeto JSON com os values que começam abertos.

Sem JavaScript os painéis ficam fechados e não podem ser abertos, então não
ponha ali nada que o leitor precise ver.
:::

```html
<c-accordion type="single" collapsible="true">
  {% for faq in faqs %}
    <c-accordion.item value="{{ faq.pk }}">
      <c-accordion.trigger value="{{ faq.pk }}">{{ faq.question }}</c-accordion.trigger>
      <c-accordion.content value="{{ faq.pk }}">{{ faq.answer }}</c-accordion.content>
    </c-accordion.item>
  {% endfor %}
</c-accordion>
```

:::en
## Examples

### Basic
:::pt-br
## Exemplos

### Básico
:::

<c-docs.example>
<c-accordion type="single" collapsible="true" class="w-full max-w-md">
  <c-accordion.item value="returns">
    <c-accordion.trigger value="returns">What is the return policy?</c-accordion.trigger>
    <c-accordion.content value="returns">Unused items come back within 30 days, at no cost.</c-accordion.content>
  </c-accordion.item>
  <c-accordion.item value="tracking">
    <c-accordion.trigger value="tracking">How do I track my order?</c-accordion.trigger>
    <c-accordion.content value="tracking">The confirmation email has a tracking link.</c-accordion.content>
  </c-accordion.item>
</c-accordion>
</c-docs.example>

:::en
### Multiple

`type="multiple"` lets several items stay open, and `open` starts the first
one open.
:::pt-br
### Múltiplo

`type="multiple"` deixa vários itens abertos, e `open` começa com o primeiro
aberto.
:::

<c-docs.example>
<c-accordion type="multiple" open='{"notifications": true}' class="w-full max-w-md">
  <c-accordion.item value="notifications">
    <c-accordion.trigger value="notifications">Notifications</c-accordion.trigger>
    <c-accordion.content value="notifications">Choose which emails we send you.</c-accordion.content>
  </c-accordion.item>
  <c-accordion.item value="privacy">
    <c-accordion.trigger value="privacy">Privacy</c-accordion.trigger>
    <c-accordion.content value="privacy">Decide who can see your profile.</c-accordion.content>
  </c-accordion.item>
</c-accordion>
</c-docs.example>

:::en
### Disabled

`disabled` on a trigger reaches its `<button>`, so that item cannot be opened
or focused.
:::pt-br
### Desabilitado

`disabled` num trigger chega ao `<button>` dele, então aquele item não pode ser
aberto nem receber foco.
:::

<c-docs.example>
<c-accordion type="single" collapsible="true" class="w-full max-w-md">
  <c-accordion.item value="plan">
    <c-accordion.trigger value="plan">Your plan</c-accordion.trigger>
    <c-accordion.content value="plan">You are on the free plan.</c-accordion.content>
  </c-accordion.item>
  <c-accordion.item value="billing">
    <c-accordion.trigger value="billing" disabled class="disabled:opacity-50">Billing</c-accordion.trigger>
    <c-accordion.content value="billing">Available on paid plans.</c-accordion.content>
  </c-accordion.item>
</c-accordion>
</c-docs.example>

:::en
### Borders
:::pt-br
### Bordas
:::

<c-docs.example>
<c-accordion type="single" collapsible="true" class="w-full max-w-md rounded-lg border">
  <c-accordion.item value="one" class="px-4 last:border-b-0">
    <c-accordion.trigger value="one">Can I change my plan?</c-accordion.trigger>
    <c-accordion.content value="one">Yes, from the billing settings, at any time.</c-accordion.content>
  </c-accordion.item>
  <c-accordion.item value="two" class="px-4 last:border-b-0">
    <c-accordion.trigger value="two">Is there a free trial?</c-accordion.trigger>
    <c-accordion.content value="two">Fourteen days, without a card.</c-accordion.content>
  </c-accordion.item>
</c-accordion>
</c-docs.example>

:::en
### Card
:::pt-br
### Card
:::

<c-docs.example>
<c-card class="w-full max-w-md">
  <c-card.header>
    <c-card.title>Frequently asked</c-card.title>
    <c-card.description>Answers to what people ask most.</c-card.description>
  </c-card.header>
  <c-card.content>
    <c-accordion type="single" collapsible="true">
      <c-accordion.item value="a" class="last:border-b-0">
        <c-accordion.trigger value="a">Do you ship abroad?</c-accordion.trigger>
        <c-accordion.content value="a">To most countries, in five to ten days.</c-accordion.content>
      </c-accordion.item>
      <c-accordion.item value="b" class="last:border-b-0">
        <c-accordion.trigger value="b">Can I cancel an order?</c-accordion.trigger>
        <c-accordion.content value="b">Until it ships, from your account.</c-accordion.content>
      </c-accordion.item>
    </c-accordion>
  </c-card.content>
</c-card>
</c-docs.example>

:::en
## RTL

The title sits at the start of the row and the chevron at its end, so under
`dir="rtl"` they change sides with the text. The chevron points down and turns
up when open, which needs no mirroring.

## Accessibility

Each trigger is a `<button>` inside an `<h3>`, so the items are headings a
screen reader can jump between, and the button reports `aria-expanded`. The
panels hide with `x-show`, which takes them out of the tab order and the
reading order while closed. Upstream also moves focus between triggers with the
arrow keys; here Tab moves between them.

## API reference
:::pt-br
## RTL

O título fica no início da linha e o chevron no fim, então sob `dir="rtl"` eles
trocam de lado junto com o texto. O chevron aponta para baixo e vira para cima
quando abre, o que não precisa de espelhamento.

## Acessibilidade

Cada trigger é um `<button>` dentro de um `<h3>`, então os itens são
cabeçalhos entre os quais um leitor de tela pode pular, e o botão informa
`aria-expanded`. Os painéis se escondem com `x-show`, o que os tira da ordem de
tab e da leitura enquanto fechados. O upstream também move o foco entre os
triggers com as setas; aqui é o Tab que passa de um para o outro.

## Referência da API
:::

<c-docs.api-reference name="accordion" />
