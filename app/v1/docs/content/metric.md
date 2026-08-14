---
title: Metric
description: The big number a KPI dashboard is made of — a label, a value, a change that knows its own direction, and room for a sparkline.
description.pt-br: O número grande de que um dashboard de KPI é feito — um rótulo, um valor, uma variação que sabe a própria direção e espaço para um sparkline.
description.es: El número grande del que está hecho un dashboard de KPI — una etiqueta, un valor, una variación que conoce su propia dirección y sitio para un sparkline.
---

<c-docs.demo-section>
<div class="grid w-full gap-6 text-left md:grid-cols-3">
<c-metric>
<c-metric.label>Revenue</c-metric.label>
<c-metric.value>$45,231.89</c-metric.value>
<c-metric.delta value="+20.1%" label="vs. last month" />
<c-chart data='[{"m": 1, "v": 900}, {"m": 2, "v": 1400}, {"m": 3, "v": 1100}, {"m": 4, "v": 1900}, {"m": 5, "v": 1700}, {"m": 6, "v": 2400}]' config='{"v": {"label": "Revenue"}}' class="aspect-auto h-12">
<c-chart.plot label="Revenue trend">
<c-chart.line data_key="v" dots="false" />
</c-chart.plot>
</c-chart>
</c-metric>
<c-metric>
<c-metric.label>Churn</c-metric.label>
<c-metric.value>2.4%</c-metric.value>
<c-metric.delta value="-1.2%" label="vs. last month" />
</c-metric>
<c-metric>
<c-metric.label>Open tickets</c-metric.label>
<c-metric.value>18</c-metric.value>
<c-metric.delta value="0" label="no change" />
</c-metric>
</div>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add metric
```

## Not from shadcn/ui

There is no metric in the upstream registry. This one exists because a KPI
dashboard is mostly this card repeated, and building it out of
<a href="{% url 'page' slug='card' %}">Card</a> every time meant retyping the
same four elements — including the only part with a rule in it, which is the
delta working out its own arrow and colour.

Everything else here is ordinary typography. If you would rather compose it
yourself, `card` and `badge` will get you the same place.

## Usage

```html
<c-metric>
    <c-metric.label>Revenue</c-metric.label>
    <c-metric.value>{{ revenue|floatformat:2 }}</c-metric.value>
    <c-metric.delta value="{{ change }}" label="vs. last month" />
</c-metric>
```

## The delta reads its own sign

`value` is shown as it arrives, and the sign in it picks the icon and the
colour — on the server, so the card is right before any JavaScript runs.

| `value` | Icon | Colour |
| --- | --- | --- |
| starts with `-` | trending down | `text-destructive` |
| exactly `0` | a dash | `text-muted-foreground` |
| anything else | trending up | `text-foreground` |

Up is not green. There is no green in the palette, and this is not the place to
invent one — a project that wants it passes it in:

```html
<c-metric.delta value="+20.1%" class="text-emerald-600 dark:text-emerald-400" />
```

Note that a value going up is not always good news. Churn rising is a bad month
with an up arrow, which is why the component states the direction and leaves the
judgement to you.

## With a sparkline

A sparkline is <a href="{% url 'page' slug='chart' %}">Chart</a> with no grid
and no axes. Each axis claims its own room, so leaving them out gives the line
the whole width of the card:

```html
<c-metric>
    <c-metric.label>Revenue</c-metric.label>
    <c-metric.value>$45,231.89</c-metric.value>
    <c-metric.delta value="+20.1%" label="vs. last month" />
    <c-chart data="{{ trend }}" config="{{ config }}" class="aspect-auto h-12">
        <c-chart.plot>
            <c-chart.line data_key="revenue" dots="false" />
        </c-chart.plot>
    </c-chart>
</c-metric>
```

## Anatomy

| Tag | What it is |
| --- | --- |
| `<c-metric>` | the card |
| `<c-metric.label>` | what is being measured |
| `<c-metric.value>` | the number, in tabular figures so a row of cards lines up |
| `<c-metric.delta>` | the change, with its arrow |

## Props

| Prop | Where | Default | Meaning |
| --- | --- | --- | --- |
| `value` | `<c-metric.delta>` | — | the change, shown as given; its sign picks the arrow |
| `label` | `<c-metric.delta>` | — | the quiet text after it, such as the period compared |
