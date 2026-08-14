---
title: Input Group
description: Wraps an input with icons, text or buttons inside a single outline.
description.pt-br: Envolve um campo com ícones, texto ou botões sob um contorno só.
description.es: Envuelve un campo con iconos, texto o botones bajo un solo contorno.
---

<c-docs.demo-section class="min-h-[350px]">
<c-input-group class="w-[320px]">
<c-input-group.addon>
<c-icon name="search" />
</c-input-group.addon>
<c-input-group.input placeholder="Search components..." />
</c-input-group>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add input_group
```

## Usage

```html
<c-input-group>
  <c-input-group.addon>
    <c-icon name="search" />
  </c-input-group.addon>
  <c-input-group.input placeholder="Search..." />
</c-input-group>
```

The outline and the focus ring live on the group, not on the input. Use
`c-input-group.input` rather than a plain `c-input` so the group can pick up
focus and validation state.

## Examples

### Leading and trailing

<c-docs.demo-section>

<div class="flex w-full flex-col gap-4">
    <c-input-group>
        <c-input-group.addon>
            <c-input-group.text>$</c-input-group.text>
        </c-input-group.addon>
        <c-input-group.input placeholder="0.00" />
        <c-input-group.addon align="inline-end">
            <c-input-group.text>USD</c-input-group.text>
        </c-input-group.addon>
    </c-input-group>
    <c-input-group>
        <c-input-group.input placeholder="Search..." />
        <c-input-group.addon align="inline-end">
            <c-kbd.group>
                <c-kbd>⌘</c-kbd>
                <c-kbd>K</c-kbd>
            </c-kbd.group>
        </c-input-group.addon>
    </c-input-group>
</div>
</c-docs.demo-section>

```html
<c-input-group>
  <c-input-group.addon>
    <c-input-group.text>$</c-input-group.text>
  </c-input-group.addon>
  <c-input-group.input placeholder="0.00" />
  <c-input-group.addon align="inline-end">
    <c-input-group.text>USD</c-input-group.text>
  </c-input-group.addon>
</c-input-group>
```

### With a button

<c-docs.demo-section>
<c-input-group>
<c-input-group.input placeholder="Paste a link" />
<c-input-group.addon align="inline-end">
<c-input-group.button size="sm" variant="outline">Copy</c-input-group.button>
</c-input-group.addon>
</c-input-group>
</c-docs.demo-section>

```html
<c-input-group.addon align="inline-end">
  <c-input-group.button size="sm" variant="outline">Copy</c-input-group.button>
</c-input-group.addon>
```

### Textarea with a block addon

<c-docs.demo-section>
<c-input-group>
<c-input-group.textarea placeholder="Write a message..." rows="3" />
<c-input-group.addon align="block-end" class="border-t">
<c-input-group.text>Markdown supported</c-input-group.text>
<c-input-group.button size="sm" class="ml-auto">Send</c-input-group.button>
</c-input-group.addon>
</c-input-group>
</c-docs.demo-section>

```html
<c-input-group>
  <c-input-group.textarea placeholder="Write a message..." rows="3" />
  <c-input-group.addon align="block-end" class="border-t">
    <c-input-group.button size="sm">Send</c-input-group.button>
  </c-input-group.addon>
</c-input-group>
```

### Invalid

<c-docs.demo-section>
<c-input-group>
<c-input-group.input placeholder="you@example.com" aria-invalid="true" />
<c-input-group.addon align="inline-end">
<c-icon name="x" class="text-destructive" />
</c-input-group.addon>
</c-input-group>
</c-docs.demo-section>

```html
<c-input-group.input aria-invalid="true" />
```

## Notes

`c-input-group.input`, `.textarea` and `.button` render their own element
rather than wrapping `c-input`, `c-textarea` and `c-button`. cotton silently
drops the `attrs` spread when it lands on another component, and these
controls have to forward whatever you put on them.

Their sizes come from the group, not from `c-button`: `xs`, `sm`, `icon-xs`
and `icon-sm`.

Clicking an addon focuses the input, which needs Alpine. The addon carries
its own `x-data`, so it works without an Alpine scope around it.
