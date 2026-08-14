---
title: Context Menu
description: A menu that opens where you right-click.
description.pt-br: Um menu que abre onde você clica com o botão direito.
description.es: Un menú que se abre donde haces clic derecho.
---

<c-docs.demo-section class="min-h-[350px]">
<c-context-menu>
<c-context-menu.trigger class="flex h-[150px] w-[300px] items-center justify-center rounded-md border border-dashed text-sm">
Right click here
</c-context-menu.trigger>
<c-context-menu.content class="w-52">
<c-context-menu.item>Back<c-context-menu.shortcut>⌘[</c-context-menu.shortcut></c-context-menu.item>
<c-context-menu.item>Forward<c-context-menu.shortcut>⌘]</c-context-menu.shortcut></c-context-menu.item>
<c-context-menu.item>Reload<c-context-menu.shortcut>⌘R</c-context-menu.shortcut></c-context-menu.item>
<c-context-menu.separator />
<c-context-menu.item variant="destructive">Delete</c-context-menu.item>
</c-context-menu.content>
</c-context-menu>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add context_menu
```

## Usage

<c-docs.demo-section>
<c-context-menu>
<c-context-menu.trigger class="flex h-[120px] w-[280px] items-center justify-center rounded-md border border-dashed text-sm">
Right click here
</c-context-menu.trigger>
<c-context-menu.content class="w-48">
<c-context-menu.item>Profile</c-context-menu.item>
<c-context-menu.item>Billing</c-context-menu.item>
<c-context-menu.item>Settings</c-context-menu.item>
</c-context-menu.content>
</c-context-menu>
</c-docs.demo-section>

```html
<c-context-menu>
    <c-context-menu.trigger class="...">Right click here</c-context-menu.trigger>
    <c-context-menu.content class="w-48">
        <c-context-menu.item>Profile</c-context-menu.item>
        <c-context-menu.item>Billing</c-context-menu.item>
        <c-context-menu.item>Settings</c-context-menu.item>
    </c-context-menu.content>
</c-context-menu>
```

The trigger swallows the browser's own menu and records where you clicked; the
content is positioned there with `fixed`, so it opens under the cursor rather
than under the element.

## Examples

### Labels, checkboxes and radios

<c-docs.demo-section>
<c-context-menu>
<c-context-menu.trigger class="flex h-[120px] w-[280px] items-center justify-center rounded-md border border-dashed text-sm">
Right click here
</c-context-menu.trigger>
<c-context-menu.content class="w-56">
<c-context-menu.label>Appearance</c-context-menu.label>
<c-context-menu.checkbox-item checked="true">Status bar</c-context-menu.checkbox-item>
<c-context-menu.checkbox-item>Activity bar</c-context-menu.checkbox-item>
<c-context-menu.separator />
<c-context-menu.label>Panel position</c-context-menu.label>
<c-context-menu.radio-group value="bottom">
<c-context-menu.radio-item value="top">Top</c-context-menu.radio-item>
<c-context-menu.radio-item value="bottom">Bottom</c-context-menu.radio-item>
<c-context-menu.radio-item value="right">Right</c-context-menu.radio-item>
</c-context-menu.radio-group>
</c-context-menu.content>
</c-context-menu>
</c-docs.demo-section>

```html
<c-context-menu.label>Appearance</c-context-menu.label>
<c-context-menu.checkbox-item checked="true">Status bar</c-context-menu.checkbox-item>

<c-context-menu.radio-group value="bottom">
    <c-context-menu.radio-item value="top">Top</c-context-menu.radio-item>
    <c-context-menu.radio-item value="bottom">Bottom</c-context-menu.radio-item>
</c-context-menu.radio-group>
```

### Submenu

<c-docs.demo-section>
<c-context-menu>
<c-context-menu.trigger class="flex h-[120px] w-[280px] items-center justify-center rounded-md border border-dashed text-sm">
Right click here
</c-context-menu.trigger>
<c-context-menu.content class="w-52">
<c-context-menu.item>New file</c-context-menu.item>
<c-context-menu.sub>
<c-context-menu.sub-trigger>Share</c-context-menu.sub-trigger>
<c-context-menu.sub-content class="w-40">
<c-context-menu.item>Copy link</c-context-menu.item>
<c-context-menu.item>Email</c-context-menu.item>
</c-context-menu.sub-content>
</c-context-menu.sub>
<c-context-menu.separator />
<c-context-menu.item variant="destructive">Delete</c-context-menu.item>
</c-context-menu.content>
</c-context-menu>
</c-docs.demo-section>

```html
<c-context-menu.sub>
    <c-context-menu.sub-trigger>Share</c-context-menu.sub-trigger>
    <c-context-menu.sub-content class="w-40">
        <c-context-menu.item>Copy link</c-context-menu.item>
        <c-context-menu.item>Email</c-context-menu.item>
    </c-context-menu.sub-content>
</c-context-menu.sub>
```

### Inset items

<c-docs.demo-section>
<c-context-menu>
<c-context-menu.trigger class="flex h-[120px] w-[280px] items-center justify-center rounded-md border border-dashed text-sm">
Right click here
</c-context-menu.trigger>
<c-context-menu.content class="w-52">
<c-context-menu.label inset="true">Actions</c-context-menu.label>
<c-context-menu.item inset="true">Rename</c-context-menu.item>
<c-context-menu.item inset="true">Duplicate</c-context-menu.item>
</c-context-menu.content>
</c-context-menu>
</c-docs.demo-section>

```html
<c-context-menu.item inset="true">Rename</c-context-menu.item>
```

`inset` lines an item up with the ones that carry a checkbox or radio mark.

## Notes

Radix opens the submenu on hover with a safe triangle, so moving diagonally
towards it does not close it. Here the submenu opens on `mouseenter` and closes
on `mouseleave` — cutting a corner too sharply closes it.

**The menu closes when the page scrolls.** It is placed at viewport
coordinates, so leaving it open through a scroll would drag it away from what
you right-clicked. Radix does the same thing for the same reason.

Upstream caps the menu height and scrolls it internally. That is dropped here:
the overflow would clip the submenu, which Radix escapes by rendering it in a
portal. A very long menu grows instead of scrolling.

There is no roving focus: the menu answers to the pointer and to `Escape`, not
to the arrow keys. Same limitation as the tooltip on positioning — the content
is placed at the cursor without measuring whether it fits, so a right-click
near the bottom edge opens a menu that runs past it.
