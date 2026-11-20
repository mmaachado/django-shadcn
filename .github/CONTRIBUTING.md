# Contributing

Thanks for your interest in contributing to django-shadcn.

Please take a moment to read this before opening your first pull request, and
check the open issues and pull requests to see if someone is already working on
something similar.

## About this repository

django-shadcn is an unofficial Django port of [shadcn/ui](https://ui.shadcn.com).
It ships a CLI that copies [django-cotton](https://django-cotton.com) templates
into your project, so you own the components and can change them freely.

## Structure

```
.
├── app/v1/docs/         the documentation site, published from this repository
├── components/          the cotton components, one directory per component
│   └── input.css        Tailwind theme: palette, tokens and fonts
├── src/django_shadcn/   the Typer CLI
└── tests/
```

| Path                              | Description                                        |
| --------------------------------- | -------------------------------------------------- |
| `src/django_shadcn/add.py`        | `add` command: copies components into a project    |
| `src/django_shadcn/initialize.py` | `init` command: creates the components directory   |
| `src/django_shadcn/list.py`       | `list` command                                     |
| `src/django_shadcn/components.py` | the registry: every component and its dependencies |
| `components/<name>/index.html`    | what `<c-name>` renders                            |
| `app/v1/docs/content/<name>.md`   | the page documenting it                            |
| `app/v1/docs/docs/nav.py`         | the sidebar, and the only route the site has       |

## Getting started

Fork the repository, then:

```bash
git clone https://github.com/your-username/django-shadcn.git
cd django-shadcn
git checkout -b my-new-branch
uv sync
```

Run the CLI from the checkout with `uv run django_shadcn list`.

## Seeing your work

The documentation site in `app/v1/docs/` renders the components in your
checkout, not a copy of them, so editing one and reloading the page is the
whole loop. It is a Django project of its own, and it runs on Python 3.14:

```bash
cd app/v1/docs
uv sync
uv run python manage.py runserver
```

The portal's test requests every page listed in `nav.py`, in every language,
and fails on any response other than a 200. Collect the static files first.
CI runs these too:

```bash
cd app/v1/docs
uv run python manage.py collectstatic --noinput
uv run python manage.py test
```

Alpine and htmx are committed under `static/js/`, so nothing has to be
downloaded. The stylesheet is built by the Tailwind CLI, and a class Tailwind
does not recognise is dropped from the build without an error — which is why a
new one is worth watching appear in the output rather than trusting by eye:

```bash
cd app/v1/docs
npm install
npx @tailwindcss/cli -i assets/input.css -o static/css/output.css --watch
```

Commit the rebuilt `static/css/output.css` along with your component. The site
is served from the file, not compiled on deploy. CI rebuilds it too, and fails
if the committed file is missing a class the build has, still has one nothing
uses anymore, or matches on class names but differs in the CSS itself.

## Adding a component

Components are written with Tailwind CSS 4.1 or newer and Alpine.js. Markup,
utility classes and variant names follow the upstream shadcn/ui component,
adapted to cotton syntax. `components/input.css` is the source of the palette
and fonts — do not introduce new design tokens.

Every component takes variants through `<c-vars>` with defaults, applies them
with `{% if %}` inside the class list, and forwards both `{{ attrs }}` and the
caller's `class`. `components/button/index.html` is the reference.

Directory names use `snake_case`, because the directory name is the tag name:
`components/alert_dialog/` is `<c-alert_dialog>`.

Icons are always `<c-icon name="...">`, never an inline `<svg>`. The subset in
`components/icon/` is generated from [Lucide](https://lucide.dev) by
`scripts/generate_icons.py` — add one by running the script, not by pasting
markup. A weekly workflow regenerates the subset against the latest Lucide
release and opens an issue when a shape changes.

Four things to touch:

1. `components/<name>/index.html`, plus any subcomponents
2. an entry in `src/django_shadcn/components.py`, naming the components it uses
   and any Alpine plugin its markup needs
3. a page in `app/v1/docs/content/<name>.md`
4. an entry in `app/v1/docs/docs/nav.py`

The test suite fails if a component is missing from the registry, if it uses
another component without declaring it as a dependency, if its markup needs an
Alpine plugin the registry does not declare, or if it has no page and no
sidebar entry.

On the page, write each demo once, in `<c-docs.example>`. It renders the
markup and shows the same text below it as the code to copy, Django tags
included, so the two cannot drift apart. Keep fenced code for what is not a
demo: install commands, Python and settings.

Two parts of the page are generated from the templates, so they cannot fall
behind them: `<c-docs.api-reference name="<name>" />`, the table of every
attribute, its default and its values, and `<c-docs.cheat-sheet name="<name>">`
under the opening demo, holding the snippet it shows beside the tag, the parts
and the attributes.

The last two are what makes the component findable, and they are written in the
same pull request as the component itself — documentation written later is
documentation that describes an earlier version.

## Adding a block

A block is a page assembled from components, such as a dashboard or a
settings screen. It is a registry entry like any component, marked
`block=True`, so `add` installs it with everything it depends on and `list`
shows it apart.

Its files live in `components/<name>/` and install to
`templates/blocks/<name>/`, one directory per block. The page is `page.html`,
and it opens with

```django
{% extends base_template|default:"base.html" %}
```

so a project renders it from a view inside its own layout, and the portal
previews it by passing a bare frame instead. The content goes in
`{% block content %}`, and the sample data is written into the markup, to be
replaced.

A block uses components and never adds one. If it needs a component that does
not exist, the component is its own pull request, and the block waits for it.

The page in `app/v1/docs/content/` shows the block with
`<c-docs.block-preview name="<name>" />`, which frames the installed file.

## Translating a page

A page is one file, whatever the language. Prose that has a translation is
written as a passage, one block per language, closed by a bare `:::`:

```markdown
:::en
## Usage

Press the button.
:::pt-br
## Uso

Aperte o botão.
:::
```

The active language picks its block, and a language with no block falls back
to English, as does prose outside any passage. Demos and fenced code stay
outside the passages, written once for every language: a passage that holds
either fails to render. The `description` in the front matter takes a suffix
instead, as in `description.pt-br:`.

`introduction` and `installation` are nearly all prose, so they are translated
as whole files in `content/<language>/`.

## Tests and linting

```bash
uv run task lint     # ruff check
uv run task format   # ruff format
uv run task test     # ruff check, then pytest with coverage
```

Code is formatted by ruff at 79 columns with single quotes. Please make sure
tests pass before opening a pull request, and add tests for new behaviour.

## Commit convention

Please write commit messages as `category(scope): message`, using one of:

`feat`, `fix`, `refactor`, `docs`, `build`, `test`, `ci`, `chore`.

For example: `feat(components): add the switch component`.

## Releases

Maintainers only. The version is never written in a file — it comes from the git
tag, so cutting a release means creating one:

```bash
git checkout master && git pull
git tag -a v1.0.0 -m "v1.0.0"
git push origin v1.0.0
```

Add the section to `CHANGELOG.md` first, headed `## <version>`. The workflow
copies it into the GitHub release and appends the generated commit list below
it. Without a matching section the release still goes out, carrying only the
generated notes — which is why anything a reader has to know before upgrading
belongs in the changelog and not in a commit message.

The Release workflow builds, checks that the artifact matches the tag, publishes
to PyPI and opens the GitHub release. Running it manually from the Actions tab
publishes to TestPyPI instead, which is the way to rehearse a change to the
pipeline without spending a version number.

Never move or recreate a published tag. PyPI refuses to accept a version it has
already seen, even after it is deleted, so a broken release is fixed by
publishing the next patch version and yanking the broken one.

## Requesting components and blocks

For a component that is not ported yet, open a component request issue. For a
full page or section built out of several components — a dashboard, a login
screen — open a blocks discussion instead.
