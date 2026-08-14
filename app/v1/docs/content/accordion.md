---
title: Accordion
description: A vertically stacked set of interactive headings that each reveal a section of content.
description.pt-br: Cabeçalhos empilhados que revelam, cada um, uma seção de conteúdo.
description.es: Encabezados apilados que revelan, cada uno, una sección de contenido.
---

<c-docs.demo-section class="min-h-[350px]">
<c-accordion type="single" collapsible="true" class="w-[450px]">
          <c-accordion.item value="item-1">
            <c-accordion.trigger value="item-1">Is it for Django?</c-accordion.trigger>
            <c-accordion.content value="item-1">
              Yes. All components are compatible with Django.
            </c-accordion.content>
          </c-accordion.item>

<c-accordion.item value="item-2">
  <c-accordion.trigger value="item-2">Is it styled?</c-accordion.trigger>
  <c-accordion.content value="item-2">
    Yes. It comes with default styles that match the other components in this library.
  </c-accordion.content>
</c-accordion.item>

          <c-accordion.item value="item-3">
            <c-accordion.trigger value="item-3">Is it animated?</c-accordion.trigger>
            <c-accordion.content value="item-3">
              Yes. It's animated by default, but you can disable it if you prefer.
            </c-accordion.content>
          </c-accordion.item>
        </c-accordion>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add accordion
```

<p class="mt-4 text-sm text-muted-foreground">
    <strong>Note:</strong> This component requires the <a href="https://alpinejs.dev/plugins/collapse" target="_blank" rel="noopener noreferrer" class="underline">Alpine.js Collapse plugin</a> for animations.
</p>

## Usage

```html
<c-accordion type='single' collapsible='true'>
    <c-accordion.item value='item-1'>
        <c-accordion.trigger value='item-1'>Is it for Django?</c-accordion.trigger>
        <c-accordion.content value='item-1'>
            Yes. All components are compatible with Django.
        </c-accordion.content>
    </c-accordion.item>
</c-accordion>
```
