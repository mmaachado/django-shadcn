---
title: Dialog
description: A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.
description.pt-br: Uma janela sobreposta à principal, que desativa o conteúdo abaixo.
description.es: Una ventana superpuesta a la principal, que desactiva el contenido de debajo.
---

<c-docs.demo-section class="min-h-[350px]">
<c-dialog>
<c-dialog.trigger>Open Dialog</c-dialog.trigger>
<c-dialog.content>
<c-dialog.header>
<c-dialog.title>Are you absolutely sure?</c-dialog.title>
<c-dialog.description>
This action is permanent and cannot be undone.
</c-dialog.description>
</c-dialog.header>
<div class="flex justify-end gap-2 pt-4">
<c-button variant="outline" @click="hideDialog">Cancel</c-button>
<c-button variant="default">Submit</c-button>
</div>
</c-dialog.content>
</c-dialog>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add dialog
```

## Usage

```html
<c-dialog>
  <c-dialog.trigger>Open Dialog</c-dialog.trigger>
  <c-dialog.content>
    <c-dialog.header>
      <c-dialog.title>Are you absolutely sure?</c-dialog.title>
      <c-dialog.description>
        This action is permanent and cannot be undone.
      </c-dialog.description>
    </c-dialog.header>
    <div class="flex justify-end gap-2 pt-4">
      <c-button variant="outline" @click="hideDialog">Cancel</c-button>
      <c-button variant="default">Submit</c-button>
    </div>
  </c-dialog.content>
</c-dialog>
```
