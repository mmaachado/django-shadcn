---
title: Sheet
description: Display content that complements the main content of the screen.
description.pt-br: Mostra conteúdo que complementa o principal, vindo de uma das bordas.
description.es: Muestra contenido que complementa al principal, entrando desde un borde.
---

<c-docs.demo-section class="min-h-[350px]">
<c-sheet>
<c-sheet.trigger>
<c-button variant="outline">Open</c-button>
</c-sheet.trigger>
<c-sheet.content side="right">
<c-sheet.header>
<c-sheet.title>Right Sheet</c-sheet.title>
<c-sheet.description>
This sheet appears from the right of the screen.
</c-sheet.description>
</c-sheet.header>
</c-sheet.content>
</c-sheet>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add sheet
```

## Usage

```html
<c-sheet>
  <c-sheet.trigger>
    <c-button variant="outline">Open</c-button>
  </c-sheet.trigger>
  <c-sheet.content side="right">
    <c-sheet.header>
      <c-sheet.title>Right Sheet</c-sheet.title>
      <c-sheet.description>
        This sheet appears from the right of the screen.
      </c-sheet.description>
    </c-sheet.header>
  </c-sheet.content>
</c-sheet>
```

## Examples

###

<c-docs.demo-section>

<div class="grid grid-cols-2 gap-2">
  {% for side in sides %}
    <c-sheet>
      <c-sheet.trigger>
        <c-button variant="outline" class="w-full">{{ side|title }}</c-button>
      </c-sheet.trigger>
      <c-sheet.content side="{{ side }}">
        <c-sheet.header>
          <c-sheet.title>{{ side|title }} Sheet</c-sheet.title>
          <c-sheet.description>
            This sheet appears from the {{ side }} of the screen.
          </c-sheet.description>
        </c-sheet.header>
      </c-sheet.content>
    </c-sheet>
  {% endfor %}
</div>
</c-docs.demo-section>

```html
<div class="grid grid-cols-2 gap-2">
  <c-sheet>
    <c-sheet.trigger>
      <c-button variant="outline" class="w-full">Top</c-button>
    </c-sheet.trigger>
    <c-sheet.content side="top">
      <c-sheet.header>
        <c-sheet.title>Top Sheet</c-sheet.title>
        <c-sheet.description>
          This sheet appears from the top of the screen.
        </c-sheet.description>
      </c-sheet.header>
    </c-sheet.content>
  </c-sheet>
</div>
```

### Adjust Size

<c-docs.demo-section>
<c-sheet>
<c-sheet.trigger>
<c-button variant="outline">Right</c-button>
</c-sheet.trigger>
<c-sheet.content side="right" class="w-[700px] sm:w-[540px]">
<c-sheet.header>
<c-sheet.title>Adjust Sheet Size</c-sheet.title>
<c-sheet.description>
This sheet content is larger and appears from the right of the screen.
</c-sheet.description>
</c-sheet.header>
</c-sheet.content>
</c-sheet>
</c-docs.demo-section>

```html
<c-sheet>
  <c-sheet.trigger>
    <c-button variant="outline" class="w-full">Right</c-button>
  </c-sheet.trigger>
  <c-sheet.content side="right" class="w-[700px] sm:w-[540px]">
    <c-sheet.header>
      <c-sheet.title>Right Sheet</c-sheet.title>
      <c-sheet.description>
        This sheet appears from the right of the screen.
      </c-sheet.description>
    </c-sheet.header>
  </c-sheet.content>
</c-sheet>
```
