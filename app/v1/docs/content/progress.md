---
title: Progress
description: Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.
description.pt-br: Um indicador do quanto de uma tarefa já foi concluído.
description.es: Un indicador de cuánto de una tarea se ha completado.
---

<c-docs.demo-section class="min-h-[350px]">
<c-progress value="60" class="w-[60%]" aria-label="Upload" />
</c-docs.demo-section>

<c-docs.cheat-sheet name="progress">
<c-progress value="{{ task.percent }}" aria-label="{{ task.name }}" />
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add progress
```

:::en
## Usage

The bar fills to `value` out of `max`, 100 by default. The width is worked out
on the server with `widthratio`, so the bar is right before any JavaScript
runs and needs none. For progress that moves, render the bar again: an htmx
poll that swaps it every second is enough.
:::pt-br
## Uso

A barra se preenche até `value` de um total de `max`, 100 por padrão. A largura
é calculada no servidor com o `widthratio`, então a barra já está certa antes de
qualquer JavaScript rodar e não precisa de nenhum. Para um progresso que anda,
renderize a barra de novo: um poll do htmx que a troca a cada segundo basta.
:::

```html
<div hx-get="{% url 'task-progress' task.pk %}" hx-trigger="every 1s" hx-swap="outerHTML">
  <c-progress value="{{ task.done }}" max="{{ task.total }}" aria-label="Import" />
</div>
```

:::en
## Examples

### Label
:::pt-br
## Exemplos

### Rótulo
:::

<c-docs.example>
<div class="grid w-full max-w-sm gap-2">
  <div class="flex justify-between text-sm">
    <span id="progress-upload">Uploading</span>
    <span class="text-muted-foreground tabular-nums">66%</span>
  </div>
  <c-progress value="66" aria-labelledby="progress-upload" />
</div>
</c-docs.example>

:::en
### Out of a total

`max` sets the total, so a count can go straight in.
:::pt-br
### De um total

O `max` define o total, então uma contagem entra direto.
:::

<c-docs.example>
<c-progress value="3" max="8" class="max-w-sm" aria-label="Steps done" />
</c-docs.example>

:::en
## RTL

The bar fills from the start, so under `dir="rtl"` it grows from the right.

## Accessibility

It is a `role="progressbar"` with `aria-valuenow`, `aria-valuemin` and
`aria-valuemax`, so a screen reader announces how far along it is. Name it with
`aria-label`, or with `aria-labelledby` pointing at a visible label.

## API reference
:::pt-br
## RTL

A barra se preenche a partir do início, então sob `dir="rtl"` ela cresce a
partir da direita.

## Acessibilidade

É um `role="progressbar"` com `aria-valuenow`, `aria-valuemin` e
`aria-valuemax`, então um leitor de tela anuncia o quanto andou. Dê um nome a
ele com `aria-label`, ou com `aria-labelledby` apontando para um rótulo
visível.

## Referência da API
:::

<c-docs.api-reference name="progress" />

:::en
## Notes

Upstream's controlled example animates the value from React state. Here the
value is rendered by the server; swap the bar to move it.
:::pt-br
## Observações

O exemplo controlado do upstream anima o valor a partir do estado do React.
Aqui o valor é renderizado pelo servidor; troque a barra para movê-lo.
:::
