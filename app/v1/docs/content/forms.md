---
title: Forms and Django
description: Rendering a Django form with the components, showing errors, keeping bound values, CSRF, and swapping a form with htmx.
description.pt-br: Renderizar um formulário Django com os componentes, mostrar erros, manter os valores preenchidos, o CSRF, e trocar um formulário com o htmx.
description.es: Renderizar un formulario de Django con los componentes, mostrar errores, mantener los valores, el CSRF, y cambiar un formulario con htmx.
---

:::en
## The components are markup

Nothing here replaces Django's forms. A form class still validates and cleans
the data; the components are what a field looks like. So rendering a form is
writing each field's markup with the values Django already has: the field's
`id_for_label`, its `html_name`, its bound `value`, its `errors` and its
`help_text`.

## One field

[Field]({% url 'page' slug='field' %}) lays out a label, the control, a
description and an error. Tie them together, so the label names the control
and the error is read with it:
:::pt-br
## Os componentes são markup

Nada aqui substitui os formulários do Django. Uma classe de formulário continua
validando e limpando os dados; os componentes são a cara de um campo. Então
renderizar um formulário é escrever o markup de cada campo com os valores que o
Django já tem: o `id_for_label` do campo, o `html_name`, o `value` preenchido,
os `errors` e o `help_text`.

## Um campo

O [Field]({% url 'page' slug='field' %}) diagrama um rótulo, o controle, uma
descrição e um erro. Ligue-os, para que o rótulo dê nome ao controle e o erro
seja lido junto com ele:
:::

```html
{% with field=form.email %}
  <c-field>
    <c-field.label for="{{ field.id_for_label }}">{{ field.label }}</c-field.label>
    <c-input id="{{ field.id_for_label }}" name="{{ field.html_name }}" type="email"
      value="{{ field.value|default:'' }}"
      {% if field.field.required %}required{% endif %}
      {% if field.errors %}aria-invalid="true" aria-describedby="{{ field.id_for_label }}-error"{% endif %} />
    {% if field.help_text %}<c-field.description>{{ field.help_text }}</c-field.description>{% endif %}
    <c-field.error id="{{ field.id_for_label }}-error" :errors="field.errors" />
  </c-field>
{% endwith %}
```

:::en
`errors` on `field.error` takes the field's error list as it is: one error is
written inline, several as a list, and nothing renders when it is empty. The
colon in front of `:errors` makes cotton pass the list rather than its text.

The bound `value` is what keeps a field filled after a failed post. Leave it
off a password field.

## A partial for every field

Written once as an include, the field above renders any text field:
:::pt-br
O `errors` do `field.error` aceita a lista de erros do campo como ela é: um
erro é escrito em linha, vários como uma lista, e nada é renderizado quando ela
está vazia. Os dois-pontos na frente de `:errors` fazem o cotton passar a lista,
e não o texto dela.

O `value` preenchido é o que mantém um campo cheio depois de um envio com
falha. Deixe-o de fora de um campo de senha.

## Um partial para cada campo

Escrito uma vez como um include, o campo acima renderiza qualquer campo de
texto:
:::

```html
{# templates/partials/field.html #}
<c-field>
  <c-field.label for="{{ field.id_for_label }}">{{ field.label }}</c-field.label>
  <c-input id="{{ field.id_for_label }}" name="{{ field.html_name }}"
    type="{{ field.field.widget.input_type|default:'text' }}"
    value="{{ field.value|default:'' }}"
    {% if field.errors %}aria-invalid="true"{% endif %} />
  <c-field.error :errors="field.errors" />
</c-field>
```

```html
<form method="post">
  {% csrf_token %}
  {% for field in form %}
    {% include "partials/field.html" %}
  {% endfor %}
  <c-button>Save</c-button>
</form>
```

:::en
## Which component for which field

| Django | Component |
| --- | --- |
| `CharField`, `EmailField`, `URLField`, `IntegerField` | [Input]({% url 'page' slug='input' %}), with the widget's `input_type` |
| a `Textarea` widget | [Textarea]({% url 'page' slug='textarea' %}) |
| `BooleanField` | [Checkbox]({% url 'page' slug='checkbox' %}) or [Switch]({% url 'page' slug='switch' %}); a checked box posts, an unchecked one posts nothing |
| `ChoiceField`, `ModelChoiceField` | [Native Select]({% url 'page' slug='native-select' %}), looping over `field.field.choices` |
| `RadioSelect` | [Radio Group]({% url 'page' slug='radio-group' %}), one `name` on every radio |
| `MultipleChoiceField` | a group of checkboxes sharing one `name`, read with `getlist` |
| `DateField` | [Date Picker]({% url 'page' slug='date-picker' %}) or [Calendar]({% url 'page' slug='calendar' %}), which post the ISO date |
| `FileField` | an Input with `type="file"`, and `enctype="multipart/form-data"` on the form |

The native controls post without JavaScript. The ones built on Alpine, the
date picker, the select and the combobox, post through a hidden input and need
it.

## Errors that are not a field's

`form.non_field_errors` belongs above the form, in an
[Alert]({% url 'page' slug='alert' %}), which a screen reader announces as the
page loads:
:::pt-br
## Que componente para que campo

| Django | Componente |
| --- | --- |
| `CharField`, `EmailField`, `URLField`, `IntegerField` | [Input]({% url 'page' slug='input' %}), com o `input_type` do widget |
| um widget `Textarea` | [Textarea]({% url 'page' slug='textarea' %}) |
| `BooleanField` | [Checkbox]({% url 'page' slug='checkbox' %}) ou [Switch]({% url 'page' slug='switch' %}); uma caixa marcada envia, uma desmarcada não envia nada |
| `ChoiceField`, `ModelChoiceField` | [Native Select]({% url 'page' slug='native-select' %}), percorrendo `field.field.choices` |
| `RadioSelect` | [Radio Group]({% url 'page' slug='radio-group' %}), com o mesmo `name` em cada radio |
| `MultipleChoiceField` | um grupo de checkboxes com o mesmo `name`, lido com `getlist` |
| `DateField` | [Date Picker]({% url 'page' slug='date-picker' %}) ou [Calendar]({% url 'page' slug='calendar' %}), que enviam a data ISO |
| `FileField` | um Input com `type="file"`, e `enctype="multipart/form-data"` no formulário |

Os controles nativos enviam sem JavaScript. Os feitos sobre o Alpine, o date
picker, o select e o combobox, enviam por um input oculto e precisam dele.

## Erros que não são de um campo

O `form.non_field_errors` fica acima do formulário, num
[Alert]({% url 'page' slug='alert' %}), que um leitor de tela anuncia quando a
página carrega:
:::

```html
{% if form.non_field_errors %}
  <c-alert variant="destructive">
    <c-alert.title>Please check the form</c-alert.title>
    <c-alert.description>{{ form.non_field_errors|join:" " }}</c-alert.description>
  </c-alert>
{% endif %}
```

:::en
## CSRF

Every form that posts needs `{% verbatim %}{% csrf_token %}{% endverbatim %}`,
including one inside a [Dialog]({% url 'page' slug='dialog' %}) or a
[Sheet]({% url 'page' slug='sheet' %}). A button inside a form submits it unless
it says `type="button"`, which matters for the triggers of a dialog or a
popover that sit inside one.

## Swapping a form with htmx

A form re-rendered on the server with its errors can be swapped in place, so
the page does not reload. The view returns the same template, and htmx puts it
where the old form was:
:::pt-br
## CSRF

Todo formulário que envia precisa de
`{% verbatim %}{% csrf_token %}{% endverbatim %}`, inclusive um dentro de um
[Dialog]({% url 'page' slug='dialog' %}) ou de um
[Sheet]({% url 'page' slug='sheet' %}). Um botão dentro de um formulário o envia
a menos que diga `type="button"`, o que importa para os triggers de um diálogo
ou de um popover que fiquem dentro de um.

## Trocando um formulário com o htmx

Um formulário renderizado de novo no servidor com os erros pode ser trocado no
lugar, para a página não recarregar. A view devolve o mesmo template, e o htmx
o põe onde estava o formulário antigo:
:::

```html
{# templates/partials/profile_form.html #}
<form hx-post="{% url 'profile' %}" hx-swap="outerHTML">
  {% csrf_token %}
  {% for field in form %}
    {% include "partials/field.html" %}
  {% endfor %}
  <c-button>Save</c-button>
</form>
```

```python
def profile(request):
    form = ProfileForm(request.POST or None, instance=request.user)
    if request.method == "POST" and form.is_valid():
        form.save()
    template = "partials/profile_form.html" if request.htmx else "profile.html"
    return render(request, template, {"form": form})
```

:::en
`request.htmx` comes from django-htmx; without it, check the `HX-Request`
header. Requests htmx sends outside a form, such as `hx-delete` on a button,
need the CSRF token too: set it once on the `<body>`, and every request below
carries it.
:::pt-br
O `request.htmx` vem do django-htmx; sem ele, confira o cabeçalho
`HX-Request`. As requisições que o htmx envia fora de um formulário, como um
`hx-delete` num botão, também precisam do token de CSRF: defina-o uma vez no
`<body>`, e toda requisição abaixo dele o leva.
:::

```html
<body hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'>
```

:::en
Alpine keeps working in the swapped markup: it starts the components in new
content on its own, so a date picker or a select inside a swapped form behaves
as on first load.
:::pt-br
O Alpine continua funcionando no markup trocado: ele inicia os componentes de
um conteúdo novo por conta própria, então um date picker ou um select dentro
de um formulário trocado se comporta como no primeiro carregamento.
:::
