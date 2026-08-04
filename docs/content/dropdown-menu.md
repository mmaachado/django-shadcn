---
title: Dropdown Menu
description: Displays a menu to the user — such as a set of actions or functions — triggered by a button.
description.pt-br: Um menu aberto por um botão — um conjunto de ações, por exemplo.
description.es: Un menú que abre un botón — un conjunto de acciones, por ejemplo.
---

<c-docs.demo-section class="min-h-[350px]">
<c-dropdown-menu>
<c-button variant="outline">
<c-dropdown-menu.trigger>Open</c-dropdown-menu.trigger>
</c-button>
<c-dropdown-menu.content class="w-56">
<c-dropdown-menu.label>My Account</c-dropdown-menu.label>
<c-dropdown-menu.separator />
<c-dropdown-menu.item>Profile</c-dropdown-menu.item>
<c-dropdown-menu.item>Billing</c-dropdown-menu.item>
<c-dropdown-menu.separator />
<c-dropdown-menu.item>Settings</c-dropdown-menu.item>
</c-dropdown-menu.content>
</c-dropdown-menu>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add dropdown_menu
```

## Usage

```html
<c-dropdown-menu>
  <c-button variant="outline">
    <c-dropdown-menu.trigger>Open</c-dropdown-menu.trigger>
  </c-button>
  <c-dropdown-menu.content class="w-56">
    <c-dropdown-menu.label>My Account</c-dropdown-menu.label>
    <c-dropdown-menu.separator />
    <c-dropdown-menu.item>Profile</c-dropdown-menu.item>
    <c-dropdown-menu.item>Billing</c-dropdown-menu.item>
    <c-dropdown-menu.separator />
    <c-dropdown-menu.item>Settings</c-dropdown-menu.item>
  </c-dropdown-menu.content>
</c-dropdown-menu>
```
