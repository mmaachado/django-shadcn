---
title: Carousel
description: A set of slides that scroll horizontally or vertically, with arrows, dots and keyboard control — and a plain scrollable list when JavaScript never arrives.
description.pt-br: Um conjunto de slides que rola na horizontal ou na vertical, com setas, dots e teclado — e uma lista rolável comum quando o JavaScript não chega.
description.es: Un conjunto de diapositivas que se desplaza en horizontal o en vertical, con flechas, puntos y teclado — y una lista desplazable común cuando el JavaScript no llega.
---

<c-docs.demo-section class="min-h-[280px]">
<div class="w-full px-12">
<c-carousel label="Five slides">
<c-carousel.content>
<c-carousel.item class="md:basis-1/3"><div class="flex h-32 items-center justify-center rounded-md border bg-background text-3xl font-medium">1</div></c-carousel.item>
<c-carousel.item class="md:basis-1/3"><div class="flex h-32 items-center justify-center rounded-md border bg-background text-3xl font-medium">2</div></c-carousel.item>
<c-carousel.item class="md:basis-1/3"><div class="flex h-32 items-center justify-center rounded-md border bg-background text-3xl font-medium">3</div></c-carousel.item>
<c-carousel.item class="md:basis-1/3"><div class="flex h-32 items-center justify-center rounded-md border bg-background text-3xl font-medium">4</div></c-carousel.item>
<c-carousel.item class="md:basis-1/3"><div class="flex h-32 items-center justify-center rounded-md border bg-background text-3xl font-medium">5</div></c-carousel.item>
</c-carousel.content>
<c-carousel.previous />
<c-carousel.next />
<c-carousel.dots />
</c-carousel>
</div>
</c-docs.demo-section>

<c-docs.cheat-sheet name="carousel">
<c-carousel>
    <c-carousel.content>
        {% for photo in photos %}
            <c-carousel.item class="md:basis-1/2 lg:basis-1/3">
                <img src="{{ photo.url }}" alt="{{ photo.alt }}">
            </c-carousel.item>
        {% endfor %}
    </c-carousel.content>
    <c-carousel.previous />
    <c-carousel.next />
    <c-carousel.dots />
</c-carousel>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add carousel
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-carousel>
    <c-carousel.content>
        {% for photo in photos %}
            <c-carousel.item class="md:basis-1/2 lg:basis-1/3">
                <img src="{{ photo.url }}" alt="{{ photo.alt }}">
            </c-carousel.item>
        {% endfor %}
    </c-carousel.content>
    <c-carousel.previous />
    <c-carousel.next />
    <c-carousel.dots />
</c-carousel>
```

:::en
Upstream drives the carousel with Embla. Here the track is an ordinary scroll
container and CSS `scroll-snap` does the moving. That is the reason dragging,
the trackpad, momentum and touch all work without a line of code, and the
reason the slides are still a scrollable list when JavaScript is disabled or
has not loaded yet. Alpine only reads where the track came to rest, which the
arrows and the dots need to know what to show.

The slides are whatever you loop over, so a queryset of images is one
`{% verbatim %}{% for %}{% endverbatim %}` inside `<c-carousel.content>`.

The arrows sit at `-left-12` and `-right-12`, outside the track, so the
carousel needs room around it: `px-12` on a wrapper, or `class="mx-12"` on the
carousel itself.

## Examples

### Sizes

Each slide is `basis-full` by default, one at a time. Give it a different
basis at a breakpoint:
:::pt-br
O upstream move o carrossel com o Embla. Aqui a trilha é um contêiner de
rolagem comum e quem faz o movimento é o `scroll-snap` do CSS. É o motivo de
arrastar, o trackpad, o embalo e o toque funcionarem sem uma linha de código, e
o motivo de os slides continuarem sendo uma lista rolável quando o JavaScript
está desligado ou ainda não carregou. O Alpine só lê onde a trilha parou, que é
o que as setas e os pontos precisam saber para mostrar.

Os slides são o que você percorrer, então um queryset de imagens é um
`{% verbatim %}{% for %}{% endverbatim %}` dentro do `<c-carousel.content>`.

As setas ficam em `-left-12` e `-right-12`, fora da trilha, então o carrossel
precisa de espaço em volta: `px-12` num elemento em volta, ou `class="mx-12"` no
próprio carrossel.

## Exemplos

### Tamanhos

Cada slide é `basis-full` por padrão, um de cada vez. Dê a ele outro basis em
um breakpoint:
:::

```html
<c-carousel.item class="md:basis-1/2 lg:basis-1/3">
```

:::en
Use a breakpoint even for a size that never changes, `md:basis-1/3` rather
than `basis-1/3`. Without one, the two `flex-basis` utilities land in the same
place in the stylesheet and the component's own default is the one that
applies.

### Spacing

The gap between slides is the content's negative start margin and each item's
start padding, `-ms-4` and `ps-4`. Change both together, with the `!` suffix,
since the component already sets them.
:::pt-br
Use um breakpoint mesmo para um tamanho que nunca muda, `md:basis-1/3` em vez
de `basis-1/3`. Sem ele, os dois utilitários de `flex-basis` caem no mesmo
lugar da folha de estilo e quem vale é o padrão do próprio componente.

### Espaçamento

O espaço entre os slides é a margem negativa do início do conteúdo e o padding
do início de cada item, `-ms-4` e `ps-4`. Mude os dois juntos, com o sufixo
`!`, já que o componente já os define.
:::

<c-docs.example>
<div class="px-12">
  <c-carousel class="w-full max-w-sm">
    <c-carousel.content class="-ms-1!">
      {% for n in "12345" %}
        <c-carousel.item class="ps-1! md:basis-1/2">
          <div class="flex aspect-square items-center justify-center rounded-md border text-2xl font-semibold">{{ n }}</div>
        </c-carousel.item>
      {% endfor %}
    </c-carousel.content>
    <c-carousel.previous />
    <c-carousel.next />
  </c-carousel>
</div>
</c-docs.example>

:::en
### Orientation

`orientation="vertical"` turns the track and rotates the arrows. The content
needs a height, since a column of slides has nothing else to scroll inside:
:::pt-br
### Orientação

`orientation="vertical"` vira a trilha e gira as setas. O conteúdo precisa de
uma altura, já que uma coluna de slides não tem mais nada dentro do que rolar:
:::

```html
<c-carousel orientation="vertical">
    <c-carousel.content class="h-64">
        ...
    </c-carousel.content>
</c-carousel>
```

<c-docs.demo-section class="min-h-[360px]">
<div class="py-12">
<c-carousel orientation="vertical" label="Three slides, vertical">
<c-carousel.content class="h-56 w-56">
<c-carousel.item class="md:basis-1/2"><div class="flex h-24 items-center justify-center rounded-md border bg-background text-3xl font-medium">A</div></c-carousel.item>
<c-carousel.item class="md:basis-1/2"><div class="flex h-24 items-center justify-center rounded-md border bg-background text-3xl font-medium">B</div></c-carousel.item>
<c-carousel.item class="md:basis-1/2"><div class="flex h-24 items-center justify-center rounded-md border bg-background text-3xl font-medium">C</div></c-carousel.item>
</c-carousel.content>
<c-carousel.previous />
<c-carousel.next />
</c-carousel>
</div>
</c-docs.demo-section>

:::en
The orientation reaches the slides as a data attribute on the carousel rather
than through the Alpine scope, so they are laid out on the first paint instead
of jumping into place once Alpine starts.

### Driving it yourself

The carousel's scope is available to anything inside it:
:::pt-br
A orientação chega aos slides como um atributo data no carrossel, e não pelo
escopo do Alpine, então eles já aparecem no lugar na primeira pintura em vez de
pularem para o lugar quando o Alpine começa.

### Controlando você mesmo

O escopo do carrossel está disponível para qualquer coisa dentro dele:
:::

```html
<c-carousel>
    ...
    <button type="button" @click="to(0)" x-bind:disabled="!canPrevious">Back to the start</button>
    <p>Slide <span x-text="index + 1"></span> of <span x-text="count"></span></p>
</c-carousel>
```

:::en
`count` is how many positions the track can stop at, not how many slides there
are. With three slides in view, the last two can never reach the edge, so five
slides are three positions. It follows the DOM, so slides swapped in by htmx
are counted without telling the component anything.

## RTL

The arrows stay where they are under `dir="rtl"`: the track scrolls in physical
coordinates, with `scrollLeft` and the left and right arrow keys, so previous
is on the left and next on the right in either direction. The arrow buttons
carry a comment saying so in their templates.

## Accessibility

The carousel is a region named with `label`, `Carousel` by default, so give it
what the slides are. <kbd>←</kbd> and <kbd>→</kbd> move it whenever focus is
inside, in both orientations, the same keys upstream uses. The arrows are
labelled buttons and are disabled at the ends. The slides themselves are not
announced as "slide 2 of 5", so put that in the content when it matters.

## API reference
:::pt-br
`count` é quantas posições a trilha pode ocupar, não quantos slides existem.
Com três slides à vista, os dois últimos nunca alcançam a borda, então cinco
slides são três posições. Ele segue o DOM, então slides trocados pelo htmx são
contados sem avisar nada ao componente.

## RTL

As setas ficam onde estão sob `dir="rtl"`: a trilha rola em coordenadas
físicas, com `scrollLeft` e as setas esquerda e direita do teclado, então o
anterior fica à esquerda e o próximo à direita nas duas direções. Os botões das
setas levam um comentário dizendo isso nos templates.

## Acessibilidade

O carrossel é uma região com o nome dado por `label`, `Carousel` por padrão,
então dê a ele o que os slides são. <kbd>←</kbd> e <kbd>→</kbd> o movem sempre
que o foco está dentro dele, nas duas orientações, as mesmas teclas que o
upstream usa. As setas são botões com rótulo e ficam desabilitadas nas pontas.
Os slides em si não são anunciados como "slide 2 de 5", então ponha isso no
conteúdo quando importar.

## Referência da API
:::

<c-docs.api-reference name="carousel" />

:::en
## Notes

**Anatomy.**

| Tag | What it is |
| --- | --- |
| `<c-carousel>` | the region, the state, and the keyboard |
| `<c-carousel.content>` | the track: the scroll container and the layout |
| `<c-carousel.item>` | one slide |
| `<c-carousel.previous>` | the arrow back |
| `<c-carousel.next>` | the arrow on |
| `<c-carousel.dots>` | one dot per position the track can stop at |

**What the attributes mean.**

| Prop | Where | Default | Meaning |
| --- | --- | --- | --- |
| `orientation` | `<c-carousel>` | `horizontal` | `horizontal` or `vertical` |
| `label` | `<c-carousel>` | `Carousel` | names the region for a screen reader |
| `variant` | the arrows | `outline` | any button variant |

**Dots.** Upstream has no dots component; its demo reads the snap list off the
Embla API and draws them in the page. That list is what `count` is here, so
`<c-carousel.dots>` carries them.

**Options, events and plugins.** Upstream passes options and plugins to Embla,
such as looping and autoplay, and listens to its events. There is no Embla
here, so there are none of the three; `index`, `count`, `canPrevious` and
`canNext` on the scope are what a page can read.
:::pt-br
## Observações

**Anatomia.**

| Tag | O que é |
| --- | --- |
| `<c-carousel>` | a região, o estado e o teclado |
| `<c-carousel.content>` | a trilha: o contêiner de rolagem e o layout |
| `<c-carousel.item>` | um slide |
| `<c-carousel.previous>` | a seta para trás |
| `<c-carousel.next>` | a seta para a frente |
| `<c-carousel.dots>` | um ponto por posição em que a trilha pode parar |

**O que os atributos significam.**

| Prop | Onde | Padrão | Significado |
| --- | --- | --- | --- |
| `orientation` | `<c-carousel>` | `horizontal` | `horizontal` ou `vertical` |
| `label` | `<c-carousel>` | `Carousel` | dá nome à região para um leitor de tela |
| `variant` | as setas | `outline` | qualquer variante de botão |

**Pontos.** O upstream não tem um componente de pontos; a demo dele lê a lista
de encaixes da API do Embla e os desenha na página. Essa lista é o que `count`
é aqui, então o `<c-carousel.dots>` os traz.

**Opções, eventos e plugins.** O upstream passa opções e plugins ao Embla, como
o loop e a reprodução automática, e escuta os eventos dele. Aqui não há Embla,
então não há nenhum dos três; `index`, `count`, `canPrevious` e `canNext` no
escopo são o que uma página pode ler.
:::
