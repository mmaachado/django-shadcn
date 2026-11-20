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
## Notes

The dimmed style for a disabled control comes from `peer-disabled:`, so the
control needs the `peer` class and has to come before the label in the
markup.
:::pt-br
## Observações

O estilo esmaecido de um controle desabilitado vem de `peer-disabled:`, então o
controle precisa da classe `peer` e tem de vir antes do rótulo no markup.
:::

:::en
## API reference
:::pt-br
## Referência da API
:::

<c-docs.api-reference name="label" />
