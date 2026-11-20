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

<c-docs.cheat-sheet name="bubble">
<c-bubble variant="{% if message.mine %}default{% else %}muted{% endif %}" align="{% if message.mine %}end{% else %}start{% endif %}">
  <c-bubble.content>{{ message.text|linebreaksbr }}</c-bubble.content>
</c-bubble>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add bubble
```

:::en
This pulls in [Collapsible]({% url 'page' slug='collapsible' %}), which the
show more example builds on, and with it Alpine's collapse plugin. The bubble
itself has no JavaScript.

## Usage

The variant lives on the root and the padding on the content, so the reactions
can hang off the edge of the surface without the surface clipping them. That
split is why the two tags are always written together.

A bubble is markup and CSS only, so a conversation renders the same without
JavaScript. The text is yours to escape: `linebreaksbr` keeps the line breaks
of a message without marking anything safe.
:::pt-br
Isto traz junto o [Collapsible]({% url 'page' slug='collapsible' %}), em que o
exemplo de mostrar mais se apoia, e com ele o plugin collapse do Alpine. O
bubble em si não tem JavaScript.

## Uso

A variante fica na raiz e o padding no conteúdo, para que as reações possam
pender para fora da borda da superfície sem que a superfície as corte. É por
essa divisão que as duas tags são sempre escritas juntas.

Um bubble é só markup e CSS, então uma conversa renderiza igual sem
JavaScript. O texto é seu para escapar: `linebreaksbr` mantém as quebras de
linha de uma mensagem sem marcar nada como seguro.
:::

```html
{% for message in conversation.messages.all %}
  <c-bubble align="{% if message.author == request.user %}end{% else %}start{% endif %}">
    <c-bubble.content>{{ message.text|linebreaksbr }}</c-bubble.content>
  </c-bubble>
{% endfor %}
```

:::en
## Examples

### Variants

Seven, matching the upstream registry. `default` is the primary colour, for the
side of the conversation the reader is on; `muted` and `secondary` are the
neutral surfaces for the other side.
:::pt-br
## Exemplos

### Variantes

Sete, as mesmas do registry do upstream. `default` é a cor primária, para o
lado da conversa em que o leitor está; `muted` e `secondary` são as superfícies
neutras para o outro lado.
:::

<c-docs.example>
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
</c-docs.example>

:::en
### Alignment

`align="end"` pushes the bubble to the far side. Inside a
[Message]({% url 'page' slug='message' %}) the row already sets the side, and
the bubble follows it without being told.
:::pt-br
### Alinhamento

`align="end"` empurra o bubble para o lado oposto. Dentro de uma
[Message]({% url 'page' slug='message' %}) a linha já define o lado, e o bubble
o acompanha sem precisar ser avisado.
:::

<c-docs.example>
<div class="flex w-full max-w-md flex-col gap-4 text-start">
  <c-bubble variant="muted">
    <c-bubble.content>Aligned to the start.</c-bubble.content>
  </c-bubble>
  <c-bubble align="end">
    <c-bubble.content>Aligned to the end.</c-bubble.content>
  </c-bubble>
</div>
</c-docs.example>

:::en
### Bubble group

`group` stacks consecutive bubbles from the same sender at a tighter rhythm
than separate messages.
:::pt-br
### Grupo de bubbles

O `group` empilha bubbles seguidos do mesmo remetente num ritmo mais apertado
do que mensagens separadas.
:::

<c-docs.example>
<c-bubble.group class="w-full max-w-md text-start">
  <c-bubble variant="muted">
    <c-bubble.content>One thought.</c-bubble.content>
  </c-bubble>
  <c-bubble variant="muted">
    <c-bubble.content>Then another, a second later.</c-bubble.content>
  </c-bubble>
</c-bubble.group>
</c-docs.example>

:::en
### Links and buttons

`tag` renders the content as a button or a link instead of a plain box, so a
suggested reply can be clicked and a shared file opened. A `button` gets
`type="button"` unless you pass your own, so a bubble inside a form does not
submit it by accident.
:::pt-br
### Links e botões

`tag` renderiza o conteúdo como um botão ou um link em vez de uma caixa
simples, para que uma resposta sugerida possa ser clicada e um arquivo
compartilhado aberto. Um `button` recebe `type="button"` a menos que você passe
o seu, para que um bubble dentro de um formulário não o envie sem querer.
:::

<c-docs.example>
<div class="flex w-full max-w-md flex-col gap-4 text-start">
  <c-bubble variant="outline">
    <c-bubble.content tag="button">I forgot my password</c-bubble.content>
  </c-bubble>
  <c-bubble variant="outline">
    <c-bubble.content tag="a" href="{% url 'page' slug='installation' %}">Read the installation guide</c-bubble.content>
  </c-bubble>
</div>
</c-docs.example>

:::en
### Reactions

Reactions overlap the edge of the surface. `side` picks the top or the bottom
edge, `align` picks the corner.
:::pt-br
### Reações

As reações sobrepõem a borda da superfície. `side` escolhe a borda de cima ou a
de baixo, `align` escolhe o canto.
:::

<c-docs.example>
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
</c-docs.example>

:::en
### Show more

A long message is a wall. Wrap the bubble in a
[Collapsible]({% url 'page' slug='collapsible' %}) and put the toggle in the
content, as upstream does: the bubble stays presentational and the open state
lives one level up.
:::pt-br
### Mostrar mais

Uma mensagem longa vira um paredão. Envolva o bubble num
[Collapsible]({% url 'page' slug='collapsible' %}) e ponha o botão de abrir no
conteúdo, como faz o upstream: o bubble continua só de apresentação e o estado
de aberto mora um nível acima.
:::

<c-docs.example>
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
</c-docs.example>

:::en
### Tooltip

A [Tooltip]({% url 'page' slug='tooltip' %}) around the bubble shows when a
message was sent, without a timestamp under every line.
:::pt-br
### Tooltip

Um [Tooltip]({% url 'page' slug='tooltip' %}) em volta do bubble mostra quando
uma mensagem foi enviada, sem um horário embaixo de cada linha.
:::

<c-docs.example>
<c-tooltip>
  <c-tooltip.trigger>
    <c-bubble variant="muted">
      <c-bubble.content tag="button">Did the deploy go out?</c-bubble.content>
    </c-bubble>
  </c-tooltip.trigger>
  <c-tooltip.content>Sent at 14:32</c-tooltip.content>
</c-tooltip>
</c-docs.example>

:::en
### Popover

A bubble rendered as a button can open a
[Popover]({% url 'page' slug='popover' %}) with the actions for that message.
:::pt-br
### Popover

Um bubble renderizado como botão pode abrir um
[Popover]({% url 'page' slug='popover' %}) com as ações daquela mensagem.
:::

<c-docs.example>
<c-popover>
  <c-popover.trigger>
    <c-bubble align="end">
      <c-bubble.content tag="button">Can you review my pull request?</c-bubble.content>
    </c-bubble>
  </c-popover.trigger>
  <c-popover.content class="w-48">
    <div class="flex flex-col gap-1 text-sm">
      <c-button variant="ghost" size="sm" class="justify-start">Reply</c-button>
      <c-button variant="ghost" size="sm" class="justify-start">Copy text</c-button>
    </div>
  </c-popover.content>
</c-popover>
</c-docs.example>

:::en
## RTL

`align` is logical: `start` is the reader's side of the line and `end` the far
side, so under `dir="rtl"` a conversation mirrors with the text. Reactions sit
on the corner `align` names, and move with it.

## Accessibility

**Labelling reactions.** A row of emoji says nothing to a screen reader on its
own. Name it:
:::pt-br
## RTL

O `align` é lógico: `start` é o lado do leitor na linha e `end` o lado oposto,
então sob `dir="rtl"` uma conversa espelha junto com o texto. As reações ficam
no canto que o `align` nomeia, e se movem com ele.

## Acessibilidade

**Rotulando reações.** Uma fileira de emojis sozinha não diz nada a um leitor
de tela. Dê um nome a ela:
:::

```html
<c-bubble.reactions role="img" aria-label="Reactions: fire, and 8 more">
  <span>🔥</span>
  <span>+8</span>
</c-bubble.reactions>
```

:::en
**Interactive bubbles.** A bubble with `tag="button"` or `tag="a"` is a real
control, focusable and announced as one. Its text is its name, so keep it the
action, not a fragment of the message around it.

**Meaning beyond colour.** Who sent a message is shown by the side and the
colour, neither of which a screen reader hears. Put the sender's name in a
[Message]({% url 'page' slug='message' %}) header, or in visually hidden text.

## API reference
:::pt-br
**Bubbles interativos.** Um bubble com `tag="button"` ou `tag="a"` é um
controle de verdade, focável e anunciado como tal. O texto dele é o nome, então
mantenha-o como a ação, e não como um trecho da mensagem em volta.

**Significado além da cor.** Quem enviou uma mensagem aparece pelo lado e pela
cor, e nenhum dos dois chega a um leitor de tela. Ponha o nome de quem enviou
num cabeçalho de [Message]({% url 'page' slug='message' %}), ou num texto
visualmente escondido.

## Referência da API
:::

<c-docs.api-reference name="bubble" />
