---
title: Installation
description: Set up Tailwind, Alpine and django-cotton, then start adding components.
---

## Requirements

- Python 3.12 or newer
- Django 4.2 or newer
- [django-cotton](https://django-cotton.com) 2.7.1 or newer, which provides the
  `<c-...>` template syntax every component is written in
- Tailwind CSS 4.1 or newer. Several components use utilities that landed in
  4.1, and a build on 4.0 drops them without an error — the component renders,
  missing a rule here and there
- Alpine.js, for the components that are interactive

### Which django-cotton

Your Django version decides this for you, so it is worth knowing before you
pick one:

| django-cotton | Works with        |
| ------------- | ----------------- |
| 1.x           | Django 4.2 to 5.1 |
| 2.x           | Django 4.2 to 6.x |

**On Django 5.2 or newer, 2.x is the only line that installs.** And versions
below 2.7.1 carry a fix worth having: a dynamic attribute holding a quote could
break out of the attribute and inject arbitrary ones. Pin the floor:

```
django-cotton>=2.7.1
```

The components themselves run on both lines — every one of them is rendered
against 1.6 and against 2.7 on each change — so an older project keeps working.
The floor is about the injection fix, not about the markup.

## Set up the project

Install django-cotton and add it to your settings:

```python
INSTALLED_APPS = [
    ...
    "django_cotton",
]
```

Then initialize the theme. This creates `templates/cotton/` and drops an
`input.css` holding the palette, the design tokens and the Geist font faces
that every component builds on:

```bash
uvx django_shadcn@latest init
```

Running it again keeps the `input.css` you have and says so — your palette is
never silently replaced. Pass `--force` when you do want the shipped one back.

Point Tailwind at that file and let it watch your templates:

```bash
npx @tailwindcss/cli -i input.css -o static/css/output.css --watch
```

Finally, load the stylesheet and Alpine from your base template:

```html
<link rel="stylesheet" href="{% static 'css/output.css' %}" />
<script src="{% static 'js/alpine.min.js' %}" defer></script>
```

Serving Alpine from your own static files keeps the page working offline and
avoids trusting a CDN at runtime. If you would rather load it from one, pin the
version instead of tracking `latest`.

### Alpine plugins

Two components — `accordion` and `collapsible` — animate through
`@alpinejs/collapse`, which Alpine's core does not include. Without it they
render correctly and simply never animate: no error, nothing in the console.

Load the plugin before Alpine itself:

```html
<script src="{% static 'js/collapse.min.js' %}" defer></script>
<script src="{% static 'js/alpine.min.js' %}" defer></script>
```

`add` names any plugin a component needs at the end of the run, so you do not
have to remember which ones do.

## Add a component

```bash
uvx django_shadcn@latest add button
```

Components land in `templates/cotton/<name>/`, and their dependencies come
along automatically. You can name several at once:

```bash
uvx django_shadcn@latest add button card input
```

Use it like any other cotton component:

```html
<c-button variant="outline">Click me</c-button>
```

## Your files stay yours

`add` never overwrites what is already on disk. Running it a second time
reports the files it skipped and leaves your edits alone — the components are
yours to change once they land.

Two flags change that, on purpose:

| Flag          | Existing file | Removes anything        |
| ------------- | ------------- | ----------------------- |
| _(default)_   | skipped       | never                   |
| `--overwrite` | replaced      | never                   |
| `--sync`      | replaced      | yes, mirrors the source |

`--sync` lists what it is about to delete and asks before doing it. Pass
`--yes` to skip the prompt in a script.

Add `--dry-run` to any of them to see the outcome without it happening:

```bash
uvx django_shadcn@latest add button --sync --dry-run
```

It prints the same per-file report the real run would, and writes nothing. This
is worth the habit before `--sync`, the one mode that deletes.

## Find what is available

```bash
uvx django_shadcn@latest list
```

Installed components are marked, so you can tell at a glance what a project is
already using.
