---
title: Menubar
description: A row of menus, the way a desktop application has one.
description.pt-br: Uma barra de menus, como a de um aplicativo de desktop.
description.es: Una barra de menús, como la de una aplicación de escritorio.
---

<c-docs.demo-section class="min-h-[350px]">
<c-menubar>
<c-menubar.menu>
<c-menubar.trigger>File</c-menubar.trigger>
<c-menubar.content>
<c-menubar.item>New tab<c-menubar.shortcut>⌘T</c-menubar.shortcut></c-menubar.item>
<c-menubar.item>New window<c-menubar.shortcut>⌘N</c-menubar.shortcut></c-menubar.item>
<c-menubar.separator />
<c-menubar.item>Print<c-menubar.shortcut>⌘P</c-menubar.shortcut></c-menubar.item>
</c-menubar.content>
</c-menubar.menu>
<c-menubar.menu>
<c-menubar.trigger>Edit</c-menubar.trigger>
<c-menubar.content>
<c-menubar.item>Undo<c-menubar.shortcut>⌘Z</c-menubar.shortcut></c-menubar.item>
<c-menubar.item>Redo<c-menubar.shortcut>⇧⌘Z</c-menubar.shortcut></c-menubar.item>
</c-menubar.content>
</c-menubar.menu>
<c-menubar.menu>
<c-menubar.trigger>View</c-menubar.trigger>
<c-menubar.content>
<c-menubar.checkbox-item checked="true">Status bar</c-menubar.checkbox-item>
<c-menubar.checkbox-item>Full screen</c-menubar.checkbox-item>
</c-menubar.content>
</c-menubar.menu>
</c-menubar>
</c-docs.demo-section>

<c-docs.cheat-sheet name="menubar">
<c-menubar>
  <c-menubar.menu>
    <c-menubar.trigger>File</c-menubar.trigger>
    <c-menubar.content>
      <c-menubar.item>New tab</c-menubar.item>
      <c-menubar.item>Open</c-menubar.item>
    </c-menubar.content>
  </c-menubar.menu>
  <c-menubar.menu>
    <c-menubar.trigger>Help</c-menubar.trigger>
    <c-menubar.content>
      <c-menubar.item>Documentation</c-menubar.item>
    </c-menubar.content>
  </c-menubar.menu>
</c-menubar>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add menubar
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-menubar>
  <c-menubar.menu>
    <c-menubar.trigger>File</c-menubar.trigger>
    <c-menubar.content>
      <c-menubar.item>New tab</c-menubar.item>
      <c-menubar.item>Open</c-menubar.item>
    </c-menubar.content>
  </c-menubar.menu>
  <c-menubar.menu>
    <c-menubar.trigger>Help</c-menubar.trigger>
    <c-menubar.content>
      <c-menubar.item>Documentation</c-menubar.item>
    </c-menubar.content>
  </c-menubar.menu>
</c-menubar>
</c-docs.example>

:::en
Open one menu and the others answer to hover — moving along the bar switches
between them without another click, which is what makes a menubar feel like
one. Clicking the open trigger again, picking an item, pressing `Escape` or
clicking away all close it.

## Examples

### Checkboxes and radios
:::pt-br
Abra um menu e os outros passam a responder ao hover — andar pela barra troca de
um para o outro sem outro clique, que é o que faz um menubar parecer um. Clicar
de novo no trigger aberto, escolher um item, apertar `Escape` ou clicar fora
fecha o menu.

## Exemplos

### Checkboxes e radios
:::

<c-docs.example>
<c-menubar>
  <c-menubar.menu>
    <c-menubar.trigger>View</c-menubar.trigger>
    <c-menubar.content>
      <c-menubar.label>Appearance</c-menubar.label>
      <c-menubar.checkbox-item checked="true">Status bar</c-menubar.checkbox-item>
      <c-menubar.checkbox-item>Activity bar</c-menubar.checkbox-item>
      <c-menubar.separator />
      <c-menubar.label>Sidebar</c-menubar.label>
      <c-menubar.radio-group value="left">
        <c-menubar.radio-item value="left">Left</c-menubar.radio-item>
        <c-menubar.radio-item value="right">Right</c-menubar.radio-item>
      </c-menubar.radio-group>
    </c-menubar.content>
  </c-menubar.menu>
</c-menubar>
</c-docs.example>

:::en
### Submenu
:::pt-br
### Submenu
:::

<c-docs.example>
<c-menubar>
  <c-menubar.menu>
    <c-menubar.trigger>File</c-menubar.trigger>
    <c-menubar.content>
      <c-menubar.item>New file</c-menubar.item>
      <c-menubar.sub>
        <c-menubar.sub-trigger>Share</c-menubar.sub-trigger>
        <c-menubar.sub-content class="w-40">
          <c-menubar.item>Copy link</c-menubar.item>
          <c-menubar.item>Email</c-menubar.item>
        </c-menubar.sub-content>
      </c-menubar.sub>
      <c-menubar.separator />
      <c-menubar.item variant="destructive">Delete</c-menubar.item>
    </c-menubar.content>
  </c-menubar.menu>
</c-menubar>
</c-docs.example>

:::en
### Alignment
:::pt-br
### Alinhamento
:::

<c-docs.example>
<c-menubar>
  <c-menubar.menu>
    <c-menubar.trigger>Start</c-menubar.trigger>
    <c-menubar.content align="start"><c-menubar.item>Aligned left</c-menubar.item></c-menubar.content>
  </c-menubar.menu>
  <c-menubar.menu>
    <c-menubar.trigger>End</c-menubar.trigger>
    <c-menubar.content align="end"><c-menubar.item>Aligned right</c-menubar.item></c-menubar.content>
  </c-menubar.menu>
</c-menubar>
</c-docs.example>

:::en
### With icons
:::pt-br
### Com ícones
:::

<c-docs.example>
<c-menubar>
  <c-menubar.menu>
    <c-menubar.trigger>File</c-menubar.trigger>
    <c-menubar.content>
      <c-menubar.item><c-icon name="folder" />Open</c-menubar.item>
      <c-menubar.item><c-icon name="copy" />Duplicate</c-menubar.item>
      <c-menubar.separator />
      <c-menubar.item><c-icon name="settings" />Settings</c-menubar.item>
    </c-menubar.content>
  </c-menubar.menu>
</c-menubar>
</c-docs.example>

:::en
## RTL

Menus open below their triggers and align with `align`, and items align to the
start with shortcuts at the end, so under `dir="rtl"` the bar and its menus
mirror. A submenu opens on the other side.

## Accessibility

Each menu is a `role="menu"` of `menuitem`, `menuitemcheckbox` and
`menuitemradio` items with `aria-checked`, and triggers report `aria-haspopup`
and `aria-expanded`. Escape closes the open menu. There is no roving focus:
the bar answers to the pointer and Tab, not to the arrow keys.

## API reference
:::pt-br
## RTL

Os menus abrem embaixo dos triggers e se alinham com `align`, e os itens se
alinham ao início com os atalhos no fim, então sob `dir="rtl"` a barra e os
menus espelham. Um submenu abre do outro lado.

## Acessibilidade

Cada menu é um `role="menu"` de itens `menuitem`, `menuitemcheckbox` e
`menuitemradio` com `aria-checked`, e os triggers informam `aria-haspopup` e
`aria-expanded`. O Escape fecha o menu aberto. Não há foco itinerante: a barra
responde ao ponteiro e ao Tab, não às setas.

## Referência da API
:::

<c-docs.api-reference name="menubar" />

:::en
## Notes

Which menu is open is tracked by element identity rather than a name you have
to invent, so a `<c-menubar.menu>` needs no `value`. The trigger and the
content find each other through the menu they share as a parent, which is why
both have to be direct children of it.

Like the context menu, there is no roving focus: the bar answers to the
pointer and to `Escape`, not to the arrow keys. The content is positioned
against its trigger with utility classes, so `align` is a choice rather than a
measurement — a menu near the right edge wants `align="end"`.
:::pt-br
## Observações

Qual menu está aberto é rastreado pela identidade do elemento, e não por um nome
que você tenha de inventar, então um `<c-menubar.menu>` não precisa de `value`.
O trigger e o conteúdo se encontram pelo menu que os dois têm como pai, e é por
isso que os dois precisam ser filhos diretos dele.

Como no context menu, não há foco itinerante: a barra responde ao ponteiro e ao
`Escape`, não às setas do teclado. O conteúdo é posicionado em relação ao
trigger com classes utilitárias, então `align` é uma escolha e não uma medição —
um menu perto da borda direita pede `align="end"`.
:::
