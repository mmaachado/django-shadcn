---
title: Radio Group
description: A set of options where only one can be picked.
description.pt-br: Um conjunto de opções em que só uma pode ser escolhida.
description.es: Un conjunto de opciones donde solo se puede elegir una.
---

<c-docs.demo-section class="min-h-[350px]">
<c-radio-group class="text-start">
<label class="flex items-center gap-3">
<c-radio-group.item name="plan" value="free" checked />
<span class="text-sm font-medium">Free</span>
</label>
<label class="flex items-center gap-3">
<c-radio-group.item name="plan" value="pro" />
<span class="text-sm font-medium">Pro</span>
</label>
<label class="flex items-center gap-3">
<c-radio-group.item name="plan" value="team" />
<span class="text-sm font-medium">Team</span>
</label>
</c-radio-group>
</c-docs.demo-section>

<c-docs.cheat-sheet name="radio-group">
<c-radio-group class="text-start">
  <label class="flex items-center gap-3">
    <c-radio-group.item name="delivery" value="standard" checked />
    <span class="text-sm font-medium">Standard</span>
  </label>
  <label class="flex items-center gap-3">
    <c-radio-group.item name="delivery" value="express" />
    <span class="text-sm font-medium">Express</span>
  </label>
</c-radio-group>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add radio_group
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-radio-group class="text-start">
  <label class="flex items-center gap-3">
    <c-radio-group.item name="delivery" value="standard" checked />
    <span class="text-sm font-medium">Standard</span>
  </label>
  <label class="flex items-center gap-3">
    <c-radio-group.item name="delivery" value="express" />
    <span class="text-sm font-medium">Express</span>
  </label>
</c-radio-group>
</c-docs.example>

:::en
Items are native radios, so `name` groups them and the browser handles the
exclusivity, the keyboard and the form submission.

## Examples

### From a Django form
:::pt-br
Os itens são radios nativos, então o `name` os agrupa e o navegador cuida da
exclusividade, do teclado e do envio do formulário.

## Exemplos

### A partir de um formulário Django
:::

```html
<c-radio-group>
    {% for radio in form.delivery %}
        <label class="flex items-center gap-3">
            <c-radio-group.item name="{{ radio.name }}" value="{{ radio.data.value }}" />
            <span class="text-sm font-medium">{{ radio.choice_label }}</span>
        </label>
    {% endfor %}
</c-radio-group>
```

:::en
### Disabled
:::pt-br
### Desabilitado
:::

<c-docs.example>
<c-radio-group class="text-start">
  <label class="flex items-center gap-3">
    <c-radio-group.item name="tier" value="one" checked disabled />
    <span class="text-sm font-medium text-muted-foreground">Locked in</span>
  </label>
  <label class="flex items-center gap-3">
    <c-radio-group.item name="tier" value="two" disabled />
    <span class="text-sm font-medium text-muted-foreground">Not available</span>
  </label>
</c-radio-group>
</c-docs.example>

:::en
### Description
:::pt-br
### Descrição
:::

<c-docs.example>
<c-radio-group class="max-w-sm text-start">
  <label class="flex items-start gap-3">
    <c-radio-group.item name="density" value="comfortable" checked class="mt-0.5" />
    <span class="grid gap-1">
      <span class="text-sm font-medium">Comfortable</span>
      <span class="text-sm text-muted-foreground">More space between rows.</span>
    </span>
  </label>
  <label class="flex items-start gap-3">
    <c-radio-group.item name="density" value="compact" class="mt-0.5" />
    <span class="grid gap-1">
      <span class="text-sm font-medium">Compact</span>
      <span class="text-sm text-muted-foreground">More rows on the screen.</span>
    </span>
  </label>
</c-radio-group>
</c-docs.example>

:::en
### Fieldset

A `<fieldset>` and a `<legend>` name the question the radios answer.
:::pt-br
### Fieldset

Um `<fieldset>` e uma `<legend>` dão nome à pergunta que os radios respondem.
:::

<c-docs.example>
<fieldset class="grid gap-3 text-start">
  <legend class="mb-2 text-sm font-medium">Notify me about</legend>
  <c-radio-group>
    <label class="flex items-center gap-3">
      <c-radio-group.item name="notify" value="all" checked />
      <span class="text-sm">All new messages</span>
    </label>
    <label class="flex items-center gap-3">
      <c-radio-group.item name="notify" value="mentions" />
      <span class="text-sm">Direct messages and mentions</span>
    </label>
  </c-radio-group>
</fieldset>
</c-docs.example>

:::en
## RTL

A radio sits where the markup puts it and its label follows the text, so under
`dir="rtl"` the label moves to the left of the radio.

## Accessibility

The group is a `role="radiogroup"` of native radios: the arrow keys move
between them, and only the chosen one is a tab stop. Name the group with
`aria-label`, or wrap it in a `<fieldset>` with a `<legend>`.

## API reference
:::pt-br
## RTL

Um radio fica onde o markup o põe e o rótulo acompanha o texto, então sob
`dir="rtl"` o rótulo vai para a esquerda do radio.

## Acessibilidade

O grupo é um `role="radiogroup"` de radios nativos: as setas passam de um
para o outro, e só o escolhido é parada de tab. Dê um nome ao grupo com
`aria-label`, ou envolva-o num `<fieldset>` com uma `<legend>`.

## Referência da API
:::

<c-docs.api-reference name="radio-group" />

:::en
## Notes

Radix draws the dot with a nested indicator element. A native radio cannot hold
children, so the dot here is the background painted onto the content box only —
`bg-clip-content` with a small padding shrinks it to a circle in the middle.
The visible result is the same and the control stays a real form field.
:::pt-br
## Observações

O Radix desenha o ponto com um elemento indicador aninhado. Um radio nativo não
pode ter filhos, então aqui o ponto é o fundo pintado só na caixa de conteúdo —
`bg-clip-content` com um padding pequeno o reduz a um círculo no meio. O
resultado visível é o mesmo e o controle continua sendo um campo de formulário
de verdade.
:::
