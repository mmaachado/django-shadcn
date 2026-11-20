---
title: Input Group
description: Wraps an input with icons, text or buttons inside a single outline.
description.pt-br: Envolve um campo com ícones, texto ou botões sob um contorno só.
description.es: Envuelve un campo con iconos, texto o botones bajo un solo contorno.
---

<c-docs.demo-section class="min-h-[350px]">
<c-input-group class="w-[320px]">
<c-input-group.addon>
<c-icon name="search" />
</c-input-group.addon>
<c-input-group.input placeholder="Search components..." />
</c-input-group>
</c-docs.demo-section>

<c-docs.cheat-sheet name="input-group">
<c-input-group>
  <c-input-group.addon>
    <c-icon name="search" />
  </c-input-group.addon>
  <c-input-group.input placeholder="Search..." />
</c-input-group>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add input_group
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-input-group>
  <c-input-group.addon>
    <c-icon name="search" />
  </c-input-group.addon>
  <c-input-group.input placeholder="Search..." />
</c-input-group>
```

:::en
The outline and the focus ring live on the group, not on the input. Use
`c-input-group.input` rather than a plain `c-input` so the group can pick up
focus and validation state.

## Examples

### Leading and trailing
:::pt-br
O contorno e o anel de foco ficam no grupo, não no input. Use
`c-input-group.input` em vez de um `c-input` simples para que o grupo possa
captar o foco e o estado de validação.

## Exemplos

### No início e no fim
:::

<c-docs.example>
<div class="flex w-full flex-col gap-4">
  <c-input-group>
    <c-input-group.addon>
      <c-input-group.text>$</c-input-group.text>
    </c-input-group.addon>
    <c-input-group.input placeholder="0.00" />
    <c-input-group.addon align="inline-end">
      <c-input-group.text>USD</c-input-group.text>
    </c-input-group.addon>
  </c-input-group>
  <c-input-group>
    <c-input-group.input placeholder="Search..." />
    <c-input-group.addon align="inline-end">
      <c-kbd.group>
        <c-kbd>⌘</c-kbd>
        <c-kbd>K</c-kbd>
      </c-kbd.group>
    </c-input-group.addon>
  </c-input-group>
</div>
</c-docs.example>

:::en
### With a button
:::pt-br
### Com um botão
:::

<c-docs.example>
<c-input-group>
  <c-input-group.input placeholder="Paste a link" />
  <c-input-group.addon align="inline-end">
    <c-input-group.button size="sm" variant="outline">Copy</c-input-group.button>
  </c-input-group.addon>
</c-input-group>
</c-docs.example>

:::en
### Textarea with a block addon
:::pt-br
### Textarea com um addon em bloco
:::

<c-docs.example>
<c-input-group>
  <c-input-group.textarea placeholder="Write a message..." rows="3" />
  <c-input-group.addon align="block-end" class="border-t">
    <c-input-group.text>Markdown supported</c-input-group.text>
    <c-input-group.button size="sm" class="ms-auto">Send</c-input-group.button>
  </c-input-group.addon>
</c-input-group>
</c-docs.example>

:::en
### Invalid
:::pt-br
### Inválido
:::

<c-docs.example>
<c-input-group>
  <c-input-group.input placeholder="you@example.com" aria-invalid="true" />
  <c-input-group.addon align="inline-end">
    <c-icon name="x" class="text-destructive" />
  </c-input-group.addon>
</c-input-group>
</c-docs.example>

:::en
### Text

`text` puts a fixed piece, a unit or a domain, beside the field.
:::pt-br
### Texto

O `text` põe um pedaço fixo, uma unidade ou um domínio, ao lado do campo.
:::

<c-docs.example>
<c-input-group class="max-w-xs">
  <c-input-group.input placeholder="example" aria-label="Subdomain" />
  <c-input-group.addon align="inline-end"><c-input-group.text>.example.com</c-input-group.text></c-input-group.addon>
</c-input-group>
</c-docs.example>

:::en
### Kbd
:::pt-br
### Kbd
:::

<c-docs.example>
<c-input-group class="max-w-xs">
  <c-input-group.addon><c-icon name="search" /></c-input-group.addon>
  <c-input-group.input placeholder="Search..." aria-label="Search" />
  <c-input-group.addon align="inline-end"><c-kbd>⌘K</c-kbd></c-input-group.addon>
</c-input-group>
</c-docs.example>

:::en
### Spinner

A spinner in an addon shows the field is waiting, such as on a lookup.
:::pt-br
### Spinner

Um spinner num addon mostra que o campo está esperando, como numa consulta.
:::

<c-docs.example>
<c-input-group class="max-w-xs">
  <c-input-group.input value="mmaachado" aria-label="Username" />
  <c-input-group.addon align="inline-end"><c-spinner /></c-input-group.addon>
</c-input-group>
</c-docs.example>

:::en
## RTL

`inline-start` and `inline-end` are logical, so under `dir="rtl"` a leading
icon moves to the right of the field and a trailing button to the left.

## Accessibility

The group is a `role="group"` and the field inside is a native input, so it
keeps its label and its validation. An addon with only an icon is decorative;
a button in it with only an icon needs an `aria-label`. Clicking an addon
focuses the field.

## API reference
:::pt-br
## RTL

`inline-start` e `inline-end` são lógicos, então sob `dir="rtl"` um ícone do
início vai para a direita do campo e um botão do fim para a esquerda.

## Acessibilidade

O grupo é um `role="group"` e o campo dentro é um input nativo, então mantém
o rótulo e a validação. Um addon só com ícone é decorativo; um botão nele só
com ícone precisa de um `aria-label`. Clicar num addon dá foco ao campo.

## Referência da API
:::

<c-docs.api-reference name="input-group" />

:::en
## Notes

`c-input-group.input`, `.textarea` and `.button` render their own element
rather than wrapping `c-input`, `c-textarea` and `c-button`. cotton silently
drops the `attrs` spread when it lands on another component, and these
controls have to forward whatever you put on them.

Their sizes come from the group, not from `c-button`: `xs`, `sm`, `icon-xs`
and `icon-sm`.

Clicking an addon focuses the input, which needs Alpine. The addon carries
its own `x-data`, so it works without an Alpine scope around it.
:::pt-br
## Observações

`c-input-group.input`, `.textarea` e `.button` renderizam o próprio elemento em
vez de envolver `c-input`, `c-textarea` e `c-button`. O cotton descarta sem
aviso o repasse de `attrs` quando ele cai em outro componente, e esses
controles precisam repassar tudo o que você coloca neles.

Os tamanhos deles vêm do grupo, não do `c-button`: `xs`, `sm`, `icon-xs` e
`icon-sm`.

Clicar num addon dá foco ao input, o que precisa do Alpine. O addon leva o
próprio `x-data`, então funciona sem um escopo do Alpine em volta.
:::
