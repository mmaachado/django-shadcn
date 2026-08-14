---
title: Message
description: The row of a chat transcript: avatar, alignment, header and footer around whatever the message itself is.
description.pt-br: A linha de uma conversa: avatar, alinhamento, cabeçalho e rodapé em volta da mensagem.
description.es: La fila de una conversación: avatar, alineación, encabezado y pie alrededor del mensaje.
---

<c-docs.demo-section class="min-h-[350px]">
<c-message.group class="w-full max-w-md text-left">
<c-message>
<c-message.avatar>
<c-avatar>
<c-avatar.fallback>CN</c-avatar.fallback>
</c-avatar>
</c-message.avatar>
<c-message.content>
<c-message.header>Assistant</c-message.header>
<c-bubble variant="muted">
<c-bubble.content>The registry entry was missing, so the CLI refused the name.</c-bubble.content>
</c-bubble>
</c-message.content>
</c-message>
<c-message align="end">
<c-message.content>
<c-bubble align="end">
<c-bubble.content>That explains it. Adding the entry now.</c-bubble.content>
</c-bubble>
<c-message.footer>Sent</c-message.footer>
</c-message.content>
</c-message>
</c-message.group>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add message
```

## Usage

```html
<c-message>
    <c-message.avatar>
        <c-avatar>
            <c-avatar.fallback>CN</c-avatar.fallback>
        </c-avatar>
    </c-message.avatar>
    <c-message.content>
        <c-message.header>Assistant</c-message.header>
        <c-bubble variant="muted">
            <c-bubble.content>How can I help?</c-bubble.content>
        </c-bubble>
        <c-message.footer>Just now</c-message.footer>
    </c-message.content>
</c-message>
```

`message` is layout and nothing else. It decides which side the row sits on and
where the avatar, the header and the footer go; what fills the middle is up to
you. In a chat that is usually a [Bubble]({% url 'page' slug='bubble' %}), but a card, a table or
a plain paragraph all work.

## Alignment

`align="end"` flips the row, and everything inside follows: the content moves to
the far side, the footer aligns with it, and the avatar changes sides.

<c-docs.demo-section>
<c-message.group class="w-full max-w-md text-left">
<c-message>
<c-message.avatar>
<c-avatar>
<c-avatar.fallback>AI</c-avatar.fallback>
</c-avatar>
</c-message.avatar>
<c-message.content>
<c-bubble variant="muted">
<c-bubble.content>Starts on the left.</c-bubble.content>
</c-bubble>
</c-message.content>
</c-message>
<c-message align="end">
<c-message.avatar>
<c-avatar>
<c-avatar.fallback>ME</c-avatar.fallback>
</c-avatar>
</c-message.avatar>
<c-message.content>
<c-bubble align="end">
<c-bubble.content>Ends on the right.</c-bubble.content>
</c-bubble>
</c-message.content>
</c-message>
</c-message.group>
</c-docs.demo-section>

```html
<c-message align="end">
    <c-message.content>
        <c-bubble align="end">
            <c-bubble.content>Ends on the right.</c-bubble.content>
        </c-bubble>
    </c-message.content>
</c-message>
```

## Examples

### Grouped

`group` stacks a run from the same sender. Give the avatar to the last message
of the run and leave it off the others, so the run reads as one turn.

<c-docs.demo-section>
<c-message.group class="w-full max-w-md text-left">
<c-message align="end">
<c-message.content>
<c-bubble align="end">
<c-bubble.content>Three questions, sorry.</c-bubble.content>
</c-bubble>
</c-message.content>
</c-message>
<c-message align="end">
<c-message.content>
<c-bubble align="end">
<c-bubble.content>Where does the registry live?</c-bubble.content>
</c-bubble>
</c-message.content>
</c-message>
<c-message align="end">
<c-message.avatar>
<c-avatar>
<c-avatar.fallback>ME</c-avatar.fallback>
</c-avatar>
</c-message.avatar>
<c-message.content>
<c-bubble align="end">
<c-bubble.content>And does <code>add</code> read it?</c-bubble.content>
</c-bubble>
</c-message.content>
</c-message>
</c-message.group>
</c-docs.demo-section>

```html
<c-message.group>
    <c-message align="end">...</c-message>
    <c-message align="end">...</c-message>
    <c-message align="end">
        <c-message.avatar>...</c-message.avatar>
        ...
    </c-message>
</c-message.group>
```

### Header and footer

The header names the sender and stays where the reader starts, whatever the
alignment. The footer carries status or actions and follows the message side.
When a footer is present the avatar lifts so it stays level with the message
rather than with the timestamp.

<c-docs.demo-section>
<c-message.group class="w-full max-w-md text-left">
<c-message>
<c-message.avatar>
<c-avatar>
<c-avatar.fallback>AI</c-avatar.fallback>
</c-avatar>
</c-message.avatar>
<c-message.content>
<c-message.header>Assistant</c-message.header>
<c-bubble variant="muted">
<c-bubble.content>Both edges of a message are yours to fill.</c-bubble.content>
</c-bubble>
<c-message.footer>Delivered · 09:41</c-message.footer>
</c-message.content>
</c-message>
</c-message.group>
</c-docs.demo-section>

```html
<c-message.content>
    <c-message.header>Assistant</c-message.header>
    <c-bubble variant="muted">
        <c-bubble.content>...</c-bubble.content>
    </c-bubble>
    <c-message.footer>Delivered · 09:41</c-message.footer>
</c-message.content>
```
