---
title: Message Scroller
description: The scroll container of a chat transcript — the part that has to survive streamed replies, restored threads and history loading in above.
description.pt-br: O container de scroll de uma conversa — a parte que precisa sobreviver a respostas em streaming, threads restauradas e histórico entrando por cima.
description.es: El contenedor de scroll de una conversación — la parte que debe sobrevivir a respuestas en streaming, hilos restaurados e historial cargando arriba.
---

<c-docs.demo-section class="min-h-[460px]">
<c-message-scroller.provider default_scroll_position="last-anchor" class="block h-[380px] w-full max-w-md text-left">
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

<p class="mt-4 text-sm text-muted-foreground">
    It opened at the last turn rather than at the bottom, with the row before it
    peeking above. Scroll it: the two controls fade in and out as there becomes
    something to scroll to in that direction.
</p>

## Installation

```bash
uvx django_shadcn@latest add message_scroller
```

## How the transcript grows

This is the decision the whole component turns on, so it comes before the
markup.

Upstream is driven by React state: the parent re-renders with new messages and
the provider reacts. A Django transcript has no such moment — it grows in the
DOM, from htmx, from an event stream, or from a socket handler.

So the provider watches the content element and reacts to whatever put a row
there. **Anything that inserts a row is enough. You write no JavaScript.**

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

Append with `beforeend` and the transcript follows the stream. Insert with
`afterbegin` and the row the reader is on stays exactly where it is while
history loads above. The same holds for an `EventSource` handler appending a
row, or a channels consumer doing it — none of them has to tell the component
anything.

<c-docs.demo-section class="min-h-[460px]">
<c-message-scroller.provider class="block h-[380px] w-full max-w-md text-left">
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

<p class="mt-4 text-sm text-muted-foreground">
    Both buttons only insert an element. Append at the bottom and the transcript
    follows; scroll up first and it does not. Prepend at any scroll position and
    the row you were reading does not move.
</p>

## Usage

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

<c-docs.demo-section class="min-h-[380px]">
<div class="grid w-full gap-4 md:grid-cols-3">

<div class="flex flex-col gap-2 text-left">
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

<div class="flex flex-col gap-2 text-left">
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

<div class="flex flex-col gap-2 text-left">
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

```html
<button type="button" @click="scrollToMessage('m-42')">Jump to that message</button>
<button type="button" @click="scrollToEnd()">Latest</button>
<button type="button" @click="scrollToStart()">Beginning</button>
```

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
