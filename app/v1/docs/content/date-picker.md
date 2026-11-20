---
title: Date Picker
description: A date field for an ordinary Django form — a button that opens a calendar and a hidden input that carries the ISO date to the server.
description.pt-br: Um campo de data para um form Django comum — um botão que abre um calendário e um input escondido que leva a data ISO até o servidor.
description.es: Un campo de fecha para un formulario Django común — un botón que abre un calendario y un input oculto que lleva la fecha ISO al servidor.
---

<c-docs.demo-section class="min-h-[460px]">
<c-date-picker />
</c-docs.demo-section>

:::en
<p class="mt-4 text-sm text-muted-foreground">
    The button shows the date the way the active locale writes it. What goes to
    the server is the ISO date, in a hidden input.
</p>

## Installation
:::pt-br
<p class="mt-4 text-sm text-muted-foreground">
    O botão mostra a data do jeito que o locale ativo a escreve. O que vai para
    o servidor é a data ISO, num input oculto.
</p>

## Instalação
:::

```bash
uvx django_shadcn@latest add date_picker
```

:::en
## Usage
:::pt-br
## Uso
:::

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

:::en
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
:::pt-br
Não é preciso mais nada do lado da view. O input oculto envia `2026-08-13`, que
é o que o `DateField` espera, e ele já leva `value` antes de o Alpine começar —
então um formulário que volta com erros mantém a data.

## Um componente, não uma receita

O upstream entrega isto como uma receita: um popover, um botão e um calendário
ligados na página, com um `useState` no meio guardando a data.

Aqui é um componente só, porque a ligação é exatamente a parte que um
formulário Django precisa acertar. Duas representações da mesma data têm de
andar juntas — a string ISO que o servidor interpreta e a frase legível que o
botão mostra — e isso não vale a pena digitar de novo em cada formulário.

Por baixo continua a mesma composição, e cada peça ainda pode ser usada
sozinha: <a href="{% url 'page' slug='popover' %}">Popover</a>,
<a href="{% url 'page' slug='calendar' %}">Calendar</a> e
<a href="{% url 'page' slug='button' %}">Button</a>.

## Limitando o intervalo

`min` e `max` são repassados ao calendário, então os dias fora do intervalo
aparecem esmaecidos e não podem ser escolhidos:
:::

```html
<c-date-picker name="appointment" min="2026-08-10" max="2026-08-20" />
```

<c-docs.demo-section class="min-h-[460px]">
<c-date-picker min="2026-08-10" max="2026-08-20" placeholder="Within range" />
</c-docs.demo-section>

:::en
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
:::pt-br
## Props

| Prop | Padrão | Significado |
| --- | --- | --- |
| `name` | — | o nome com que o input oculto é enviado; deixe de fora para um seletor só de exibição |
| `value` | — | a data ISO selecionada quando a página carrega |
| `placeholder` | `Pick a date` | o texto do botão enquanto nada está selecionado |
| `first_day` | a do locale | `0` para domingo até `6` para sábado |
| `min` | — | a data ISO mais cedo que pode ser escolhida |
| `max` | — | a data ISO mais tarde que pode ser escolhida |

## Deixando mais largo

O upstream põe a largura no trigger. Aqui ela fica no próprio componente, para
que `class` possa mudá-la — uma classe passada a um componente não alcança um
elemento que o componente renderiza mais para dentro:
:::

```html
<c-date-picker name="due_date" class="w-full" />
```

:::en
It is `w-[240px]` by default, as upstream.
:::pt-br
É `w-[240px]` por padrão, como no upstream.
:::

:::en
## API reference
:::pt-br
## Referência da API
:::

<c-docs.api-reference name="date-picker" />
