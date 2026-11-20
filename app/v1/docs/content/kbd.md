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

<c-docs.demo-section>
<c-kbd>K</c-kbd>
</c-docs.demo-section>

```html
<c-kbd>K</c-kbd>
```

:::en
## Examples

### Group
:::pt-br
## Exemplos

### Grupo
:::

<c-docs.demo-section>

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
</c-docs.demo-section>

```html
<c-kbd.group>
  <c-kbd>Ctrl</c-kbd>
  <c-kbd>K</c-kbd>
</c-kbd.group>
```

:::en
### Inside a button
:::pt-br
### Dentro de um botão
:::

<c-docs.demo-section>
<c-button variant="outline" size="sm">
Search
<c-kbd.group>
<c-kbd>⌘</c-kbd>
<c-kbd>K</c-kbd>
</c-kbd.group>
</c-button>
</c-docs.demo-section>

```html
<c-button variant="outline" size="sm">
  Search
  <c-kbd.group>
    <c-kbd>⌘</c-kbd>
    <c-kbd>K</c-kbd>
  </c-kbd.group>
</c-button>
```

:::en
### In a sentence
:::pt-br
### Numa frase
:::

<c-docs.demo-section>

<p class="text-sm text-muted-foreground">
    Press <c-kbd>Esc</c-kbd> to close this dialog.
</p>
</c-docs.demo-section>

```html
Press <c-kbd>Esc</c-kbd> to close this dialog.
```
