---
title: Popover
description: Displays rich content in a portal, triggered by a button.
description.pt-br: Exibe conteúdo rico sobre a página, aberto por um botão.
description.es: Muestra contenido enriquecido sobre la página, abierto por un botón.
---

<c-docs.demo-section class="min-h-[350px]">
<c-popover>
<c-popover.trigger>
<c-button variant="outline">Open popover</c-button>
</c-popover.trigger>
<c-popover.content class="w-72">
<div class="grid gap-2">
<p class="text-sm font-medium">Dimensions</p>
<p class="text-sm text-muted-foreground">Set the size of the layer.</p>
</div>
</c-popover.content>
</c-popover>
</c-docs.demo-section>

<c-docs.cheat-sheet name="popover">
<c-popover>
  <c-popover.trigger>
    <c-button variant="outline">Open</c-button>
  </c-popover.trigger>
  <c-popover.content>...</c-popover.content>
</c-popover>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add popover
```

:::en
## Usage

The trigger opens a panel under it, and a click outside closes it.
It is Alpine state, so without JavaScript the panel never opens. A form inside
the content posts like any other, which suits a small edit next to what it
changes.
:::pt-br
## Uso

O trigger abre um painel embaixo dele, e um clique fora o fecha. É
estado do Alpine, então sem JavaScript o painel nunca abre. Um formulário
dentro do conteúdo envia como qualquer outro, o que combina com uma edição
pequena ao lado do que ela muda.
:::

:::en
## Examples

### Basic
:::pt-br
## Exemplos

### Básico
:::

<c-docs.example>
<c-popover>
  <c-popover.trigger>
    <c-button variant="outline">Details</c-button>
  </c-popover.trigger>
  <c-popover.content class="w-64 text-sm">
    Shipped on 12 August, tracking number BR123456.
  </c-popover.content>
</c-popover>
</c-docs.example>

:::en
### With a form
:::pt-br
### Com formulário
:::

<c-docs.example>
<c-popover>
  <c-popover.trigger>
    <c-button variant="outline">Rename</c-button>
  </c-popover.trigger>
  <c-popover.content class="w-72">
    <form class="grid gap-3" onsubmit="return false">
      <c-label for="popover-name">Name</c-label>
      <c-input id="popover-name" value="Quarterly report" />
      <c-button size="sm">Save</c-button>
    </form>
  </c-popover.content>
</c-popover>
</c-docs.example>

:::en
## RTL

The content opens from the start of the trigger, so under `dir="rtl"` it lines
up with the trigger's right edge.

## Accessibility

The panel is shown and hidden with Alpine and is not announced as a dialog,
focus does not move into it when it opens, and Escape does not close it. Keep the trigger a real button,
and when the panel holds a form, the reader tabs into it from the trigger.

## API reference
:::pt-br
## RTL

O conteúdo abre a partir do início do trigger, então sob `dir="rtl"` ele se
alinha com a borda direita do trigger.

## Acessibilidade

O painel é mostrado e escondido pelo Alpine e não é anunciado como diálogo, o
foco não vai para dentro dele quando abre, e o Escape não o fecha. Mantenha o trigger como um botão de
verdade, e quando o painel tiver um formulário, o leitor chega a ele pelo Tab a
partir do trigger.

## Referência da API
:::

<c-docs.api-reference name="popover" />

:::en
## Notes

Upstream aligns the content with `align` and measures the viewport to keep it
on screen. Here it is placed against the trigger with classes, without
collision detection.
:::pt-br
## Observações

O upstream alinha o conteúdo com `align` e mede a viewport para mantê-lo na
tela. Aqui ele é posicionado em relação ao trigger com classes, sem detecção de
colisão.
:::
