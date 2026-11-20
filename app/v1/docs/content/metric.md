---
title: Metric
description: The big number a KPI dashboard is made of — a label, a value, a change that knows its own direction, and room for a sparkline.
description.pt-br: O número grande de que um dashboard de KPI é feito — um rótulo, um valor, uma variação que sabe a própria direção e espaço para um sparkline.
description.es: El número grande del que está hecho un dashboard de KPI — una etiqueta, un valor, una variación que conoce su propia dirección y sitio para un sparkline.
---

<c-docs.demo-section>
<div class="grid w-full gap-6 text-start md:grid-cols-3">
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

<c-docs.cheat-sheet name="metric">
<c-metric>
    <c-metric.label>Revenue</c-metric.label>
    <c-metric.value>{{ revenue|floatformat:2 }}</c-metric.value>
    <c-metric.delta value="{{ change }}" label="vs. last month" />
</c-metric>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add metric
```

:::en
## Not from shadcn/ui

There is no metric in the upstream registry. This one exists because a KPI
dashboard is mostly this card repeated, and building it out of
<a href="{% url 'page' slug='card' %}">Card</a> every time meant retyping the
same four elements — including the only part with a rule in it, which is the
delta working out its own arrow and colour.

Everything else here is ordinary typography. If you would rather compose it
yourself, `card` and `badge` will get you the same place.

## Usage
:::pt-br
## Não vem do shadcn/ui

Não há metric no registry do upstream. Este existe porque um dashboard de KPI é,
na maior parte, este card repetido, e montá-lo a partir do
<a href="{% url 'page' slug='card' %}">Card</a> toda vez significava digitar de
novo os mesmos quatro elementos — incluindo a única parte com uma regra, que é a
variação descobrindo a própria seta e a própria cor.

Todo o resto aqui é tipografia comum. Se preferir montar você mesmo, `card` e
`badge` levam ao mesmo lugar.

## Uso
:::

```html
<c-metric>
    <c-metric.label>Revenue</c-metric.label>
    <c-metric.value>{{ revenue|floatformat:2 }}</c-metric.value>
    <c-metric.delta value="{{ change }}" label="vs. last month" />
</c-metric>
```

:::en
## Examples

### The delta reads its own sign

`value` is shown as it arrives, and the sign in it picks the icon and the
colour — on the server, so the card is right before any JavaScript runs.

| `value` | Icon | Colour |
| --- | --- | --- |
| starts with `-` | trending down | `text-destructive` |
| exactly `0` | a dash | `text-muted-foreground` |
| anything else | trending up | `text-foreground` |

Up is not green. There is no green in the palette, and this is not the place to
invent one — a project that wants it passes it in:
:::pt-br
## Exemplos

### A variação lê o próprio sinal

`value` é mostrado como chega, e o sinal nele escolhe o ícone e a cor — no
servidor, então o card já está certo antes de qualquer JavaScript rodar.

| `value` | Ícone | Cor |
| --- | --- | --- |
| começa com `-` | em queda | `text-destructive` |
| exatamente `0` | um traço | `text-muted-foreground` |
| qualquer outra coisa | em alta | `text-foreground` |

Subir não é verde. Não há verde na paleta, e aqui não é o lugar de inventar um —
um projeto que o queira passa a cor:
:::

```html
<c-metric.delta value="+20.1%" class="text-emerald-600 dark:text-emerald-400" />
```

:::en
Note that a value going up is not always good news. Churn rising is a bad month
with an up arrow, which is why the component states the direction and leaves the
judgement to you.

### With a sparkline

A sparkline is <a href="{% url 'page' slug='chart' %}">Chart</a> with no grid
and no axes. Each axis claims its own room, so leaving them out gives the line
the whole width of the card:
:::pt-br
Repare que um valor subindo nem sempre é boa notícia. Churn em alta é um mês
ruim com uma seta para cima, e é por isso que o componente informa a direção e
deixa o julgamento com você.

### Com um sparkline

Um sparkline é o <a href="{% url 'page' slug='chart' %}">Chart</a> sem grade e
sem eixos. Cada eixo reserva o próprio espaço, então deixá-los de fora dá à
linha a largura inteira do card:
:::

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

:::en
## RTL

The label, the value and the delta align to the start, so a card mirrors under
`dir="rtl"`. The trend arrow does not turn: up is up in every language.

## Accessibility

The card is text read in order: the label, the value, then the delta. The
delta's arrow and colour are not read, so its sign has to be in the value, as
in `+20.1%`, and the label after it says what it is compared with.

## API reference
:::pt-br
## RTL

O rótulo, o valor e a variação se alinham ao início, então um card espelha sob
`dir="rtl"`. A seta de tendência não vira: para cima é para cima em qualquer
idioma.

## Acessibilidade

O card é texto lido em ordem: o rótulo, o valor e depois a variação. A seta e
a cor da variação não são lidas, então o sinal tem de estar no valor, como em
`+20.1%`, e o rótulo depois dele diz com o que se compara.

## Referência da API
:::

<c-docs.api-reference name="metric" />

:::en
## Notes

**Anatomy.**

| Tag | What it is |
| --- | --- |
| `<c-metric>` | the card |
| `<c-metric.label>` | what is being measured |
| `<c-metric.value>` | the number, in tabular figures so a row of cards lines up |
| `<c-metric.delta>` | the change, with its arrow |

**What the attributes mean.**

| Prop | Where | Default | Meaning |
| --- | --- | --- | --- |
| `value` | `<c-metric.delta>` | — | the change, shown as given; its sign picks the arrow |
| `label` | `<c-metric.delta>` | — | the quiet text after it, such as the period compared |
:::pt-br
## Observações

**Anatomia.**

| Tag | O que é |
| --- | --- |
| `<c-metric>` | o card |
| `<c-metric.label>` | o que está sendo medido |
| `<c-metric.value>` | o número, em algarismos tabulares para que uma fileira de cards se alinhe |
| `<c-metric.delta>` | a variação, com a seta |

**O que os atributos significam.**

| Prop | Onde | Padrão | Significado |
| --- | --- | --- | --- |
| `value` | `<c-metric.delta>` | — | a variação, mostrada como veio; o sinal escolhe a seta |
| `label` | `<c-metric.delta>` | — | o texto discreto depois dela, como o período comparado |
:::
