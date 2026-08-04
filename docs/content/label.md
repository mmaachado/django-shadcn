---
title: Label
description: Renders an accessible label associated with controls.
description.pt-br: Um rótulo acessível associado a um controle.
description.es: Una etiqueta accesible asociada a un control.
---

<c-docs.demo-section class="min-h-[350px]">

<div class="grid w-full max-w-sm gap-2 text-left">
            <c-label for="email">Email</c-label>
            <c-input id="email" type="email" placeholder="you@example.com" />
        </div>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add label
```

## Usage

```html
<c-label for="email">Email</c-label> <c-input id="email" type="email" />
```

The `for` attribute has to match the control's `id`. That is what lets a
click on the text focus the field, and what a screen reader announces.

## Examples

### With an input

<c-docs.demo-section>

<div class="grid w-full max-w-sm gap-2">
    <c-label for="project">Project name</c-label>
    <c-input id="project" placeholder="django-shadcn" />
</div>
</c-docs.demo-section>

```html
<c-label for="project">Project name</c-label>
<c-input id="project" placeholder="django-shadcn" />
```

### With a checkbox

<c-docs.demo-section>

<div class="flex items-center space-x-2">
    <c-checkbox id="newsletter" />
    <c-label for="newsletter">Subscribe to the newsletter</c-label>
</div>
</c-docs.demo-section>

```html
<c-checkbox id="newsletter" />
<c-label for="newsletter">Subscribe to the newsletter</c-label>
```

### Required

<c-docs.demo-section>

<div class="grid w-full max-w-sm gap-2">
    <c-label for="handle">
        Handle
        <span class="text-destructive" aria-hidden="true">*</span>
    </c-label>
    <c-input id="handle" required />
</div>
</c-docs.demo-section>

```html
<c-label for="handle">
  Handle
  <span class="text-destructive" aria-hidden="true">*</span>
</c-label>
```

### Disabled control

<c-docs.demo-section>

<div class="grid w-full max-w-sm gap-2">
    <c-input id="locked" class="peer" placeholder="Not editable" disabled />
    <c-label for="locked">Locked field</c-label>
</div>
</c-docs.demo-section>

```html
<c-input id="locked" class="peer" disabled />
<c-label for="locked">Locked field</c-label>
```

## Notes

The dimmed style for a disabled control comes from `peer-disabled:`, so the
control needs the `peer` class and has to come before the label in the
markup.
