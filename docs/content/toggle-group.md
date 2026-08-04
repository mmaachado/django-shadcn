---
title: Toggle Group
description: A set of toggles that share one outline.
description.pt-br: Um conjunto de toggles que dividem o mesmo contorno.
description.es: Un conjunto de toggles que comparten un mismo contorno.
---

<c-docs.demo-section class="min-h-[350px]">
<c-toggle-group variant="outline">
<c-toggle-group.item aria-label="Bold"><span class="font-bold">B</span></c-toggle-group.item>
<c-toggle-group.item aria-label="Italic"><span class="italic">I</span></c-toggle-group.item>
<c-toggle-group.item aria-label="Underline"><span class="underline">U</span></c-toggle-group.item>
</c-toggle-group>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add toggle-group
```

## Usage

<c-docs.demo-section>
<c-toggle-group>
<c-toggle-group.item>Left</c-toggle-group.item>
<c-toggle-group.item>Center</c-toggle-group.item>
<c-toggle-group.item>Right</c-toggle-group.item>
</c-toggle-group>
</c-docs.demo-section>

```html
<c-toggle-group>
    <c-toggle-group.item>Left</c-toggle-group.item>
    <c-toggle-group.item>Center</c-toggle-group.item>
    <c-toggle-group.item>Right</c-toggle-group.item>
</c-toggle-group>
```

Variant and size go on the group, not on each item.

## Examples

### Outline

<c-docs.demo-section>
<c-toggle-group variant="outline">
<c-toggle-group.item>Left</c-toggle-group.item>
<c-toggle-group.item>Center</c-toggle-group.item>
<c-toggle-group.item>Right</c-toggle-group.item>
</c-toggle-group>
</c-docs.demo-section>

```html
<c-toggle-group variant="outline">
    <c-toggle-group.item>Left</c-toggle-group.item>
    <c-toggle-group.item>Center</c-toggle-group.item>
    <c-toggle-group.item>Right</c-toggle-group.item>
</c-toggle-group>
```

### Sizes

<c-docs.demo-section>
<div class="flex flex-col items-center gap-4">
<c-toggle-group variant="outline" size="sm">
<c-toggle-group.item>S</c-toggle-group.item>
<c-toggle-group.item>M</c-toggle-group.item>
<c-toggle-group.item>L</c-toggle-group.item>
</c-toggle-group>
<c-toggle-group variant="outline" size="lg">
<c-toggle-group.item>S</c-toggle-group.item>
<c-toggle-group.item>M</c-toggle-group.item>
<c-toggle-group.item>L</c-toggle-group.item>
</c-toggle-group>
</div>
</c-docs.demo-section>

```html
<c-toggle-group variant="outline" size="sm">...</c-toggle-group>
<c-toggle-group variant="outline" size="lg">...</c-toggle-group>
```

### Spaced

<c-docs.demo-section>
<c-toggle-group variant="outline" spacing="1">
<c-toggle-group.item>Left</c-toggle-group.item>
<c-toggle-group.item>Center</c-toggle-group.item>
<c-toggle-group.item>Right</c-toggle-group.item>
</c-toggle-group>
</c-docs.demo-section>

```html
<c-toggle-group variant="outline" spacing="1">
    <c-toggle-group.item>Left</c-toggle-group.item>
</c-toggle-group>
```

## Notes

Radix hands variant and size down through React context. Cotton has no
equivalent, so the group styles its own children with `[&>*]` selectors. Two
`data-*` conditions on one element combine the way you would expect; two
`group-data-*` would chain into a descendant selector instead, which is why the
rules live on the group rather than on the item.

Each item keeps its own pressed state. Radix also offers single-selection mode,
where picking one clears the rest — that needs shared state and is not here yet.
