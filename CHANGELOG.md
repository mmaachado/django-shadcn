# Changelog

## 1.3.0 — 2026-08-10

`add` now tells you what a component needs in order to actually work, shows you
what it would do before doing it, and refuses to write into a layout it would
corrupt.

### Read this before upgrading

**If you have `accordion` or `collapsible` in your project, they need
`@alpinejs/collapse`, and nothing has ever told you.** Both use `x-collapse`,
which Alpine's core does not provide. Without the plugin they render correctly
and simply never animate — no error, no warning, nothing in the console. It is
the only plugin the library requires beyond the Alpine core.

Upgrading the CLI does not fix a project that already has them. Add the plugin
to your static files the same way the installation guide has you add Alpine
itself, and load it first:

```html
<script src="{% static 'js/collapse.min.js' %}" defer></script>
<script src="{% static 'js/alpine.min.js' %}" defer></script>
```

From now on `add` names it at the end of the run.

**`list` marks fewer components as installed.** It used to count a component as
installed whenever its destination directory existed, which was never a reliable
signal and was plainly wrong for `allauth`. If a component you did install now
reads as missing, some of the files it ships are gone from your project;
re-running `add` restores them without touching anything you changed.

### Added

- **`add --dry-run`.** Runs the whole calculation and reports it without
  writing. It matters most with `--sync`, the one mode that deletes: the
  preview lists exactly which files would go. The report comes from the code
  that does the real work rather than a separate planner, so the two cannot
  drift apart.

- **`add` names the JavaScript a component needs.** The registry now records
  per-component script requirements, printed once at the end of a run however
  many components asked for them.

### Changed

- **Component names are read more forgivingly.** `add BUTTON`,
  `add Toggle-Group` and a name with stray whitespace around it all resolve
  instead of being rejected as unknown.

- **A typo gets a suggestion instead of a wall of names.** `add buton` now
  answers `buton -> button?`. It used to print all 57 component names and leave
  you to find it.

### Fixed

- **`list` no longer reports `allauth` as installed in any django-allauth
  project.** The seventeen templates it ships are named `login.html`,
  `signup.html` and so on because they _are_ django-allauth's own template
  names, so any project that had hand-written one of them matched.

- **`add` no longer corrupts a project whose layout collides with a
  component.** A directory sitting where a file belongs made the copy land
  _inside_ it, so `add --overwrite` reported overwriting `index.html` while
  actually writing `index.html/index.html`, leaving a component that cannot
  render. A file sitting where a directory belongs raised `FileExistsError`
  partway through, in every mode. Both are now detected for every component in
  the run before anything is written, so a conflict in a dependency cannot
  leave half an install behind.

- **`rich` is declared as a dependency.** The package imports it directly but
  relied on typer bringing it along. An environment that resolved typer without
  it failed at import time, on every command.

## 1.2.0 — 2026-08-06

The components now travel inside the package instead of being fetched from
GitHub. `add` and `init` no longer touch the network, and the version you have
installed is the version of the components you get.

### Read this before upgrading

**The CLI version now decides which components you install.** Until now every
`add` cloned this repository at `master`, so an install from six months ago
still fetched whatever was on `master` that day. The templates are now shipped
in the wheel and read from disk, which means a given release always writes the
same files — and that a component added after your version was published is
reached by upgrading the CLI, not by waiting.

If you pin `django-shadcn` in a lockfile, pin it knowing this. `uvx
django_shadcn@latest` is unaffected: it resolves the newest release each time.

Nothing changes for components already in your project. They are yours, `add`
still leaves them alone, and the markup they were written from is unchanged in
this release.

### Changed

- **`add` and `init` work offline.** Both used to reach GitHub through copier,
  so a flaky connection, a rate limit or a missing `git` surfaced as a raw
  traceback under a spinner. Neither command opens a socket now.

  This also removes the partial-install path: `add` could write several
  components and then fail on one that no longer existed upstream, leaving the
  project half-updated with nothing to roll it back.

- **`copier` is no longer a dependency.** It never rendered anything here —
  `copier.yml` set an impossible template suffix precisely so Jinja would leave
  the Django and cotton syntax alone — so it acted only as a `git clone`
  wrapper around the merge logic that already lived in the CLI. Dropping it
  takes 18 packages out of the dependency tree, `jinja2`, `pydantic`,
  `plumbum` and `questionary` among them.

### Fixed

- **`init` no longer clobbers an existing `input.css`, or hangs asking about
  it.** It called copier without `overwrite`, which produced a confirmation
  prompt drawn underneath the progress spinner, and raised
  `InteractiveSessionError` outright in any non-interactive terminal — CI, a
  container, anything without a tty. The command took no arguments, so there
  was no way past it.

  An existing `input.css` is now kept and reported as kept. `init --force`
  replaces it. If you had worked around this by deleting the file before
  running `init`, you no longer need to.

## 1.1.0 — 2026-08-05

Six components, bringing the total to 57, a guide for building a data table on
a queryset, and a security fix.

**The security fix does not reach copies already in your project.** Components
under `templates/cotton/` are yours and `add` leaves them alone, by design. Run
`add <name> --overwrite` on the ones listed under Security to take it.

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
- **The parts `dropdown_menu` was missing** — `group`, `shortcut`,
  `checkbox_item`, `radio_group`, `radio_item`, `sub`, `sub_trigger` and
  `sub_content`, plus `align` on the content and `variant="destructive"` and
  `inset` on the item. It had six parts against the registry's fifteen and had
  drifted off the classes the other menus share; it now carries the same ones
  as `context_menu` and `menubar`.

  An item closes the menu when clicked, as upstream does. Pass
  `close_on_select="false"` when the item holds a control of its own — it is
  the cotton reading of Radix's `onSelect` with the default prevented.

- **Data Table** — a guide, not a component. Upstream ships one because React
  needs TanStack Table to sort a list of rows; here `order_by`, `filter` and
  `Paginator` already do it, so the page shows the wiring: sortable headers,
  a filter that survives paging through `{% querystring %}`,
  `get_elided_page_range` feeding `pagination.ellipsis`, row selection and
  column visibility.

### Changed

- **`data-slot` reaches the older components.** shadcn/ui uses it as a selector
  target, not as decoration — `button_group` sizes a select inside it through
  `[&>[data-slot=select-trigger]]`, and rules like that were inert here because
  only the newer components emitted the attribute. 91 files now carry the value
  the registry defines for them.

  Where upstream defines none, none was invented. `typography` is plain
  elements with classes; `spinner`, `toast`, `combobox`, `command_dialog`,
  `table.empty`, `button_group.text`, `input_group.text`,
  `navigation_menu.link_details` and `form.fieldset` have no counterpart
  carrying a slot, so they still have none.

  This changes markup, not behaviour. Copies in your project are untouched
  until you run `add <name> --overwrite`.

- **A component's `class` no longer leaks past the element it belongs to.**
  cotton hands a component both `{{ class }}` and `{{ attrs }}`, and `class`
  stays inside `attrs`, so a component writing both emitted the attribute
  twice — 3481 tags across the documentation site. Worse, `{{ class }}` in a
  component that never declared it fell through to the enclosing context, so
  `<c-pagination.next class="w-40">` also put `w-40` on the chevron inside it.
  259 component templates now declare `class` in `<c-vars>`, which gives it a
  local default and takes it out of `attrs`.

  Two of them were rendering wrong because of it. `menubar.sub-trigger` wrote
  `{{ attrs }}` before its own `class`, and a parser keeps the first of a
  repeated attribute — so passing any `class` to it discarded every base class
  the component had. `accordion.content` and `command_dialog` applied the
  class to two elements at once.

  The suite now renders every component with a class and fails on any element
  carrying an attribute twice, or on a class landing in more than one place.

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

- **Pin `django-cotton>=2.7.1`.** Below that, a dynamic attribute holding a
  quote could break out of the attribute and inject arbitrary ones. It is
  cotton's fix, not ours, but nothing on our side made the requirement visible;
  the installation page now carries it, along with which cotton line each
  Django version can install.

### Fixed

- `add` now accepts the spelling you see in the markup. The tag is
  `<c-toggle-group>` but the directory has to be `toggle_group`, and only the
  second worked; `add toggle-group`, `add hover-card`, `add radio-group` and
  `add scroll-area` failed with "Unknown component". Both spellings work now.
- The install command on four documentation pages named the component the way
  the CLI rejected it.
- `table.empty` carried a stray `',` left over from the React source and put
  `text-foreground',` on the cell as a class.
- `accordion.trigger` and `menubar.sub-trigger` had `{{ attrs }}` broken across
  a line by an editor reflowing the attribute list. Django substitutes it
  anyway; `django-cotton` 2.x does not, so on any project running Django 5.2 or
  newer — where cotton 2.x is the only option — the braces reached the page as
  text and every attribute passed to those two components was dropped.
- `toast.trigger` carried `x-data` twice, the second one empty. HTML keeps the
  first, so it was dead markup rather than a broken toast, but it is gone.
- `toast.trigger`, `toast.content` and `navigation_menu.link_details` dropped
  every attribute passed to them, and the last two took no `class` either.
- `dropdown_menu` positioned its menu against the page rather than the trigger.
  The content is `absolute` and nothing above it was positioned, so it anchored
  to whatever ancestor happened to be, landing under the trigger only because
  an `absolute` box with no offsets stays where it fell in the flow. Giving it
  `left-0` — or any alignment at all — sent it to the corner of the page. The
  menu is now positioned against the component, and `align` works.

  Its markup changed with it: items were `<li>` inside a `<ul>` that also held
  the labels and separators, which is not valid, and the whole list is now
  `<div role="menu">` as the registry has it. Copies already in your project
  are untouched until you run `add dropdown_menu --overwrite`.

- `separator` ignored `decorative`. Any value made the test pass, including
  `decorative="false"`, so the separator was always `role="none"` and a screen
  reader always skipped it. It now emits `role="separator"` with an
  `aria-orientation` when you ask for the semantic one.

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
