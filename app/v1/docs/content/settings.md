---
title: Settings
description: A settings page in two tabs, a profile form and a list of labelled switches.
description.pt-br: Uma página de configurações em duas abas, um formulário de perfil e uma lista de switches com rótulo.
description.es: Una página de ajustes en dos pestañas, un formulario de perfil y una lista de switches con etiqueta.
---

<c-docs.block-preview name="settings" />

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add settings
```

:::en
This is a block, not a component. It installs
`templates/blocks/settings/page.html`, and the components it uses to
`templates/cotton/`.

## Usage
:::pt-br
Isto é um bloco, não um componente. Ele instala
`templates/blocks/settings/page.html`, e os componentes que ele usa em
`templates/cotton/`.

## Uso
:::

```python
def settings_page(request):
    return render(request, "blocks/settings/page.html")
```

:::en
The page extends your `base.html` and fills its
`{% verbatim %}{% block content %}{% endverbatim %}`. To show it inside the
[Sidebar Layout]({% url 'page' slug='sidebar-layout' %}), move what is inside
`content` into that layout's `{% verbatim %}{% block main %}{% endverbatim %}`.

## Wiring the forms

Each tab is its own form, posting to the page's URL, so one save does not
submit the other tab. The profile fields are named `name`, `email` and
`website`; replace the sample values with the user's, or render a Django form's
fields into the same `form.field` rows.

The switches are real checkboxes. One that is on posts its name, and one that
is off posts nothing, so read them with `name in request.POST`. Set `checked`
from the stored preference when the page renders.

## Made of

[Tabs]({% url 'page' slug='tabs' %}),
[Form]({% url 'page' slug='form' %}),
[Input]({% url 'page' slug='input' %}),
[Switch]({% url 'page' slug='switch' %}),
[Label]({% url 'page' slug='label' %}),
[Separator]({% url 'page' slug='separator' %}) and
[Button]({% url 'page' slug='button' %}).
:::pt-br
A página estende o seu `base.html` e preenche o
`{% verbatim %}{% block content %}{% endverbatim %}` dele. Para mostrá-la dentro
do [Sidebar Layout]({% url 'page' slug='sidebar-layout' %}), leve o que está
dentro de `content` para o `{% verbatim %}{% block main %}{% endverbatim %}`
daquele layout.

## Ligando os formulários

Cada aba é um formulário próprio, enviando para a URL da página, então salvar
uma não envia a outra. Os campos do perfil se chamam `name`, `email` e
`website`; troque os valores de exemplo pelos do usuário, ou renderize os
campos de um formulário Django nas mesmas linhas de `form.field`.

Os switches são checkboxes de verdade. Um ligado envia o nome dele, e um
desligado não envia nada, então leia-os com `name in request.POST`. Defina
`checked` a partir da preferência guardada quando a página renderizar.

## Feito de

[Tabs]({% url 'page' slug='tabs' %}),
[Form]({% url 'page' slug='form' %}),
[Input]({% url 'page' slug='input' %}),
[Switch]({% url 'page' slug='switch' %}),
[Label]({% url 'page' slug='label' %}),
[Separator]({% url 'page' slug='separator' %}) e
[Button]({% url 'page' slug='button' %}).
:::
