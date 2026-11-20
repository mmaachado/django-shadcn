---
title: Command
description: Fast, composable, unstyled command menu for Django.
description.pt-br: Menu de comandos rápido e componível para Django.
description.es: Menú de comandos rápido y componible para Django.
---

<c-docs.demo-section class="min-h-[350px]">
<c-command class="rounded-lg border shadow-md md:min-w-[450px]">
<c-command.input placeholder="Type a command or search..." />
<c-command.list>
<c-command.empty>No results found.</c-command.empty>
<c-command.group heading="Suggestions">
<c-command.item value="calendar"><c-icon name="calendar" />Calendar</c-command.item>
<c-command.item value="search"><c-icon name="search" />Search</c-command.item>
</c-command.group>
<c-command.separator />
<c-command.group heading="Settings">
<c-command.item value="profile"><c-icon name="users" />Profile<c-command.shortcut>⌘P</c-command.shortcut></c-command.item>
<c-command.item value="settings"><c-icon name="settings" />Settings<c-command.shortcut>⌘S</c-command.shortcut></c-command.item>
</c-command.group>
</c-command.list>
</c-command>
</c-docs.demo-section>

<c-docs.cheat-sheet name="command">
<c-command>
  <c-command.input placeholder="Search..." />
  <c-command.list>
    <c-command.empty>No results found.</c-command.empty>
    <c-command.group heading="Pages">
      <c-command.item value="{% url 'home' %}">Home</c-command.item>
    </c-command.group>
  </c-command.list>
</c-command>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add command
```

:::en
## Usage

A search field over a list of items. Typing filters the items by their text,
the up and down arrows move the highlight, and Enter picks the highlighted one.
Picking an item, by click or Enter, dispatches a bubbling `item-selected` event
carrying its `value`, so the page decides what an item does. With URLs as the
values, a menu of pages is one listener:
:::pt-br
## Uso

Um campo de busca sobre uma lista de itens. Digitar filtra os itens pelo texto,
as setas para cima e para baixo movem o realce, e o Enter escolhe o realçado.
Escolher um item, pelo clique ou pelo Enter, dispara um evento `item-selected`
que borbulha e carrega o `value` dele, então a página decide o que um item
faz. Com URLs como values, um menu de páginas é um listener só:
:::

```html
<c-command x-on:item-selected="window.location = $event.detail">
  <c-command.input placeholder="Go to..." />
  <c-command.list>
    <c-command.group heading="Pages">
      <c-command.item value="{% url 'orders' %}">Orders</c-command.item>
      <c-command.item value="{% url 'customers' %}">Customers</c-command.item>
    </c-command.group>
  </c-command.list>
</c-command>
```

:::en
The filtering and the keyboard are Alpine. Without JavaScript the list shows
in full and the items do nothing; put real links inside them when they must
work without it.
:::pt-br
O filtro e o teclado são do Alpine. Sem JavaScript a lista aparece inteira e os
itens não fazem nada; ponha links de verdade dentro deles quando precisarem
funcionar sem ele.
:::

:::en
## Examples

### Basic
:::pt-br
## Exemplos

### Básico
:::

<c-docs.example>
<c-command class="rounded-lg border shadow-md md:min-w-[400px]">
  <c-command.input placeholder="Search..." />
  <c-command.list>
    <c-command.empty>No results found.</c-command.empty>
    <c-command.item value="calendar">Calendar</c-command.item>
    <c-command.item value="emoji">Search emoji</c-command.item>
    <c-command.item value="calculator">Calculator</c-command.item>
  </c-command.list>
</c-command>
</c-docs.example>

:::en
### Shortcuts

`shortcut` shows a key combination at the end of an item. It is a label only:
wire the keys yourself.
:::pt-br
### Atalhos

O `shortcut` mostra uma combinação de teclas no fim de um item. É só um rótulo:
ligue as teclas você mesmo.
:::

<c-docs.example>
<c-command class="rounded-lg border shadow-md md:min-w-[400px]">
  <c-command.input placeholder="Search..." />
  <c-command.list>
    <c-command.item value="profile">Profile<c-command.shortcut>⌘P</c-command.shortcut></c-command.item>
    <c-command.item value="billing">Billing<c-command.shortcut>⌘B</c-command.shortcut></c-command.item>
    <c-command.item value="settings">Settings<c-command.shortcut>⌘S</c-command.shortcut></c-command.item>
  </c-command.list>
</c-command>
</c-docs.example>

:::en
### Groups

`group` takes a `heading`, and `separator` draws a line between groups.
:::pt-br
### Grupos

O `group` aceita um `heading`, e o `separator` desenha uma linha entre os
grupos.
:::

<c-docs.example>
<c-command class="rounded-lg border shadow-md md:min-w-[400px]">
  <c-command.input placeholder="Search..." />
  <c-command.list>
    <c-command.group heading="Suggestions">
      <c-command.item value="calendar"><c-icon name="calendar" />Calendar</c-command.item>
      <c-command.item value="search"><c-icon name="search" />Search</c-command.item>
    </c-command.group>
    <c-command.separator />
    <c-command.group heading="Settings">
      <c-command.item value="team"><c-icon name="users" />Team</c-command.item>
      <c-command.item value="preferences"><c-icon name="settings" />Preferences</c-command.item>
    </c-command.group>
  </c-command.list>
</c-command>
</c-docs.example>

:::en
### Scrollable

The list scrolls once it is taller than 300 pixels.
:::pt-br
### Com rolagem

A lista passa a rolar quando fica mais alta do que 300 pixels.
:::

<c-docs.example>
<c-command class="rounded-lg border shadow-md md:min-w-[400px]">
  <c-command.input placeholder="Search a timezone..." />
  <c-command.list>
    <c-command.item value="cairo">Africa/Cairo</c-command.item>
    <c-command.item value="bogota">America/Bogota</c-command.item>
    <c-command.item value="new-york">America/New_York</c-command.item>
    <c-command.item value="sao-paulo">America/Sao_Paulo</c-command.item>
    <c-command.item value="dubai">Asia/Dubai</c-command.item>
    <c-command.item value="kolkata">Asia/Kolkata</c-command.item>
    <c-command.item value="tokyo">Asia/Tokyo</c-command.item>
    <c-command.item value="sydney">Australia/Sydney</c-command.item>
    <c-command.item value="berlin">Europe/Berlin</c-command.item>
    <c-command.item value="lisbon">Europe/Lisbon</c-command.item>
    <c-command.item value="london">Europe/London</c-command.item>
    <c-command.item value="auckland">Pacific/Auckland</c-command.item>
  </c-command.list>
</c-command>
</c-docs.example>

:::en
## RTL

The search icon sits before the field and a shortcut at the end of its item,
so under `dir="rtl"` both change sides with the text.

## Accessibility

The items carry `role="option"` and the field takes the arrow keys, Enter and
Escape. The list itself is not a `listbox` and the highlight is not tied to the
field with `aria-activedescendant`, so a screen reader does not follow the
highlight as it moves. Give the field an `aria-label` when it has no visible
label.

## API reference
:::pt-br
## RTL

O ícone de busca fica antes do campo e um atalho no fim do item, então sob
`dir="rtl"` os dois trocam de lado com o texto.

## Acessibilidade

Os itens levam `role="option"` e o campo atende às setas, ao Enter e ao Escape.
A lista em si não é um `listbox` e o realce não está ligado ao campo por
`aria-activedescendant`, então um leitor de tela não acompanha o realce quando
ele se move. Dê ao campo um `aria-label` quando ele não tiver rótulo visível.

## Referência da API
:::

<c-docs.api-reference name="command" />
