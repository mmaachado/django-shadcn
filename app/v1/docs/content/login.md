---
title: Login and Sign Up
description: A split-screen log-in page and its sign-up twin, each a card with the form, a divider and two provider buttons.
description.pt-br: Uma página de login em tela dividida e a irmã dela de cadastro, cada uma um card com o formulário, um divisor e dois botões de provedor.
description.es: Una página de inicio de sesión en pantalla dividida y su gemela de registro, cada una una tarjeta con el formulario, un divisor y dos botones de proveedor.
---

<c-docs.block-preview name="login" />

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add login
```

:::en
This is a block, not a component. It installs two pages,
`templates/blocks/login/page.html` and `templates/blocks/login/signup.html`,
and the components they use to `templates/cotton/`.

## Sign up

The second page is the same layout with a name field and a password hint.
:::pt-br
Isto é um bloco, não um componente. Ele instala duas páginas,
`templates/blocks/login/page.html` e `templates/blocks/login/signup.html`, e os
componentes que elas usam em `templates/cotton/`.

## Cadastro

A segunda página é o mesmo layout, com um campo de nome e uma dica de senha.
:::

<c-docs.block-preview name="login" page="signup" />

:::en
## Usage

Each page extends your `base.html` and fills its
`{% verbatim %}{% block content %}{% endverbatim %}`. Render them from your
views, and pass `base_template` to put them inside another layout:
:::pt-br
## Uso

Cada página estende o seu `base.html` e preenche o
`{% verbatim %}{% block content %}{% endverbatim %}` dele. Renderize-as a
partir das suas views, e passe `base_template` para colocá-las dentro de outro
layout:
:::

```python
def log_in(request):
    return render(request, "blocks/login/page.html")


def sign_up(request):
    return render(request, "blocks/login/signup.html")
```

:::en
## Wiring the form

The block is markup. Each form posts to its own URL, with fields named
`email` and `password`, plus `name` on the sign-up page, and carries
`{% verbatim %}{% csrf_token %}{% endverbatim %}`. Point the form at the view
that handles it, and the two provider buttons at your providers' login URLs.

With django-allauth the pages are already written: the
[django-allauth]({% url 'page' slug='allauth' %}) block fills its templates
with the same components. Use this one for a project that handles accounts
itself, or as the layout to move those forms into.

## Made of

[Card]({% url 'page' slug='card' %}),
[Field]({% url 'page' slug='field' %}),
[Input]({% url 'page' slug='input' %}) and
[Button]({% url 'page' slug='button' %}). The divider is `field.separator` with
its label painted in the card's colour.
:::pt-br
## Ligando o formulário

O bloco é markup. Cada formulário envia para a própria URL, com campos chamados
`email` e `password`, mais `name` na página de cadastro, e leva
`{% verbatim %}{% csrf_token %}{% endverbatim %}`. Aponte o formulário para a
view que o trata, e os dois botões de provedor para as URLs de login dos seus
provedores.

Com o django-allauth as páginas já estão escritas: o bloco
[django-allauth]({% url 'page' slug='allauth' %}) preenche os templates dele com
os mesmos componentes. Use este num projeto que cuida das contas por conta
própria, ou como o layout para onde levar aqueles formulários.

## Feito de

[Card]({% url 'page' slug='card' %}),
[Field]({% url 'page' slug='field' %}),
[Input]({% url 'page' slug='input' %}) e
[Button]({% url 'page' slug='button' %}). O divisor é o `field.separator` com o
rótulo pintado na cor do card.
:::
