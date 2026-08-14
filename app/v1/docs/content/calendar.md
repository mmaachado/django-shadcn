---
title: Calendar
description: A month grid for picking a date, with the month and weekday names coming from the locale Django has active for the request.
description.pt-br: Um grid de mês para escolher uma data, com os nomes de mês e de dia da semana vindos do locale que o Django tem ativo na requisição.
description.es: Una cuadrícula mensual para elegir una fecha, con los nombres de mes y de día de la semana tomados del locale que Django tiene activo en la petición.
---

<c-docs.demo-section>
<c-calendar class="rounded-md border" />
</c-docs.demo-section>

<p class="mt-4 text-sm text-muted-foreground">
    Page the months, pick a day. Today is outlined; days from the neighbouring
    months are dimmed and still selectable.
</p>

## Installation

```bash
uvx django_shadcn@latest add calendar
```

## Usage

```html
<c-calendar name="due_date" value="{{ form.due_date.value|date:'Y-m-d' }}" />
```

With `name` set, the component is a form field on its own: it renders a hidden
input carrying the ISO date, so an ordinary Django form receives
`request.POST['due_date']` as `2026-08-13` and `forms.DateField` parses it
without any help.

For a field that opens on click instead of sitting on the page, use
<a href="{% url 'page' slug='date-picker' %}">Date Picker</a>, which is
this component inside a popover.

## Where the month grid comes from

Upstream hands the grid to `react-day-picker`. There is no library to hand it to
here, and a copied template carries no Python of its own, so the grid is built
from the calendar the browser already has.

What the browser does **not** decide is the language. That comes from Django:

```html
{% get_current_language as LANGUAGE_CODE %}
```

so the month and weekday names follow the site's active language, not the
visitor's browser settings. Switch the language and the same page renders
`agosto de 2026` or `août 2026`.

The first day of the week follows the same language. `fr` starts on Monday,
`en-us` and `pt-br` on Sunday, `ar-eg` on Saturday — without a setting to keep
in sync.

Set `first_day` when a project disagrees with its own locale:

```html
<c-calendar first_day="1" />
```

`0` is Sunday and `6` is Saturday, matching Django's `FIRST_DAY_OF_WEEK`.

## Limiting the range

```html
<c-calendar name="appointment" min="2026-08-10" max="2026-08-20" />
```

Days outside the range render dimmed and their buttons are disabled, so they
cannot be clicked or reached by keyboard.

<c-docs.demo-section>
<c-calendar min="2026-08-10" max="2026-08-20" value="2026-08-13" class="rounded-md border" />
</c-docs.demo-section>

## Reacting to a selection

Picking a day dispatches a bubbling `calendar-change` event carrying the ISO
date, which is how
<a href="{% url 'page' slug='date-picker' %}">Date Picker</a> is built:

```html
<div x-data="{ chosen: '' }" x-on:calendar-change="chosen = $event.detail.value">
    <c-calendar />
    <p x-text="chosen"></p>
</div>
```

The selection is also on the Alpine scope as `selected`.

## Props

| Prop | Default | Meaning |
| --- | --- | --- |
| `name` | — | renders a hidden input under this name; leave it out for a display-only calendar |
| `value` | — | the ISO date selected when the page loads |
| `first_day` | the locale's | `0` for Sunday through `6` for Saturday |
| `min` | — | the earliest selectable ISO date |
| `max` | — | the latest selectable ISO date |

## A note on what is not here

Range and multiple selection are not implemented. They have no behavioural
parity with `react-day-picker` in a grid this size, and half of a range picker
is worse than none — it would look like the upstream component and answer to a
different set of rules. Single-date selection is faithful, and it is what a
Django form field needs.
