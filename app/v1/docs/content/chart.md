---
title: Chart
description: Area, line, bar and pie, drawn from a queryset your view already has — no charting library, no npm, and the series follow your theme on their own.
description.pt-br: Área, linha, barra e pizza, desenhados a partir de um queryset que sua view já tem — sem biblioteca de gráficos, sem npm, e as séries seguem o seu tema sozinhas.
description.es: Área, línea, barra y tarta, dibujados desde un queryset que tu vista ya tiene — sin librería de gráficos, sin npm, y las series siguen tu tema solas.
---

<c-docs.demo-section class="min-h-[380px]">
<div class="w-full text-start">
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

<c-docs.cheat-sheet name="chart">
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
</c-docs.cheat-sheet>

:::en
<p class="mt-4 text-sm text-muted-foreground">
    Move across it: the reading follows the pointer. Switch the site to dark and
    the two series change colour without a line of JavaScript running again.
</p>

## Installation
:::pt-br
<p class="mt-4 text-sm text-muted-foreground">
    Passe o ponteiro por ele: a leitura acompanha o ponteiro. Mude o site para o
    tema escuro e as duas séries trocam de cor sem nenhuma linha de JavaScript
    rodar de novo.
</p>

## Instalação
:::

```bash
uvx django_shadcn@latest add chart
```

:::en
Nothing else. No npm package, no script tag: `scripts` is empty for this
component, and the drawing is done with SVG paths and positioned elements the
component writes itself.

## Usage

The view serialises; the template passes it on.
:::pt-br
Mais nada. Nenhum pacote npm, nenhuma tag de script: `scripts` está vazio para
este componente, e o desenho é feito com paths SVG e elementos posicionados que
o próprio componente escreve.

## Uso

A view serializa; o template repassa.
:::

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

:::en
**Do not put `|safe` on it.** The JSON has to reach the attribute escaped —
Django escapes it, the browser decodes it back, and the component reads the
decoded string. Marked safe, the first quote ends the attribute and the chart
gets nothing.

## The config

`config` maps a key in your rows to how it should be presented. It is the same
shape as upstream's:
:::pt-br
**Não coloque `|safe` nele.** O JSON precisa chegar escapado ao atributo — o
Django escapa, o navegador decodifica de volta e o componente lê a string
decodificada. Marcado como seguro, a primeira aspa encerra o atributo e o
gráfico não recebe nada.

## O config

`config` liga uma chave das suas linhas a como ela deve ser apresentada. É o
mesmo formato do upstream:
:::

```python
{
    'revenue': {'label': 'Revenue'},
    'profit': {'label': 'Profit', 'color': 'var(--chart-3)'},
}
```

:::en
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

## Examples

### Bars
:::pt-br
Sem uma cor, uma chave recebe o próximo dos cinco tokens de gráfico, em ordem.
Esses tokens são definidos no `input.css` para o claro e o escuro, e é por isso
que uma série muda de cor quando o site muda, e que um projeto que personaliza
os tokens personaliza os gráficos junto com todo o resto.

O upstream escreve um bloco `<style>` por gráfico para fazer isso. Um
componente que é só um template não pode injetar CSS, então as propriedades são
definidas no elemento do gráfico — o resultado é o mesmo `--color-<key>` que o
seu próprio CSS pode ler.

## Anatomia

| Tag | O que é |
| --- | --- |
| `<c-chart>` | os dados, o config, as cores e a escala compartilhada |
| `<c-chart.plot>` | a área de desenho, medida, e o rastreio do ponteiro |
| `<c-chart.grid>` | uma linha em cada valor do eixo y |
| `<c-chart.axis-y>` | as marcas de valor; reserva a própria largura no plot |
| `<c-chart.axis-x>` | os rótulos das categorias; reserva a própria altura no plot |
| `<c-chart.area>` | uma linha preenchida, empilhável |
| `<c-chart.line>` | uma linha, com ou sem pontos |
| `<c-chart.bar>` | colunas, agrupadas ou empilhadas |
| `<c-chart.pie>` | pizza ou rosca; polar, então substitui o plot |
| `<c-chart.tooltip>` | a leitura sob o ponteiro |
| `<c-chart.legend>` | uma entrada por série, ou por linha numa pizza |

A ordem importa dentro do plot: a grade vem primeiro para que as séries fiquem
por cima dela.

## Exemplos

### Barras
:::

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
<div class="w-full text-start">
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

:::en
Two bar series share the category side by side. Add `stack="true"` to both and
they pile up instead, with the axis rescaling to the total:
:::pt-br
Duas séries de barras dividem a categoria lado a lado. Acrescente
`stack="true"` às duas e elas se empilham, com o eixo se ajustando ao total:
:::

<c-docs.demo-section class="min-h-[380px]">
<div class="w-full text-start">
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

:::en
`stack="true"` works the same way on `<c-chart.area>`.

### Lines

`<c-chart.line>` is the stroke without the fill. `dots="false"` drops the
points, which is what you want when the series is dense.
:::pt-br
`stack="true"` funciona do mesmo jeito no `<c-chart.area>`.

### Linhas

`<c-chart.line>` é o traço sem o preenchimento. `dots="false"` tira os pontos,
que é o que você quer quando a série é densa.
:::

<c-docs.demo-section class="min-h-[380px]">
<div class="w-full text-start">
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

:::en
### Pie and doughnut

A pie is polar, so it replaces the plot rather than going inside it. Its config
is keyed by the row names, and the legend takes `name_key` to match:
:::pt-br
### Pizza e rosca

Uma pizza é polar, então ela substitui o plot em vez de ir dentro dele. O config
dela é indexado pelos nomes das linhas, e a legenda recebe `name_key` para
combinar:
:::

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

:::en
`thickness` is how many pixels wide the ring is, measured inwards from the edge.

### Sparklines

There is no sparkline component. A sparkline is this one with no grid and no
axes, and since each axis claims its own room, dropping them gives the line the
whole width:
:::pt-br
`thickness` é quantos pixels de largura o anel tem, medidos da borda para
dentro.

### Sparklines

Não existe um componente de sparkline. Um sparkline é este sem grade e sem
eixos, e como cada eixo reserva o próprio espaço, tirá-los dá à linha a largura
inteira:
:::

```html
<c-chart data="{{ series }}" config="{{ config }}" class="aspect-auto h-12">
    <c-chart.plot>
        <c-chart.line data_key="revenue" dots="false" />
    </c-chart.plot>
</c-chart>
```

:::en
That is what sits inside a
<a href="{% url 'page' slug='metric' %}">Metric</a> card.

### Numbers follow the site's language

Ticks and readings are formatted with the language Django has active for the
request, not the one the visitor's browser is set to. The same page renders
`3,000` in English and `3.000` in Portuguese without being told twice.


### Reading it from your own markup

Anything inside the chart can read its scope:
:::pt-br
É isso que fica dentro de um card de
<a href="{% url 'page' slug='metric' %}">Metric</a>.

### Os números seguem o idioma do site

As marcas e as leituras são formatadas com o idioma que o Django tem ativo na
requisição, não com o que o navegador de quem visita usa. A mesma página
renderiza `3,000` em inglês e `3.000` em português sem precisar de aviso.


### Lendo do seu próprio markup

Qualquer coisa dentro do gráfico pode ler o escopo dele:
:::

```html
<c-chart data="{{ series }}" config="{{ config }}">
    ...
    <p x-show="hovered >= 0" x-text="reading ? reading.month : ''"></p>
</c-chart>
```

:::en
`rows`, `series`, `hovered`, `reading`, `ticks` and `format(value)` are all
there.
:::pt-br
`rows`, `series`, `hovered`, `reading`, `ticks` e `format(value)` estão todos
lá.
:::

:::en
## RTL

The chart does not mirror. A value axis does not turn around because the
language does, so the plot, the axis and its ticks stay physical under
`dir="rtl"`, on purpose and with a comment in the template. The legend and the
tooltip are text, and follow the page.

## Accessibility

The plot is labelled with `label`, `Chart` by default, so give it what the
chart shows. The drawing itself is not described point by point: the tooltip
follows the pointer and is not reachable by keyboard, so a reader who cannot
see the chart needs the same numbers elsewhere, such as a table beside it or
the figures in the text.

## API reference
:::pt-br
## RTL

O gráfico não espelha. Um eixo de valores não se vira porque o idioma vira,
então o plot, o eixo e as marcas ficam físicos sob `dir="rtl"`, de propósito e
com um comentário no template. A legenda e o tooltip são texto, e seguem a
página.

## Acessibilidade

O plot é rotulado com `label`, `Chart` por padrão, então dê a ele o que o
gráfico mostra. O desenho em si não é descrito ponto a ponto: o tooltip
acompanha o ponteiro e não é alcançável pelo teclado, então um leitor que não
vê o gráfico precisa dos mesmos números em outro lugar, como uma tabela ao lado
ou os valores no texto.

## Referência da API
:::

<c-docs.api-reference name="chart" />

:::en
## Notes

**What this does not do.**

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

**What each attribute means.**

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
:::pt-br
## Observações

**O que isto não faz.**

- **Nada é desenhado antes de o Alpine começar.** Os paths são calculados a
  partir da largura medida, e não há largura até a página ser diagramada. Toda
  biblioteca de gráficos funciona assim; o resto desta biblioteca não, então
  vale saber.
- **Nada de zoom, seleção ou arrastar.**
- **Nada de escala logarítmica, nem de eixo de tempo que escolhe as próprias
  marcas.** O eixo x é categórico: a view envia o rótulo que quer mostrar.
- **Não serve para séries muito grandes.** Alguns milhares de pontos é onde
  elementos posicionados começam a custar alguma coisa. Um dashboard de KPI
  passa longe disso.

Se uma dessas coisas é o que você precisa, a resposta honesta é uma biblioteca
de gráficos, e o registry pode declarar uma por componente quando chegar a
hora.

**O que cada atributo significa.**

| Prop | Onde | Padrão | Significado |
| --- | --- | --- | --- |
| `data` | `<c-chart>` | `[]` | as linhas, em JSON |
| `config` | `<c-chart>` | `{}` | de chave para rótulo e cor, em JSON |
| `label` | `<c-chart.plot>` | `Chart` | dá nome ao desenho para um leitor de tela |
| `key` | `<c-chart.axis-x>` | — | o campo com o nome de cada linha |
| `height` | `<c-chart.axis-x>` | `24` | pixels reservados embaixo |
| `width` | `<c-chart.axis-y>` | `44` | pixels reservados à esquerda |
| `data_key` | séries | — | o campo que esta série desenha |
| `stack` | `area`, `bar` | `false` | empilha sobre a série declarada antes dela |
| `dots` | `line` | `true` | desenha um ponto em cada valor |
| `donut` | `pie` | `false` | deixa um furo no meio |
| `thickness` | `pie` | `60` | a largura do anel, em pixels |
| `name_key` | `pie`, `legend` | — | o campo que dá nome a cada linha |
:::
