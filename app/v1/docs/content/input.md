---
title: Input
description: Displays a form input field or a component that looks like an input field.
description.pt-br: Exibe um campo de formulário, ou um componente com cara de campo.
description.es: Muestra un campo de formulario, o un componente con aspecto de campo.
---

<c-docs.demo-section class="min-h-[350px]">
<c-input type="email" placeholder="Email" class="max-w-sm" />
</c-docs.demo-section>

<c-docs.cheat-sheet name="input">
<c-input name="email" type="email" value="{{ form.email.value|default:'' }}" />
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add input
```

:::en
## Usage

`<c-input>` is a native `<input>`, and every attribute lands on it: `type`,
`name`, `value`, `required`, `pattern`, `autocomplete`. It posts with the form
and needs no JavaScript. Pass the bound value back so a failed post keeps what
was typed:
:::pt-br
## Uso

O `<c-input>` é um `<input>` nativo, e todo atributo cai nele: `type`, `name`,
`value`, `required`, `pattern`, `autocomplete`. Ele é enviado com o formulário
e não precisa de JavaScript. Devolva o valor preenchido para que um envio com
falha mantenha o que foi digitado:
:::

```html
<c-input id="{{ form.email.id_for_label }}" name="{{ form.email.html_name }}"
  type="email" value="{{ form.email.value|default:'' }}" required />
```

:::en
## Examples

### Basic
:::pt-br
## Exemplos

### Básico
:::

<c-docs.example>
<c-input placeholder="Your name" aria-label="Name" class="max-w-sm" />
</c-docs.example>

:::en
### With a label
:::pt-br
### Com rótulo
:::

<c-docs.example>
<div class="grid max-w-sm gap-2">
  <c-label for="input-email">Email</c-label>
  <c-input id="input-email" type="email" placeholder="you@example.com" />
</div>
</c-docs.example>

:::en
### Disabled
:::pt-br
### Desabilitado
:::

<c-docs.example>
<c-input disabled value="Read only for now" aria-label="Plan" class="max-w-sm" />
</c-docs.example>

:::en
### Invalid

There is no invalid style built in: mark the field `aria-invalid="true"` and
give it a class of your own.
:::pt-br
### Inválido

Não há estilo de inválido embutido: marque o campo com `aria-invalid="true"` e
dê a ele uma classe sua.
:::

<c-docs.example>
<c-input value="not-an-email" aria-invalid="true" aria-label="Email" class="max-w-sm aria-invalid:border-destructive" />
</c-docs.example>

:::en
### File
:::pt-br
### Arquivo
:::

<c-docs.example>
<div class="grid max-w-sm gap-2">
  <c-label for="input-file">Picture</c-label>
  <c-input id="input-file" type="file" />
</div>
</c-docs.example>

:::en
### Required
:::pt-br
### Obrigatório
:::

<c-docs.example>
<div class="grid max-w-sm gap-2">
  <c-label for="input-required">Username <span class="text-destructive">*</span></c-label>
  <c-input id="input-required" required />
</div>
</c-docs.example>

:::en
### Inline

An input and a button side by side, for a single-field form.
:::pt-br
### Em linha

Um input e um botão lado a lado, para um formulário de um campo só.
:::

<c-docs.example>
<form class="flex max-w-sm gap-2" onsubmit="return false">
  <c-input type="email" placeholder="Email" aria-label="Email" />
  <c-button>Subscribe</c-button>
</form>
</c-docs.example>

:::en
### Grid
:::pt-br
### Grid
:::

<c-docs.example>
<div class="grid max-w-md grid-cols-2 gap-4">
  <div class="grid gap-2">
    <c-label for="input-first">First name</c-label>
    <c-input id="input-first" />
  </div>
  <div class="grid gap-2">
    <c-label for="input-last">Last name</c-label>
    <c-input id="input-last" />
  </div>
</div>
</c-docs.example>

:::en
## RTL

The text starts at the start of the field, so under `dir="rtl"` it runs from
the right, and the browser places the caret to match.

## Accessibility

It is a native input, so it takes its name from a `<label>` tied to it with
`for`, or from an `aria-label` when there is no visible label. A placeholder is
not a label: it disappears as soon as someone types.

## API reference
:::pt-br
## RTL

O texto começa no início do campo, então sob `dir="rtl"` ele corre a partir da
direita, e o navegador posiciona o cursor de acordo.

## Acessibilidade

É um input nativo, então recebe o nome de um `<label>` ligado a ele com `for`,
ou de um `aria-label` quando não há rótulo visível. Um placeholder não é um
rótulo: ele some assim que alguém digita.

## Referência da API
:::

<c-docs.api-reference name="input" />

:::en
## Notes

Upstream's field, field group, badge, input group, button group and form
examples are the input inside other components; see
[Field]({% url 'page' slug='field' %}),
[Input Group]({% url 'page' slug='input-group' %}) and
[Button Group]({% url 'page' slug='button-group' %}).
:::pt-br
## Observações

Os exemplos de field, field group, badge, input group, button group e form do
upstream são o input dentro de outros componentes; veja o
[Field]({% url 'page' slug='field' %}), o
[Input Group]({% url 'page' slug='input-group' %}) e o
[Button Group]({% url 'page' slug='button-group' %}).
:::
