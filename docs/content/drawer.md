---
title: Drawer
description: A panel that slides in from an edge and can be dragged shut.
description.pt-br: Um painel que entra por uma borda e pode ser arrastado para fechar.
description.es: Un panel que entra desde un borde y se puede arrastrar para cerrar.
---

<c-docs.demo-section class="min-h-[350px]">
<c-drawer>
<c-drawer.trigger>
<c-button variant="outline">Open drawer</c-button>
</c-drawer.trigger>
<c-drawer.overlay />
<c-drawer.content>
<c-drawer.header>
<c-drawer.title>Move to folder</c-drawer.title>
<c-drawer.description>Pick where this should live.</c-drawer.description>
</c-drawer.header>
<div class="px-4 pb-2 text-sm text-muted-foreground">
Drag the handle down to dismiss, or press Escape.
</div>
<c-drawer.footer>
<c-button>Move</c-button>
<c-drawer.close>
<c-button variant="outline" class="w-full">Cancel</c-button>
</c-drawer.close>
</c-drawer.footer>
</c-drawer.content>
</c-drawer>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add drawer
```

## Usage

```html
<c-drawer>
    <c-drawer.trigger>
        <c-button variant="outline">Open drawer</c-button>
    </c-drawer.trigger>
    <c-drawer.overlay />
    <c-drawer.content>
        <c-drawer.header>
            <c-drawer.title>Move to folder</c-drawer.title>
            <c-drawer.description>Pick where this should live.</c-drawer.description>
        </c-drawer.header>
        <c-drawer.footer>
            <c-button>Move</c-button>
            <c-drawer.close>
                <c-button variant="outline" class="w-full">Cancel</c-button>
            </c-drawer.close>
        </c-drawer.footer>
    </c-drawer.content>
</c-drawer>
```

The grab handle at the top follows your pointer. Let go past about four tenths
of the panel's height and it closes; let go short of that and it springs back.
Escape and a click on the overlay close it too.

The overlay is a separate element, so you can leave it out for a drawer that
does not dim the page.

## Examples

### Direction

<c-docs.demo-section>
<div class="flex items-center gap-3">
<c-drawer direction="right">
<c-drawer.trigger><c-button variant="outline" size="sm">Right</c-button></c-drawer.trigger>
<c-drawer.overlay />
<c-drawer.content>
<c-drawer.header>
<c-drawer.title>From the right</c-drawer.title>
<c-drawer.description>No handle on this one.</c-drawer.description>
</c-drawer.header>
</c-drawer.content>
</c-drawer>
<c-drawer direction="top">
<c-drawer.trigger><c-button variant="outline" size="sm">Top</c-button></c-drawer.trigger>
<c-drawer.overlay />
<c-drawer.content>
<c-drawer.header>
<c-drawer.title>From the top</c-drawer.title>
<c-drawer.description>Useful for a notification tray.</c-drawer.description>
</c-drawer.header>
</c-drawer.content>
</c-drawer>
</div>
</c-docs.demo-section>

```html
<c-drawer direction="right">...</c-drawer>
<c-drawer direction="top">...</c-drawer>
<c-drawer direction="left">...</c-drawer>
```

### Without the overlay

<c-docs.demo-section>
<c-drawer>
<c-drawer.trigger><c-button variant="outline">No dimming</c-button></c-drawer.trigger>
<c-drawer.content>
<c-drawer.header>
<c-drawer.title>The page stays lit</c-drawer.title>
<c-drawer.description>Drop the overlay when the drawer is not modal.</c-drawer.description>
</c-drawer.header>
<c-drawer.footer>
<c-drawer.close><c-button variant="outline" class="w-full">Close</c-button></c-drawer.close>
</c-drawer.footer>
</c-drawer.content>
</c-drawer>
</c-docs.demo-section>

```html
<c-drawer>
    <c-drawer.trigger>...</c-drawer.trigger>
    <c-drawer.content>...</c-drawer.content>
</c-drawer>
```

## Notes

Upstream builds on `vaul`, which adds momentum, snap points that let the panel
rest at intermediate heights, and a scaling effect on the page behind. None of
that is reproduced. What is here is the part people actually use: a panel from
the edge, a handle, and drag to dismiss.

**Dragging works on the bottom drawer only** — the handle appears there and
nowhere else, which is upstream's own arrangement. The other directions open
and close by click, Escape and the overlay.

If you only need a panel from an edge, [Sheet]({% url 'page' slug='sheet' %})
covers that with less machinery. Reach for the drawer when the drag matters.

The directional classes come from the registry, with `data-vaul-drawer-direction`
renamed to `data-direction` — carrying a library name for a library we do not
ship would be misleading.
