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
## API reference
:::pt-br
## Referência da API
:::

<c-docs.api-reference name="kbd" />
