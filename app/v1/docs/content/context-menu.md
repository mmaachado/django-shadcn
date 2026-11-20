---
title: Context Menu
description: A menu that opens where you right-click.
description.pt-br: Um menu que abre onde você clica com o botão direito.
description.es: Un menú que se abre donde haces clic derecho.
---

<c-docs.demo-section class="min-h-[350px]">
<c-context-menu>
<c-context-menu.trigger class="flex h-[150px] w-[300px] items-center justify-center rounded-md border border-dashed text-sm">
Right click here
</c-context-menu.trigger>
<c-context-menu.content class="w-52">
<c-context-menu.item>Back<c-context-menu.shortcut>⌘[</c-context-menu.shortcut></c-context-menu.item>
<c-context-menu.item>Forward<c-context-menu.shortcut>⌘]</c-context-menu.shortcut></c-context-menu.item>
<c-context-menu.item>Reload<c-context-menu.shortcut>⌘R</c-context-menu.shortcut></c-context-menu.item>
<c-context-menu.separator />
<c-context-menu.item variant="destructive">Delete</c-context-menu.item>
</c-context-menu.content>
</c-context-menu>
</c-docs.demo-section>

<c-docs.cheat-sheet name="context-menu">
<c-context-menu>
  <c-context-menu.trigger class="flex h-[120px] w-[280px] items-center justify-center rounded-md border border-dashed text-sm">
    Right click here
  </c-context-menu.trigger>
  <c-context-menu.content class="w-48">
    <c-context-menu.item>Profile</c-context-menu.item>
    <c-context-menu.item>Billing</c-context-menu.item>
    <c-context-menu.item>Settings</c-context-menu.item>
  </c-context-menu.content>
</c-context-menu>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add context_menu
```

:::en
## Usage

The trigger swallows the browser's own menu and records where you clicked; the
content is placed there with `fixed`, so it opens under the cursor rather than
under the element. Items close the menu when picked.

An item is a plain element: put a link in it to navigate, or a `<button>` in a
`<form>` to post, so the menu does things the Django way. The menu is Alpine,
so without JavaScript a right click opens the browser's own menu as usual.
:::pt-br
## Uso

O trigger engole o menu do próprio navegador e registra onde você clicou; o
conteúdo é posicionado ali com `fixed`, então ele abre embaixo do cursor e não
embaixo do elemento. Os itens fecham o menu quando escolhidos.

Um item é um elemento simples: ponha um link nele para navegar, ou um
`<button>` num `<form>` para enviar, e o menu faz as coisas do jeito do Django.
O menu é Alpine, então sem JavaScript um clique com o botão direito abre o menu
do próprio navegador, como sempre.
:::

<c-docs.example>
<c-context-menu>
  <c-context-menu.trigger class="flex h-[120px] w-[280px] items-center justify-center rounded-md border border-dashed text-sm">
    Right click here
  </c-context-menu.trigger>
  <c-context-menu.content class="w-48">
    <c-context-menu.item>Profile</c-context-menu.item>
    <c-context-menu.item>Billing</c-context-menu.item>
    <c-context-menu.item>Settings</c-context-menu.item>
  </c-context-menu.content>
</c-context-menu>
</c-docs.example>

:::en
## Examples

### Basic
:::pt-br
## Exemplos

### Básico
:::

<c-docs.example>
<c-context-menu>
  <c-context-menu.trigger class="flex h-[120px] w-[280px] items-center justify-center rounded-md border border-dashed text-sm">
    Right click here
  </c-context-menu.trigger>
  <c-context-menu.content class="w-48">
    <c-context-menu.item>Back</c-context-menu.item>
    <c-context-menu.item>Forward</c-context-menu.item>
    <c-context-menu.item>Reload</c-context-menu.item>
  </c-context-menu.content>
</c-context-menu>
</c-docs.example>

:::en
### Submenu
:::pt-br
### Submenu
:::

<c-docs.example>
<c-context-menu>
  <c-context-menu.trigger class="flex h-[120px] w-[280px] items-center justify-center rounded-md border border-dashed text-sm">
    Right click here
  </c-context-menu.trigger>
  <c-context-menu.content class="w-52">
    <c-context-menu.item>New file</c-context-menu.item>
    <c-context-menu.sub>
      <c-context-menu.sub-trigger>Share</c-context-menu.sub-trigger>
      <c-context-menu.sub-content class="w-40">
        <c-context-menu.item>Copy link</c-context-menu.item>
        <c-context-menu.item>Email</c-context-menu.item>
      </c-context-menu.sub-content>
    </c-context-menu.sub>
    <c-context-menu.separator />
    <c-context-menu.item variant="destructive">Delete</c-context-menu.item>
  </c-context-menu.content>
</c-context-menu>
</c-docs.example>

:::en
### Shortcuts

`shortcut` shows a key combination at the end of an item, as a label.
:::pt-br
### Atalhos

O `shortcut` mostra uma combinação de teclas no fim de um item, como rótulo.
:::

<c-docs.example>
<c-context-menu>
  <c-context-menu.trigger class="flex h-[120px] w-[280px] items-center justify-center rounded-md border border-dashed text-sm">
    Right click here
  </c-context-menu.trigger>
  <c-context-menu.content class="w-56">
    <c-context-menu.item>Copy<c-context-menu.shortcut>⌘C</c-context-menu.shortcut></c-context-menu.item>
    <c-context-menu.item>Paste<c-context-menu.shortcut>⌘V</c-context-menu.shortcut></c-context-menu.item>
    <c-context-menu.item>Select all<c-context-menu.shortcut>⌘A</c-context-menu.shortcut></c-context-menu.item>
  </c-context-menu.content>
</c-context-menu>
</c-docs.example>

:::en
### Groups

`group` holds related items, and `label` and `separator` set the groups apart.
:::pt-br
### Grupos

O `group` reúne itens relacionados, e o `label` e o `separator` separam os
grupos.
:::

<c-docs.example>
<c-context-menu>
  <c-context-menu.trigger class="flex h-[120px] w-[280px] items-center justify-center rounded-md border border-dashed text-sm">
    Right click here
  </c-context-menu.trigger>
  <c-context-menu.content class="w-48">
    <c-context-menu.label>File</c-context-menu.label>
    <c-context-menu.group>
      <c-context-menu.item>New file</c-context-menu.item>
      <c-context-menu.item>Open</c-context-menu.item>
    </c-context-menu.group>
    <c-context-menu.separator />
    <c-context-menu.label>Edit</c-context-menu.label>
    <c-context-menu.group>
      <c-context-menu.item>Undo</c-context-menu.item>
      <c-context-menu.item>Redo</c-context-menu.item>
    </c-context-menu.group>
  </c-context-menu.content>
</c-context-menu>
</c-docs.example>

:::en
### Icons
:::pt-br
### Ícones
:::

<c-docs.example>
<c-context-menu>
  <c-context-menu.trigger class="flex h-[120px] w-[280px] items-center justify-center rounded-md border border-dashed text-sm">
    Right click here
  </c-context-menu.trigger>
  <c-context-menu.content class="w-48">
    <c-context-menu.item><c-icon name="copy" />Copy link</c-context-menu.item>
    <c-context-menu.item><c-icon name="folder" />Move to folder</c-context-menu.item>
    <c-context-menu.item><c-icon name="users" />Share</c-context-menu.item>
  </c-context-menu.content>
</c-context-menu>
</c-docs.example>

:::en
### Checkboxes and radios

These two keep the menu open when picked, so several can be set in one go.
:::pt-br
### Checkboxes e radios

Esses dois mantêm o menu aberto quando escolhidos, para que vários possam ser
definidos de uma vez.
:::

<c-docs.example>
<c-context-menu>
  <c-context-menu.trigger class="flex h-[120px] w-[280px] items-center justify-center rounded-md border border-dashed text-sm">
    Right click here
  </c-context-menu.trigger>
  <c-context-menu.content class="w-56">
    <c-context-menu.label>Appearance</c-context-menu.label>
    <c-context-menu.checkbox-item checked="true">Status bar</c-context-menu.checkbox-item>
    <c-context-menu.checkbox-item>Activity bar</c-context-menu.checkbox-item>
    <c-context-menu.separator />
    <c-context-menu.label>Panel position</c-context-menu.label>
    <c-context-menu.radio-group value="bottom">
      <c-context-menu.radio-item value="top">Top</c-context-menu.radio-item>
      <c-context-menu.radio-item value="bottom">Bottom</c-context-menu.radio-item>
      <c-context-menu.radio-item value="right">Right</c-context-menu.radio-item>
    </c-context-menu.radio-group>
  </c-context-menu.content>
</c-context-menu>
</c-docs.example>

:::en
### Inset items

`inset` lines an item up with the ones that carry a checkbox or radio mark.
:::pt-br
### Itens recuados

`inset` alinha um item com os que levam uma marca de checkbox ou de radio.
:::

<c-docs.example>
<c-context-menu>
  <c-context-menu.trigger class="flex h-[120px] w-[280px] items-center justify-center rounded-md border border-dashed text-sm">
    Right click here
  </c-context-menu.trigger>
  <c-context-menu.content class="w-52">
    <c-context-menu.label inset="true">Actions</c-context-menu.label>
    <c-context-menu.item inset="true">Rename</c-context-menu.item>
    <c-context-menu.item inset="true">Duplicate</c-context-menu.item>
  </c-context-menu.content>
</c-context-menu>
</c-docs.example>

:::en
### Destructive
:::pt-br
### Destructive
:::

<c-docs.example>
<c-context-menu>
  <c-context-menu.trigger class="flex h-[120px] w-[280px] items-center justify-center rounded-md border border-dashed text-sm">
    Right click here
  </c-context-menu.trigger>
  <c-context-menu.content class="w-48">
    <c-context-menu.item>Rename</c-context-menu.item>
    <c-context-menu.separator />
    <c-context-menu.item variant="destructive">Delete</c-context-menu.item>
  </c-context-menu.content>
</c-context-menu>
</c-docs.example>

:::en
## RTL

The content opens at the cursor, and its items align their text to the start,
with shortcuts and submenu arrows at the end, so under `dir="rtl"` they mirror
with the text. A submenu opens on the other side.

## Accessibility

The content is a `role="menu"`, the items `menuitem`, `menuitemcheckbox` or
`menuitemradio` with `aria-checked`, and a submenu trigger reports
`aria-haspopup` and `aria-expanded`. Escape closes the menu. There is no roving
focus: the menu answers to the pointer and to Escape, not to the arrow keys,
and a right click is the only way to open it, so whatever it offers needs
another way in for a keyboard.

## API reference
:::pt-br
## RTL

O conteúdo abre no cursor, e os itens alinham o texto ao início, com atalhos e
setas de submenu no fim, então sob `dir="rtl"` eles espelham com o texto. Um
submenu abre do outro lado.

## Acessibilidade

O conteúdo é um `role="menu"`, os itens são `menuitem`, `menuitemcheckbox` ou
`menuitemradio` com `aria-checked`, e um trigger de submenu informa
`aria-haspopup` e `aria-expanded`. O Escape fecha o menu. Não há foco
itinerante: o menu responde ao ponteiro e ao Escape, não às setas, e um clique
com o botão direito é o único jeito de abri-lo, então o que ele oferece precisa
de outro caminho para o teclado.

## Referência da API
:::

<c-docs.api-reference name="context-menu" />

:::en
## Notes

Radix opens the submenu on hover with a safe triangle, so moving diagonally
towards it does not close it. Here the submenu opens on `mouseenter` and closes
on `mouseleave` — cutting a corner too sharply closes it.

**The menu closes when the page scrolls.** It is placed at viewport
coordinates, so leaving it open through a scroll would drag it away from what
you right-clicked. Radix does the same thing for the same reason.

Upstream caps the menu height and scrolls it internally. That is dropped here:
the overflow would clip the submenu, which Radix escapes by rendering it in a
portal. A very long menu grows instead of scrolling.

There is no roving focus: the menu answers to the pointer and to `Escape`, not
to the arrow keys. Same limitation as the tooltip on positioning — the content
is placed at the cursor without measuring whether it fits, so a right-click
near the bottom edge opens a menu that runs past it.
:::pt-br
## Observações

O Radix abre o submenu no hover com um triângulo de segurança, então ir na
diagonal em direção a ele não o fecha. Aqui o submenu abre no `mouseenter` e
fecha no `mouseleave` — cortar caminho demais o fecha.

**O menu fecha quando a página rola.** Ele é posicionado em coordenadas da
viewport, então deixá-lo aberto durante uma rolagem o arrastaria para longe do
que você clicou com o botão direito. O Radix faz o mesmo, pelo mesmo motivo.

O upstream limita a altura do menu e faz a rolagem dentro dele. Isso foi
deixado de fora aqui: o overflow cortaria o submenu, coisa de que o Radix escapa
renderizando-o num portal. Um menu muito longo cresce em vez de rolar.

Não há foco itinerante: o menu responde ao ponteiro e ao `Escape`, não às setas
do teclado. A mesma limitação do tooltip no posicionamento — o conteúdo é
colocado no cursor sem medir se cabe, então um clique com o botão direito perto
da borda de baixo abre um menu que passa dela.
:::
