---
title: Bubble
description: The message surface itself, with the variant, the alignment and the reactions that sit on it.
description.pt-br: A superfície da mensagem, com a variante, o alinhamento e as reações que ficam sobre ela.
description.es: La superficie del mensaje, con la variante, la alineación y las reacciones que van sobre ella.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="flex w-full max-w-md flex-col gap-8 text-start">
<c-bubble variant="muted">
<c-bubble.content>I checked the registry output and removed the stale route.</c-bubble.content>
</c-bubble>
<c-bubble align="end">
<c-bubble.content>Thanks, that was the last one.</c-bubble.content>
<c-bubble.reactions>
<span>👍</span>
</c-bubble.reactions>
</c-bubble>
</div>
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add bubble
```

:::en
<p class="mt-4 text-sm text-muted-foreground">
    <strong>Note:</strong> This pulls in <a href="{% url 'page' slug='collapsible' %}" class="underline">Collapsible</a>, which the <em>Long messages</em> example below builds on, and with it the <a href="https://alpinejs.dev/plugins/collapse" target="_blank" rel="noopener noreferrer" class="underline">Alpine.js Collapse plugin</a>. The bubble itself has no JavaScript.
</p>

## Usage
:::pt-br
<p class="mt-4 text-sm text-muted-foreground">
    <strong>Observação:</strong> isto traz junto o <a href="{% url 'page' slug='collapsible' %}" class="underline">Collapsible</a>, em que o exemplo <em>Mensagens longas</em> abaixo se apoia, e com ele o <a href="https://alpinejs.dev/plugins/collapse" target="_blank" rel="noopener noreferrer" class="underline">plugin Collapse do Alpine.js</a>. O bubble em si não tem JavaScript.
</p>

## Uso
:::

```html
<c-bubble variant="muted">
    <c-bubble.content>How can I help you today?</c-bubble.content>
</c-bubble>
```

:::en
The variant lives on the root and the padding lives on the content, so the
reactions can hang off the edge of the surface without the surface clipping
them. That split is why the two tags are always written together.

## Variants

Seven, matching the upstream registry. `default` is the primary colour, for the
side of the conversation the reader is on; `muted` and `secondary` are the
neutral surfaces for the other side.
:::pt-br
A variante fica na raiz e o padding fica no conteúdo, para que as reações possam
pender para fora da borda da superfície sem que a superfície as corte. É por
essa divisão que as duas tags são sempre escritas juntas.

## Variantes

Sete, as mesmas do registry do upstream. `default` é a cor primária, para o lado
da conversa em que o leitor está; `muted` e `secondary` são as superfícies
neutras para o outro lado.
:::

<c-docs.demo-section>
<div class="flex w-full max-w-md flex-col gap-4 text-start">
<c-bubble>
<c-bubble.content>Default</c-bubble.content>
</c-bubble>
<c-bubble variant="secondary">
<c-bubble.content>Secondary</c-bubble.content>
</c-bubble>
<c-bubble variant="muted">
<c-bubble.content>Muted</c-bubble.content>
</c-bubble>
<c-bubble variant="tinted">
<c-bubble.content>Tinted</c-bubble.content>
</c-bubble>
<c-bubble variant="outline">
<c-bubble.content>Outline</c-bubble.content>
</c-bubble>
<c-bubble variant="ghost">
<c-bubble.content>Ghost, with no surface at all</c-bubble.content>
</c-bubble>
<c-bubble variant="destructive">
<c-bubble.content>Destructive</c-bubble.content>
</c-bubble>
</div>
</c-docs.demo-section>

```html
<c-bubble variant="secondary">...</c-bubble>
<c-bubble variant="tinted">...</c-bubble>
<c-bubble variant="ghost">...</c-bubble>
```

:::en
## Alignment

`align="end"` pushes the bubble to the far side. Inside a
[Message]({% url 'page' slug='message' %}) the row already sets the side, and
the bubble follows it without being told.
:::pt-br
## Alinhamento

`align="end"` empurra o bubble para o lado oposto. Dentro de uma
[Message]({% url 'page' slug='message' %}) a linha já define o lado, e o bubble
o acompanha sem precisar ser avisado.
:::

<c-docs.demo-section>
<div class="flex w-full max-w-md flex-col gap-4 text-start">
<c-bubble variant="muted">
<c-bubble.content>Aligned to the start.</c-bubble.content>
</c-bubble>
<c-bubble align="end">
<c-bubble.content>Aligned to the end.</c-bubble.content>
</c-bubble>
</div>
</c-docs.demo-section>

```html
<c-bubble align="end">
    <c-bubble.content>Aligned to the end.</c-bubble.content>
</c-bubble>
```

:::en
## Examples

### Reactions

Reactions overlap the edge of the surface. `side` picks the top or the bottom
edge, `align` picks the corner.
:::pt-br
## Exemplos

### Reações

As reações sobrepõem a borda da superfície. `side` escolhe a borda de cima ou a
de baixo, `align` escolhe o canto.
:::

<c-docs.demo-section>
<div class="flex w-full max-w-md flex-col gap-10 text-start">
<c-bubble variant="muted">
<c-bubble.content>Bottom and end, the default.</c-bubble.content>
<c-bubble.reactions>
<span>🔥</span>
<span>+8</span>
</c-bubble.reactions>
</c-bubble>
<c-bubble variant="muted">
<c-bubble.content>Top and start.</c-bubble.content>
<c-bubble.reactions side="top" align="start">
<span>👍</span>
</c-bubble.reactions>
</c-bubble>
</div>
</c-docs.demo-section>

```html
<c-bubble variant="muted">
    <c-bubble.content>Bottom and end, the default.</c-bubble.content>
    <c-bubble.reactions>
        <span>🔥</span>
        <span>+8</span>
    </c-bubble.reactions>
</c-bubble>

<c-bubble.reactions side="top" align="start">...</c-bubble.reactions>
```

:::en
A row of emoji says nothing to a screen reader on its own. Name it:
:::pt-br
Uma fileira de emojis sozinha não diz nada a um leitor de tela. Dê um nome a ela:
:::

```html
<c-bubble.reactions role="img" aria-label="Reactions: fire, and 8 more">
    <span>🔥</span>
    <span>+8</span>
</c-bubble.reactions>
```

:::en
### A bubble that does something

`tag` renders the content as a button or a link instead of a plain box, so a
suggested reply can be clicked and a shared file can be opened. The hover and
focus treatment is already in the variant, waiting for an element that can take
it.
:::pt-br
### Um bubble que faz alguma coisa

`tag` renderiza o conteúdo como um botão ou um link em vez de uma caixa simples,
para que uma resposta sugerida possa ser clicada e um arquivo compartilhado
possa ser aberto. O tratamento de hover e de foco já está na variante,
esperando por um elemento que o aceite.
:::

<c-docs.demo-section>
<div class="flex w-full max-w-md flex-col gap-4 text-start">
<c-bubble variant="outline">
<c-bubble.content tag="button">I forgot my password</c-bubble.content>
</c-bubble>
<c-bubble variant="outline">
<c-bubble.content tag="a" href="{% url 'page' slug='installation' %}">Read the installation guide</c-bubble.content>
</c-bubble>
</div>
</c-docs.demo-section>

```html
<c-bubble variant="outline">
    <c-bubble.content tag="button">I forgot my password</c-bubble.content>
</c-bubble>

<c-bubble variant="outline">
    <c-bubble.content tag="a" href="/help/">Read the guide</c-bubble.content>
</c-bubble>
```

:::en
A `button` gets `type="button"` unless you pass your own, so a bubble inside a
form does not submit it by accident.

### Long messages

A long message is a wall. Wrap the bubble in a
[Collapsible]({% url 'page' slug='collapsible' %}) and put the toggle in the
content, exactly as the upstream example does — the bubble stays presentational
and the open state lives one level up.
:::pt-br
Um `button` recebe `type="button"` a menos que você passe o seu, para que um
bubble dentro de um formulário não o envie sem querer.

### Mensagens longas

Uma mensagem longa vira um paredão. Envolva o bubble em um
[Collapsible]({% url 'page' slug='collapsible' %}) e ponha o botão de abrir no
conteúdo, exatamente como faz o exemplo do upstream — o bubble continua só de
apresentação e o estado de aberto mora um nível acima.
:::

<c-docs.demo-section>
<c-collapsible class="w-full max-w-md text-start">
<c-bubble variant="muted">
<c-bubble.content>
<p>The focus ring was being drawn by the primitive and by the style file at the same time, which is why it doubled up on the outline variant.</p>
<c-collapsible.content>
<p class="mt-2">Moving it to the style file keeps the primitive neutral, so the other themes can pick their own treatment later instead of overriding this one.</p>
</c-collapsible.content>
<c-collapsible.trigger class="mt-2 text-xs underline underline-offset-4 opacity-80">
<span x-text="open ? 'Show less' : 'Show more'">Show more</span>
</c-collapsible.trigger>
</c-bubble.content>
</c-bubble>
</c-collapsible>
</c-docs.demo-section>

```html
<c-collapsible>
    <c-bubble variant="muted">
        <c-bubble.content>
            <p>The first paragraph, always visible.</p>
            <c-collapsible.content>
                <p>The rest, hidden until asked for.</p>
            </c-collapsible.content>
            <c-collapsible.trigger>
                <span x-text="open ? 'Show less' : 'Show more'">Show more</span>
            </c-collapsible.trigger>
        </c-bubble.content>
    </c-bubble>
</c-collapsible>
```

:::en
### Grouped

`group` stacks consecutive bubbles from the same sender at a tighter rhythm than
separate messages.
:::pt-br
### Agrupados

O `group` empilha bubbles seguidos do mesmo remetente num ritmo mais apertado
do que mensagens separadas.
:::

<c-docs.demo-section>
<c-bubble.group class="w-full max-w-md text-start">
<c-bubble variant="muted">
<c-bubble.content>One thought.</c-bubble.content>
</c-bubble>
<c-bubble variant="muted">
<c-bubble.content>Then another, a second later.</c-bubble.content>
</c-bubble>
</c-bubble.group>
</c-docs.demo-section>

```html
<c-bubble.group>
    <c-bubble variant="muted">
        <c-bubble.content>One thought.</c-bubble.content>
    </c-bubble>
    <c-bubble variant="muted">
        <c-bubble.content>Then another.</c-bubble.content>
    </c-bubble>
</c-bubble.group>
```
