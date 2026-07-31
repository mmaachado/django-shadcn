# Contributing

Thanks for your interest in contributing to django-shadcn.

Please take a moment to read this before opening your first pull request, and
check the open issues and pull requests to see if someone is already working on
something similar.

## About this repository

django-shadcn is an unofficial Django port of [shadcn/ui](https://ui.shadcn.com).
It ships a CLI that copies [django-cotton](https://django-cotton.com) templates
into your project, so you own the components and can change them freely.

The repository holds two separate [uv](https://docs.astral.sh/uv/) projects: the
library at the root and the playground under `docs/`.

## Structure

```
.
├── components/          the cotton components, one directory per component
│   └── input.css        Tailwind theme: palette, tokens and fonts
├── docs/                Django playground used to render components locally
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

## Getting started

Fork the repository, then:

```bash
git clone https://github.com/your-username/django-shadcn.git
cd django-shadcn
git checkout -b my-new-branch
uv sync
```

Run the CLI from the checkout with `uv run django_shadcn list`.

## The playground

`docs/` is a small Django site that renders every component. Use it to check
your work:

```bash
cd docs
uv sync
uv run manage.py runserver
```

## Adding a component

Components are written with Tailwind CSS v4 and Alpine.js. Markup, utility
classes and variant names follow the upstream shadcn/ui component, adapted to
cotton syntax. `components/input.css` is the source of the palette and fonts —
do not introduce new design tokens.

Every component takes variants through `<c-vars>` with defaults, applies them
with `{% if %}` inside the class list, and forwards both `{{ attrs }}` and the
caller's `class`. `components/button/index.html` is the reference.

Directory names use `snake_case`, because the directory name is the tag name:
`components/alert_dialog/` is `<c-alert_dialog>`.

Five things to touch:

1. `components/<name>/index.html`, plus any subcomponents
2. an entry in `src/django_shadcn/components.py`, listing the components it uses
3. a page in `docs/templates/<name>.html` showing every variant
4. a view in `docs/docs/views.py` and a route in `docs/docs/urls.py`
5. a link in the sidebar of `docs/templates/base.html`

The test suite fails if a component is missing from the registry, or if it uses
another component without declaring it as a dependency.

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
