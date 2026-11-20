---
title: Field
description: Lays out a label, a control, its description and its errors.
description.pt-br: Organiza o rótulo, o controle, a descrição e os erros de um campo.
description.es: Organiza la etiqueta, el control, la descripción y los errores de un campo.
---

<c-docs.demo-section class="min-h-[350px]">
<c-field class="w-[360px] text-start">
<c-field.label for="email">Email</c-field.label>
<c-input id="email" type="email" placeholder="you@example.com" />
<c-field.description>We will never share your address.</c-field.description>
</c-field>
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add field
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-field>
  <c-field.label for="email">Email</c-field.label>
  <c-input id="email" type="email" />
  <c-field.description>We will never share your address.</c-field.description>
</c-field>
```

:::en
<a href="{% url 'page' slug='form' %}" class="font-medium underline underline-offset-4">Form</a>
covers the same ground with a smaller surface. Field is the newer shadcn/ui
component: more parts, orientations, and a group that lays out several
fields at once.

## Examples

### Group
:::pt-br
O <a href="{% url 'page' slug='form' %}" class="font-medium underline underline-offset-4">Form</a>
cobre o mesmo terreno com uma superfície menor. O Field é o componente mais novo
do shadcn/ui: mais partes, orientações, e um grupo que diagrama vários campos de
uma vez.

## Exemplos

### Grupo
:::

<c-docs.example>
<c-field.group class="w-full max-w-md text-start">
  <c-field>
    <c-field.label for="name">Name</c-field.label>
    <c-input id="name" placeholder="Ada Lovelace" />
  </c-field>
  <c-field>
    <c-field.label for="bio">Bio</c-field.label>
    <c-textarea id="bio" rows="3"></c-textarea>
    <c-field.description>A short paragraph about yourself.</c-field.description>
  </c-field>
</c-field.group>
</c-docs.example>

:::en
### Horizontal
:::pt-br
### Horizontal
:::

<c-docs.example>
<c-field orientation="horizontal" class="w-full max-w-md text-start">
  <c-checkbox id="terms" />
  <c-field.content>
    <c-field.label for="terms">Accept the terms</c-field.label>
    <c-field.description>You agree to our terms of service.</c-field.description>
  </c-field.content>
</c-field>
</c-docs.example>

:::en
### Fieldset and legend
:::pt-br
### Fieldset e legenda
:::

<c-docs.example>
<c-field.set class="w-full max-w-md text-start">
  <c-field.legend>Notifications</c-field.legend>
  <c-field.description>Choose how you want to be reached.</c-field.description>
  <c-field.group>
    <c-field orientation="horizontal">
      <c-checkbox id="by-email" />
      <c-field.label for="by-email">Email</c-field.label>
    </c-field>
    <c-field orientation="horizontal">
      <c-checkbox id="by-push" />
      <c-field.label for="by-push">Push notifications</c-field.label>
    </c-field>
  </c-field.group>
</c-field.set>
</c-docs.example>

:::en
### Separator
:::pt-br
### Separador
:::

<c-docs.example>
<c-field.group class="w-full max-w-md text-start">
  <c-field>
    <c-field.label for="username">Username</c-field.label>
    <c-input id="username" />
  </c-field>
  <c-field.separator>or</c-field.separator>
  <c-field>
    <c-field.label for="sso">Single sign-on</c-field.label>
    <c-input id="sso" placeholder="company.com" />
  </c-field>
</c-field.group>
</c-docs.example>

:::en
### Errors
:::pt-br
### Erros
:::

<c-docs.example>
<div class="flex w-full max-w-md flex-col gap-6 text-start">
  <c-field data-invalid="true">
    <c-field.label for="password">Password</c-field.label>
    <c-input id="password" type="password" aria-invalid="true" />
    <c-field.error>Password is too short.</c-field.error>
  </c-field>
  <c-field data-invalid="true">
    <c-field.label for="handle">Handle</c-field.label>
    <c-input id="handle" aria-invalid="true" />
    <c-field.error :errors="handle_errors" />
  </c-field>
</div>
</c-docs.example>

:::en
### Title inside a label
:::pt-br
### Título dentro de um rótulo
:::

<c-docs.example>
<c-field.label class="w-full max-w-md text-start">
  <c-field orientation="horizontal">
    <c-checkbox id="pro" />
    <c-field.content>
      <c-field.title>Pro plan</c-field.title>
      <c-field.description>Everything in Free, plus priority support.</c-field.description>
    </c-field.content>
  </c-field>
</c-field.label>
</c-docs.example>

:::en
## Notes

Upstream, `FieldError` takes either children or an array of errors and
renders a list when there is more than one. Here `errors` takes a Django
form field's error list directly, with the same rule: one error inline,
several as a bulleted list. Nothing renders when both are empty.
:::pt-br
## Observações

No upstream, o `FieldError` aceita ou filhos ou um array de erros, e renderiza
uma lista quando há mais de um. Aqui `errors` aceita diretamente a lista de
erros de um campo de formulário Django, com a mesma regra: um erro em linha,
vários como uma lista com marcadores. Nada é renderizado quando os dois estão
vazios.
:::
