---
title: Input
description: Displays a form input field or a component that looks like an input field.
description.pt-br: Exibe um campo de formulário, ou um componente com cara de campo.
description.es: Muestra un campo de formulario, o un componente con aspecto de campo.
---

<c-docs.demo-section class="min-h-[350px]">
<c-input type="email" placeholder="Email" />
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add input
```

## Usage

<c-docs.demo-section>
<c-input type="email" placeholder="Email" />
</c-docs.demo-section>

```html
<c-input type="email" placeholder="Email" />
```

## Examples

### Default

<c-docs.demo-section>
<c-input type="email" placeholder="Email" />
</c-docs.demo-section>

```html
<c-input type="email" placeholder="Email" />
```

### File

<c-docs.demo-section>
<c-input type="file" id="picture" />
</c-docs.demo-section>

```html
<c-input type="file" id="picture" />
```

### Disabled

<c-docs.demo-section>
<c-input type="email" placeholder="Email" disabled />
</c-docs.demo-section>

```html
<c-input type="email" placeholder="Email" disabled />
```

### With Label

<c-docs.demo-section>

<div class="grid w-full max-w-sm items-center gap-1.5">
    <c-label for="email">Email</c-label>
    <c-input type="email" placeholder="you@example.com" />
</div>
</c-docs.demo-section>

```html
<div class="grid w-full max-w-sm items-center gap-1.5">
  <c-label for="email">Email</c-label>
  <c-input type="email" placeholder="you@example.com" />
</div>
```

### With Button

<c-docs.demo-section>

<div class="flex w-full max-w-sm items-center space-x-2">
    <c-input type="email" placeholder="you@example.com" />
    <c-button type="submit">Subscribe</c-button>
</div>
</c-docs.demo-section>

```html
<div class="flex w-full max-w-sm items-center space-x-2">
  <c-input type="email" placeholder="you@example.com" />
  <c-button type="submit">Subscribe</c-button>
</div>
```
