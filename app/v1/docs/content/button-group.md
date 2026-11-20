---
title: Button Group
description: Groups related buttons together, sharing a single outline.
description.pt-br: Agrupa botões relacionados sob um contorno só.
description.es: Agrupa botones relacionados bajo un solo contorno.
---

<c-docs.demo-section class="min-h-[350px]">
<c-button-group>
<c-button variant="outline">Day</c-button>
<c-button variant="outline">Week</c-button>
<c-button variant="outline">Month</c-button>
</c-button-group>
</c-docs.demo-section>

<c-docs.cheat-sheet name="button-group">
<c-button-group aria-label="Text alignment">
  <c-button variant="outline">Left</c-button>
  <c-button variant="outline">Center</c-button>
  <c-button variant="outline">Right</c-button>
</c-button-group>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add button_group
```

:::en
## Usage

The group flattens the inner corners and drops the doubled borders through
descendant selectors, so the buttons inside need nothing special. It is CSS
only.

A button group holds actions that are each done on their own. For buttons that
stay pressed, one or several at a time, use
[Toggle Group]({% url 'page' slug='toggle-group' %}) instead: it keeps the
pressed state.
:::pt-br
## Uso

O grupo achata os cantos internos e tira as bordas duplicadas por seletores de
descendente, então os botões dentro dele não precisam de nada especial. É só
CSS.

Um grupo de botões reúne ações que são feitas cada uma por si. Para botões que
ficam pressionados, um ou vários por vez, use o
[Toggle Group]({% url 'page' slug='toggle-group' %}): ele guarda o estado de
pressionado.
:::

<c-docs.example>
<c-button-group>
  <c-button variant="outline">Day</c-button>
  <c-button variant="outline">Week</c-button>
</c-button-group>
</c-docs.example>

:::en
## Examples

### Orientation
:::pt-br
## Exemplos

### Orientação
:::

<c-docs.example>
<c-button-group orientation="vertical">
  <c-button variant="outline">Top</c-button>
  <c-button variant="outline">Middle</c-button>
  <c-button variant="outline">Bottom</c-button>
</c-button-group>
</c-docs.example>

:::en
### Size

The buttons keep their own `size`; give every button in the group the same
one.
:::pt-br
### Tamanho

Os botões mantêm o próprio `size`; dê o mesmo a todos os botões do grupo.
:::

<c-docs.example>
<div class="flex flex-col items-start gap-3">
  <c-button-group>
    <c-button variant="outline" size="sm">Small</c-button>
    <c-button variant="outline" size="sm">Button</c-button>
  </c-button-group>
  <c-button-group>
    <c-button variant="outline" size="lg">Large</c-button>
    <c-button variant="outline" size="lg">Button</c-button>
  </c-button-group>
</div>
</c-docs.example>

:::en
### Nested

A group inside a group keeps a gap between them, for toolbars.
:::pt-br
### Aninhado

Um grupo dentro de outro mantém um espaço entre eles, para barras de
ferramentas.
:::

<c-docs.example>
<c-button-group>
  <c-button-group>
    <c-button variant="outline">Undo</c-button>
    <c-button variant="outline">Redo</c-button>
  </c-button-group>
  <c-button-group>
    <c-button variant="outline">Cut</c-button>
    <c-button variant="outline">Paste</c-button>
  </c-button-group>
</c-button-group>
</c-docs.example>

:::en
### Separator and split

`separator` draws a line between buttons that share a colour, where the border
alone would not show. A primary action beside its options is the split button.
:::pt-br
### Separador e split

O `separator` desenha uma linha entre botões da mesma cor, onde a borda sozinha
não apareceria. Uma ação principal ao lado das opções dela é o botão split.
:::

<c-docs.example>
<c-button-group>
  <c-button>Save</c-button>
  <c-button-group.separator />
  <c-button size="icon">
    <c-icon name="chevron-down" />
  </c-button>
</c-button-group>
</c-docs.example>

:::en
### Input

An input joins the row like a button, and `text` adds a label piece.
:::pt-br
### Input

Um input entra na fileira como um botão, e o `text` acrescenta um pedaço de
rótulo.
:::

<c-docs.example>
<c-button-group>
  <c-button-group.text>https://</c-button-group.text>
  <c-input placeholder="example.com" class="w-[220px]" />
  <c-button variant="outline">Go</c-button>
</c-button-group>
</c-docs.example>

:::en
### Input group
:::pt-br
### Input group
:::

<c-docs.example>
<c-button-group>
  <c-input-group class="w-[220px]">
    <c-input-group.addon>
      <c-icon name="search" />
    </c-input-group.addon>
    <c-input-group.input placeholder="Search" />
  </c-input-group>
  <c-button variant="outline">Search</c-button>
</c-button-group>
</c-docs.example>

:::en
### Dropdown menu

A [Dropdown Menu]({% url 'page' slug='dropdown-menu' %}) wraps its trigger in an
element of its own, so the group flattens that element and not the button in
it. Flatten the button's start corners yourself, with the `!` suffix.
:::pt-br
### Dropdown menu

Um [Dropdown Menu]({% url 'page' slug='dropdown-menu' %}) envolve o trigger num
elemento próprio, então o grupo achata esse elemento e não o botão dentro dele.
Achate você mesmo os cantos do início do botão, com o sufixo `!`.
:::

<c-docs.example>
<c-button-group>
  <c-button variant="outline">Follow</c-button>
  <c-dropdown-menu>
    <c-dropdown-menu.trigger>
      <c-button variant="outline" size="icon" class="rounded-s-none! border-s-0!" aria-label="More options">
        <c-icon name="chevron-down" />
      </c-button>
    </c-dropdown-menu.trigger>
    <c-dropdown-menu.content align="end">
      <c-dropdown-menu.item>Mute</c-dropdown-menu.item>
      <c-dropdown-menu.item>Report</c-dropdown-menu.item>
    </c-dropdown-menu.content>
  </c-dropdown-menu>
</c-button-group>
</c-docs.example>

:::en
## RTL

The rounded ends and the shared borders are logical, so under `dir="rtl"` the
row reverses and keeps its rounded ends on the outside.

## Accessibility

The group is a `role="group"`. Give it an `aria-label` when the buttons only
make sense together, such as text alignment, so a screen reader announces what
the set is for. Each button stays its own tab stop.

## API reference
:::pt-br
## RTL

As pontas arredondadas e as bordas compartilhadas são lógicas, então sob
`dir="rtl"` a fileira se inverte e mantém as pontas arredondadas do lado de
fora.

## Acessibilidade

O grupo é um `role="group"`. Dê a ele um `aria-label` quando os botões só fazem
sentido juntos, como no alinhamento de texto, para que um leitor de tela
anuncie para que serve o conjunto. Cada botão continua sendo a própria parada de
tab.

## Referência da API
:::

<c-docs.api-reference name="button-group" />

:::en
## Notes

Upstream also groups a select and a popover trigger. Both wrap their trigger
here, like the dropdown menu, so they need the same corner classes on the
trigger, and a [Native Select]({% url 'page' slug='native-select' %}) sits
better beside the group than inside it.
:::pt-br
## Observações

O upstream também agrupa um select e o trigger de um popover. Aqui os dois
envolvem o trigger, como o dropdown menu, então pedem as mesmas classes de canto
no trigger, e um [Native Select]({% url 'page' slug='native-select' %}) fica
melhor ao lado do grupo do que dentro dele.
:::
