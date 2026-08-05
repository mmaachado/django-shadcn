# Changelog

## Unreleased

### Added

- **`context_menu`** — opens where the pointer is, on right click. Closes on
  scroll and on resize, since a menu anchored to the viewport would otherwise
  follow the page down.
- **`menubar`** — the application menu bar. One open menu at a time, and moving
  the pointer across the bar switches between them once one is open.
- **`input_otp`** — one transparent input holding the whole code, laid over the
  slots that display it. Paste, autofill and `autocomplete="one-time-code"`
  work because the field is real.
- **`resizable`** — dragging a handle adjusts the `flex-grow` of the two panels
  it sits between. Sizes are not persisted between loads.
- **`drawer`** — a panel from any edge, with a grab handle and drag to dismiss
  on the bottom one. Upstream builds on `vaul`; its momentum, snap points and
  background scaling are not reproduced, and `data-vaul-drawer-direction` is
  named `data-direction` here.
- **`sidebar`** — the collapsible application sidebar, with the rail, the icon
  rail, groups, sub-menus, actions and badges. Toggling writes a
  `sidebar_state` cookie; read it in the view and pass `default_open` so the
  server renders the shape the visitor left. Below `md` the panel slides in
  over a backdrop instead of becoming a `sheet`, so the menu is written once
  and the page holds no duplicate ids.
- **Data Table** — a guide, not a component. Upstream ships one because React
  needs TanStack Table to sort a list of rows; here `order_by`, `filter` and
  `Paginator` already do it, so the page shows the wiring: sortable headers,
  a filter that survives paging through `{% querystring %}`,
  `get_elided_page_range` feeding `pagination.ellipsis`, row selection and
  column visibility.

### Security

- **Values passed to a component no longer reach Alpine as code.** Components
  wrote things like `x-data="{ value: '{{ value }}' }"`. Django escapes that
  for HTML, but the browser turns the entities back into quotes before Alpine
  evaluates the attribute as JavaScript, so a value carrying a quote could
  close the string and run whatever followed. Anything looping user or
  database content into a component — `<c-tabs.trigger value="{{ tag.slug }}">`
  is the obvious shape — was exposed.

  Values now travel through `data-*` attributes, where Django's escaping is the
  right escaping, and Alpine reads them at runtime instead of having them baked
  into the expression. Booleans render as literal `true`/`false` and interpolate
  nothing at all. `combobox` built its options list with `|safe`, which skipped
  escaping entirely; it now emits real JSON through the built-in `escapejs`.

  Affected: `accordion`, `alert_dialog`, `combobox`, `command`,
  `command_dialog`, `context_menu`, `dialog`, `menubar`, `navigation_menu`,
  `popover`, `select`, `sheet`, `slider`, `tabs`, `toast`, `toggle`,
  `toggle_group`, `hover_card`, `collapsible`.

  Component APIs are unchanged — `<c-combobox :options="[...]">` still takes a
  Python list. Copies already in your project keep the old markup; run
  `add <name> --overwrite` to take the fix.

### Fixed

- `add` now accepts the spelling you see in the markup. The tag is
  `<c-toggle-group>` but the directory has to be `toggle_group`, and only the
  second worked; `add toggle-group`, `add hover-card`, `add radio-group` and
  `add scroll-area` failed with "Unknown component". Both spellings work now.
- The install command on four documentation pages named the component the way
  the CLI rejected it.
- `table.empty` carried a stray `',` left over from the React source and put
  `text-foreground',` on the cell as a class.

## 1.0.0 — 2026-08-04

First stable release. `django-shadcn` ships 51 cotton components, a CLI that
copies them into your project, and a documentation site.

### Read this before upgrading

**Icons moved from inline `<svg>` to `<c-icon>`.** Components that used to
paste an SVG now render `<c-icon name="chevron-down" />`, and the shapes come
from a generated `icon/` directory. Nothing you already installed breaks — the
copies in your project are yours and stay as they are — but running `add` again
on a component that draws an icon produces a diff you did not write. The
components affected are `accordion`, `select`, `navigation_menu`, `combobox`,
`command`, `dialog`, `sheet` and `toast`.

`toast` also drops a Heroicons path that had been sitting among the lucide
ones, so its close icon changes shape slightly.

**`add` no longer overwrites your files.** It used to replace whatever it found
and, for `allauth`, delete the destination directory first. The default now
skips files that already exist and reports them; `--overwrite` replaces them,
and `--sync` mirrors the source and is the only path that deletes anything.
`--sync` lists what it will remove and asks before doing it.

This reverses the previous behaviour. There is no compatibility promise being
broken here — `1.0.0rc1` was a pre-release that only reserved the name on PyPI,
and no stable version has existed until now — but if you had a script relying
on `add` replacing files, it needs `--overwrite`.

### Added

- **CLI.** `init` prepares the project, `add` installs one or more components
  with their dependencies in a single fetch, `list` shows what exists and marks
  what is installed, and `--version` reports the installed release.
- **Components.** 51 in total. This release adds `avatar`, `skeleton`,
  `aspect_ratio`, `kbd`, `breadcrumb`, `typography`, `empty`, `spinner`,
  `item`, `field`, `button_group`, `input_group` and `native_select`, followed
  by `switch`, `toggle`, `toggle_group`, `collapsible`, `radio_group`,
  `slider`, `tooltip`, `hover_card`, `pagination` and `scroll_area`.
- **Icons.** Lucide icons as a component, with a pinned subset generated from
  `lucide-static` and checked against usage by the test suite.
- **Documentation site.** Every page is Markdown that can embed live component
  demos, in English with Portuguese and Spanish available, plus `llms.txt` and
  `llms-full.txt` for tools that read the docs.

### Changed

- Components are served from a single `components/` directory. The duplicate
  copy under `docs/templates/cotton/` is gone, so the playground and the CLI
  can no longer drift.
- Newer components emit `data-slot`, which the shadcn/ui styles use as a
  selector target rather than decoration. The older ones do not emit it yet.
- Version numbers come from the git tag. No file in the repository carries one.

### Known limitations

- `toggle_group` has no single-selection mode and `slider` takes one value, as
  both need state shared between children.
- `tooltip` and `hover_card` position themselves with utility classes instead
  of measuring the viewport, so `side` and `align` are choices rather than
  something worked out at runtime.
- `switch`, `radio_group` and `slider` are native form controls rather than the
  button-based widgets Radix builds. They submit with the form; the trade is
  that their internals differ from the upstream markup.
- `scroll_area` styles the native scrollbar instead of drawing its own. Firefox
  honours only its width and colour.

### Credits

A port of [shadcn/ui](https://ui.shadcn.com), forked from
[SarthakJariwala/shadcn-django](https://github.com/SarthakJariwala/shadcn-django).
Icons from [Lucide](https://lucide.dev), ISC licensed.
