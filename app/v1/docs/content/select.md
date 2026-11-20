---
title: Select
description: Displays a list of options for the user to pick from—triggered by a button.
description.pt-br: Uma lista de opções para o usuário escolher, aberta por um botão.
description.es: Una lista de opciones para que el usuario elija, abierta por un botón.
---

<c-docs.demo-section class="min-h-[350px]">
<c-select class="w-[180px]">
<c-select.trigger>
<c-select.value placeholder="Select a fruit" />
</c-select.trigger>
<c-select.content>
<c-select.item value="apple">Apple</c-select.item>
<c-select.item value="banana">Banana</c-select.item>
<c-select.item value="blueberry">Blueberry</c-select.item>
</c-select.content>
</c-select>
</c-docs.demo-section>

<c-docs.cheat-sheet name="select">
<c-select name="fruit">
  <c-select.trigger>
    <c-select.value placeholder="Select a fruit" />
  </c-select.trigger>
  <c-select.content>
    <c-select.item value="apple">Apple</c-select.item>
  </c-select.content>
</c-select>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add select
```

:::en
## Usage

A button that opens a styled list. With `name` set, a hidden input posts the
chosen `value`. It starts empty, with no way to pre-select an option, and its
list and choice are Alpine, so without JavaScript nothing can be chosen.

For a form field, [Native Select]({% url 'page' slug='native-select' %}) is
usually the better choice: it posts without JavaScript, keeps a bound value,
works with the keyboard and opens the platform picker on a phone. Reach for
this one when the options need markup of their own.
:::pt-br
## Uso

Um botão que abre uma lista estilizada. Com `name` definido, um input oculto
envia o `value` escolhido. Ele começa vazio, sem como pré-selecionar uma opção,
e a lista e a escolha são do Alpine, então sem JavaScript nada pode ser
escolhido.

Para um campo de formulário, o
[Native Select]({% url 'page' slug='native-select' %}) costuma ser a melhor
escolha: ele envia sem JavaScript, mantém um valor preenchido, funciona com o
teclado e abre o seletor da plataforma num celular. Recorra a este quando as
opções precisarem de markup próprio.
:::

:::en
## Examples

### Scrollable

A long list scrolls inside the content once you give it a height.
:::pt-br
## Exemplos

### Com rolagem

Uma lista longa rola dentro do conteúdo quando você dá uma altura a ele.
:::

<c-docs.example>
<c-select class="w-[200px]">
  <c-select.trigger>
    <c-select.value placeholder="Select a timezone" />
  </c-select.trigger>
  <c-select.content class="max-h-48 overflow-y-auto">
    <c-select.item value="sao-paulo">America/Sao_Paulo</c-select.item>
    <c-select.item value="new-york">America/New_York</c-select.item>
    <c-select.item value="lisbon">Europe/Lisbon</c-select.item>
    <c-select.item value="london">Europe/London</c-select.item>
    <c-select.item value="berlin">Europe/Berlin</c-select.item>
    <c-select.item value="dubai">Asia/Dubai</c-select.item>
    <c-select.item value="tokyo">Asia/Tokyo</c-select.item>
    <c-select.item value="sydney">Australia/Sydney</c-select.item>
  </c-select.content>
</c-select>
</c-docs.example>

:::en
### Disabled
:::pt-br
### Desabilitado
:::

<c-docs.example>
<c-select class="w-[180px]">
  <c-select.trigger disabled>
    <c-select.value placeholder="Not available" />
  </c-select.trigger>
</c-select>
</c-docs.example>

:::en
## RTL

The value sits at the start of the trigger and the chevron at its end, and each
option's check mark at the start, so under `dir="rtl"` they change sides with
the text.

## Accessibility

The trigger is a `<button role="combobox">` that reports `aria-expanded` and
controls a `role="listbox"` of `option`s; the chosen one reports
`aria-selected="true"`. Focus stays on the trigger while the list is open, and
`aria-activedescendant` points at the option the keyboard is on, so a screen
reader reads it as it moves.

Down, Up, Enter or Space open the list. Down and Up then move through the
options, Home and End go to the ends, typing jumps to an option that starts
with what was typed, and Enter or Space picks one and returns to the trigger.
Escape and Tab close it. Options with `data-disabled` are skipped.

It needs JavaScript to post anything. For a form that must work without it,
use [Native Select]({% url 'page' slug='native-select' %}).

## API reference
:::pt-br
## RTL

O valor fica no início do trigger e o chevron no fim, e a marca de cada opção
no início, então sob `dir="rtl"` eles trocam de lado com o texto.

## Acessibilidade

O trigger é um `<button role="combobox">` que informa `aria-expanded` e
controla um `role="listbox"` de `option`s; a escolhida informa
`aria-selected="true"`. O foco fica no trigger enquanto a lista está aberta, e
o `aria-activedescendant` aponta para a opção em que o teclado está, então um
leitor de tela a lê enquanto ela muda.

As setas para baixo e para cima, o Enter ou o Espaço abrem a lista. Depois, as
setas passam pelas opções, Home e End vão para as pontas, digitar pula para
uma opção que começa com o que foi digitado, e o Enter ou o Espaço escolhem
uma e voltam para o trigger. O Escape e o Tab a fecham. Opções com
`data-disabled` são puladas.

Ele precisa de JavaScript para enviar alguma coisa. Para um formulário que
precisa funcionar sem ele, use o
[Native Select]({% url 'page' slug='native-select' %}).

## Referência da API
:::

<c-docs.api-reference name="select" />

:::en
## Notes

Upstream's groups, invalid state and aligning the selected item with the
trigger are not here, and neither is keyboard choice: the gaps above are why
Native Select is the form field to start from.
:::pt-br
## Observações

Os grupos, o estado inválido e o alinhamento do item escolhido com o trigger do
upstream não estão aqui, e a escolha pelo teclado também não: as lacunas acima
são o motivo de o Native Select ser o campo de formulário por onde começar.
:::
