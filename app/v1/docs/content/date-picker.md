---
title: Date Picker
description: A date field for an ordinary Django form — a button that opens a calendar and a hidden input that carries the ISO date to the server.
description.pt-br: Um campo de data para um form Django comum — um botão que abre um calendário e um input escondido que leva a data ISO até o servidor.
description.es: Un campo de fecha para un formulario Django común — un botón que abre un calendario y un input oculto que lleva la fecha ISO al servidor.
---

<c-docs.demo-section class="min-h-[460px]">
<c-date-picker />
</c-docs.demo-section>

<p class="mt-4 text-sm text-muted-foreground">
    The button shows the date the way the active locale writes it. What goes to
    the server is the ISO date, in a hidden input.
</p>

## Installation

```bash
uvx django_shadcn@latest add date_picker
```

## Usage

```html
<form method="post">
    {% csrf_token %}
    <c-date-picker name="due_date" value="{{ form.due_date.value|date:'Y-m-d' }}" />
    <c-button type="submit">Save</c-button>
</form>
```

```python
class TaskForm(forms.Form):
    due_date = forms.DateField()
```

Nothing else is needed on the view side. The hidden input posts `2026-08-13`,
which is what `DateField` expects, and it already carries `value` before Alpine
has started — so a form that round-trips with errors keeps the date.

## One component, not a recipe

Upstream ships this as a recipe: a popover, a button and a calendar wired
together in the page, with `useState` in the middle holding the date.

Here it is one component, because the wiring is exactly the part a Django form
needs to get right. Two representations of the same date have to stay in step —
the ISO string the server parses and the human sentence the button shows — and
that is not something worth retyping per form.

Under it is still the same composition, and each piece can still be used on its
own: <a href="{% url 'page' slug='popover' %}">Popover</a>,
<a href="{% url 'page' slug='calendar' %}">Calendar</a> and
<a href="{% url 'page' slug='button' %}">Button</a>.

## Limiting the range

`min` and `max` are handed to the calendar, so the days outside the range are
dimmed and cannot be picked:

```html
<c-date-picker name="appointment" min="2026-08-10" max="2026-08-20" />
```

<c-docs.demo-section class="min-h-[460px]">
<c-date-picker min="2026-08-10" max="2026-08-20" placeholder="Within range" />
</c-docs.demo-section>

## Props

| Prop | Default | Meaning |
| --- | --- | --- |
| `name` | — | the name the hidden input posts under; leave it out for a display-only picker |
| `value` | — | the ISO date selected when the page loads |
| `placeholder` | `Pick a date` | the button's text while nothing is selected |
| `first_day` | the locale's | `0` for Sunday through `6` for Saturday |
| `min` | — | the earliest selectable ISO date |
| `max` | — | the latest selectable ISO date |

## Widening it

Upstream puts the width on the trigger. Here it is on the component itself, so
`class` can change it — a class handed to a component cannot reach an element
that component renders further in:

```html
<c-date-picker name="due_date" class="w-full" />
```

It is `w-[240px]` by default, as upstream.
