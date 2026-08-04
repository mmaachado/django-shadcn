---
title: Avatar
description: An image element with a fallback for representing the user.
description.pt-br: Uma imagem com fallback para representar o usuário.
description.es: Una imagen con alternativa para representar al usuario.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="flex items-center gap-4">
<c-avatar>
<c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
<c-avatar.fallback>MM</c-avatar.fallback>
</c-avatar>
<c-avatar>
<c-avatar.fallback>CN</c-avatar.fallback>
</c-avatar>
</div>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add avatar
```

## Usage

<c-docs.demo-section>
<c-avatar>
<c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
<c-avatar.fallback>MM</c-avatar.fallback>
</c-avatar>
</c-docs.demo-section>

```html
<c-avatar>
  <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
  <c-avatar.fallback>MM</c-avatar.fallback>
</c-avatar>
```

Radix hides the fallback once the image loads. Here the image is stacked on top
of the fallback instead, and removes itself on `error` so the initials show
through. Both are always in the markup.

That last part is one Alpine attribute on the image, with its own `x-data`.
Without Alpine the avatar still works, but a broken source leaves the browser's
broken-image glyph over the fallback.

## Examples

### Sizes

<c-docs.demo-section>
<div class="flex items-center gap-4">
<c-avatar size="sm">
<c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
<c-avatar.fallback>MM</c-avatar.fallback>
</c-avatar>
<c-avatar>
<c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
<c-avatar.fallback>MM</c-avatar.fallback>
</c-avatar>
<c-avatar size="lg">
<c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
<c-avatar.fallback>MM</c-avatar.fallback>
</c-avatar>
</div>
</c-docs.demo-section>

```html
<c-avatar size="sm">...</c-avatar>
<c-avatar>...</c-avatar>
<c-avatar size="lg">...</c-avatar>
```

### Fallback

<c-docs.demo-section>
<c-avatar>
<c-avatar.image src="/does-not-exist.png" alt="" />
<c-avatar.fallback>CN</c-avatar.fallback>
</c-avatar>
</c-docs.demo-section>

```html
<c-avatar>
  <c-avatar.fallback>CN</c-avatar.fallback>
</c-avatar>
```

### Badge

<c-docs.demo-section>
<div class="flex items-center gap-4">
<c-avatar>
<c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
<c-avatar.fallback>MM</c-avatar.fallback>
<c-avatar.badge class="bg-emerald-500!" />
</c-avatar>
<c-avatar size="lg">
<c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
<c-avatar.fallback>MM</c-avatar.fallback>
<c-avatar.badge class="bg-emerald-500!" />
</c-avatar>
</div>
</c-docs.demo-section>

```html
<c-avatar>
  <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
  <c-avatar.fallback>MM</c-avatar.fallback>
  <c-avatar.badge class="bg-emerald-500!" />
</c-avatar>
```

### Group

<c-docs.demo-section>
<c-avatar.group>
<c-avatar>
<c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
<c-avatar.fallback>MM</c-avatar.fallback>
</c-avatar>
<c-avatar>
<c-avatar.image src="https://github.com/SarthakJariwala.png" alt="@SarthakJariwala" />
<c-avatar.fallback>SJ</c-avatar.fallback>
</c-avatar>
<c-avatar>
<c-avatar.image src="https://github.com/shadcn.png" alt="@shadcn" />
<c-avatar.fallback>SH</c-avatar.fallback>
</c-avatar>
<c-avatar.group-count>+3</c-avatar.group-count>
</c-avatar.group>
</c-docs.demo-section>

```html
<c-avatar.group>
  <c-avatar>
    <c-avatar.fallback>MM</c-avatar.fallback>
  </c-avatar>
  <c-avatar>
    <c-avatar.fallback>SJ</c-avatar.fallback>
  </c-avatar>
  <c-avatar.group-count>+3</c-avatar.group-count>
</c-avatar.group>
```

## Notes

The badge defaults to `bg-primary`. Colouring it takes the `!` suffix —
`bg-emerald-500!` — because two background utilities on the same element are
decided by their order in the compiled stylesheet, not by the order you wrote
them. Tailwind sorts them by name, so `bg-primary` lands after
`bg-emerald-500` and wins.

The rule holds for any class of yours that collides with one the component
already sets. It applies to every component here, not just this one.
