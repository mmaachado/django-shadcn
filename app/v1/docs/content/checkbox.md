---
title: Checkbox
description: A control that allows the user to toggle between checked and not checked.
description.pt-br: Um controle que o usuário alterna entre marcado e desmarcado.
description.es: Un control que el usuario alterna entre marcado y sin marcar.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="flex items-center gap-2">
<c-checkbox id="demo-terms" checked />
<c-label for="demo-terms">Accept terms and conditions</c-label>
</div>
</c-docs.demo-section>

<c-docs.cheat-sheet name="checkbox">
<c-checkbox id="newsletter" name="newsletter" {% if form.newsletter.value %}checked{% endif %} />
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add checkbox
```

:::en
## Usage

`<c-checkbox>` is a native `<input type="checkbox">`, coloured with
`accent-primary`, and every attribute lands on it. It needs no JavaScript.

A checked box posts its `name` with its `value`, `on` by default, and an
unchecked one posts nothing, which is what a `BooleanField` expects. Set
`checked` from the bound value so the box keeps its state after a failed post:
:::pt-br
## Uso

O `<c-checkbox>` é um `<input type="checkbox">` nativo, colorido com
`accent-primary`, e todo atributo cai nele. Ele não precisa de JavaScript.

Uma caixa marcada envia o `name` com o `value`, `on` por padrão, e uma
desmarcada não envia nada, que é o que um `BooleanField` espera. Defina
`checked` a partir do valor preenchido para a caixa manter o estado depois de
um envio com falha:
:::

```html
<div class="flex items-center gap-2">
  <c-checkbox id="{{ form.newsletter.id_for_label }}" name="{{ form.newsletter.html_name }}"
    {% if form.newsletter.value %}checked{% endif %} />
  <c-label for="{{ form.newsletter.id_for_label }}">{{ form.newsletter.label }}</c-label>
</div>
```

:::en
## Examples

### Basic
:::pt-br
## Exemplos

### Básico
:::

<c-docs.example>
<div class="flex items-center gap-2">
  <c-checkbox id="basic-terms" />
  <c-label for="basic-terms">Accept terms and conditions</c-label>
</div>
</c-docs.example>

:::en
### Checked
:::pt-br
### Marcado
:::

<c-docs.example>
<div class="flex items-center gap-2">
  <c-checkbox id="checked-updates" checked />
  <c-label for="checked-updates">Send me product updates</c-label>
</div>
</c-docs.example>

:::en
### Description
:::pt-br
### Descrição
:::

<c-docs.example>
<div class="flex items-start gap-2">
  <c-checkbox id="description-terms" class="mt-0.5" />
  <div class="grid gap-1.5">
    <c-label for="description-terms">Accept terms and conditions</c-label>
    <p class="text-sm text-muted-foreground">You agree to our Terms of Service and Privacy Policy.</p>
  </div>
</div>
</c-docs.example>

:::en
### Disabled
:::pt-br
### Desabilitado
:::

<c-docs.example>
<div class="flex items-center gap-2">
  <c-checkbox id="disabled-sync" class="peer" disabled />
  <c-label for="disabled-sync">Sync across devices</c-label>
</div>
</c-docs.example>

:::en
### Group

A `<fieldset>` and a `<legend>` name a group of boxes that share one `name`, so
the view reads every checked value with `getlist`.
:::pt-br
### Grupo

Um `<fieldset>` e uma `<legend>` dão nome a um grupo de caixas que dividem o
mesmo `name`, então a view lê todos os valores marcados com `getlist`.
:::

<c-docs.example>
<fieldset class="grid gap-3">
  <legend class="mb-2 text-sm font-medium">Show these items on the desktop</legend>
  <div class="flex items-center gap-2">
    <c-checkbox id="group-disks" name="items" value="disks" checked />
    <c-label for="group-disks">Hard disks</c-label>
  </div>
  <div class="flex items-center gap-2">
    <c-checkbox id="group-servers" name="items" value="servers" />
    <c-label for="group-servers">Connected servers</c-label>
  </div>
</fieldset>
</c-docs.example>

:::en
### Table

A box per row, all with the same `name` and each with its row's pk as the
`value`, posts the selection as a list.
:::pt-br
### Tabela

Uma caixa por linha, todas com o mesmo `name` e cada uma com o pk da linha como
`value`, envia a seleção como uma lista.
:::

<c-docs.example>
<c-table class="max-w-md">
  <c-table.header>
    <c-table.row>
      <c-table.head class="w-8"><c-checkbox aria-label="Select all" /></c-table.head>
      <c-table.head>Name</c-table.head>
    </c-table.row>
  </c-table.header>
  <c-table.body>
    <c-table.row>
      <c-table.cell><c-checkbox name="selected" value="1" aria-label="Select Sarah Chen" /></c-table.cell>
      <c-table.cell>Sarah Chen</c-table.cell>
    </c-table.row>
    <c-table.row>
      <c-table.cell><c-checkbox name="selected" value="2" aria-label="Select Marc Rivera" /></c-table.cell>
      <c-table.cell>Marc Rivera</c-table.cell>
    </c-table.row>
  </c-table.body>
</c-table>
</c-docs.example>

:::en
## RTL

The box sits where the markup puts it, and a label after it follows the text,
so under `dir="rtl"` the label moves to the left of the box.

## Accessibility

It is a native checkbox: Space toggles it, and a screen reader announces it as
checked or not. A `<c-label>` with `for` set to the box's id names it, and
clicking the label toggles the box. A box without visible text, as in a table,
needs an `aria-label`.

## API reference
:::pt-br
## RTL

A caixa fica onde o markup a põe, e um rótulo depois dela acompanha o texto,
então sob `dir="rtl"` o rótulo vai para a esquerda da caixa.

## Acessibilidade

É um checkbox nativo: o Espaço o alterna, e um leitor de tela o anuncia como
marcado ou não. Um `<c-label>` com `for` igual ao id da caixa dá nome a ela, e
clicar no rótulo alterna a caixa. Uma caixa sem texto visível, como numa
tabela, precisa de um `aria-label`.

## Referência da API
:::

<c-docs.api-reference name="checkbox" />

:::en
## Notes

Being native, the box is drawn by the browser, tinted with `accent-primary`, so
it does not match upstream's square to the pixel. There is no invalid style:
give an invalid box `aria-invalid="true"` and a class of your own, such as
`aria-invalid:outline-destructive`. Upstream's indeterminate state is the
input's `indeterminate` property, set from JavaScript.
:::pt-br
## Observações

Por ser nativa, a caixa é desenhada pelo navegador, tingida com
`accent-primary`, então não bate pixel a pixel com o quadrado do upstream. Não
há estilo de inválido: dê a uma caixa inválida `aria-invalid="true"` e uma
classe sua, como `aria-invalid:outline-destructive`. O estado indeterminado do
upstream é a propriedade `indeterminate` do input, definida por JavaScript.
:::
