---
title: Slider
description: Pick a value from a range.
description.pt-br: Escolhe um valor dentro de um intervalo.
description.es: Elige un valor dentro de un intervalo.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="w-[320px]"><c-slider name="volume" value="60" /></div>
</c-docs.demo-section>

<c-docs.cheat-sheet name="slider">
<div class="w-[320px]"><c-slider name="volume" value="50" /></div>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add slider
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<div class="w-[320px]"><c-slider name="volume" value="50" /></div>
</c-docs.example>

:::en
The slider fills the width it is given, so set the width on a wrapper
rather than passing a `w-*` class to the component: two width utilities on
the same element are settled by the compiled stylesheet, not by you.

A real `<input type="range">` sits transparent on top and carries the value,
the keyboard and the form submission. The track, the filled range and the thumb
below it are what you see, which keeps the styling in utility classes instead
of vendor pseudo-elements.

## Examples

### Range and step
:::pt-br
O slider preenche a largura que recebe, então defina a largura num elemento em
volta em vez de passar uma classe `w-*` ao componente: dois utilitários de
largura no mesmo elemento são decididos pela folha de estilo compilada, não por
você.

Um `<input type="range">` de verdade fica transparente por cima e carrega o
valor, o teclado e o envio do formulário. A trilha, o trecho preenchido e o
puxador embaixo dele são o que você vê, o que mantém o estilo em classes
utilitárias em vez de pseudo-elementos de cada navegador.

## Exemplos

### Intervalo e passo
:::

<c-docs.example>
<div class="flex w-[320px] flex-col gap-6">
  <c-slider name="temperature" min="16" max="30" step="1" value="22" />
  <c-slider name="ratio" min="0" max="1" step="0.05" value="0.4" />
</div>
</c-docs.example>

:::en
### Disabled
:::pt-br
### Desabilitado
:::

<c-docs.example>
<div class="w-[320px]"><c-slider value="35" disabled /></div>
</c-docs.example>

:::en
## RTL

The range input fills from the start, so under `dir="rtl"` the track fills
from the right and the arrow keys follow the browser's direction.

## Accessibility

A real `<input type="range">` carries the value, so the arrow keys, Home and
End move it and a screen reader announces it. Name it with a `<label>` or an
`aria-label`.

## API reference
:::pt-br
## RTL

O input de intervalo se preenche a partir do início, então sob `dir="rtl"` a
trilha se preenche a partir da direita e as setas seguem a direção do
navegador.

## Acessibilidade

Um `<input type="range">` de verdade carrega o valor, então as setas, o Home e
o End o movem e um leitor de tela o anuncia. Dê um nome a ele com um `<label>`
ou um `aria-label`.

## Referência da API
:::

<c-docs.api-reference name="slider" />

:::en
## Notes

Radix supports several thumbs on one track for a range selection. That needs
shared state between thumbs and is not here; one value per slider.
:::pt-br
## Observações

O Radix aceita vários puxadores numa mesma trilha para selecionar um intervalo.
Isso precisa de estado compartilhado entre os puxadores e não está aqui; um
valor por slider.
:::
