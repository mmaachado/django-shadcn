---
title: Command Dialog
description: Fast, composable, unstyled command menu in a dialog.
description.pt-br: Menu de comandos rápido e componível, dentro de um diálogo.
description.es: Menú de comandos rápido y componible, dentro de un diálogo.
---

<c-docs.demo-section class="min-h-[350px]">
<c-command-dialog shortcut_key="k">
<c-slot name="trigger_slot">
<p class="text-sm text-muted-foreground">Press <c-kbd>⌘</c-kbd> <c-kbd>K</c-kbd></p>
</c-slot>
<c-command.input placeholder="Type a command or search..." />
<c-command.list>
<c-command.empty>No results found.</c-command.empty>
<c-command.group heading="Suggestions">
<c-command.item value="calendar">Calendar</c-command.item>
<c-command.item value="search">Search</c-command.item>
<c-command.item value="settings">Settings</c-command.item>
</c-command.group>
</c-command.list>
</c-command-dialog>
</c-docs.demo-section>

<c-docs.cheat-sheet name="command-dialog">
<c-command-dialog shortcut_key="k">
  <c-slot name="trigger_slot">
    <c-button variant="outline">Search <c-kbd>⌘K</c-kbd></c-button>
  </c-slot>
  <c-command.input placeholder="Search..." />
  <c-command.list>
    <c-command.item value="{% url 'home' %}">Home</c-command.item>
  </c-command.list>
</c-command-dialog>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add command_dialog
```

:::en
## Usage

[Command]({% url 'page' slug='command' %}) in a modal. It opens when
<c-kbd>⌘</c-kbd> or <c-kbd>Ctrl</c-kbd> is held with `shortcut_key`, `k` by
default, and when whatever is in the `trigger_slot` is clicked. The input, the
list and the items are the command's own parts, so picking an item dispatches
the same `item-selected` event, and a listener on the dialog sends the reader
where the item points:
:::pt-br
## Uso

O [Command]({% url 'page' slug='command' %}) num modal. Ele abre quando
<c-kbd>⌘</c-kbd> ou <c-kbd>Ctrl</c-kbd> é segurado com o `shortcut_key`, `k`
por padrão, e quando o que estiver no `trigger_slot` é clicado. O input, a
lista e os itens são as partes do próprio command, então escolher um item
dispara o mesmo evento `item-selected`, e um listener no diálogo leva o leitor
para onde o item aponta:
:::

```html
<c-command-dialog shortcut_key="k" x-on:item-selected="window.location = $event.detail">
  <c-slot name="trigger_slot">
    <c-button variant="outline">Search <c-kbd>⌘K</c-kbd></c-button>
  </c-slot>
  <c-command.input placeholder="Go to..." />
  <c-command.list>
    <c-command.item value="{% url 'orders' %}">Orders</c-command.item>
    <c-command.item value="{% url 'customers' %}">Customers</c-command.item>
  </c-command.list>
</c-command-dialog>
```

:::en
It is Alpine state, so without JavaScript neither the shortcut nor the trigger
opens it. Put it in your base template once, so the shortcut works on every
page.

## Examples

### Shortcut

`shortcut_key` picks the letter held with <c-kbd>⌘</c-kbd> or
<c-kbd>Ctrl</c-kbd>.
:::pt-br
É estado do Alpine, então sem JavaScript nem o atalho nem o trigger o abrem.
Ponha-o uma vez no seu template base, para o atalho funcionar em todas as
páginas.

## Exemplos

### Atalho

O `shortcut_key` escolhe a letra segurada junto com <c-kbd>⌘</c-kbd> ou
<c-kbd>Ctrl</c-kbd>.
:::

<c-docs.example>
<c-command-dialog shortcut_key="j">
  <c-slot name="trigger_slot">
    <p class="text-sm text-muted-foreground">Press <c-kbd>⌘</c-kbd> <c-kbd>J</c-kbd></p>
  </c-slot>
  <c-command.input placeholder="Search..." />
  <c-command.list>
    <c-command.empty>No results found.</c-command.empty>
    <c-command.item value="docs">Documentation</c-command.item>
    <c-command.item value="components">Components</c-command.item>
  </c-command.list>
</c-command-dialog>
</c-docs.example>

:::en
### Button trigger
:::pt-br
### Trigger em botão
:::

<c-docs.example>
<c-command-dialog shortcut_key="m">
  <c-slot name="trigger_slot">
    <c-button variant="outline" class="w-64 justify-between text-muted-foreground">
      Search...
      <c-kbd>⌘M</c-kbd>
    </c-button>
  </c-slot>
  <c-command.input placeholder="Search..." />
  <c-command.list>
    <c-command.item value="orders">Orders</c-command.item>
    <c-command.item value="customers">Customers</c-command.item>
  </c-command.list>
</c-command-dialog>
</c-docs.example>

:::en
## RTL

The dialog is centred and its contents follow the command's: the search icon
before the field and the shortcuts at the end of their items change sides
under `dir="rtl"`.

## Accessibility

The panel is a `role="dialog"` with `aria-modal="true"`. Opening it moves
focus to the search field, and Escape closes it. Tab and Shift+Tab cycle through what is inside and never reach the page
behind, and closing it returns focus to the element that opened it.
Keep the trigger a real button and tell readers the shortcut in words, as the
trigger text does here.

## API reference
:::pt-br
## RTL

O diálogo fica centralizado e o conteúdo segue o do command: o ícone de busca
antes do campo e os atalhos no fim dos itens trocam de lado sob `dir="rtl"`.

## Acessibilidade

O painel é um `role="dialog"` com `aria-modal="true"`. Abri-lo leva o foco ao
campo de busca, e o Escape o fecha. O Tab e o Shift+Tab passam pelo que está dentro e nunca chegam à página de
trás, e fechá-lo devolve o foco ao elemento que o abriu.
Mantenha o trigger como um botão de verdade e diga o atalho em palavras ao
leitor, como o texto do trigger faz aqui.

## Referência da API
:::

<c-docs.api-reference name="command-dialog" />
