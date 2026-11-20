---
title: Message Scroller
description: The scroll container of a chat transcript — the part that has to survive streamed replies, restored threads and history loading in above.
description.pt-br: O container de scroll de uma conversa — a parte que precisa sobreviver a respostas em streaming, threads restauradas e histórico entrando por cima.
description.es: El contenedor de scroll de una conversación — la parte que debe sobrevivir a respuestas en streaming, hilos restaurados e historial cargando arriba.
---

<c-docs.demo-section class="min-h-[460px]">
<c-message-scroller.provider default_scroll_position="last-anchor" class="block h-[380px] w-full max-w-md text-start">
<c-message-scroller class="rounded-lg border bg-background">
<c-message-scroller.viewport class="p-4">
<c-message-scroller.content class="gap-4">
<c-message-scroller.item message_id="d-1" scroll_anchor="true">
<c-message><c-message.content>
<c-bubble variant="muted"><c-bubble.content>Can you look at the registry output?</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
<c-message-scroller.item message_id="d-2">
<c-message align="end"><c-message.content>
<c-bubble align="end"><c-bubble.content>Reading it now.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
<c-message-scroller.item message_id="d-3">
<c-message><c-message.content>
<c-bubble variant="muted"><c-bubble.content>There is a stale route in there somewhere.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
<c-message-scroller.item message_id="d-4" scroll_anchor="true">
<c-message align="end"><c-message.content>
<c-bubble align="end"><c-bubble.content>Found it — the entry was never added.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
<c-message-scroller.item message_id="d-5">
<c-message><c-message.content>
<c-bubble variant="muted"><c-bubble.content>That explains why the CLI refused the name.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
<c-message-scroller.item message_id="d-6">
<c-message align="end"><c-message.content>
<c-bubble align="end"><c-bubble.content>Adding it now, with a test that would have caught it.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
<c-message-scroller.item message_id="d-7">
<c-message><c-message.content>
<c-bubble variant="muted"><c-bubble.content>The test is the part that matters. Where does it go?</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
<c-message-scroller.item message_id="d-8">
<c-message align="end"><c-message.content>
<c-bubble align="end"><c-bubble.content>Next to the one that reads the registry, so they fail together.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
<c-message-scroller.item message_id="d-9">
<c-message><c-message.content>
<c-bubble variant="muted"><c-bubble.content>Good. Push it and I will look.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
<c-message-scroller.item message_id="d-10">
<c-message align="end"><c-message.content>
<c-bubble align="end"><c-bubble.content>Pushed.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
</c-message-scroller.content>
</c-message-scroller.viewport>
<c-message-scroller.button direction="start" />
<c-message-scroller.button direction="end" />
</c-message-scroller>
</c-message-scroller.provider>
</c-docs.demo-section>

:::en
<p class="mt-4 text-sm text-muted-foreground">
    It opened at the last turn rather than at the bottom, with the row before it
    peeking above. Scroll it: the two controls fade in and out as there becomes
    something to scroll to in that direction.
</p>

## Installation
:::pt-br
<p class="mt-4 text-sm text-muted-foreground">
    Ele abriu na última vez de falar e não no fim, com a linha anterior
    aparecendo acima. Role: os dois controles aparecem e somem conforme passa a
    haver algo para onde rolar naquela direção.
</p>

## Instalação
:::

```bash
uvx django_shadcn@latest add message_scroller
```

:::en
## How the transcript grows

This is the decision the whole component turns on, so it comes before the
markup.

Upstream is driven by React state: the parent re-renders with new messages and
the provider reacts. A Django transcript has no such moment — it grows in the
DOM, from htmx, from an event stream, or from a socket handler.

So the provider watches the content element and reacts to whatever put a row
there. **Anything that inserts a row is enough. You write no JavaScript.**
:::pt-br
## Como a transcrição cresce

Esta é a decisão em torno da qual o componente inteiro gira, então ela vem
antes do markup.

O upstream é movido por estado do React: o pai renderiza de novo com mensagens
novas e o provider reage. Uma transcrição Django não tem esse momento — ela
cresce no DOM, pelo htmx, por um event stream ou por um handler de socket.

Então o provider observa o elemento de conteúdo e reage a qualquer coisa que
tenha posto uma linha ali. **Qualquer coisa que insira uma linha basta. Você
não escreve JavaScript.**
:::

```html
<c-message-scroller.content
    hx-get="{% url 'messages' %}"
    hx-trigger="every 2s"
    hx-swap="beforeend">
    {% for message in messages %}
        <c-message-scroller.item message_id="{{ message.id }}">
            ...
        </c-message-scroller.item>
    {% endfor %}
</c-message-scroller.content>
```

:::en
Append with `beforeend` and the transcript follows the stream. Insert with
`afterbegin` and the row the reader is on stays exactly where it is while
history loads above. The same holds for an `EventSource` handler appending a
row, or a channels consumer doing it — none of them has to tell the component
anything.
:::pt-br
Acrescente com `beforeend` e a transcrição acompanha o fluxo. Insira com
`afterbegin` e a linha em que o leitor está fica exatamente onde está enquanto o
histórico carrega acima. O mesmo vale para um handler de `EventSource` que
acrescenta uma linha, ou para um consumer do channels que faça isso — nenhum
deles precisa avisar nada ao componente.
:::

<c-docs.demo-section class="min-h-[460px]">
<c-message-scroller.provider class="block h-[380px] w-full max-w-md text-start">
<div class="flex h-full flex-col gap-3">
<c-message-scroller class="rounded-lg border bg-background">
<c-message-scroller.viewport class="p-4">
<c-message-scroller.content x-ref="rows" class="gap-4">
<c-message-scroller.item message_id="g-1">
<c-message><c-message.content>
<c-bubble variant="muted"><c-bubble.content>Watch what happens when a row arrives.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
<c-message-scroller.item message_id="g-2">
<c-message><c-message.content>
<c-bubble variant="muted"><c-bubble.content>Scroll up first, and it will leave you alone.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
<c-message-scroller.item message_id="g-3">
<c-message><c-message.content>
<c-bubble variant="muted"><c-bubble.content>Come back to the bottom and it follows again.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
<c-message-scroller.item message_id="g-4">
<c-message align="end"><c-message.content>
<c-bubble align="end"><c-bubble.content>The buttons below stand in for your server.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
<c-message-scroller.item message_id="g-5">
<c-message><c-message.content>
<c-bubble variant="muted"><c-bubble.content>Neither of them tells the component anything.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
<c-message-scroller.item message_id="g-6">
<c-message><c-message.content>
<c-bubble variant="muted"><c-bubble.content>They only put an element in the DOM, which is all htmx does.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
<c-message-scroller.item message_id="g-7">
<c-message align="end"><c-message.content>
<c-bubble align="end"><c-bubble.content>Try it from the bottom, then from halfway up.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</c-message-scroller.item>
</c-message-scroller.content>
</c-message-scroller.viewport>
<c-message-scroller.button direction="start" />
<c-message-scroller.button direction="end" />
</c-message-scroller>

<template x-ref="newest">
<div data-slot="message-scroller-item" data-scroll-anchor="false" class="min-w-0 shrink-0">
<c-message><c-message.content>
<c-bubble variant="muted"><c-bubble.content>A new message, appended straight into the DOM.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</div>
</template>

<template x-ref="older">
<div data-slot="message-scroller-item" data-scroll-anchor="false" class="min-w-0 shrink-0">
<c-message><c-message.content>
<c-bubble variant="outline"><c-bubble.content>An older message, loaded in above. You did not move.</c-bubble.content></c-bubble>
</c-message.content></c-message>
</div>
</template>

<div class="flex shrink-0 gap-2">
<c-button variant="outline" size="sm" x-on:click="$refs.rows.appendChild($refs.newest.content.cloneNode(true))">
Append a message
</c-button>
<c-button variant="outline" size="sm" x-on:click="$refs.rows.prepend($refs.older.content.cloneNode(true))">
Prepend history
</c-button>
</div>
</div>
</c-message-scroller.provider>
</c-docs.demo-section>

:::en
<p class="mt-4 text-sm text-muted-foreground">
    Both buttons only insert an element. Append at the bottom and the transcript
    follows; scroll up first and it does not. Prepend at any scroll position and
    the row you were reading does not move.
</p>

## Usage
:::pt-br
<p class="mt-4 text-sm text-muted-foreground">
    Os dois botões só inserem um elemento. Acrescente no fim e a transcrição
    acompanha; role para cima antes e ela não acompanha. Insira no começo em
    qualquer posição de rolagem e a linha que você estava lendo não se mexe.
</p>

## Uso
:::

```html
<c-message-scroller.provider default_scroll_position="last-anchor">
    <c-message-scroller class="h-[600px]">
        <c-message-scroller.viewport class="p-4">
            <c-message-scroller.content>
                {% for message in messages %}
                    <c-message-scroller.item
                        message_id="{{ message.id }}"
                        scroll_anchor="{{ message.starts_a_turn|yesno:'true,false' }}">
                        <c-message align="{{ message.align }}">
                            <c-message.content>
                                <c-bubble variant="muted">
                                    <c-bubble.content>{{ message.text }}</c-bubble.content>
                                </c-bubble>
                            </c-message.content>
                        </c-message>
                    </c-message-scroller.item>
                {% endfor %}
            </c-message-scroller.content>
        </c-message-scroller.viewport>
        <c-message-scroller.button direction="start" />
        <c-message-scroller.button direction="end" />
    </c-message-scroller>
</c-message-scroller.provider>
```

:::en
The provider holds the state and the frame holds the layout, which is why they
are two tags: a control placed inside the provider but outside the frame still
reaches the scroll methods.

## Identifying a row

`message_id` is required, and it should be the id the server already knows.
It is what anchoring, jumping and visibility tracking all key on — an index
would stop matching the moment older messages load in above.

`scroll_anchor="true"` marks a row as the start of a turn. Only anchors are
candidates for the opening position and for the reported anchor.

## Opening position

`default_scroll_position` on the provider takes:

| Value | Opens at |
| --- | --- |
| `end` | the live edge, following the stream. The default |
| `start` | the top of the transcript |
| `last-anchor` | the last turn, near the top, with the previous row peeking above it |

`previous_item_peek` is how many pixels of the previous row stay visible above
the anchor. It defaults to `48`.

Only `end` engages the follow-the-stream behaviour. Opening part-way up is a
reading position, and following the stream would throw the reader out of it.

The same transcript, opened three ways:
:::pt-br
O provider guarda o estado e o frame guarda o layout, e é por isso que são duas
tags: um controle posto dentro do provider mas fora do frame ainda alcança os
métodos de rolagem.

## Identificando uma linha

`message_id` é obrigatório, e deve ser o id que o servidor já conhece. É nele
que se apoiam a ancoragem, os saltos e o rastreio de visibilidade — um índice
deixaria de bater no momento em que mensagens mais antigas carregassem acima.

`scroll_anchor="true"` marca uma linha como o início de uma vez de falar. Só as
âncoras são candidatas à posição de abertura e à âncora informada.

## Posição de abertura

`default_scroll_position` no provider aceita:

| Valor | Abre em |
| --- | --- |
| `end` | a borda viva, acompanhando o fluxo. O padrão |
| `start` | o topo da transcrição |
| `last-anchor` | a última vez de falar, perto do topo, com a linha anterior aparecendo acima |

`previous_item_peek` é quantos pixels da linha anterior continuam visíveis acima
da âncora. O padrão é `48`.

Só `end` liga o comportamento de acompanhar o fluxo. Abrir no meio do caminho é
uma posição de leitura, e acompanhar o fluxo tiraria o leitor dela.

A mesma transcrição, aberta de três jeitos:
:::

<c-docs.demo-section class="min-h-[380px]">
<div class="grid w-full gap-4 md:grid-cols-3">

<div class="flex flex-col gap-2 text-start">
<p class="font-mono text-xs text-muted-foreground">start</p>
<c-message-scroller.provider default_scroll_position="start" class="block h-[240px]">
<c-message-scroller class="rounded-lg border bg-background">
<c-message-scroller.viewport class="p-3">
<c-message-scroller.content class="gap-3">
<c-message-scroller.item message_id="s-1"><c-bubble variant="muted"><c-bubble.content>Row 1</c-bubble.content></c-bubble></c-message-scroller.item>
<c-message-scroller.item message_id="s-2"><c-bubble variant="muted"><c-bubble.content>Row 2</c-bubble.content></c-bubble></c-message-scroller.item>
<c-message-scroller.item message_id="s-3"><c-bubble variant="muted"><c-bubble.content>Row 3</c-bubble.content></c-bubble></c-message-scroller.item>
<c-message-scroller.item message_id="s-4" scroll_anchor="true"><c-bubble variant="outline"><c-bubble.content>Row 4 · anchor</c-bubble.content></c-bubble></c-message-scroller.item>
<c-message-scroller.item message_id="s-5"><c-bubble variant="muted"><c-bubble.content>Row 5</c-bubble.content></c-bubble></c-message-scroller.item>
<c-message-scroller.item message_id="s-6"><c-bubble variant="muted"><c-bubble.content>Row 6</c-bubble.content></c-bubble></c-message-scroller.item>
</c-message-scroller.content>
</c-message-scroller.viewport>
</c-message-scroller>
</c-message-scroller.provider>
</div>

<div class="flex flex-col gap-2 text-start">
<p class="font-mono text-xs text-muted-foreground">end</p>
<c-message-scroller.provider default_scroll_position="end" class="block h-[240px]">
<c-message-scroller class="rounded-lg border bg-background">
<c-message-scroller.viewport class="p-3">
<c-message-scroller.content class="gap-3">
<c-message-scroller.item message_id="e-1"><c-bubble variant="muted"><c-bubble.content>Row 1</c-bubble.content></c-bubble></c-message-scroller.item>
<c-message-scroller.item message_id="e-2"><c-bubble variant="muted"><c-bubble.content>Row 2</c-bubble.content></c-bubble></c-message-scroller.item>
<c-message-scroller.item message_id="e-3"><c-bubble variant="muted"><c-bubble.content>Row 3</c-bubble.content></c-bubble></c-message-scroller.item>
<c-message-scroller.item message_id="e-4" scroll_anchor="true"><c-bubble variant="outline"><c-bubble.content>Row 4 · anchor</c-bubble.content></c-bubble></c-message-scroller.item>
<c-message-scroller.item message_id="e-5"><c-bubble variant="muted"><c-bubble.content>Row 5</c-bubble.content></c-bubble></c-message-scroller.item>
<c-message-scroller.item message_id="e-6"><c-bubble variant="muted"><c-bubble.content>Row 6</c-bubble.content></c-bubble></c-message-scroller.item>
</c-message-scroller.content>
</c-message-scroller.viewport>
</c-message-scroller>
</c-message-scroller.provider>
</div>

<div class="flex flex-col gap-2 text-start">
<p class="font-mono text-xs text-muted-foreground">last-anchor</p>
<c-message-scroller.provider default_scroll_position="last-anchor" class="block h-[240px]">
<c-message-scroller class="rounded-lg border bg-background">
<c-message-scroller.viewport class="p-3">
<c-message-scroller.content class="gap-3">
<c-message-scroller.item message_id="a-1"><c-bubble variant="muted"><c-bubble.content>Row 1</c-bubble.content></c-bubble></c-message-scroller.item>
<c-message-scroller.item message_id="a-2"><c-bubble variant="muted"><c-bubble.content>Row 2</c-bubble.content></c-bubble></c-message-scroller.item>
<c-message-scroller.item message_id="a-3"><c-bubble variant="muted"><c-bubble.content>Row 3</c-bubble.content></c-bubble></c-message-scroller.item>
<c-message-scroller.item message_id="a-4" scroll_anchor="true"><c-bubble variant="outline"><c-bubble.content>Row 4 · anchor</c-bubble.content></c-bubble></c-message-scroller.item>
<c-message-scroller.item message_id="a-5"><c-bubble variant="muted"><c-bubble.content>Row 5</c-bubble.content></c-bubble></c-message-scroller.item>
<c-message-scroller.item message_id="a-6"><c-bubble variant="muted"><c-bubble.content>Row 6</c-bubble.content></c-bubble></c-message-scroller.item>
</c-message-scroller.content>
</c-message-scroller.viewport>
</c-message-scroller>
</c-message-scroller.provider>
</div>

</div>
</c-docs.demo-section>

:::en
## Following the stream

With `auto_scroll` on — the default — reaching the live edge engages
stick-to-bottom, and new rows keep the newest in view. Scrolling away releases
it, and the transcript stops moving under the reader. Coming back to the bottom
engages it again.

`auto_scroll="false"` turns it off entirely.

## Preserving the reader's place

`preserve_on_prepend` is on by default. The provider keeps a fixed point — the
row the reader is on and where it sits — and restores it after anything changes
the content. That covers history arriving above, and it also covers a row above
growing taller, which is what a streamed reply does.

## Scrolling from your own controls

The provider exposes three methods to anything inside it:
:::pt-br
## Acompanhando o fluxo

Com `auto_scroll` ligado — o padrão —, chegar à borda viva liga o grudar no fim,
e linhas novas mantêm a mais recente à vista. Rolar para longe solta, e a
transcrição para de se mexer sob o leitor. Voltar ao fim liga de novo.

`auto_scroll="false"` desliga isso por completo.

## Preservando o lugar do leitor

`preserve_on_prepend` vem ligado por padrão. O provider guarda um ponto fixo — a
linha em que o leitor está e onde ela fica — e o restaura depois de qualquer
coisa que mude o conteúdo. Isso cobre o histórico chegando acima, e cobre também
uma linha acima ficando mais alta, que é o que faz uma resposta em streaming.

## Rolando a partir dos seus controles

O provider expõe três métodos a qualquer coisa dentro dele:
:::

```html
<button type="button" @click="scrollToMessage('m-42')">Jump to that message</button>
<button type="button" @click="scrollToEnd()">Latest</button>
<button type="button" @click="scrollToStart()">Beginning</button>
```

:::en
`scrollToMessage` returns `false` when the id is not on the page, so a link to
a message that has not loaded yet can fall back to a full page load.

`anchorId` and `visibleIds` are readable the same way, for a header that names
the turn being read.

## Reading the state from CSS

The viewport mirrors its state, so a page can style against the scroll position
without touching the Alpine scope:

| Attribute | Meaning |
| --- | --- |
| `data-at-start` | the transcript is scrolled to the top |
| `data-at-end` | the transcript is at the live edge |
| `data-stick` | new rows are being followed |
| `data-autoscrolling` | a programmatic scroll is running |
| `data-pending-scroll` | the opening position has not applied yet, and the viewport is held invisible |

The scroll buttons use the same idea: each carries `data-active`, and the one
with nothing to scroll to fades out and stops taking clicks rather than
disappearing, so it keeps its place in the tab order.

## Accessibility

The viewport is a `region` with a label, and the content is a `log` with
`aria-relevant="additions"` — a new message is announced as it arrives, without
the whole transcript being read back each time. Change the region's name with
`label` on the viewport when a page has more than one transcript.

## A note on what is not here

Upstream sets `content-visibility: auto` and `contain-intrinsic-size` on each
row to skip painting what is off screen. Those change what the provider
measures, and a measurement error here is a scroll jump — which is the one
defect this component exists to prevent. They belong after the behaviour has
proven itself, not before.
:::pt-br
`scrollToMessage` devolve `false` quando o id não está na página, então um link
para uma mensagem que ainda não carregou pode cair para um carregamento
completo da página.

`anchorId` e `visibleIds` podem ser lidos do mesmo jeito, para um cabeçalho que
dê nome à vez de falar sendo lida.

## Lendo o estado pelo CSS

A viewport espelha o próprio estado, então uma página pode estilizar conforme a
posição de rolagem sem mexer no escopo do Alpine:

| Atributo | Significado |
| --- | --- |
| `data-at-start` | a transcrição está rolada até o topo |
| `data-at-end` | a transcrição está na borda viva |
| `data-stick` | as linhas novas estão sendo acompanhadas |
| `data-autoscrolling` | uma rolagem programática está em andamento |
| `data-pending-scroll` | a posição de abertura ainda não foi aplicada, e a viewport fica invisível |

Os botões de rolagem usam a mesma ideia: cada um leva `data-active`, e o que não
tem para onde rolar esmaece e para de aceitar cliques em vez de sumir, para
manter o lugar dele na ordem de tab.

## Acessibilidade

A viewport é uma `region` com rótulo, e o conteúdo é um `log` com
`aria-relevant="additions"` — uma mensagem nova é anunciada quando chega, sem
que a transcrição inteira seja lida de novo a cada vez. Mude o nome da região
com `label` na viewport quando uma página tiver mais de uma transcrição.

## Sobre o que não está aqui

O upstream define `content-visibility: auto` e `contain-intrinsic-size` em cada
linha para não pintar o que está fora da tela. Isso muda o que o provider mede,
e um erro de medição aqui é um salto na rolagem — que é justamente o defeito que
este componente existe para evitar. Essas propriedades entram depois que o
comportamento tiver se provado, não antes.
:::
