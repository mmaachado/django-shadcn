---
title: Card
description: Displays a card with header, content, and footer.
description.pt-br: Um cartão com cabeçalho, conteúdo e rodapé.
description.es: Una tarjeta con encabezado, contenido y pie.
---

<c-docs.demo-section class="min-h-[350px]">
<c-card class="w-[380px]">
<c-card.header>
<c-card.title>Create Project</c-card.title>
<c-card.description>Deploy your new project in one-click.</c-card.description>
</c-card.header>
<c-card.content class="space-y-2">
<div class="flex flex-col space-y-1">
<c-label for="name">Name</c-label>
<c-input id="name" placeholder="Name of your project" />
</div>
</c-card.content>
<c-card.footer class="flex justify-between">
<c-button variant="outline">Cancel</c-button>
<c-button>Submit</c-button>
</c-card.footer>
</c-card>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add card
```

## Usage

```html
<c-card class="w-[380px]">
  <c-card.header>
    <c-card.title>Title</c-card.title>
    <c-card.description>Description</c-card.description>
  </c-card.header>
  <c-card.content>Content</c-card.content>
  <c-card.footer> Footer </c-card.footer>
</c-card>
```

## Examples

###

<c-docs.demo-section>
<c-card class="w-[380px]">
<c-card.header>
<c-card.title>Create Project</c-card.title>
<c-card.description>Deploy your new project in one-click.</c-card.description>
</c-card.header>
<c-card.content class="space-y-2">
<div class="flex flex-col space-y-1">
<c-label for="name">Name</c-label>
<c-input id="name" placeholder="Name of your project" />
</div>
</c-card.content>
<c-card.footer class="flex justify-between">
<c-button variant="outline">Cancel</c-button>
<c-button>Submit</c-button>
</c-card.footer>
</c-card>
</c-docs.demo-section>

```html
<c-card class="w-[380px]">
  <c-card.header>
    <c-card.title>Create Project</c-card.title>
    <c-card.description
      >Deploy your new project in one-click.</c-card.description
    >
  </c-card.header>
  <c-card.content class="space-y-2">
    <div class="flex flex-col space-y-1">
      <c-label for="name">Name</c-label>
      <c-input id="name" placeholder="Name of your project" />
    </div>
  </c-card.content>
  <c-card.footer class="flex justify-between">
    <c-button variant="outline">Cancel</c-button>
    <c-button>Submit</c-button>
  </c-card.footer>
</c-card>
```
