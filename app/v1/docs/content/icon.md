---
title: Icon
description: Lucide icons as a cotton component. Every icon used by the library goes through it.
description.pt-br: Ícones do lucide como componente cotton. Todo ícone da biblioteca passa por ele.
description.es: Iconos de lucide como componente cotton. Todo icono de la biblioteca pasa por él.
---

<c-docs.demo-section class="min-h-[350px]">

<div class="flex items-center gap-6">
            <c-icon name="search" />
            <c-icon name="check" />
            <c-icon name="chevron-down" />
            <c-icon name="x" />
        </div>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add icon
```

Components that use icons pull this one in on their own, so most of the time
it is already installed.

## Usage

<c-docs.demo-section>
<c-icon name="search" />
</c-docs.demo-section>

```html
<c-icon name="search" />
```

The `name` is the icon name as it appears on <a
href="https://lucide.dev/icons" target="_blank" rel="noopener noreferrer"
class="font-medium underline underline-offset-4">lucide.dev</a>, in kebab-
case. Only the icons shipped with the library are available — see the list
below.

## Examples

### Sizing

<c-docs.demo-section>

<div class="flex items-end gap-4">
    <c-icon name="search" class="size-4" />
    <c-icon name="search" class="size-6" />
    <c-icon name="search" class="size-8" />
</div>
</c-docs.demo-section>

```html
<c-icon name="search" class="size-4" />
<c-icon name="search" class="size-6" />
<c-icon name="search" class="size-8" />
```

### Color

<c-docs.demo-section>

<div class="flex items-center gap-4">
    <c-icon name="check" class="size-5 text-muted-foreground" />
    <c-icon name="check" class="size-5 text-primary" />
    <c-icon name="check" class="size-5 text-destructive" />
</div>
</c-docs.demo-section>

```html
<c-icon name="check" class="size-5 text-muted-foreground" />
```

### Inside a button

<c-docs.demo-section>
<c-button variant="outline">
<c-icon name="search" class="size-4" />
Search
</c-button>
</c-docs.demo-section>

```html
<c-button variant="outline">
  <c-icon name="search" class="size-4" />
  Search
</c-button>
```

### Reacting to state

<c-docs.demo-section>

<div x-data="{ open: false }" class="flex items-center gap-3">
    <c-button variant="outline" x-on:click="open = !open">Toggle</c-button>
    <c-icon
        name="chevron-down"
        class="size-5 transition-transform"
        x-bind:class="{ 'rotate-180': open }"
    />
</div>
</c-docs.demo-section>

```html
<c-icon
    name='chevron-down'
    class='size-5 transition-transform'
    x-bind:class=\"{ 'rotate-180': open }\"
/>
```

### Accessibility

<c-docs.demo-section>

<div class="flex items-center gap-4">
    <c-icon name="x" class="size-5" aria-hidden="true" />
    <c-icon name="search" class="size-5" role="img" aria-label="Search" />
</div>
</c-docs.demo-section>

```html
<!-- decorative, next to a visible label -->
<c-icon name="x" class="size-5" aria-hidden="true" />

<!-- carries the meaning on its own -->
<c-icon name="search" class="size-5" role="img" aria-label="Search" />
```

## Available icons

The library ships only the icons its components use. Each one lives in its
own file under `icon/` and is generated from lucide, never written by hand.

<c-docs.demo-section>
<div class="grid w-full grid-cols-2 gap-4 sm:grid-cols-3 md:grid-cols-4">
{% for name in icons %}
<div class="flex flex-col items-center gap-2 rounded-md border p-4">
<c-icon name="{{ name }}" class="size-6" />
<span class="text-xs text-muted-foreground">{{ name }}</span>
</div>
{% endfor %}
</div>
</c-docs.demo-section>

## Adding an icon

Reference it in your markup with `&lt;c-icon name="..."&gt;` and run the
generator. It reads the icon names straight out of the templates, downloads
what is missing from lucide and drops whatever nothing references anymore.

```bash
uv run python scripts/generate_icons.py
```

## License

Icons come from <a href="https://lucide.dev" target="_blank" rel="noopener
noreferrer" class="font-medium underline underline-offset-4">Lucide</a>,
under the ISC license. The full notice ships with the component, in
`icon/LICENSE`.
