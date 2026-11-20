---
title: Label
description: Renders an accessible label associated with controls.
description.pt-br: Um rótulo acessível associado a um controle.
description.es: Una etiqueta accesible asociada a un control.
---

<c-docs.demo-section class="min-h-[350px]">

<div class="grid w-full max-w-sm gap-2 text-start">
            <c-label for="email">Email</c-label>
            <c-input id="email" type="email" placeholder="you@example.com" />
        </div>
</c-docs.demo-section>

<c-docs.cheat-sheet name="label">
<c-label for="email">Email</c-label> <c-input id="email" type="email" />
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add label
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-label for="email">Email</c-label> <c-input id="email" type="email" />
```

:::en
The `for` attribute has to match the control's `id`. That is what lets a
click on the text focus the field, and what a screen reader announces.

## Examples

### With an input
:::pt-br
O atributo `for` precisa bater com o `id` do controle. É isso que faz um clique
no texto dar foco ao campo, e é o que um leitor de tela anuncia.

## Exemplos

### Com um input
:::

<c-docs.example>
<div class="grid w-full max-w-sm gap-2">
  <c-label for="project">Project name</c-label>
  <c-input id="project" placeholder="django-shadcn" />
</div>
</c-docs.example>

:::en
### With a checkbox
:::pt-br
### Com um checkbox
:::

<c-docs.example>
<div class="flex items-center space-x-2">
  <c-checkbox id="newsletter" />
  <c-label for="newsletter">Subscribe to the newsletter</c-label>
</div>
</c-docs.example>

:::en
### Required
:::pt-br
### Obrigatório
:::

<c-docs.example>
<div class="grid w-full max-w-sm gap-2">
  <c-label for="handle">
    Handle
    <span class="text-destructive" aria-hidden="true">*</span>
  </c-label>
  <c-input id="handle" required />
</div>
</c-docs.example>

:::en
### Disabled control
:::pt-br
### Controle desabilitado
:::

<c-docs.example>
<div class="grid w-full max-w-sm gap-2">
  <c-input id="locked" class="peer" placeholder="Not editable" disabled />
  <c-label for="locked">Locked field</c-label>
</div>
</c-docs.example>

:::en
### Label in a field

[Field]({% url 'page' slug='field' %}) has a label part of its own, laid out with the
control, a description and an error.
:::pt-br
### Rótulo num field

O [Field]({% url 'page' slug='field' %}) tem uma parte de rótulo própria,
diagramada com o controle, uma descrição e um erro.
:::

<c-docs.example>
<c-field class="max-w-sm">
  <c-field.label for="label-field-email">Email</c-field.label>
  <c-input id="label-field-email" type="email" />
  <c-field.description>We never share it.</c-field.description>
</c-field>
</c-docs.example>

:::en
## RTL

A label follows the text, so under `dir="rtl"` it sits to the right of the
field it names when they share a row.

## Accessibility

It is a native `<label>`. With `for` set to the control's id it names the
control, and a click on it focuses or toggles the control.

## API reference
:::pt-br
## RTL

Um rótulo acompanha o texto, então sob `dir="rtl"` ele fica à direita do
campo que nomeia quando os dois dividem uma linha.

## Acessibilidade

É um `<label>` nativo. Com `for` igual ao id do controle ele dá nome ao
controle, e um clique nele dá foco ao controle ou o alterna.

## Referência da API
:::

<c-docs.api-reference name="label" />

:::en
## Notes

The dimmed style for a disabled control comes from `peer-disabled:`, so the
control needs the `peer` class and has to come before the label in the
markup.
:::pt-br
## Observações

O estilo esmaecido de um controle desabilitado vem de `peer-disabled:`, então o
controle precisa da classe `peer` e tem de vir antes do rótulo no markup.
:::
