---
title: Radio Group
description: A set of options where only one can be picked.
description.pt-br: Um conjunto de opções em que só uma pode ser escolhida.
description.es: Un conjunto de opciones donde solo se puede elegir una.
---

<c-docs.demo-section class="min-h-[350px]">
<c-radio-group class="text-left">
<label class="flex items-center gap-3">
<c-radio-group.item name="plan" value="free" checked />
<span class="text-sm font-medium">Free</span>
</label>
<label class="flex items-center gap-3">
<c-radio-group.item name="plan" value="pro" />
<span class="text-sm font-medium">Pro</span>
</label>
<label class="flex items-center gap-3">
<c-radio-group.item name="plan" value="team" />
<span class="text-sm font-medium">Team</span>
</label>
</c-radio-group>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add radio_group
```

## Usage

<c-docs.demo-section>
<c-radio-group class="text-left">
<label class="flex items-center gap-3">
<c-radio-group.item name="delivery" value="standard" checked />
<span class="text-sm font-medium">Standard</span>
</label>
<label class="flex items-center gap-3">
<c-radio-group.item name="delivery" value="express" />
<span class="text-sm font-medium">Express</span>
</label>
</c-radio-group>
</c-docs.demo-section>

```html
<c-radio-group>
    <label class="flex items-center gap-3">
        <c-radio-group.item name="delivery" value="standard" checked />
        <span class="text-sm font-medium">Standard</span>
    </label>
    <label class="flex items-center gap-3">
        <c-radio-group.item name="delivery" value="express" />
        <span class="text-sm font-medium">Express</span>
    </label>
</c-radio-group>
```

Items are native radios, so `name` groups them and the browser handles the
exclusivity, the keyboard and the form submission.

## Examples

### From a Django form

```html
<c-radio-group>
    {% for radio in form.delivery %}
        <label class="flex items-center gap-3">
            <c-radio-group.item name="{{ radio.name }}" value="{{ radio.data.value }}" />
            <span class="text-sm font-medium">{{ radio.choice_label }}</span>
        </label>
    {% endfor %}
</c-radio-group>
```

### Disabled

<c-docs.demo-section>
<c-radio-group class="text-left">
<label class="flex items-center gap-3">
<c-radio-group.item name="tier" value="one" checked disabled />
<span class="text-sm font-medium text-muted-foreground">Locked in</span>
</label>
<label class="flex items-center gap-3">
<c-radio-group.item name="tier" value="two" disabled />
<span class="text-sm font-medium text-muted-foreground">Not available</span>
</label>
</c-radio-group>
</c-docs.demo-section>

```html
<c-radio-group.item name="tier" value="one" checked disabled />
```

## Notes

Radix draws the dot with a nested indicator element. A native radio cannot hold
children, so the dot here is the background painted onto the content box only —
`bg-clip-content` with a small padding shrinks it to a circle in the middle.
The visible result is the same and the control stays a real form field.
