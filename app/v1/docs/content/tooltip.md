---
title: Tooltip
description: A short label that appears on hover or focus.
description.pt-br: Um rótulo curto que aparece ao passar o mouse ou focar.
description.es: Una etiqueta breve que aparece al pasar el ratón o enfocar.
---

<c-docs.demo-section class="min-h-[350px]">
<c-tooltip>
<c-tooltip.trigger>
<c-button variant="outline">Hover me</c-button>
</c-tooltip.trigger>
<c-tooltip.content>Add to library</c-tooltip.content>
</c-tooltip>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add tooltip
```

## Usage

<c-docs.demo-section>
<c-tooltip>
<c-tooltip.trigger>
<c-button variant="outline">Hover me</c-button>
</c-tooltip.trigger>
<c-tooltip.content>Add to library</c-tooltip.content>
</c-tooltip>
</c-docs.demo-section>

```html
<c-tooltip>
    <c-tooltip.trigger>
        <c-button variant="outline">Hover me</c-button>
    </c-tooltip.trigger>
    <c-tooltip.content>Add to library</c-tooltip.content>
</c-tooltip>
```

The trigger reacts to `mouseenter` and to `focusin`, so the tooltip shows for
the keyboard as well as the pointer.

## Examples

### Sides

<c-docs.demo-section>
<div class="flex items-center gap-4">
<c-tooltip>
<c-tooltip.trigger><c-button variant="outline" size="sm">Top</c-button></c-tooltip.trigger>
<c-tooltip.content side="top">On top</c-tooltip.content>
</c-tooltip>
<c-tooltip>
<c-tooltip.trigger><c-button variant="outline" size="sm">Right</c-button></c-tooltip.trigger>
<c-tooltip.content side="right">To the right</c-tooltip.content>
</c-tooltip>
<c-tooltip>
<c-tooltip.trigger><c-button variant="outline" size="sm">Bottom</c-button></c-tooltip.trigger>
<c-tooltip.content side="bottom">Below</c-tooltip.content>
</c-tooltip>
<c-tooltip>
<c-tooltip.trigger><c-button variant="outline" size="sm">Left</c-button></c-tooltip.trigger>
<c-tooltip.content side="left">To the left</c-tooltip.content>
</c-tooltip>
</div>
</c-docs.demo-section>

```html
<c-tooltip.content side="top">On top</c-tooltip.content>
<c-tooltip.content side="right">To the right</c-tooltip.content>
<c-tooltip.content side="bottom">Below</c-tooltip.content>
<c-tooltip.content side="left">To the left</c-tooltip.content>
```

## Notes

Radix puts the tooltip in a portal and measures the viewport to flip the side
when there is no room. Here the content is positioned against the trigger with
utility classes, so `side` is a choice you make rather than something worked
out at runtime. Near the edge of the screen, pick the side that fits.
