---
title: Menubar
description: A row of menus, the way a desktop application has one.
description.pt-br: Uma barra de menus, como a de um aplicativo de desktop.
description.es: Una barra de menús, como la de una aplicación de escritorio.
---

<c-docs.demo-section class="min-h-[350px]">
<c-menubar>
<c-menubar.menu>
<c-menubar.trigger>File</c-menubar.trigger>
<c-menubar.content>
<c-menubar.item>New tab<c-menubar.shortcut>⌘T</c-menubar.shortcut></c-menubar.item>
<c-menubar.item>New window<c-menubar.shortcut>⌘N</c-menubar.shortcut></c-menubar.item>
<c-menubar.separator />
<c-menubar.item>Print<c-menubar.shortcut>⌘P</c-menubar.shortcut></c-menubar.item>
</c-menubar.content>
</c-menubar.menu>
<c-menubar.menu>
<c-menubar.trigger>Edit</c-menubar.trigger>
<c-menubar.content>
<c-menubar.item>Undo<c-menubar.shortcut>⌘Z</c-menubar.shortcut></c-menubar.item>
<c-menubar.item>Redo<c-menubar.shortcut>⇧⌘Z</c-menubar.shortcut></c-menubar.item>
</c-menubar.content>
</c-menubar.menu>
<c-menubar.menu>
<c-menubar.trigger>View</c-menubar.trigger>
<c-menubar.content>
<c-menubar.checkbox-item checked="true">Status bar</c-menubar.checkbox-item>
<c-menubar.checkbox-item>Full screen</c-menubar.checkbox-item>
</c-menubar.content>
</c-menubar.menu>
</c-menubar>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add menubar
```

## Usage

<c-docs.demo-section>
<c-menubar>
<c-menubar.menu>
<c-menubar.trigger>File</c-menubar.trigger>
<c-menubar.content>
<c-menubar.item>New tab</c-menubar.item>
<c-menubar.item>Open</c-menubar.item>
</c-menubar.content>
</c-menubar.menu>
<c-menubar.menu>
<c-menubar.trigger>Help</c-menubar.trigger>
<c-menubar.content>
<c-menubar.item>Documentation</c-menubar.item>
</c-menubar.content>
</c-menubar.menu>
</c-menubar>
</c-docs.demo-section>

```html
<c-menubar>
    <c-menubar.menu>
        <c-menubar.trigger>File</c-menubar.trigger>
        <c-menubar.content>
            <c-menubar.item>New tab</c-menubar.item>
            <c-menubar.item>Open</c-menubar.item>
        </c-menubar.content>
    </c-menubar.menu>
    <c-menubar.menu>
        <c-menubar.trigger>Help</c-menubar.trigger>
        <c-menubar.content>
            <c-menubar.item>Documentation</c-menubar.item>
        </c-menubar.content>
    </c-menubar.menu>
</c-menubar>
```

Open one menu and the others answer to hover — moving along the bar switches
between them without another click, which is what makes a menubar feel like
one. Clicking the open trigger again, picking an item, pressing `Escape` or
clicking away all close it.

## Examples

### Checkboxes and radios

<c-docs.demo-section>
<c-menubar>
<c-menubar.menu>
<c-menubar.trigger>View</c-menubar.trigger>
<c-menubar.content>
<c-menubar.label>Appearance</c-menubar.label>
<c-menubar.checkbox-item checked="true">Status bar</c-menubar.checkbox-item>
<c-menubar.checkbox-item>Activity bar</c-menubar.checkbox-item>
<c-menubar.separator />
<c-menubar.label>Sidebar</c-menubar.label>
<c-menubar.radio-group value="left">
<c-menubar.radio-item value="left">Left</c-menubar.radio-item>
<c-menubar.radio-item value="right">Right</c-menubar.radio-item>
</c-menubar.radio-group>
</c-menubar.content>
</c-menubar.menu>
</c-menubar>
</c-docs.demo-section>

```html
<c-menubar.checkbox-item checked="true">Status bar</c-menubar.checkbox-item>

<c-menubar.radio-group value="left">
    <c-menubar.radio-item value="left">Left</c-menubar.radio-item>
    <c-menubar.radio-item value="right">Right</c-menubar.radio-item>
</c-menubar.radio-group>
```

### Submenu

<c-docs.demo-section>
<c-menubar>
<c-menubar.menu>
<c-menubar.trigger>File</c-menubar.trigger>
<c-menubar.content>
<c-menubar.item>New file</c-menubar.item>
<c-menubar.sub>
<c-menubar.sub-trigger>Share</c-menubar.sub-trigger>
<c-menubar.sub-content class="w-40">
<c-menubar.item>Copy link</c-menubar.item>
<c-menubar.item>Email</c-menubar.item>
</c-menubar.sub-content>
</c-menubar.sub>
<c-menubar.separator />
<c-menubar.item variant="destructive">Delete</c-menubar.item>
</c-menubar.content>
</c-menubar.menu>
</c-menubar>
</c-docs.demo-section>

```html
<c-menubar.sub>
    <c-menubar.sub-trigger>Share</c-menubar.sub-trigger>
    <c-menubar.sub-content class="w-40">
        <c-menubar.item>Copy link</c-menubar.item>
        <c-menubar.item>Email</c-menubar.item>
    </c-menubar.sub-content>
</c-menubar.sub>
```

### Alignment

<c-docs.demo-section>
<c-menubar>
<c-menubar.menu>
<c-menubar.trigger>Start</c-menubar.trigger>
<c-menubar.content align="start"><c-menubar.item>Aligned left</c-menubar.item></c-menubar.content>
</c-menubar.menu>
<c-menubar.menu>
<c-menubar.trigger>End</c-menubar.trigger>
<c-menubar.content align="end"><c-menubar.item>Aligned right</c-menubar.item></c-menubar.content>
</c-menubar.menu>
</c-menubar>
</c-docs.demo-section>

```html
<c-menubar.content align="start">...</c-menubar.content>
<c-menubar.content align="end">...</c-menubar.content>
```

## Notes

Which menu is open is tracked by element identity rather than a name you have
to invent, so a `<c-menubar.menu>` needs no `value`. The trigger and the
content find each other through the menu they share as a parent, which is why
both have to be direct children of it.

Like the context menu, there is no roving focus: the bar answers to the
pointer and to `Escape`, not to the arrow keys. The content is positioned
against its trigger with utility classes, so `align` is a choice rather than a
measurement — a menu near the right edge wants `align="end"`.
