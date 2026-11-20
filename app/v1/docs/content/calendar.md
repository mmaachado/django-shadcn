---
title: Calendar
description: A month grid for picking a date, with the month and weekday names coming from the locale Django has active for the request.
description.pt-br: Um grid de mês para escolher uma data, com os nomes de mês e de dia da semana vindos do locale que o Django tem ativo na requisição.
description.es: Una cuadrícula mensual para elegir una fecha, con los nombres de mes y de día de la semana tomados del locale que Django tiene activo en la petición.
---

<c-docs.demo-section>
<c-calendar class="rounded-md border" />
</c-docs.demo-section>

:::en
<p class="mt-4 text-sm text-muted-foreground">
    Page the months, pick a day. Today is outlined; days from the neighbouring
    months are dimmed and still selectable.
</p>

## Installation
:::pt-br
<p class="mt-4 text-sm text-muted-foreground">
    Passe os meses, escolha um dia. Hoje aparece contornado; os dias dos meses
    vizinhos aparecem esmaecidos e continuam selecionáveis.
</p>

## Instalação
:::

```bash
uvx django_shadcn@latest add calendar
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-calendar name="due_date" value="{{ form.due_date.value|date:'Y-m-d' }}" />
```

:::en
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
:::pt-br
Com `name` definido, o componente é um campo de formulário por conta própria:
ele renderiza um input oculto com a data ISO, então um formulário Django comum
recebe `request.POST['due_date']` como `2026-08-13` e o `forms.DateField` faz o
parse sem ajuda nenhuma.

Para um campo que abre no clique em vez de ficar na página, use o
<a href="{% url 'page' slug='date-picker' %}">Date Picker</a>, que é este
componente dentro de um popover.

## De onde vem a grade do mês

O upstream entrega a grade ao `react-day-picker`. Aqui não há biblioteca a quem
entregá-la, e um template copiado não traz Python próprio, então a grade é
montada a partir do calendário que o navegador já tem.

O que o navegador **não** decide é o idioma. Isso vem do Django:
:::

```html
{% get_current_language as LANGUAGE_CODE %}
```

:::en
so the month and weekday names follow the site's active language, not the
visitor's browser settings. Switch the language and the same page renders
`agosto de 2026` or `août 2026`.

The first day of the week follows the same language. `fr` starts on Monday,
`en-us` and `pt-br` on Sunday, `ar-eg` on Saturday — without a setting to keep
in sync.

Set `first_day` when a project disagrees with its own locale:
:::pt-br
então os nomes dos meses e dos dias da semana seguem o idioma ativo do site, e
não as configurações do navegador de quem visita. Troque o idioma e a mesma
página renderiza `agosto de 2026` ou `août 2026`.

O primeiro dia da semana segue o mesmo idioma. `fr` começa na segunda-feira,
`en-us` e `pt-br` no domingo, `ar-eg` no sábado — sem uma configuração para
manter em sincronia.

Defina `first_day` quando um projeto discordar do próprio locale:
:::

```html
<c-calendar first_day="1" />
```

:::en
`0` is Sunday and `6` is Saturday, matching Django's `FIRST_DAY_OF_WEEK`.

## Limiting the range
:::pt-br
`0` é domingo e `6` é sábado, como no `FIRST_DAY_OF_WEEK` do Django.

## Limitando o intervalo
:::

```html
<c-calendar name="appointment" min="2026-08-10" max="2026-08-20" />
```

:::en
Days outside the range render dimmed and their buttons are disabled, so they
cannot be clicked or reached by keyboard.
:::pt-br
Os dias fora do intervalo aparecem esmaecidos e os botões deles ficam
desabilitados, então não podem ser clicados nem alcançados pelo teclado.
:::

<c-docs.demo-section>
<c-calendar min="2026-08-10" max="2026-08-20" value="2026-08-13" class="rounded-md border" />
</c-docs.demo-section>

:::en
## Reacting to a selection

Picking a day dispatches a bubbling `calendar-change` event carrying the ISO
date, which is how
<a href="{% url 'page' slug='date-picker' %}">Date Picker</a> is built:
:::pt-br
## Reagindo a uma seleção

Escolher um dia dispara um evento `calendar-change` que borbulha e carrega a
data ISO, que é como o
<a href="{% url 'page' slug='date-picker' %}">Date Picker</a> é montado:
:::

```html
<div x-data="{ chosen: '' }" x-on:calendar-change="chosen = $event.detail.value">
    <c-calendar />
    <p x-text="chosen"></p>
</div>
```

:::en
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
:::pt-br
A seleção também fica no escopo do Alpine, como `selected`.

## Props

| Prop | Padrão | Significado |
| --- | --- | --- |
| `name` | — | renderiza um input oculto com este nome; deixe de fora para um calendário só de exibição |
| `value` | — | a data ISO selecionada quando a página carrega |
| `first_day` | a do locale | `0` para domingo até `6` para sábado |
| `min` | — | a data ISO mais cedo que pode ser escolhida |
| `max` | — | a data ISO mais tarde que pode ser escolhida |

## Sobre o que não está aqui

Seleção de intervalo e seleção múltipla não estão implementadas. Elas não têm
paridade de comportamento com o `react-day-picker` numa grade deste tamanho, e
meio seletor de intervalo é pior do que nenhum — ele pareceria o componente do
upstream e obedeceria a outras regras. A seleção de uma data só é fiel, e é o
que um campo de formulário Django precisa.
:::
