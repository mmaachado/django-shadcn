---
title: Calendar
description: A month grid for picking a date, with the month and weekday names coming from the locale Django has active for the request.
description.pt-br: Um grid de mês para escolher uma data, com os nomes de mês e de dia da semana vindos do locale que o Django tem ativo na requisição.
description.es: Una cuadrícula mensual para elegir una fecha, con los nombres de mes y de día de la semana tomados del locale que Django tiene activo en la petición.
---

<c-docs.demo-section>
<c-calendar class="rounded-md border" />
</c-docs.demo-section>

<c-docs.cheat-sheet name="calendar">
<c-calendar name="due_date" value="{{ form.due_date.value|date:'Y-m-d' }}" />
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add calendar
```

:::en
## Usage

With `name` set, the calendar is a form field on its own: it renders a hidden
input carrying the ISO date, so an ordinary Django form receives
`request.POST['due_date']` as `2026-08-13` and `forms.DateField` parses it
without help. `value` selects a date when the page loads, so a form that comes
back with errors keeps the choice.

The grid is drawn by Alpine from the calendar the browser already has, so it
needs JavaScript. Upstream hands it to `react-day-picker`; here there is no
library to hand it to, and a copied template carries no Python of its own.

What the browser does **not** decide is the language. It comes from Django,
so the month and weekday names follow the site's active language, not the
visitor's browser settings, and so does the first day of the week: `fr` starts
on Monday, `en-us` and `pt-br` on Sunday, `ar-eg` on Saturday.

For a field that opens on click instead of sitting on the page, use
[Date Picker]({% url 'page' slug='date-picker' %}), which is this calendar
inside a popover.
:::pt-br
## Uso

Com `name` definido, o calendário é um campo de formulário por conta própria:
ele renderiza um input oculto com a data ISO, então um formulário Django comum
recebe `request.POST['due_date']` como `2026-08-13` e o `forms.DateField` faz o
parse sem ajuda. `value` seleciona uma data quando a página carrega, então um
formulário que volta com erros mantém a escolha.

A grade é desenhada pelo Alpine a partir do calendário que o navegador já tem,
então precisa de JavaScript. O upstream a entrega ao `react-day-picker`; aqui
não há biblioteca a quem entregá-la, e um template copiado não traz Python
próprio.

O que o navegador **não** decide é o idioma. Ele vem do Django, então os nomes
dos meses e dos dias da semana seguem o idioma ativo do site, e não as
configurações do navegador de quem visita, e o primeiro dia da semana também:
`fr` começa na segunda, `en-us` e `pt-br` no domingo, `ar-eg` no sábado.

Para um campo que abre no clique em vez de ficar na página, use o
[Date Picker]({% url 'page' slug='date-picker' %}), que é este calendário
dentro de um popover.
:::

```html
<form method="post">
  {% csrf_token %}
  <c-calendar name="due_date" value="{{ form.due_date.value|date:'Y-m-d' }}" />
  <c-button>Save</c-button>
</form>
```

:::en
## Examples

### Basic
:::pt-br
## Exemplos

### Básico
:::

<c-docs.example>
<c-calendar value="2026-08-13" class="rounded-md border" />
</c-docs.example>

:::en
### Limiting the range

`min` and `max` take ISO dates. Days outside render dimmed and their buttons
are disabled, so they cannot be clicked or reached by keyboard.
:::pt-br
### Limitando o intervalo

`min` e `max` aceitam datas ISO. Os dias fora aparecem esmaecidos e os botões
deles ficam desabilitados, então não podem ser clicados nem alcançados pelo
teclado.
:::

<c-docs.example>
<c-calendar min="2026-08-10" max="2026-08-20" value="2026-08-13" class="rounded-md border" />
</c-docs.example>

:::en
### First day of the week

`first_day` overrides the locale, `0` for Sunday through `6` for Saturday, as
in Django's `FIRST_DAY_OF_WEEK`.
:::pt-br
### Primeiro dia da semana

`first_day` passa por cima do locale, de `0` para domingo até `6` para sábado,
como no `FIRST_DAY_OF_WEEK` do Django.
:::

<c-docs.example>
<c-calendar first_day="1" value="2026-08-13" class="rounded-md border" />
</c-docs.example>

:::en
### Reacting to a selection

Picking a day dispatches a bubbling `calendar-change` event carrying the ISO
date, which is how the date picker is built. The selection is also on the
Alpine scope as `selected`.
:::pt-br
### Reagindo a uma seleção

Escolher um dia dispara um evento `calendar-change` que borbulha e carrega a
data ISO, que é como o date picker é montado. A seleção também fica no escopo
do Alpine, como `selected`.
:::

<c-docs.example>
<div x-data="{ chosen: '' }" x-on:calendar-change="chosen = $event.detail.value" class="flex flex-col items-center gap-2">
  <c-calendar class="rounded-md border" />
  <p class="text-sm text-muted-foreground" x-text="chosen || 'Pick a day'"></p>
</div>
</c-docs.example>

:::en
## RTL

The weekdays run with the text, so under `dir="rtl"` the week starts on the
right, and the previous and next arrows change sides and turn to point
outwards.

## Accessibility

The month is a `role="grid"` table. Each day is a button labelled with its full
date and carrying `aria-selected`, and the month name is a live region, so
paging is announced. The previous and next buttons are labelled. Upstream also
moves between days with the arrow keys; here Tab moves through them, and
disabled days are skipped.

## API reference
:::pt-br
## RTL

Os dias da semana correm com o texto, então sob `dir="rtl"` a semana começa à
direita, e as setas de anterior e próximo trocam de lado e se viram para fora.

## Acessibilidade

O mês é uma tabela `role="grid"`. Cada dia é um botão rotulado com a data
completa e que leva `aria-selected`, e o nome do mês é uma região viva, então
trocar de mês é anunciado. Os botões de anterior e próximo têm rótulo. O
upstream também passa de um dia para o outro com as setas; aqui o Tab percorre
os dias, e os desabilitados ficam de fora.

## Referência da API
:::

<c-docs.api-reference name="calendar" />

:::en
## Notes

Upstream's range and multiple selection are not implemented. Half of a range
picker is worse than none, as it would look like the upstream component and
answer to a different set of rules. Single-date selection is faithful, and it
is what a Django form field needs. The examples built on ranges, the presets,
the date and time picker and the booked dates, have no counterpart for the
same reason; a set of disabled days beyond `min` and `max` is the one most
worth adding later.

The month and year dropdowns, week numbers, custom cell sizes and other
calendar systems such as Persian or Hijri are not here either. The dates are
plain ISO dates with no time zone, which is what `DateField` stores.
:::pt-br
## Observações

A seleção de intervalo e a múltipla do upstream não estão implementadas. Meio
seletor de intervalo é pior do que nenhum, porque pareceria o componente do
upstream e obedeceria a outras regras. A seleção de uma data só é fiel, e é o
que um campo de formulário Django precisa. Os exemplos que dependem de
intervalos, os presets, o seletor de data e hora e as datas reservadas, não têm
equivalente pelo mesmo motivo; um conjunto de dias desabilitados além de `min`
e `max` é o que mais vale acrescentar depois.

Os dropdowns de mês e ano, os números de semana, os tamanhos de célula
personalizados e outros sistemas de calendário, como o persa ou o hijri,
também não estão aqui. As datas são datas ISO simples, sem fuso horário, que é
o que o `DateField` guarda.
:::
