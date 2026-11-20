---
title: Resizable
description: Panels the reader can resize by dragging the divider.
description.pt-br: Painéis que o leitor redimensiona arrastando a divisa.
description.es: Paneles que se redimensionan arrastrando el divisor.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="h-[220px] w-[420px] rounded-lg border">
<c-resizable>
<c-resizable.panel default_size="1">
<div class="flex h-full items-center justify-center p-6 text-sm font-medium">One</div>
</c-resizable.panel>
<c-resizable.handle with_handle="true" />
<c-resizable.panel default_size="1">
<div class="flex h-full items-center justify-center p-6 text-sm font-medium">Two</div>
</c-resizable.panel>
</c-resizable>
</div>
</c-docs.demo-section>

<c-docs.cheat-sheet name="resizable">
<div class="h-[180px] w-[420px] rounded-lg border">
  <c-resizable>
    <c-resizable.panel>
      <div class="flex h-full items-center justify-center p-6 text-sm font-medium">Sidebar</div>
    </c-resizable.panel>
    <c-resizable.handle />
    <c-resizable.panel default_size="2">
      <div class="flex h-full items-center justify-center p-6 text-sm font-medium">Content</div>
    </c-resizable.panel>
  </c-resizable>
</div>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add resizable
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<div class="h-[180px] w-[420px] rounded-lg border">
  <c-resizable>
    <c-resizable.panel>
      <div class="flex h-full items-center justify-center p-6 text-sm font-medium">Sidebar</div>
    </c-resizable.panel>
    <c-resizable.handle />
    <c-resizable.panel default_size="2">
      <div class="flex h-full items-center justify-center p-6 text-sm font-medium">Content</div>
    </c-resizable.panel>
  </c-resizable>
</div>
</c-docs.example>

:::en
`default_size` is a share, not a percentage: two panels at `1` and `2` split
the space one third to two thirds. Dragging the handle moves that share between
the two panels either side of it and leaves the rest alone.

The group carries `h-full w-full` from the registry, so a `h-*` or `w-*` of
your own passed as `class` loses to it — two utilities for the same property
are settled by the compiled stylesheet. Size the wrapper and let the group
fill it.

## Examples

### Vertical
:::pt-br
`default_size` é uma proporção, não uma porcentagem: dois painéis com `1` e `2`
dividem o espaço em um terço e dois terços. Arrastar a alça move essa proporção
entre os dois painéis de cada lado dela e deixa o resto como está.

O grupo leva `h-full w-full` do registry, então um `h-*` ou `w-*` seu passado
como `class` perde para ele — dois utilitários para a mesma propriedade são
decididos pela folha de estilo compilada. Dimensione o elemento em volta e
deixe o grupo preenchê-lo.

## Exemplos

### Vertical
:::

<c-docs.example>
<div class="h-[260px] w-[420px] rounded-lg border">
  <c-resizable orientation="vertical">
    <c-resizable.panel>
      <div class="flex h-full items-center justify-center p-6 text-sm font-medium">Top</div>
    </c-resizable.panel>
    <c-resizable.handle with_handle="true" />
    <c-resizable.panel>
      <div class="flex h-full items-center justify-center p-6 text-sm font-medium">Bottom</div>
    </c-resizable.panel>
  </c-resizable>
</div>
</c-docs.example>

:::en
### Three panels
:::pt-br
### Três painéis
:::

<c-docs.example>
<div class="h-[200px] w-[520px] rounded-lg border">
  <c-resizable>
    <c-resizable.panel>
      <div class="flex h-full items-center justify-center p-4 text-sm font-medium">One</div>
    </c-resizable.panel>
    <c-resizable.handle />
    <c-resizable.panel default_size="2">
      <div class="flex h-full items-center justify-center p-4 text-sm font-medium">Two</div>
    </c-resizable.panel>
    <c-resizable.handle />
    <c-resizable.panel>
      <div class="flex h-full items-center justify-center p-4 text-sm font-medium">Three</div>
    </c-resizable.panel>
  </c-resizable>
</div>
</c-docs.example>

:::en
### Nested
:::pt-br
### Aninhados
:::

<c-docs.example>
<div class="h-[240px] w-[480px] rounded-lg border">
  <c-resizable>
    <c-resizable.panel>
      <div class="flex h-full items-center justify-center p-4 text-sm font-medium">Left</div>
    </c-resizable.panel>
    <c-resizable.handle with_handle="true" />
    <c-resizable.panel default_size="2">
      <div class="h-full">
        <c-resizable orientation="vertical">
          <c-resizable.panel>
            <div class="flex h-full items-center justify-center p-4 text-sm font-medium">Top right</div>
          </c-resizable.panel>
          <c-resizable.handle with_handle="true" />
          <c-resizable.panel>
            <div class="flex h-full items-center justify-center p-4 text-sm font-medium">Bottom right</div>
          </c-resizable.panel>
        </c-resizable>
      </div>
    </c-resizable.panel>
  </c-resizable>
</div>
</c-docs.example>

:::en
### Handle

`with_handle="true"` draws a grip on the divider, so it reads as something to drag.
:::pt-br
### Alça

`with_handle="true"` desenha um puxador no divisor, para ele parecer algo que se arrasta.
:::

<c-docs.example>
<div class="h-[180px] w-[420px] rounded-lg border">
  <c-resizable>
    <c-resizable.panel>
      <div class="flex h-full items-center justify-center p-6 text-sm font-medium">One</div>
    </c-resizable.panel>
    <c-resizable.handle with_handle="true" />
    <c-resizable.panel>
      <div class="flex h-full items-center justify-center p-6 text-sm font-medium">Two</div>
    </c-resizable.panel>
  </c-resizable>
</div>
</c-docs.example>

:::en
## RTL

Panels run with the text, so under `dir="rtl"` the first panel is on the
right. Dragging still moves the divider under the pointer.

## Accessibility

The handle is a `role="separator"` with `aria-orientation` and takes focus,
but it does not move with the keyboard yet: resizing needs a pointer.

## API reference
:::pt-br
## RTL

Os painéis correm com o texto, então sob `dir="rtl"` o primeiro painel fica à
direita. Arrastar continua movendo o divisor que está sob o ponteiro.

## Acessibilidade

A alça é um `role="separator"` com `aria-orientation` e recebe foco, mas
ainda não se move pelo teclado: redimensionar precisa de um ponteiro.

## Referência da API
:::

<c-docs.api-reference name="resizable" />

:::en
## Notes

The handle takes the pointer, not the keyboard: upstream lets you nudge a
divider with the arrow keys, and that is not here yet. It is focusable and
shows a focus ring, so the gap is visible rather than hidden.

Sizes are not remembered between visits. `react-resizable-panels` can persist a
layout by id; here a reload starts from `default_size` again.

Nothing enforces a minimum: a panel can be dragged shut. Give the content
inside it a `min-w-*` if that matters.
:::pt-br
## Observações

A alça responde ao ponteiro, não ao teclado: o upstream deixa você empurrar um
divisor com as setas, e isso ainda não está aqui. Ela recebe foco e mostra um
anel de foco, então a lacuna fica visível em vez de escondida.

Os tamanhos não são lembrados entre visitas. O `react-resizable-panels` pode
guardar um layout por id; aqui um recarregamento começa de novo do
`default_size`.

Nada impõe um mínimo: um painel pode ser arrastado até fechar. Dê ao conteúdo
dentro dele um `min-w-*` se isso importar.
:::
