---
title: Switch
description: A control that toggles between on and off.
description.pt-br: Um controle que alterna entre ligado e desligado.
description.es: Un control que alterna entre encendido y apagado.
---

<c-docs.demo-section class="min-h-[350px]">
<label class="flex items-center gap-3">
<c-switch name="airplane" />
<span class="text-sm font-medium">Airplane mode</span>
</label>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add switch
```

## Usage

<c-docs.demo-section>
<c-switch name="notifications" checked />
</c-docs.demo-section>

```html
<c-switch name="notifications" checked />
```

The switch is a real `<input type="checkbox">` wrapped in the label that draws
it. It submits with the form, reaches the field through `name`, and answers to
the keyboard without any JavaScript.

## Examples

### Sizes

<c-docs.demo-section>
<div class="flex items-center gap-6">
<c-switch size="sm" checked />
<c-switch checked />
</div>
</c-docs.demo-section>

```html
<c-switch size="sm" />
<c-switch />
```

### With a label

<c-docs.demo-section>
<label class="flex items-center gap-3">
<c-switch name="marketing" />
<span class="text-sm font-medium">Send me product updates</span>
</label>
</c-docs.demo-section>

```html
<label class="flex items-center gap-3">
    <c-switch name="marketing" />
    <span class="text-sm font-medium">Send me product updates</span>
</label>
```

### Disabled

<c-docs.demo-section>
<div class="flex items-center gap-6">
<c-switch disabled />
<c-switch checked disabled />
</div>
</c-docs.demo-section>

```html
<c-switch disabled />
<c-switch checked disabled />
```

## Notes

Radix renders a button and mirrors the state into `data-state`. Here the
checked state lives in the input itself, and the styling reads it with
`has-[:checked]` on the wrapper and `group-has-[:checked]` on the thumb. The
practical difference is that this one is a form control: no hidden field, no
JavaScript, and `checked` works the way it does anywhere else.
