---
title: Chart
description: Area, line, bar and pie, drawn from a queryset your view already has — no charting library, no npm, and the series follow your theme on their own.
description.pt-br: Área, linha, barra e pizza, desenhados a partir de um queryset que sua view já tem — sem biblioteca de gráficos, sem npm, e as séries seguem o seu tema sozinhas.
description.es: Área, línea, barra y tarta, dibujados desde un queryset que tu vista ya tiene — sin librería de gráficos, sin npm, y las series siguen tu tema solas.
---

<c-docs.demo-section class="min-h-[380px]">
<div class="w-full text-left">
<c-chart data='[{"month": "January", "revenue": 1200, "profit": 300}, {"month": "February", "revenue": 1800, "profit": 500}, {"month": "March", "revenue": 1500, "profit": 400}, {"month": "April", "revenue": 2400, "profit": 900}, {"month": "May", "revenue": 2100, "profit": 700}, {"month": "June", "revenue": 3000, "profit": 1100}]' config='{"revenue": {"label": "Revenue"}, "profit": {"label": "Profit"}}'>
<c-chart.plot label="Revenue and profit by month">
<c-chart.grid />
<c-chart.axis-y />
<c-chart.axis-x key="month" />
<c-chart.area data_key="revenue" />
<c-chart.area data_key="profit" />
</c-chart.plot>
<c-chart.tooltip />
<c-chart.legend />
</c-chart>
</div>
</c-docs.demo-section>

<p class="mt-4 text-sm text-muted-foreground">
    Move across it: the reading follows the pointer. Switch the site to dark and
    the two series change colour without a line of JavaScript running again.
</p>

## Installation

```bash
uvx django_shadcn@latest add chart
```

Nothing else. No npm package, no script tag: `scripts` is empty for this
component, and the drawing is done with SVG paths and positioned elements the
component writes itself.

## Usage

The view serialises; the template passes it on.

```python
import json

def dashboard(request):
    rows = (
        Order.objects
        .values('month')
        .annotate(revenue=Sum('total'), profit=Sum('margin'))
        .order_by('month')
    )
    return render(request, 'dashboard.html', {
        'series': json.dumps(list(rows)),
        'config': json.dumps({
            'revenue': {'label': 'Revenue'},
            'profit': {'label': 'Profit'},
        }),
    })
```

```html
<c-chart data="{{ series }}" config="{{ config }}">
    <c-chart.plot>
        <c-chart.grid />
        <c-chart.axis-y />
        <c-chart.axis-x key="month" />
        <c-chart.area data_key="revenue" />
    </c-chart.plot>
    <c-chart.tooltip />
    <c-chart.legend />
</c-chart>
```

**Do not put `|safe` on it.** The JSON has to reach the attribute escaped —
Django escapes it, the browser decodes it back, and the component reads the
decoded string. Marked safe, the first quote ends the attribute and the chart
gets nothing.

## The config

`config` maps a key in your rows to how it should be presented. It is the same
shape as upstream's:

```python
{
    'revenue': {'label': 'Revenue'},
    'profit': {'label': 'Profit', 'color': 'var(--chart-3)'},
}
```

Without a colour, a key takes the next of the five chart tokens in order.
Those tokens are defined in `input.css` for light and dark, which is why a
series changes colour when the site does and why a project that themes the
tokens themes the charts along with everything else.

Upstream writes a `<style>` block per chart to do this. A component that is only
a template cannot inject CSS, so the properties are set on the chart element
instead — the result is the same `--color-<key>` your own CSS can read.

## Anatomy

| Tag | What it is |
| --- | --- |
| `<c-chart>` | the data, the config, the colours and the shared scale |
| `<c-chart.plot>` | the drawing area, measured, and the pointer tracking |
| `<c-chart.grid>` | a line at each value on the y axis |
| `<c-chart.axis-y>` | the value ticks; claims its width from the plot |
| `<c-chart.axis-x>` | the category labels; claims its height from the plot |
| `<c-chart.area>` | a filled line, stackable |
| `<c-chart.line>` | a line, with or without dots |
| `<c-chart.bar>` | columns, grouped or stacked |
| `<c-chart.pie>` | pie or doughnut; polar, so it replaces the plot |
| `<c-chart.tooltip>` | the reading under the pointer |
| `<c-chart.legend>` | one entry per series, or per row for a pie |

Order matters inside the plot: the grid goes first so the series sit on top of
it.

## Bars

```html
<c-chart.plot>
    <c-chart.grid />
    <c-chart.axis-y />
    <c-chart.axis-x key="month" />
    <c-chart.bar data_key="revenue" />
    <c-chart.bar data_key="profit" />
</c-chart.plot>
```

<c-docs.demo-section class="min-h-[380px]">
<div class="w-full text-left">
<c-chart data='[{"month": "Jan", "revenue": 1200, "profit": 300}, {"month": "Feb", "revenue": 1800, "profit": 500}, {"month": "Mar", "revenue": 1500, "profit": 400}, {"month": "Apr", "revenue": 2400, "profit": 900}, {"month": "May", "revenue": 2100, "profit": 700}, {"month": "Jun", "revenue": 3000, "profit": 1100}]' config='{"revenue": {"label": "Revenue"}, "profit": {"label": "Profit"}}'>
<c-chart.plot label="Revenue and profit by month">
<c-chart.grid />
<c-chart.axis-y />
<c-chart.axis-x key="month" />
<c-chart.bar data_key="revenue" />
<c-chart.bar data_key="profit" />
</c-chart.plot>
<c-chart.tooltip />
<c-chart.legend />
</c-chart>
</div>
</c-docs.demo-section>

Two bar series share the category side by side. Add `stack="true"` to both and
they pile up instead, with the axis rescaling to the total:

<c-docs.demo-section class="min-h-[380px]">
<div class="w-full text-left">
<c-chart data='[{"month": "Jan", "revenue": 1200, "profit": 300}, {"month": "Feb", "revenue": 1800, "profit": 500}, {"month": "Mar", "revenue": 1500, "profit": 400}, {"month": "Apr", "revenue": 2400, "profit": 900}, {"month": "May", "revenue": 2100, "profit": 700}, {"month": "Jun", "revenue": 3000, "profit": 1100}]' config='{"revenue": {"label": "Revenue"}, "profit": {"label": "Profit"}}'>
<c-chart.plot label="Revenue and profit stacked by month">
<c-chart.grid />
<c-chart.axis-y />
<c-chart.axis-x key="month" />
<c-chart.bar data_key="revenue" stack="true" />
<c-chart.bar data_key="profit" stack="true" />
</c-chart.plot>
<c-chart.tooltip />
<c-chart.legend />
</c-chart>
</div>
</c-docs.demo-section>

`stack="true"` works the same way on `<c-chart.area>`.

## Lines

`<c-chart.line>` is the stroke without the fill. `dots="false"` drops the
points, which is what you want when the series is dense.

<c-docs.demo-section class="min-h-[380px]">
<div class="w-full text-left">
<c-chart data='[{"day": "Mon", "signups": 34, "trials": 12}, {"day": "Tue", "signups": 41, "trials": 18}, {"day": "Wed", "signups": 28, "trials": 9}, {"day": "Thu", "signups": 55, "trials": 24}, {"day": "Fri", "signups": 47, "trials": 21}, {"day": "Sat", "signups": 22, "trials": 7}, {"day": "Sun", "signups": 19, "trials": 5}]' config='{"signups": {"label": "Signups"}, "trials": {"label": "Trials"}}'>
<c-chart.plot label="Signups and trials by day">
<c-chart.grid />
<c-chart.axis-y />
<c-chart.axis-x key="day" />
<c-chart.line data_key="signups" />
<c-chart.line data_key="trials" />
</c-chart.plot>
<c-chart.tooltip />
<c-chart.legend />
</c-chart>
</div>
</c-docs.demo-section>

## Pie and doughnut

A pie is polar, so it replaces the plot rather than going inside it. Its config
is keyed by the row names, and the legend takes `name_key` to match:

```html
<c-chart data="{{ shares }}" config="{{ palette }}">
    <c-chart.pie data_key="visitors" name_key="browser" donut="true" />
    <c-chart.legend name_key="browser" />
</c-chart>
```

<c-docs.demo-section class="min-h-[380px]">
<div class="grid w-full gap-6 md:grid-cols-2">
<c-chart data='[{"browser": "Chrome", "visitors": 275}, {"browser": "Safari", "visitors": 200}, {"browser": "Firefox", "visitors": 187}, {"browser": "Edge", "visitors": 173}, {"browser": "Other", "visitors": 90}]' config='{"Chrome": {}, "Safari": {}, "Firefox": {}, "Edge": {}, "Other": {}}'>
<c-chart.pie data_key="visitors" name_key="browser" />
<c-chart.legend name_key="browser" />
</c-chart>
<c-chart data='[{"browser": "Chrome", "visitors": 275}, {"browser": "Safari", "visitors": 200}, {"browser": "Firefox", "visitors": 187}, {"browser": "Edge", "visitors": 173}, {"browser": "Other", "visitors": 90}]' config='{"Chrome": {}, "Safari": {}, "Firefox": {}, "Edge": {}, "Other": {}}'>
<c-chart.pie data_key="visitors" name_key="browser" donut="true" thickness="40" />
<c-chart.legend name_key="browser" />
</c-chart>
</div>
</c-docs.demo-section>

`thickness` is how many pixels wide the ring is, measured inwards from the edge.

## Sparklines

There is no sparkline component. A sparkline is this one with no grid and no
axes, and since each axis claims its own room, dropping them gives the line the
whole width:

```html
<c-chart data="{{ series }}" config="{{ config }}" class="aspect-auto h-12">
    <c-chart.plot>
        <c-chart.line data_key="revenue" dots="false" />
    </c-chart.plot>
</c-chart>
```

That is what sits inside a
<a href="{% url 'page' slug='metric' %}">Metric</a> card.

## Numbers follow the site's language

Ticks and readings are formatted with the language Django has active for the
request, not the one the visitor's browser is set to. The same page renders
`3,000` in English and `3.000` in Portuguese without being told twice.

## Props

| Prop | Where | Default | Meaning |
| --- | --- | --- | --- |
| `data` | `<c-chart>` | `[]` | the rows, as JSON |
| `config` | `<c-chart>` | `{}` | key to label and colour, as JSON |
| `label` | `<c-chart.plot>` | `Chart` | names the drawing for a screen reader |
| `key` | `<c-chart.axis-x>` | — | the field holding each row's name |
| `height` | `<c-chart.axis-x>` | `24` | pixels reserved at the bottom |
| `width` | `<c-chart.axis-y>` | `44` | pixels reserved at the left |
| `data_key` | series | — | the field this series draws |
| `stack` | `area`, `bar` | `false` | pile onto the series declared before it |
| `dots` | `line` | `true` | draw a point at each value |
| `donut` | `pie` | `false` | leave a hole in the middle |
| `thickness` | `pie` | `60` | how wide the ring is, in pixels |
| `name_key` | `pie`, `legend` | — | the field naming each row |

## Reading it from your own markup

Anything inside the chart can read its scope:

```html
<c-chart data="{{ series }}" config="{{ config }}">
    ...
    <p x-show="hovered >= 0" x-text="reading ? reading.month : ''"></p>
</c-chart>
```

`rows`, `series`, `hovered`, `reading`, `ticks` and `format(value)` are all
there.

## What this does not do

- **Nothing is drawn before Alpine starts.** The paths are computed from the
  measured width, and there is no width until the page is laid out. Every
  charting library works this way; the rest of this library does not, so it is
  worth knowing.
- **No zoom, brush or pan.**
- **No log scale, and no time axis that picks its own ticks.** The x axis is
  categorical: the view sends the label it wants shown.
- **Not for very large series.** A few thousand points is where positioned
  elements start to cost something. A KPI dashboard is nowhere near that.

If one of those is what you need, the honest answer is a charting library, and
the registry can declare one per component when the time comes.
