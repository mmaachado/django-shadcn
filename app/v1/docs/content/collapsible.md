---
title: Collapsible
description: An interactive panel that expands and collapses.
description.pt-br: Um painel que expande e recolhe.
description.es: Un panel que se expande y se contrae.
---

<c-docs.demo-section class="min-h-[350px]">
<c-collapsible class="w-[350px] space-y-2">
<div class="flex items-center justify-between gap-4 px-4">
<h4 class="text-sm font-semibold">@mmaachado starred 3 repositories</h4>
<c-collapsible.trigger class="inline-flex size-8 items-center justify-center rounded-md hover:bg-accent" aria-label="Toggle">
<c-icon name="chevrons-up-down" class="size-4" />
</c-collapsible.trigger>
</div>
<div class="rounded-md border px-4 py-2 font-mono text-sm">django-shadcn</div>
<c-collapsible.content class="space-y-2">
<div class="rounded-md border px-4 py-2 font-mono text-sm">django-cotton</div>
<div class="rounded-md border px-4 py-2 font-mono text-sm">alpinejs</div>
</c-collapsible.content>
</c-collapsible>
</c-docs.demo-section>

<c-docs.cheat-sheet name="collapsible">
<c-collapsible>
  <c-collapsible.trigger>Show details</c-collapsible.trigger>
  <c-collapsible.content>{{ order.notes }}</c-collapsible.content>
</c-collapsible>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add collapsible
```

:::en
The height animates through Alpine's collapse plugin, `@alpinejs/collapse`,
which `add` names at the end of the run. Without it the panel still opens and
closes, just instantly.

## Usage

`open` is Alpine state on the root, so the trigger and the content both see it
without being told about each other. Start it open with `default_open="true"`.
The trigger is a `<button type="button">`, so it never submits a form around
it.

Without JavaScript the content stays hidden and the trigger does nothing, so
keep anything the reader must see outside it.
:::pt-br
A altura anima pelo plugin collapse do Alpine, o `@alpinejs/collapse`, que o
`add` cita no fim da execução. Sem ele o painel continua abrindo e fechando, só
que na hora.

## Uso

`open` é estado do Alpine na raiz, então o trigger e o conteúdo enxergam o
estado sem precisarem saber um do outro. Comece aberto com
`default_open="true"`. O trigger é um `<button type="button">`, então nunca
envia um formulário em volta dele.

Sem JavaScript o conteúdo fica escondido e o trigger não faz nada, então deixe
fora dele o que o leitor precisa ver.
:::

<c-docs.example>
<c-collapsible class="w-[350px]">
  <c-collapsible.trigger class="text-sm font-medium underline-offset-4 hover:underline">Order details</c-collapsible.trigger>
  <c-collapsible.content class="pt-2 text-sm text-muted-foreground">
    Shipped on 12 August to Rua das Flores, 120.
  </c-collapsible.content>
</c-collapsible>
</c-docs.example>

:::en
## Examples

### Open by default
:::pt-br
## Exemplos

### Aberto por padrão
:::

<c-docs.example>
<c-collapsible default_open="true" class="w-[350px]">
  <c-collapsible.trigger class="text-sm font-medium underline-offset-4 hover:underline">Shipping address</c-collapsible.trigger>
  <c-collapsible.content class="pt-2 text-sm text-muted-foreground">
    Rua das Flores, 120, São Paulo.
  </c-collapsible.content>
</c-collapsible>
</c-docs.example>

:::en
### Settings panel

Advanced options stay out of the way until asked for. The content shows the
open state through `data-state`, which the chevron reads to turn.
:::pt-br
### Painel de configurações

As opções avançadas ficam fora do caminho até serem pedidas. O conteúdo mostra
o estado de aberto pelo `data-state`, que o chevron lê para girar.
:::

<c-docs.example>
<c-collapsible class="w-[350px] rounded-md border p-4">
  <c-collapsible.trigger class="group flex w-full items-center justify-between text-sm font-medium">
    Advanced settings
    <c-icon name="chevron-down" class="size-4 transition-transform group-data-[state=open]:rotate-180" />
  </c-collapsible.trigger>
  <c-collapsible.content class="space-y-3 pt-4">
    <div class="flex items-center gap-2">
      <c-checkbox id="settings-cache" checked />
      <c-label for="settings-cache">Cache responses</c-label>
    </div>
    <div class="flex items-center gap-2">
      <c-checkbox id="settings-logs" />
      <c-label for="settings-logs">Keep debug logs</c-label>
    </div>
  </c-collapsible.content>
</c-collapsible>
</c-docs.example>

:::en
### File tree

Collapsibles nest, each folder with its own state.
:::pt-br
### Árvore de arquivos

Collapsibles se aninham, cada pasta com o próprio estado.
:::

<c-docs.example>
<div class="w-[280px] font-mono text-sm">
  <c-collapsible default_open="true">
    <c-collapsible.trigger class="group flex items-center gap-1">
      <c-icon name="chevron-right" class="size-4 transition-transform group-data-[state=open]:rotate-90" />
      <c-icon name="folder" class="size-4" />
      components
    </c-collapsible.trigger>
    <c-collapsible.content class="ps-5">
      <c-collapsible>
        <c-collapsible.trigger class="group flex items-center gap-1">
          <c-icon name="chevron-right" class="size-4 transition-transform group-data-[state=open]:rotate-90" />
          <c-icon name="folder" class="size-4" />
          button
        </c-collapsible.trigger>
        <c-collapsible.content class="ps-10">index.html</c-collapsible.content>
      </c-collapsible>
      <div class="ps-5">input.css</div>
    </c-collapsible.content>
  </c-collapsible>
</div>
</c-docs.example>

:::en
## RTL

The collapsible has no side of its own. A chevron that points right to mean
"closed", as in the file tree, needs `rtl:-scale-x-100` to point the other way
under `dir="rtl"`.

## Accessibility

The trigger is a `<button>` reporting `aria-expanded`, and the content is
hidden with `x-show` while closed, so it leaves the tab order and the reading
order. A trigger that holds only an icon needs an `aria-label`.

## API reference
:::pt-br
## RTL

O collapsible não tem um lado próprio. Um chevron que aponta para a direita
para dizer "fechado", como na árvore de arquivos, precisa de `rtl:-scale-x-100`
para apontar para o outro lado sob `dir="rtl"`.

## Acessibilidade

O trigger é um `<button>` que informa `aria-expanded`, e o conteúdo fica
escondido com `x-show` enquanto fechado, saindo da ordem de tab e da leitura.
Um trigger só com ícone precisa de um `aria-label`.

## Referência da API
:::

<c-docs.api-reference name="collapsible" />

:::en
## Notes

Upstream's controlled state hands `open` to the parent. Here the state is
Alpine's: read or set `open` from anything inside the root, or start it with
`default_open`.
:::pt-br
## Observações

O estado controlado do upstream entrega o `open` ao componente pai. Aqui o
estado é do Alpine: leia ou defina `open` a partir de qualquer coisa dentro da
raiz, ou comece com `default_open`.
:::
