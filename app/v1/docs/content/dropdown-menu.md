---
title: Dropdown Menu
description: Displays a menu to the user — such as a set of actions or functions — triggered by a button.
description.pt-br: Um menu aberto por um botão — um conjunto de ações, por exemplo.
description.es: Un menú que abre un botón — un conjunto de acciones, por ejemplo.
---

<c-docs.demo-section class="min-h-[350px]">
<c-dropdown-menu>
<c-dropdown-menu.trigger>
<c-button variant="outline">Open</c-button>
</c-dropdown-menu.trigger>
<c-dropdown-menu.content class="w-56">
<c-dropdown-menu.label>My Account</c-dropdown-menu.label>
<c-dropdown-menu.separator />
<c-dropdown-menu.group>
<c-dropdown-menu.item>Profile<c-dropdown-menu.shortcut>⇧⌘P</c-dropdown-menu.shortcut></c-dropdown-menu.item>
<c-dropdown-menu.item>Billing<c-dropdown-menu.shortcut>⌘B</c-dropdown-menu.shortcut></c-dropdown-menu.item>
<c-dropdown-menu.item>Settings<c-dropdown-menu.shortcut>⌘S</c-dropdown-menu.shortcut></c-dropdown-menu.item>
</c-dropdown-menu.group>
<c-dropdown-menu.separator />
<c-dropdown-menu.item variant="destructive">Log out</c-dropdown-menu.item>
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
    <c-dropdown-menu.trigger>
        <c-button variant="outline">Open</c-button>
    </c-dropdown-menu.trigger>
    <c-dropdown-menu.content class="w-56">
        <c-dropdown-menu.label>My Account</c-dropdown-menu.label>
        <c-dropdown-menu.separator />
        <c-dropdown-menu.item>Profile</c-dropdown-menu.item>
        <c-dropdown-menu.item>Billing</c-dropdown-menu.item>
        <c-dropdown-menu.separator />
        <c-dropdown-menu.item variant="destructive">Log out</c-dropdown-menu.item>
    </c-dropdown-menu.content>
</c-dropdown-menu>
```

The trigger wraps the button instead of sitting inside it. It is the element
that takes the click, and the content is positioned against the menu around
both.

## Examples

### Alignment

<c-docs.demo-section class="min-h-[280px]">
<div class="flex gap-4">
<c-dropdown-menu>
<c-dropdown-menu.trigger>
<c-button variant="outline">Start</c-button>
</c-dropdown-menu.trigger>
<c-dropdown-menu.content class="w-40">
<c-dropdown-menu.item>Profile</c-dropdown-menu.item>
<c-dropdown-menu.item>Billing</c-dropdown-menu.item>
</c-dropdown-menu.content>
</c-dropdown-menu>
<c-dropdown-menu>
<c-dropdown-menu.trigger>
<c-button variant="outline">Center</c-button>
</c-dropdown-menu.trigger>
<c-dropdown-menu.content align="center" class="w-40">
<c-dropdown-menu.item>Profile</c-dropdown-menu.item>
<c-dropdown-menu.item>Billing</c-dropdown-menu.item>
</c-dropdown-menu.content>
</c-dropdown-menu>
<c-dropdown-menu>
<c-dropdown-menu.trigger>
<c-button variant="outline">End</c-button>
</c-dropdown-menu.trigger>
<c-dropdown-menu.content align="end" class="w-40">
<c-dropdown-menu.item>Profile</c-dropdown-menu.item>
<c-dropdown-menu.item>Billing</c-dropdown-menu.item>
</c-dropdown-menu.content>
</c-dropdown-menu>
</div>
</c-docs.demo-section>

```html
<c-dropdown-menu.content align="end" class="w-40">
    <c-dropdown-menu.item>Profile</c-dropdown-menu.item>
</c-dropdown-menu.content>
```

`align` takes `start`, `center` or `end` and defaults to `start`.

### Checkboxes and radios

<c-docs.demo-section class="min-h-[340px]">
<c-dropdown-menu>
<c-dropdown-menu.trigger>
<c-button variant="outline">View</c-button>
</c-dropdown-menu.trigger>
<c-dropdown-menu.content class="w-56">
<c-dropdown-menu.label>Appearance</c-dropdown-menu.label>
<c-dropdown-menu.checkbox-item checked="true">Status bar</c-dropdown-menu.checkbox-item>
<c-dropdown-menu.checkbox-item>Activity bar</c-dropdown-menu.checkbox-item>
<c-dropdown-menu.separator />
<c-dropdown-menu.label>Panel position</c-dropdown-menu.label>
<c-dropdown-menu.radio-group value="bottom">
<c-dropdown-menu.radio-item value="top">Top</c-dropdown-menu.radio-item>
<c-dropdown-menu.radio-item value="bottom">Bottom</c-dropdown-menu.radio-item>
<c-dropdown-menu.radio-item value="right">Right</c-dropdown-menu.radio-item>
</c-dropdown-menu.radio-group>
</c-dropdown-menu.content>
</c-dropdown-menu>
</c-docs.demo-section>

```html
<c-dropdown-menu.checkbox-item checked="true">Status bar</c-dropdown-menu.checkbox-item>

<c-dropdown-menu.radio-group value="bottom">
    <c-dropdown-menu.radio-item value="top">Top</c-dropdown-menu.radio-item>
    <c-dropdown-menu.radio-item value="bottom">Bottom</c-dropdown-menu.radio-item>
</c-dropdown-menu.radio-group>
```

These two keep the menu open when clicked, so a list of toggles can be worked
through in one go.

### Submenu

<c-docs.demo-section class="min-h-[300px]">
<c-dropdown-menu>
<c-dropdown-menu.trigger>
<c-button variant="outline">Actions</c-button>
</c-dropdown-menu.trigger>
<c-dropdown-menu.content class="w-52">
<c-dropdown-menu.item>New file</c-dropdown-menu.item>
<c-dropdown-menu.sub>
<c-dropdown-menu.sub-trigger>Share</c-dropdown-menu.sub-trigger>
<c-dropdown-menu.sub-content class="w-40">
<c-dropdown-menu.item>Copy link</c-dropdown-menu.item>
<c-dropdown-menu.item>Email</c-dropdown-menu.item>
</c-dropdown-menu.sub-content>
</c-dropdown-menu.sub>
<c-dropdown-menu.separator />
<c-dropdown-menu.item variant="destructive">Delete</c-dropdown-menu.item>
</c-dropdown-menu.content>
</c-dropdown-menu>
</c-docs.demo-section>

```html
<c-dropdown-menu.sub>
    <c-dropdown-menu.sub-trigger>Share</c-dropdown-menu.sub-trigger>
    <c-dropdown-menu.sub-content class="w-40">
        <c-dropdown-menu.item>Copy link</c-dropdown-menu.item>
    </c-dropdown-menu.sub-content>
</c-dropdown-menu.sub>
```

### Inset items

<c-docs.demo-section class="min-h-[280px]">
<c-dropdown-menu>
<c-dropdown-menu.trigger>
<c-button variant="outline">Edit</c-button>
</c-dropdown-menu.trigger>
<c-dropdown-menu.content class="w-52">
<c-dropdown-menu.label inset="true">Actions</c-dropdown-menu.label>
<c-dropdown-menu.item inset="true">Rename</c-dropdown-menu.item>
<c-dropdown-menu.item inset="true">Duplicate</c-dropdown-menu.item>
</c-dropdown-menu.content>
</c-dropdown-menu>
</c-docs.demo-section>

```html
<c-dropdown-menu.item inset="true">Rename</c-dropdown-menu.item>
```

`inset` lines an item up with the ones that carry a checkbox or radio mark.

### Keeping the menu open

An item closes the menu when clicked. Pass `close_on_select="false"` when the
item carries a control of its own.

```html
<c-dropdown-menu.item close_on_select="false">
    <label class="flex items-center gap-2">
        <c-checkbox x-model="compact" /> Compact rows
    </label>
</c-dropdown-menu.item>
```

## Notes

The content is placed with `absolute` against the trigger, so `align` is a
choice rather than a measurement: a menu near the right edge of the viewport
runs past it instead of flipping. Radix measures.

The submenu opens on `mouseenter` and closes on `mouseleave`, without the safe
triangle Radix draws — cutting a corner too sharply closes it.

Upstream caps the menu height and scrolls it internally. That is dropped here,
as in the context menu: the overflow would clip the submenu, which Radix
escapes through a portal. A very long menu grows instead of scrolling.

There is no roving focus. The menu answers to the pointer and to `Escape`, not
to the arrow keys.
