---
title: Marker
description: The rows in a transcript that are not messages: status, system notes, tool activity and date breaks.
description.pt-br: As linhas de uma conversa que não são mensagens: status, avisos do sistema, atividade de ferramentas e quebras de data.
description.es: Las filas de una conversación que no son mensajes: estado, avisos del sistema, actividad de herramientas y cortes de fecha.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="flex w-full max-w-md flex-col gap-4 text-left">
<c-marker>
<c-marker.icon>
<c-icon name="check" />
</c-marker.icon>
<c-marker.content>Explored 4 files</c-marker.content>
</c-marker>
<c-marker variant="separator">
<c-marker.content>Today</c-marker.content>
</c-marker>
<c-marker role="status">
<c-marker.icon>
<c-icon name="loader-circle" class="animate-spin" />
</c-marker.icon>
<c-marker.content class="shimmer">Compacting conversation</c-marker.content>
</c-marker>
</div>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add marker
```

## Usage

```html
<c-marker>
    <c-marker.icon>
        <c-icon name="check" />
    </c-marker.icon>
    <c-marker.content>Explored 4 files</c-marker.content>
</c-marker>
```

The icon slot is decorative and hidden from assistive technology, so the content
has to carry the whole meaning on its own. Nothing here is stateful.

## Variants

<c-docs.demo-section>
<div class="flex w-full max-w-md flex-col gap-6 text-left">
<c-marker>
<c-marker.icon>
<c-icon name="check" />
</c-marker.icon>
<c-marker.content>Default, an inline row</c-marker.content>
</c-marker>
<c-marker variant="border">
<c-marker.icon>
<c-icon name="check" />
</c-marker.icon>
<c-marker.content>Border, with a rule underneath</c-marker.content>
</c-marker>
<c-marker variant="separator">
<c-marker.content>Separator, centred between two rules</c-marker.content>
</c-marker>
</div>
</c-docs.demo-section>

```html
<c-marker variant="border">...</c-marker>
<c-marker variant="separator">
    <c-marker.content>Today</c-marker.content>
</c-marker>
```

`separator` draws its rules with `before` and `after`, so an icon inside it
lands between the label and the left rule rather than at the start of the row.
Date breaks usually read better without one.

## Examples

### Announcing a change

A marker that reports work in progress should be announced, not just drawn.
`role="status"` reaches the root through the attributes, and the shimmer marks
the text as live.

<c-docs.demo-section>
<div class="flex w-full max-w-md flex-col gap-4 text-left">
<c-marker role="status">
<c-marker.icon>
<c-icon name="loader-circle" class="animate-spin" />
</c-marker.icon>
<c-marker.content class="shimmer">Thinking</c-marker.content>
</c-marker>
</div>
</c-docs.demo-section>

```html
<c-marker role="status">
    <c-marker.icon>
        <c-icon name="loader-circle" class="animate-spin" />
    </c-marker.icon>
    <c-marker.content class="shimmer">Thinking</c-marker.content>
</c-marker>
```

`shimmer` is a utility in `input.css`, not part of the component. It works on
any text element and turns itself off when the reader has asked for reduced
motion.

### Linking out

A marker can point somewhere. Put the link in the content rather than on the
root, so only the words are clickable and the row keeps its layout.

<c-docs.demo-section>
<div class="flex w-full max-w-md flex-col gap-4 text-left">
<c-marker>
<c-marker.icon>
<c-icon name="check" />
</c-marker.icon>
<c-marker.content>
<a href="{% url 'page' slug='installation' %}">Opened the installation guide</a>
</c-marker.content>
</c-marker>
</div>
</c-docs.demo-section>

```html
<c-marker>
    <c-marker.icon>
        <c-icon name="check" />
    </c-marker.icon>
    <c-marker.content>
        <a href="/pull/482/">View the pull request</a>
    </c-marker.content>
</c-marker>
```

### In a transcript

Between messages, a marker is the line that explains a gap.

<c-docs.demo-section>
<c-message.group class="w-full max-w-md text-left">
<c-message>
<c-message.content>
<c-bubble variant="muted">
<c-bubble.content>Give me a moment, I am reading the registry.</c-bubble.content>
</c-bubble>
</c-message.content>
</c-message>
<c-marker>
<c-marker.icon>
<c-icon name="search" />
</c-marker.icon>
<c-marker.content>Explored 4 files</c-marker.content>
</c-marker>
<c-message>
<c-message.content>
<c-bubble variant="muted">
<c-bubble.content>Found it. The entry was never added.</c-bubble.content>
</c-bubble>
</c-message.content>
</c-message>
</c-message.group>
</c-docs.demo-section>
