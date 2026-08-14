---
title: Empty
description: Use to display an empty state, when there is nothing to show yet.
description.pt-br: Para quando ainda não há nada a mostrar.
description.es: Para cuando todavía no hay nada que mostrar.
---

<c-docs.demo-section class="min-h-[350px]">
<c-empty class="w-full border">
<c-empty.header>
<c-empty.media variant="icon">
<c-icon name="search" />
</c-empty.media>
<c-empty.title>No results found</c-empty.title>
<c-empty.description>
Try adjusting your search or filters to find what you are
looking for.
</c-empty.description>
</c-empty.header>
<c-empty.content>
<c-button variant="outline">Clear filters</c-button>
</c-empty.content>
</c-empty>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add empty
```

## Usage

```html
<c-empty>
  <c-empty.header>
    <c-empty.media variant="icon">
      <c-icon name="search" />
    </c-empty.media>
    <c-empty.title>No results found</c-empty.title>
    <c-empty.description>Try a different search.</c-empty.description>
  </c-empty.header>
  <c-empty.content>
    <c-button variant="outline">Clear filters</c-button>
  </c-empty.content>
</c-empty>
```

The border is dashed but no border width is applied, exactly as upstream.
Add `border` when you want the outline to show.

## Examples

### Outline

<c-docs.demo-section>
<c-empty class="w-full border">
<c-empty.header>
<c-empty.media variant="icon">
<c-icon name="x" />
</c-empty.media>
<c-empty.title>No projects</c-empty.title>
<c-empty.description>
Projects you create will show up here.
</c-empty.description>
</c-empty.header>
<c-empty.content>
<c-button>Create project</c-button>
</c-empty.content>
</c-empty>
</c-docs.demo-section>

```html
<c-empty class="border">...</c-empty>
```

### Without media

<c-docs.demo-section>
<c-empty class="w-full border">
<c-empty.header>
<c-empty.title>Nothing here yet</c-empty.title>
<c-empty.description>
Read the <a href="{% url 'page' slug='introduction' %}">introduction</a> to get
started.
</c-empty.description>
</c-empty.header>
</c-empty>
</c-docs.demo-section>

```html
<c-empty>
  <c-empty.header>
    <c-empty.title>Nothing here yet</c-empty.title>
    <c-empty.description>Read the docs to get started.</c-empty.description>
  </c-empty.header>
</c-empty>
```

### Loading

<c-docs.demo-section>
<c-empty class="w-full border">
<c-empty.header>
<c-empty.media>
<c-spinner class="size-6" />
</c-empty.media>
<c-empty.title>Loading projects</c-empty.title>
<c-empty.description>This will only take a moment.</c-empty.description>
</c-empty.header>
</c-empty>
</c-docs.demo-section>

```html
<c-empty.media>
  <c-spinner class="size-6" />
</c-empty.media>
```
