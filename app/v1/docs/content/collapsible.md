---
title: Collapsible
description: An interactive panel that expands and collapses.
description.pt-br: Um painel que expande e recolhe.
description.es: Un panel que se expande y se contrae.
---

<c-docs.demo-section class="min-h-[350px]">
<c-collapsible class="w-[350px] text-start">
<div class="flex items-center justify-between gap-4 px-1">
<h4 class="text-sm font-semibold">@mmaachado starred 3 repositories</h4>
<c-collapsible.trigger class="inline-flex size-8 items-center justify-center rounded-md hover:bg-accent">
<c-icon name="chevrons-up-down" class="size-4" />
<span class="sr-only">Toggle</span>
</c-collapsible.trigger>
</div>
<div class="mt-2 rounded-md border px-4 py-3 font-mono text-sm">django-shadcn</div>
<c-collapsible.content class="space-y-2">
<div class="mt-2 rounded-md border px-4 py-3 font-mono text-sm">django-cotton</div>
<div class="rounded-md border px-4 py-3 font-mono text-sm">tailwindcss</div>
</c-collapsible.content>
</c-collapsible>
</c-docs.demo-section>

<c-docs.cheat-sheet name="collapsible">
<c-collapsible class="w-[350px] text-start">
  <c-collapsible.trigger class="inline-flex h-9 items-center rounded-md border px-4 text-sm font-medium hover:bg-accent">
    Show details
  </c-collapsible.trigger>
  <c-collapsible.content>
    <p class="mt-2 rounded-md border px-4 py-3 text-sm text-muted-foreground">
      Everything you were not looking at a moment ago.
    </p>
  </c-collapsible.content>
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
<p class="mt-4 text-sm text-muted-foreground">
    <strong>Note:</strong> This component requires the <a href="https://alpinejs.dev/plugins/collapse" target="_blank" rel="noopener noreferrer" class="underline">Alpine.js Collapse plugin</a> for animations. Without it the panel still opens and closes, without the transition.
</p>

## Usage
:::pt-br
<p class="mt-4 text-sm text-muted-foreground">
    <strong>Observação:</strong> este componente precisa do <a href="https://alpinejs.dev/plugins/collapse" target="_blank" rel="noopener noreferrer" class="underline">plugin Collapse do Alpine.js</a> para as animações. Sem ele o painel continua abrindo e fechando, só que sem a transição.
</p>

## Uso
:::

<c-docs.example>
<c-collapsible class="w-[350px] text-start">
  <c-collapsible.trigger class="inline-flex h-9 items-center rounded-md border px-4 text-sm font-medium hover:bg-accent">
    Show details
  </c-collapsible.trigger>
  <c-collapsible.content>
    <p class="mt-2 rounded-md border px-4 py-3 text-sm text-muted-foreground">
      Everything you were not looking at a moment ago.
    </p>
  </c-collapsible.content>
</c-collapsible>
</c-docs.example>

:::en
`open` is Alpine state on the root, so the trigger and the content both see it
without being told about each other. Start it expanded with
`default_open="true"`.

## Examples

### Open by default
:::pt-br
`open` é estado do Alpine na raiz, então o trigger e o conteúdo enxergam o
estado sem precisarem saber um do outro. Comece aberto com
`default_open="true"`.

## Exemplos

### Aberto por padrão
:::

<c-docs.example>
<c-collapsible default_open="true" class="w-[350px] text-start">
  <c-collapsible.trigger class="inline-flex h-9 items-center rounded-md border px-4 text-sm font-medium hover:bg-accent">
    Already open
  </c-collapsible.trigger>
  <c-collapsible.content>
    <p class="mt-2 rounded-md border px-4 py-3 text-sm text-muted-foreground">
      Visible from the first paint.
    </p>
  </c-collapsible.content>
</c-collapsible>
</c-docs.example>

:::en
## Notes

The height animation comes from Alpine's `collapse` plugin, the same one the
accordion uses. Without it the panel still opens and closes, just instantly.
:::pt-br
## Observações

A animação de altura vem do plugin `collapse` do Alpine, o mesmo que o accordion
usa. Sem ele o painel continua abrindo e fechando, só que na hora.
:::

:::en
## API reference
:::pt-br
## Referência da API
:::

<c-docs.api-reference name="collapsible" />
