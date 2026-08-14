---
title: Slider
description: Pick a value from a range.
description.pt-br: Escolhe um valor dentro de um intervalo.
description.es: Elige un valor dentro de un intervalo.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="w-[320px]"><c-slider name="volume" value="60" /></div>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add slider
```

## Usage

<c-docs.demo-section>
<div class="w-[320px]"><c-slider name="volume" value="50" /></div>
</c-docs.demo-section>

```html
<div class="w-[320px]">
    <c-slider name="volume" value="50" />
</div>
```

The slider fills the width it is given, so set the width on a wrapper
rather than passing a `w-*` class to the component: two width utilities on
the same element are settled by the compiled stylesheet, not by you.

A real `<input type="range">` sits transparent on top and carries the value,
the keyboard and the form submission. The track, the filled range and the thumb
below it are what you see, which keeps the styling in utility classes instead
of vendor pseudo-elements.

## Examples

### Range and step

<c-docs.demo-section>
<div class="flex w-[320px] flex-col gap-6">
<c-slider name="temperature" min="16" max="30" step="1" value="22" />
<c-slider name="ratio" min="0" max="1" step="0.05" value="0.4" />
</div>
</c-docs.demo-section>

```html
<c-slider name="temperature" min="16" max="30" step="1" value="22" />
<c-slider name="ratio" min="0" max="1" step="0.05" value="0.4" />
```

### Disabled

<c-docs.demo-section>
<div class="w-[320px]"><c-slider value="35" disabled /></div>
</c-docs.demo-section>

```html
<c-slider value="35" disabled />
```

## Notes

Radix supports several thumbs on one track for a range selection. That needs
shared state between thumbs and is not here; one value per slider.
