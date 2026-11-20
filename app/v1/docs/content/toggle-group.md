---
title: Toggle Group
description: A set of toggles that share one outline.
description.pt-br: Um conjunto de toggles que dividem o mesmo contorno.
description.es: Un conjunto de toggles que comparten un mismo contorno.
---

<c-docs.demo-section class="min-h-[350px]">
<c-toggle-group variant="outline">
<c-toggle-group.item aria-label="Bold"><span class="font-bold">B</span></c-toggle-group.item>
<c-toggle-group.item aria-label="Italic"><span class="italic">I</span></c-toggle-group.item>
<c-toggle-group.item aria-label="Underline"><span class="underline">U</span></c-toggle-group.item>
</c-toggle-group>
</c-docs.demo-section>

<c-docs.cheat-sheet name="toggle-group">
<c-toggle-group>
  <c-toggle-group.item>Left</c-toggle-group.item>
  <c-toggle-group.item>Center</c-toggle-group.item>
  <c-toggle-group.item>Right</c-toggle-group.item>
</c-toggle-group>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add toggle_group
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-toggle-group>
  <c-toggle-group.item>Left</c-toggle-group.item>
  <c-toggle-group.item>Center</c-toggle-group.item>
  <c-toggle-group.item>Right</c-toggle-group.item>
</c-toggle-group>
</c-docs.example>

:::en
Variant and size go on the group, not on each item.

## Examples

### Outline
:::pt-br
A variante e o tamanho vão no grupo, não em cada item.

## Exemplos

### Outline
:::

<c-docs.example>
<c-toggle-group variant="outline">
  <c-toggle-group.item>Left</c-toggle-group.item>
  <c-toggle-group.item>Center</c-toggle-group.item>
  <c-toggle-group.item>Right</c-toggle-group.item>
</c-toggle-group>
</c-docs.example>

:::en
### Sizes
:::pt-br
### Tamanhos
:::

<c-docs.example>
<div class="flex flex-col items-center gap-4">
  <c-toggle-group variant="outline" size="sm">
    <c-toggle-group.item>S</c-toggle-group.item>
    <c-toggle-group.item>M</c-toggle-group.item>
    <c-toggle-group.item>L</c-toggle-group.item>
  </c-toggle-group>
  <c-toggle-group variant="outline" size="lg">
    <c-toggle-group.item>S</c-toggle-group.item>
    <c-toggle-group.item>M</c-toggle-group.item>
    <c-toggle-group.item>L</c-toggle-group.item>
  </c-toggle-group>
</div>
</c-docs.example>

:::en
### Spaced
:::pt-br
### Espaçado
:::

<c-docs.example>
<c-toggle-group variant="outline" spacing="1">
  <c-toggle-group.item>Left</c-toggle-group.item>
  <c-toggle-group.item>Center</c-toggle-group.item>
  <c-toggle-group.item>Right</c-toggle-group.item>
</c-toggle-group>
</c-docs.example>

:::en
### Disabled

`disabled` on an item reaches its button.
:::pt-br
### Desabilitado

`disabled` num item chega ao botão dele.
:::

<c-docs.example>
<c-toggle-group aria-label="Alignment">
  <c-toggle-group.item>Left</c-toggle-group.item>
  <c-toggle-group.item>Center</c-toggle-group.item>
  <c-toggle-group.item disabled>Right</c-toggle-group.item>
</c-toggle-group>
</c-docs.example>

:::en
## RTL

The row reverses under `dir="rtl"` and keeps its rounded ends on the
outside, through logical radii and borders.

## Accessibility

The group is a `role="group"` and each item a button reporting
`aria-pressed`. Name the group with `aria-label`, such as "Text formatting".

## API reference
:::pt-br
## RTL

A fileira se inverte sob `dir="rtl"` e mantém as pontas arredondadas do lado
de fora, por raios e bordas lógicos.

## Acessibilidade

O grupo é um `role="group"` e cada item um botão que informa
`aria-pressed`. Dê um nome ao grupo com `aria-label`, como "Formatação de
texto".

## Referência da API
:::

<c-docs.api-reference name="toggle-group" />

:::en
## Notes

Radix hands variant and size down through React context. Cotton has no
equivalent, so the group styles its own children with `[&>*]` selectors. Two
`data-*` conditions on one element combine the way you would expect; two
`group-data-*` would chain into a descendant selector instead, which is why the
rules live on the group rather than on the item.

Each item keeps its own pressed state. Radix also offers single-selection mode,
where picking one clears the rest — that needs shared state and is not here yet.
:::pt-br
## Observações

O Radix passa a variante e o tamanho para baixo pelo contexto do React. O cotton
não tem equivalente, então o grupo estiliza os próprios filhos com seletores
`[&>*]`. Duas condições `data-*` num mesmo elemento se combinam como você
esperaria; dois `group-data-*` se encadeariam num seletor de descendente, e é
por isso que as regras ficam no grupo e não no item.

Cada item mantém o próprio estado de pressionado. O Radix também oferece um modo
de seleção única, em que escolher um desmarca os outros — isso precisa de estado
compartilhado e ainda não está aqui.
:::
