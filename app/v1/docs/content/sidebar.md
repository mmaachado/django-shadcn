---
title: Sidebar
description: A composable, collapsible sidebar that remembers whether it was open.
description.pt-br: Uma sidebar composta e recolhível que lembra se estava aberta.
description.es: Una barra lateral componible y plegable que recuerda si estaba abierta.
---

<c-docs.demo-section>
<div class="relative h-[420px] w-full transform-gpu overflow-hidden rounded-lg border">
<c-sidebar.provider class="min-h-full!">
<c-sidebar class="h-full!">
<c-sidebar.header>
<c-sidebar.input placeholder="Search" />
</c-sidebar.header>
<c-sidebar.content>
<c-sidebar.group>
<c-sidebar.group-label>Workspace</c-sidebar.group-label>
<c-sidebar.group-content>
<c-sidebar.menu>
<c-sidebar.menu-item>
<c-sidebar.menu-button is_active="true" tooltip="Search">
<c-icon name="search" />
<span>Search</span>
</c-sidebar.menu-button>
</c-sidebar.menu-item>
<c-sidebar.menu-item>
<c-sidebar.menu-button tooltip="Drafts">
<c-icon name="circle" />
<span>Drafts</span>
</c-sidebar.menu-button>
<c-sidebar.menu-badge>7</c-sidebar.menu-badge>
</c-sidebar.menu-item>
<c-sidebar.menu-item>
<c-sidebar.menu-button tooltip="Done">
<c-icon name="check" />
<span>Done</span>
</c-sidebar.menu-button>
<c-sidebar.menu-action><c-icon name="ellipsis" /></c-sidebar.menu-action>
</c-sidebar.menu-item>
</c-sidebar.menu>
</c-sidebar.group-content>
</c-sidebar.group>
</c-sidebar.content>
<c-sidebar.footer>
<c-sidebar.menu>
<c-sidebar.menu-item>
<c-sidebar.menu-button tooltip="Account">
<c-icon name="circle" />
<span>Account</span>
</c-sidebar.menu-button>
</c-sidebar.menu-item>
</c-sidebar.menu>
</c-sidebar.footer>
<c-sidebar.rail />
</c-sidebar>
<c-sidebar.inset>
<header class="flex h-12 shrink-0 items-center gap-2 border-b px-4">
<c-sidebar.trigger />
<span class="text-sm font-medium">Inbox</span>
</header>
<div class="p-4 text-sm text-muted-foreground">
Toggle with the button, the rail on the panel's edge, or <c-kbd>⌘</c-kbd> <c-kbd>B</c-kbd>.
</div>
</c-sidebar.inset>
</c-sidebar.provider>
</div>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add sidebar
```

## Usage

```html
<c-sidebar.provider>
    <c-sidebar>
        <c-sidebar.header>...</c-sidebar.header>
        <c-sidebar.content>
            <c-sidebar.group>
                <c-sidebar.group-label>Workspace</c-sidebar.group-label>
                <c-sidebar.group-content>
                    <c-sidebar.menu>
                        <c-sidebar.menu-item>
                            <c-sidebar.menu-button href="/inbox/" tooltip="Inbox">
                                <c-icon name="search" />
                                <span>Inbox</span>
                            </c-sidebar.menu-button>
                        </c-sidebar.menu-item>
                    </c-sidebar.menu>
                </c-sidebar.group-content>
            </c-sidebar.group>
        </c-sidebar.content>
        <c-sidebar.footer>...</c-sidebar.footer>
        <c-sidebar.rail />
    </c-sidebar>
    <c-sidebar.inset>
        <c-sidebar.trigger />
        {{ content }}
    </c-sidebar.inset>
</c-sidebar.provider>
```

`<c-sidebar.provider>` holds the open state and has to wrap both the panel and
the page. Put it in your base template, around everything.

`<c-sidebar.inset>` is where the page goes. It must be a sibling that comes
after `<c-sidebar>` — the `inset` variant styles it from there.

A `<c-sidebar.menu-button>` with an `href` renders an `<a>`; without one it
renders a `<button>`. Mark the current page with `is_active="true"`.

## Remembering the state

Toggling writes a `sidebar_state` cookie. Read it back in the view so the
server renders the panel in the shape the visitor left it, instead of drawing
it expanded and letting it snap shut once Alpine boots:

```python
def dashboard(request):
    return render(request, "dashboard.html", {
        "sidebar_open": request.COOKIES.get("sidebar_state", "true"),
    })
```

```html
<c-sidebar.provider default_open="{{ sidebar_open }}">
```

## Examples

### Collapse to icons

`collapsible="icon"` keeps a rail of icons instead of sliding the whole panel
away. Labels, badges and sub-menus hide themselves; the `tooltip` on each
button takes over as the label.

<c-docs.demo-section>
<div class="relative h-[300px] w-full transform-gpu overflow-hidden rounded-lg border">
<c-sidebar.provider class="min-h-full!">
<c-sidebar collapsible="icon" class="h-full!">
<c-sidebar.content>
<c-sidebar.group>
<c-sidebar.group-label>Workspace</c-sidebar.group-label>
<c-sidebar.group-content>
<c-sidebar.menu>
<c-sidebar.menu-item>
<c-sidebar.menu-button tooltip="Search">
<c-icon name="search" />
<span>Search</span>
</c-sidebar.menu-button>
</c-sidebar.menu-item>
<c-sidebar.menu-item>
<c-sidebar.menu-button tooltip="Drafts">
<c-icon name="circle" />
<span>Drafts</span>
</c-sidebar.menu-button>
</c-sidebar.menu-item>
<c-sidebar.menu-item>
<c-sidebar.menu-button tooltip="Done">
<c-icon name="check" />
<span>Done</span>
</c-sidebar.menu-button>
</c-sidebar.menu-item>
</c-sidebar.menu>
</c-sidebar.group-content>
</c-sidebar.group>
</c-sidebar.content>
<c-sidebar.rail />
</c-sidebar>
<c-sidebar.inset>
<header class="flex h-12 shrink-0 items-center gap-2 border-b px-4">
<c-sidebar.trigger />
<span class="text-sm font-medium">Collapse me</span>
</header>
</c-sidebar.inset>
</c-sidebar.provider>
</div>
</c-docs.demo-section>

```html
<c-sidebar collapsible="icon">...</c-sidebar>
```

### Variants and side

```html
<c-sidebar variant="floating">...</c-sidebar>
<c-sidebar variant="inset">...</c-sidebar>
<c-sidebar side="right">...</c-sidebar>
<c-sidebar collapsible="none">...</c-sidebar>
```

`floating` detaches the panel with a border and a radius. `inset` does the same
to the page instead, and needs the provider to sit on the sidebar background —
`has-data-[variant=inset]:bg-sidebar` already handles that. `none` drops the
toggle entirely and leaves a panel that is always there.

### Nested items

```html
<c-sidebar.menu-item>
    <c-sidebar.menu-button>
        <span>Settings</span>
    </c-sidebar.menu-button>
    <c-sidebar.menu-sub>
        <c-sidebar.menu-sub-item>
            <c-sidebar.menu-sub-button href="/settings/team/" is_active="true">
                <span>Team</span>
            </c-sidebar.menu-sub-button>
        </c-sidebar.menu-sub-item>
    </c-sidebar.menu-sub>
</c-sidebar.menu-item>
```

Wrap the sub-menu in a [Collapsible]({% url 'page' slug='collapsible' %}) if
you want it to fold.

### Actions and badges

```html
<c-sidebar.menu-item>
    <c-sidebar.menu-button>
        <span>Done</span>
    </c-sidebar.menu-button>
    <c-sidebar.menu-action show_on_hover="true">
        <c-icon name="ellipsis" />
    </c-sidebar.menu-action>
</c-sidebar.menu-item>
```

Both the action and the badge sit on top of the button, so they go after it,
inside the same `<c-sidebar.menu-item>`. Only one of the two per item — they
claim the same corner.

### Loading placeholder

<c-docs.demo-section>
<div class="w-[240px] rounded-lg bg-sidebar p-2">
<c-sidebar.menu>
<c-sidebar.menu-item><c-sidebar.menu-skeleton show_icon="true" width="60%" /></c-sidebar.menu-item>
<c-sidebar.menu-item><c-sidebar.menu-skeleton show_icon="true" width="85%" /></c-sidebar.menu-item>
<c-sidebar.menu-item><c-sidebar.menu-skeleton show_icon="true" width="70%" /></c-sidebar.menu-item>
</c-sidebar.menu>
</div>
</c-docs.demo-section>

```html
<c-sidebar.menu-skeleton show_icon="true" width="60%" />
```

## Notes

Below `md` the panel slides in over a backdrop rather than becoming a
[Sheet]({% url 'page' slug='sheet' %}) as upstream does. One tree serves both
widths, so the menu is written once and there are no duplicate ids in the page.

The width comes from `--sidebar-width` and `--sidebar-width-icon`, set on the
provider. Override them with an inline style, which beats the defaults:

```html
<c-sidebar.provider style="--sidebar-width: 20rem">
```

`<c-sidebar.menu-button>` renders its `tooltip` as a plain sibling label
instead of composing [Tooltip]({% url 'page' slug='tooltip' %}), because the
badge and action rules position themselves against the button as a sibling and
a wrapper would break them.

The sidebar's own colour tokens — `--sidebar`, `--sidebar-accent`,
`--sidebar-border` and the rest — live in `input.css`. Restyle the panel there,
not with utility classes on each part.
