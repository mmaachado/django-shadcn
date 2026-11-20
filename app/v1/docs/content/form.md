---
title: Form
description: Displays well-designed HTML forms.
description.pt-br: Formulários HTML bem apresentados.
description.es: Formularios HTML bien presentados.
---

<c-docs.demo-section class="min-h-[350px]">
<form class="w-full max-w-sm space-y-4" onsubmit="return false">
<c-form.field>
<c-form.label for="form-demo-email">Email</c-form.label>
<c-input id="form-demo-email" type="email" placeholder="you@example.com" />
<c-form.description>We never share your address.</c-form.description>
</c-form.field>
<c-button>Subscribe</c-button>
</form>
</c-docs.demo-section>

<c-docs.cheat-sheet name="form">
<c-form.field>
  <c-form.label for="{{ field.id_for_label }}" error="{{ field.errors|yesno:'true,' }}">{{ field.label }}</c-form.label>
  <c-input id="{{ field.id_for_label }}" name="{{ field.html_name }}" value="{{ field.value|default:'' }}" />
  <c-form.error>{{ field.errors|first }}</c-form.error>
</c-form.field>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add form
```

:::en
## Usage

The parts lay out one form field: `field` stacks a `label`, the control, a
`description` and an `error`. They are markup only, so rendering a Django form
is a loop over its fields, with the bound value and the first error in place:
:::pt-br
## Uso

As partes diagramam um campo de formulário: o `field` empilha um `label`, o
controle, uma `description` e um `error`. São só markup, então renderizar um
formulário Django é um laço sobre os campos, com o valor preenchido e o
primeiro erro no lugar:
:::

```html
<form method="post">
  {% csrf_token %}
  {% for field in form %}
    <c-form.field>
      <c-form.label for="{{ field.id_for_label }}" error="{{ field.errors|yesno:'true,' }}">{{ field.label }}</c-form.label>
      <c-input id="{{ field.id_for_label }}" name="{{ field.html_name }}" value="{{ field.value|default:'' }}" />
      {% if field.help_text %}<c-form.description>{{ field.help_text }}</c-form.description>{% endif %}
      {% if field.errors %}<c-form.error>{{ field.errors|first }}</c-form.error>{% endif %}
    </c-form.field>
  {% endfor %}
  <c-button>Save</c-button>
</form>
```

:::en
`error` on the label turns it red when it has a value; `yesno` gives it one
only when the field has errors. [Field]({% url 'page' slug='field' %}) is the
newer component for the same job, with orientations, sets and a group.

## Examples

### Errors
:::pt-br
O `error` no rótulo o deixa vermelho quando tem um valor; o `yesno` só dá um a
ele quando o campo tem erros. O [Field]({% url 'page' slug='field' %}) é o
componente mais novo para o mesmo trabalho, com orientações, sets e um grupo.

## Exemplos

### Erros
:::

<c-docs.example>
<c-form.field class="max-w-sm">
  <c-form.label for="form-error-username" error="true">Username</c-form.label>
  <c-input id="form-error-username" value="ada carter" aria-invalid="true" aria-describedby="form-error-username-message" />
  <c-form.error id="form-error-username-message">Usernames cannot contain spaces.</c-form.error>
</c-form.field>
</c-docs.example>

:::en
## RTL

Labels, descriptions and errors align to the start, so under `dir="rtl"` a
field mirrors with the text.

## Accessibility

`form.label` is a `<label>`: tie it to the control with `for` and the field's
id. The error is plain text and is not announced on its own, so point the
control at it with `aria-describedby` and mark it `aria-invalid="true"`, as the
example does.

## API reference
:::pt-br
## RTL

Rótulos, descrições e erros se alinham ao início, então sob `dir="rtl"` um
campo espelha com o texto.

## Acessibilidade

O `form.label` é um `<label>`: ligue-o ao controle com `for` e o id do campo. O
erro é texto simples e não é anunciado sozinho, então aponte o controle para
ele com `aria-describedby` e marque-o com `aria-invalid="true"`, como faz o
exemplo.

## Referência da API
:::

<c-docs.api-reference name="form" />
