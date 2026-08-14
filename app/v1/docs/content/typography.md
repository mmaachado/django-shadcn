---
title: Typography
description: Styles for headings, paragraphs, lists and inline text.
description.pt-br: Estilos para títulos, parágrafos, listas e texto em linha.
description.es: Estilos para títulos, párrafos, listas y texto en línea.
---

<c-docs.demo-section class="min-h-[350px]">

<div class="text-left">
            <c-typography.h2 class="mt-0">The Joke Tax</c-typography.h2>
            <c-typography.p>
                The king's subjects were not amused. They grumbled and complained,
                but the king was firm.
            </c-typography.p>
        </div>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add typography
```

## Usage

```html
<c-typography.h1>Taxing Laughter</c-typography.h1>
<c-typography.p>The king thought long and hard.</c-typography.p>
```

shadcn/ui documents typography as utility classes rather than shipping a
component. There is no per-file equivalent of a `prose` wrapper in a Django
template, so each style is its own subcomponent here. The classes are the
ones from the original page, unchanged.

## Examples

### h1

<c-docs.demo-section>
<c-typography.h1>Taxing Laughter: The Joke Tax Chronicles</c-typography.h1>
</c-docs.demo-section>

```html
<c-typography.h1>Taxing Laughter</c-typography.h1>
```

### h2

<c-docs.demo-section>
<c-typography.h2 class="w-full">The People of the Kingdom</c-typography.h2>
</c-docs.demo-section>

```html
<c-typography.h2>The People of the Kingdom</c-typography.h2>
```

### h3

<c-docs.demo-section>
<c-typography.h3>The Joke Tax</c-typography.h3>
</c-docs.demo-section>

```html
<c-typography.h3>The Joke Tax</c-typography.h3>
```

### h4

<c-docs.demo-section>
<c-typography.h4>People stopped telling jokes</c-typography.h4>
</c-docs.demo-section>

```html
<c-typography.h4>People stopped telling jokes</c-typography.h4>
```

### Paragraph

<c-docs.demo-section>
<c-typography.p>
The king, seeing how much happier his subjects were, realized the
error of his ways and repealed the joke tax.
</c-typography.p>
</c-docs.demo-section>

```html
<c-typography.p>The king repealed the joke tax.</c-typography.p>
```

### Blockquote

<c-docs.demo-section>
<c-typography.blockquote>
"After all," he said, "everyone enjoys a good joke, so it's only
fair that they should pay for the privilege."
</c-typography.blockquote>
</c-docs.demo-section>

```html
<c-typography.blockquote>After all, he said.</c-typography.blockquote>
```

### List

<c-docs.demo-section>
<c-typography.list>
<li>1st level of puns: 5 gold coins</li>
<li>2nd level of jokes: 10 gold coins</li>
<li>3rd level of one-liners: 20 gold coins</li>
</c-typography.list>
</c-docs.demo-section>

```html
<c-typography.list>
  <li>1st level of puns: 5 gold coins</li>
  <li>2nd level of jokes: 10 gold coins</li>
</c-typography.list>
```

### Inline code

<c-docs.demo-section>
<c-typography.code>django-cotton</c-typography.code>
</c-docs.demo-section>

```html
<c-typography.code>django-cotton</c-typography.code>
```

### Lead

<c-docs.demo-section>
<c-typography.lead>
A modal dialog that interrupts the user with important content and
expects a response.
</c-typography.lead>
</c-docs.demo-section>

```html
<c-typography.lead>A modal dialog.</c-typography.lead>
```

### Large

<c-docs.demo-section>
<c-typography.large>Are you absolutely sure?</c-typography.large>
</c-docs.demo-section>

```html
<c-typography.large>Are you absolutely sure?</c-typography.large>
```

### Small

<c-docs.demo-section>
<c-typography.small>Email address</c-typography.small>
</c-docs.demo-section>

```html
<c-typography.small>Email address</c-typography.small>
```

### Muted

<c-docs.demo-section>
<c-typography.muted>Enter your email address.</c-typography.muted>
</c-docs.demo-section>

```html
<c-typography.muted>Enter your email address.</c-typography.muted>
```
