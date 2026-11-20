---
title: Switch
description: A control that toggles between on and off.
description.pt-br: Um controle que alterna entre ligado e desligado.
description.es: Un control que alterna entre encendido y apagado.
---

<c-docs.demo-section class="min-h-[350px]">
<label class="flex items-center gap-3">
<c-switch name="airplane" />
<span class="text-sm font-medium">Airplane mode</span>
</label>
</c-docs.demo-section>

<c-docs.cheat-sheet name="switch">
<c-switch name="notifications" checked />
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add switch
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-switch name="notifications" checked />
</c-docs.example>

:::en
The switch is a real `<input type="checkbox">` wrapped in the label that draws
it. It submits with the form, reaches the field through `name`, and answers to
the keyboard without any JavaScript.

## Examples

### Sizes
:::pt-br
O switch é um `<input type="checkbox">` de verdade, envolvido pelo rótulo que o
desenha. Ele é enviado com o formulário, chega ao campo pelo `name` e responde
ao teclado sem nenhum JavaScript.

## Exemplos

### Tamanhos
:::

<c-docs.example>
<div class="flex items-center gap-6">
  <c-switch size="sm" checked />
  <c-switch checked />
</div>
</c-docs.example>

:::en
### With a label
:::pt-br
### Com um rótulo
:::

<c-docs.example>
<label class="flex items-center gap-3">
  <c-switch name="marketing" />
  <span class="text-sm font-medium">Send me product updates</span>
</label>
</c-docs.example>

:::en
### Disabled
:::pt-br
### Desabilitado
:::

<c-docs.example>
<div class="flex items-center gap-6">
  <c-switch disabled />
  <c-switch checked disabled />
</div>
</c-docs.example>

:::en
### Description
:::pt-br
### Descrição
:::

<c-docs.example>
<div class="flex max-w-sm items-start justify-between gap-6">
  <div class="grid gap-1">
    <c-label for="switch-airplane">Airplane mode</c-label>
    <p class="text-sm text-muted-foreground">Turns off every connection.</p>
  </div>
  <c-switch id="switch-airplane" name="airplane" />
</div>
</c-docs.example>

:::en
## RTL

The thumb moves from the start to the end when switched on, and a label after
the switch follows the text.

## Accessibility

It is a native checkbox inside its label: Space toggles it and a screen reader
announces it as checked or not. Give it a visible label, or an `aria-label`
on the switch.

## API reference
:::pt-br
## RTL

O puxador vai do início para o fim quando ligado, e um rótulo depois do
switch acompanha o texto.

## Acessibilidade

É um checkbox nativo dentro do próprio rótulo: o Espaço o alterna e um leitor
de tela o anuncia como marcado ou não. Dê a ele um rótulo visível, ou um
`aria-label` no switch.

## Referência da API
:::

<c-docs.api-reference name="switch" />

:::en
## Notes

Radix renders a button and mirrors the state into `data-state`. Here the
checked state lives in the input itself, and the styling reads it with
`has-[:checked]` on the wrapper and `group-has-[:checked]` on the thumb. The
practical difference is that this one is a form control: no hidden field, no
JavaScript, and `checked` works the way it does anywhere else.
:::pt-br
## Observações

O Radix renderiza um botão e espelha o estado em `data-state`. Aqui o estado de
marcado mora no próprio input, e o estilo o lê com `has-[:checked]` no elemento
em volta e `group-has-[:checked]` no puxador. A diferença na prática é que este
é um controle de formulário: nenhum campo oculto, nenhum JavaScript, e `checked`
funciona como em qualquer outro lugar.
:::
