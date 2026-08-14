# Description

<!-- What does this change and why. Link the issue it closes, if any. -->

Closes #

## Type of change

- [ ] Bug fix
- [ ] New component
- [ ] Component change
- [ ] CLI change
- [ ] Documentation
- [ ] Repository tooling

## Checklist

- [ ] `uv run task lint` passes
- [ ] `uv run task test` passes
- [ ] New or changed behaviour is covered by a test
- [ ] For a component: it is registered in `components.py` with its dependencies
- [ ] For a component: it has a page in `app/v1/docs/content/` and a line in `docs/nav.py`
- [ ] For a component: it renders on the site (`cd app/v1/docs && uv run python manage.py runserver`)
- [ ] For a component: `static/css/output.css` is rebuilt and committed

## Screenshots

<!-- For component changes, show the result. Delete this section otherwise. -->
