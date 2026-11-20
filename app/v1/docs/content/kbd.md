---
title: Kbd
description: Displays a keyboard key or a combination of keys.
description.pt-br: Exibe uma tecla ou uma combinação de teclas.
description.es: Muestra una tecla o una combinación de teclas.
---

<c-docs.demo-section class="min-h-[350px]">
<c-kbd.group>
<c-kbd>Ctrl</c-kbd>
<c-kbd>K</c-kbd>
</c-kbd.group>
</c-docs.demo-section>

<c-docs.cheat-sheet name="kbd">
<c-kbd>K</c-kbd>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add kbd
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-kbd>K</c-kbd>
</c-docs.example>

:::en
## Examples

### Group
:::pt-br
## Exemplos

### Grupo
:::

<c-docs.example>
<div class="flex items-center gap-4">
  <c-kbd.group>
    <c-kbd>Ctrl</c-kbd>
    <c-kbd>K</c-kbd>
  </c-kbd.group>
  <c-kbd.group>
    <c-kbd>⌘</c-kbd>
    <c-kbd>⇧</c-kbd>
    <c-kbd>P</c-kbd>
  </c-kbd.group>
</div>
</c-docs.example>

:::en
### Inside a button
:::pt-br
### Dentro de um botão
:::

<c-docs.example>
<c-button variant="outline" size="sm">
  Search
  <c-kbd.group>
    <c-kbd>⌘</c-kbd>
    <c-kbd>K</c-kbd>
  </c-kbd.group>
</c-button>
</c-docs.example>

:::en
### In a sentence
:::pt-br
### Numa frase
:::

<c-docs.example>
<p class="text-sm text-muted-foreground">
  Press <c-kbd>Esc</c-kbd> to close this dialog.
</p>
</c-docs.example>

:::en
### Tooltip

A tooltip can name the shortcut for a button.
:::pt-br
### Tooltip

Um tooltip pode dizer o atalho de um botão.
:::

<c-docs.example>
<c-tooltip>
  <c-tooltip.trigger>
    <c-button variant="outline" size="sm">Save</c-button>
  </c-tooltip.trigger>
  <c-tooltip.content>Save <c-kbd>⌘S</c-kbd></c-tooltip.content>
</c-tooltip>
</c-docs.example>

:::en
### Input group
:::pt-br
### Input group
:::

<c-docs.example>
<c-input-group class="max-w-xs">
  <c-input-group.addon><c-icon name="search" /></c-input-group.addon>
  <c-input-group.input placeholder="Search..." aria-label="Search" />
  <c-input-group.addon align="inline-end"><c-kbd>⌘K</c-kbd></c-input-group.addon>
</c-input-group>
</c-docs.example>

:::en
## RTL

A key stays where the markup puts it, so a combination reads in the order
you write it under `dir="rtl"` too.

## Accessibility

It renders a `<kbd>`, which a screen reader can announce as keyboard input.
Write the key's name as text, such as "Ctrl", rather than only a symbol, so
it reads out as something.

## API reference
:::pt-br
## RTL

Uma tecla fica onde o markup a põe, então uma combinação é lida na ordem em
que você a escreve também sob `dir="rtl"`.

## Acessibilidade

Ele renderiza um `<kbd>`, que um leitor de tela pode anunciar como entrada de
teclado. Escreva o nome da tecla como texto, como "Ctrl", e não só um
símbolo, para ele ser lido como algo.

## Referência da API
:::

<c-docs.api-reference name="kbd" />
