---
title: Dropdown Menu
description: Displays a menu to the user — such as a set of actions or functions — triggered by a button.
description.pt-br: Um menu aberto por um botão — um conjunto de ações, por exemplo.
description.es: Un menú que abre un botón — un conjunto de acciones, por ejemplo.
---

<c-docs.demo-section class="min-h-[350px]">
<c-dropdown-menu>
<c-dropdown-menu.trigger>
<c-button variant="outline">Open</c-button>
</c-dropdown-menu.trigger>
<c-dropdown-menu.content class="w-56">
<c-dropdown-menu.label>My Account</c-dropdown-menu.label>
<c-dropdown-menu.separator />
<c-dropdown-menu.group>
<c-dropdown-menu.item>Profile<c-dropdown-menu.shortcut>⇧⌘P</c-dropdown-menu.shortcut></c-dropdown-menu.item>
<c-dropdown-menu.item>Billing<c-dropdown-menu.shortcut>⌘B</c-dropdown-menu.shortcut></c-dropdown-menu.item>
<c-dropdown-menu.item>Settings<c-dropdown-menu.shortcut>⌘S</c-dropdown-menu.shortcut></c-dropdown-menu.item>
</c-dropdown-menu.group>
<c-dropdown-menu.separator />
<c-dropdown-menu.item variant="destructive">Log out</c-dropdown-menu.item>
</c-dropdown-menu.content>
</c-dropdown-menu>
</c-docs.demo-section>

<c-docs.cheat-sheet name="dropdown-menu">
<c-dropdown-menu>
    <c-dropdown-menu.trigger>
        <c-button variant="outline">Open</c-button>
    </c-dropdown-menu.trigger>
    <c-dropdown-menu.content class="w-56">
        <c-dropdown-menu.label>My Account</c-dropdown-menu.label>
        <c-dropdown-menu.separator />
        <c-dropdown-menu.item>Profile</c-dropdown-menu.item>
        <c-dropdown-menu.item>Billing</c-dropdown-menu.item>
        <c-dropdown-menu.separator />
        <c-dropdown-menu.item variant="destructive">Log out</c-dropdown-menu.item>
    </c-dropdown-menu.content>
</c-dropdown-menu>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add dropdown_menu
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-dropdown-menu>
    <c-dropdown-menu.trigger>
        <c-button variant="outline">Open</c-button>
    </c-dropdown-menu.trigger>
    <c-dropdown-menu.content class="w-56">
        <c-dropdown-menu.label>My Account</c-dropdown-menu.label>
        <c-dropdown-menu.separator />
        <c-dropdown-menu.item>Profile</c-dropdown-menu.item>
        <c-dropdown-menu.item>Billing</c-dropdown-menu.item>
        <c-dropdown-menu.separator />
        <c-dropdown-menu.item variant="destructive">Log out</c-dropdown-menu.item>
    </c-dropdown-menu.content>
</c-dropdown-menu>
```

:::en
The trigger wraps the button instead of sitting inside it. It is the element
that takes the click, and the content is positioned against the menu around
both.

## Examples

### Basic
:::pt-br
O trigger envolve o botão em vez de ficar dentro dele. É ele o elemento que
recebe o clique, e o conteúdo é posicionado em relação ao menu que envolve os
dois.

## Exemplos

### Básico
:::

<c-docs.example>
<c-dropdown-menu>
  <c-dropdown-menu.trigger>
    <c-button variant="outline">Open</c-button>
  </c-dropdown-menu.trigger>
  <c-dropdown-menu.content class="w-48">
    <c-dropdown-menu.label>My account</c-dropdown-menu.label>
    <c-dropdown-menu.separator />
    <c-dropdown-menu.item>Profile</c-dropdown-menu.item>
    <c-dropdown-menu.item>Billing</c-dropdown-menu.item>
    <c-dropdown-menu.item>Settings</c-dropdown-menu.item>
  </c-dropdown-menu.content>
</c-dropdown-menu>
</c-docs.example>

:::en
### Alignment
:::pt-br
### Alinhamento
:::

<c-docs.example class="min-h-[280px]">
<div class="flex gap-4">
  <c-dropdown-menu>
    <c-dropdown-menu.trigger>
      <c-button variant="outline">Start</c-button>
    </c-dropdown-menu.trigger>
    <c-dropdown-menu.content class="w-40">
      <c-dropdown-menu.item>Profile</c-dropdown-menu.item>
      <c-dropdown-menu.item>Billing</c-dropdown-menu.item>
    </c-dropdown-menu.content>
  </c-dropdown-menu>
  <c-dropdown-menu>
    <c-dropdown-menu.trigger>
      <c-button variant="outline">Center</c-button>
    </c-dropdown-menu.trigger>
    <c-dropdown-menu.content align="center" class="w-40">
      <c-dropdown-menu.item>Profile</c-dropdown-menu.item>
      <c-dropdown-menu.item>Billing</c-dropdown-menu.item>
    </c-dropdown-menu.content>
  </c-dropdown-menu>
  <c-dropdown-menu>
    <c-dropdown-menu.trigger>
      <c-button variant="outline">End</c-button>
    </c-dropdown-menu.trigger>
    <c-dropdown-menu.content align="end" class="w-40">
      <c-dropdown-menu.item>Profile</c-dropdown-menu.item>
      <c-dropdown-menu.item>Billing</c-dropdown-menu.item>
    </c-dropdown-menu.content>
  </c-dropdown-menu>
</div>
</c-docs.example>

:::en
`align` takes `start`, `center` or `end` and defaults to `start`.

### Checkboxes and radios
:::pt-br
`align` aceita `start`, `center` ou `end`, e o padrão é `start`.

### Checkboxes e radios
:::

<c-docs.example class="min-h-[340px]">
<c-dropdown-menu>
  <c-dropdown-menu.trigger>
    <c-button variant="outline">View</c-button>
  </c-dropdown-menu.trigger>
  <c-dropdown-menu.content class="w-56">
    <c-dropdown-menu.label>Appearance</c-dropdown-menu.label>
    <c-dropdown-menu.checkbox-item checked="true">Status bar</c-dropdown-menu.checkbox-item>
    <c-dropdown-menu.checkbox-item>Activity bar</c-dropdown-menu.checkbox-item>
    <c-dropdown-menu.separator />
    <c-dropdown-menu.label>Panel position</c-dropdown-menu.label>
    <c-dropdown-menu.radio-group value="bottom">
      <c-dropdown-menu.radio-item value="top">Top</c-dropdown-menu.radio-item>
      <c-dropdown-menu.radio-item value="bottom">Bottom</c-dropdown-menu.radio-item>
      <c-dropdown-menu.radio-item value="right">Right</c-dropdown-menu.radio-item>
    </c-dropdown-menu.radio-group>
  </c-dropdown-menu.content>
</c-dropdown-menu>
</c-docs.example>

:::en
These two keep the menu open when clicked, so a list of toggles can be worked
through in one go.

### Submenu
:::pt-br
Esses dois mantêm o menu aberto quando clicados, para que uma lista de opções
possa ser percorrida de uma vez.

### Submenu
:::

<c-docs.example class="min-h-[300px]">
<c-dropdown-menu>
  <c-dropdown-menu.trigger>
    <c-button variant="outline">Actions</c-button>
  </c-dropdown-menu.trigger>
  <c-dropdown-menu.content class="w-52">
    <c-dropdown-menu.item>New file</c-dropdown-menu.item>
    <c-dropdown-menu.sub>
      <c-dropdown-menu.sub-trigger>Share</c-dropdown-menu.sub-trigger>
      <c-dropdown-menu.sub-content class="w-40">
        <c-dropdown-menu.item>Copy link</c-dropdown-menu.item>
        <c-dropdown-menu.item>Email</c-dropdown-menu.item>
      </c-dropdown-menu.sub-content>
    </c-dropdown-menu.sub>
    <c-dropdown-menu.separator />
    <c-dropdown-menu.item variant="destructive">Delete</c-dropdown-menu.item>
  </c-dropdown-menu.content>
</c-dropdown-menu>
</c-docs.example>

:::en
### Inset items
:::pt-br
### Itens recuados
:::

<c-docs.example class="min-h-[280px]">
<c-dropdown-menu>
  <c-dropdown-menu.trigger>
    <c-button variant="outline">Edit</c-button>
  </c-dropdown-menu.trigger>
  <c-dropdown-menu.content class="w-52">
    <c-dropdown-menu.label inset="true">Actions</c-dropdown-menu.label>
    <c-dropdown-menu.item inset="true">Rename</c-dropdown-menu.item>
    <c-dropdown-menu.item inset="true">Duplicate</c-dropdown-menu.item>
  </c-dropdown-menu.content>
</c-dropdown-menu>
</c-docs.example>

:::en
`inset` lines an item up with the ones that carry a checkbox or radio mark.

### Keeping the menu open

An item closes the menu when clicked. Pass `close_on_select="false"` when the
item carries a control of its own.
:::pt-br
`inset` alinha um item com os que levam uma marca de checkbox ou de radio.

### Mantendo o menu aberto

Um item fecha o menu quando é clicado. Passe `close_on_select="false"` quando o
item tiver um controle próprio.
:::

```html
<c-dropdown-menu.item close_on_select="false">
    <label class="flex items-center gap-2">
        <c-checkbox x-model="compact" /> Compact rows
    </label>
</c-dropdown-menu.item>
```

:::en
### Shortcuts
:::pt-br
### Atalhos
:::

<c-docs.example>
<c-dropdown-menu>
  <c-dropdown-menu.trigger>
    <c-button variant="outline">Open</c-button>
  </c-dropdown-menu.trigger>
  <c-dropdown-menu.content class="w-48">
    <c-dropdown-menu.item>New tab<c-dropdown-menu.shortcut>⌘T</c-dropdown-menu.shortcut></c-dropdown-menu.item>
    <c-dropdown-menu.item>New window<c-dropdown-menu.shortcut>⌘N</c-dropdown-menu.shortcut></c-dropdown-menu.item>
  </c-dropdown-menu.content>
</c-dropdown-menu>
</c-docs.example>

:::en
### Icons
:::pt-br
### Ícones
:::

<c-docs.example>
<c-dropdown-menu>
  <c-dropdown-menu.trigger>
    <c-button variant="outline">Open</c-button>
  </c-dropdown-menu.trigger>
  <c-dropdown-menu.content class="w-48">
    <c-dropdown-menu.item><c-icon name="users" />Team</c-dropdown-menu.item>
    <c-dropdown-menu.item><c-icon name="settings" />Settings</c-dropdown-menu.item>
  </c-dropdown-menu.content>
</c-dropdown-menu>
</c-docs.example>

:::en
### Destructive
:::pt-br
### Destructive
:::

<c-docs.example>
<c-dropdown-menu>
  <c-dropdown-menu.trigger>
    <c-button variant="outline">Open</c-button>
  </c-dropdown-menu.trigger>
  <c-dropdown-menu.content class="w-48">
    <c-dropdown-menu.item>Edit</c-dropdown-menu.item>
    <c-dropdown-menu.separator />
    <c-dropdown-menu.item variant="destructive">Delete</c-dropdown-menu.item>
  </c-dropdown-menu.content>
</c-dropdown-menu>
</c-docs.example>

:::en
## RTL

Items align their text to the start, with shortcuts and submenu arrows at
the end, so under `dir="rtl"` they mirror, and `align="start"` lines the menu
up with the start of the trigger. A submenu opens on the other side.

## Accessibility

The content is a `role="menu"`, the items `menuitem`, `menuitemcheckbox` or
`menuitemradio` with `aria-checked`, and the trigger and submenu triggers report
`aria-haspopup` and `aria-expanded`. Enter, Space or Down on the trigger open the menu. Opening it from the keyboard focuses the first item; opening it with the
pointer focuses the menu, and Down or Up then go to the first or last item.
Down and Up move through the items, wrapping, Home and End go to the ends,
typing a letter jumps to the next item that starts with it, and Enter or Space
activates the item. Right opens a submenu on its first item and Left closes it,
swapped under `dir="rtl"`. Disabled items are skipped.
Escape, picking an item or Tab close it, and focus goes back to the trigger.

## API reference
:::pt-br
## RTL

Os itens alinham o texto ao início, com atalhos e setas de submenu no fim,
então sob `dir="rtl"` eles espelham, e `align="start"` alinha o menu com o
início do trigger. Um submenu abre do outro lado.

## Acessibilidade

O conteúdo é um `role="menu"`, os itens são `menuitem`, `menuitemcheckbox`
ou `menuitemradio` com `aria-checked`, e o trigger e os triggers de submenu
informam `aria-haspopup` e `aria-expanded`. O Enter, o Espaço ou a seta para baixo no trigger abrem o menu. Abri-lo pelo teclado foca o primeiro item; abri-lo com o ponteiro foca o
menu, e as setas para baixo ou para cima vão então para o primeiro ou o último
item. As setas para baixo e para cima passam pelos itens, dando a volta, Home e
End vão para as pontas, digitar uma letra pula para o próximo item que começa
com ela, e o Enter ou o Espaço ativam o item. A seta para a direita abre um
submenu no primeiro item e a seta para a esquerda o fecha, trocadas sob
`dir="rtl"`. Itens desabilitados são pulados.
O Escape, escolher um item ou o Tab o fecham, e o foco volta para o trigger.

## Referência da API
:::

<c-docs.api-reference name="dropdown-menu" />

:::en
## Notes

The content is placed with `absolute` against the trigger, so `align` is a
choice rather than a measurement: a menu near the right edge of the viewport
runs past it instead of flipping. Radix measures.

The submenu opens on `mouseenter` and closes on `mouseleave`, without the safe
triangle Radix draws — cutting a corner too sharply closes it.

Upstream caps the menu height and scrolls it internally. That is dropped here,
as in the context menu: the overflow would clip the submenu, which Radix
escapes through a portal. A very long menu grows instead of scrolling.

There is no roving focus. The menu answers to the pointer and to `Escape`, not
to the arrow keys.
:::pt-br
## Observações

O conteúdo é posicionado com `absolute` em relação ao trigger, então `align` é
uma escolha e não uma medição: um menu perto da borda direita da viewport passa
dela em vez de virar para o outro lado. O Radix mede.

O submenu abre no `mouseenter` e fecha no `mouseleave`, sem o triângulo de
segurança que o Radix desenha — cortar caminho demais o fecha.

O upstream limita a altura do menu e faz a rolagem dentro dele. Isso foi
deixado de fora aqui, como no context menu: o overflow cortaria o submenu, coisa
de que o Radix escapa com um portal. Um menu muito longo cresce em vez de rolar.

Não há foco itinerante. O menu responde ao ponteiro e ao `Escape`, não às setas
do teclado.
:::
