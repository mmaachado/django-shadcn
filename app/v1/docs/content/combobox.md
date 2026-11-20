---
title: Combobox
description: Autocomplete input and command palette with a list of suggestions.
description.pt-br: Campo com autocompletar e paleta de comandos, com lista de sugestões.
description.es: Campo con autocompletado y paleta de comandos, con lista de sugerencias.
---

<c-docs.demo-section class="min-h-[350px]">
<c-combobox :options="[{'value': 'django', 'label': 'Django'}, {'value': 'tailwind', 'label': 'Tailwind'}, {'value': 'alpine', 'label': 'Alpine.js'}, {'value': 'htmx', 'label': 'htmx'}]" placeholder="Search framework..." button_text="Select framework..." />
</c-docs.demo-section>

<c-docs.cheat-sheet name="combobox">
<c-combobox name="country" :options="countries" button_text="Select a country..." />
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add combobox
```

:::en
## Usage

A button that opens a searchable list, built on
[Popover]({% url 'page' slug='popover' %}). `options` is a list of dicts with a
`value` and a `label`, passed with a leading colon so cotton reads it as a
variable rather than a string:
:::pt-br
## Uso

Um botão que abre uma lista com busca, feito sobre o
[Popover]({% url 'page' slug='popover' %}). `options` é uma lista de dicts com
`value` e `label`, passada com dois-pontos na frente para que o cotton a leia
como variável e não como string:
:::

```python
countries = [{"value": c.code, "label": c.name} for c in Country.objects.all()]
```

```html
<c-combobox name="country" :options="countries" button_text="Select a country..." />
```

:::en
With `name` set, a hidden input posts the chosen `value`, so the view reads
`request.POST["country"]`. To start with a choice, pass its value as
`selected_value` and its label as `button_text`: the button shows
`button_text` until something is picked. Picking the selected option again
clears it.

The list, the search and the keyboard are Alpine. Without JavaScript the button
does nothing and nothing is posted, so a form that must work without it needs
a [Native Select]({% url 'page' slug='native-select' %}).
:::pt-br
Com `name` definido, um input oculto envia o `value` escolhido, então a view
lê `request.POST["country"]`. Para começar com uma escolha, passe o value dela
como `selected_value` e o rótulo como `button_text`: o botão mostra o
`button_text` até algo ser escolhido. Escolher de novo a opção selecionada a
limpa.

A lista, a busca e o teclado são do Alpine. Sem JavaScript o botão não faz nada
e nada é enviado, então um formulário que precisa funcionar sem ele pede um
[Native Select]({% url 'page' slug='native-select' %}).
:::

:::en
## Examples

### Basic
:::pt-br
## Exemplos

### Básico
:::

<c-docs.example>
<c-combobox :options="[{'value': 'next', 'label': 'Next.js'}, {'value': 'django', 'label': 'Django'}, {'value': 'rails', 'label': 'Rails'}]" button_text="Select framework..." />
</c-docs.example>

:::en
### With a value

`selected_value` and `button_text` together start the combobox on a choice.
:::pt-br
### Com valor

`selected_value` e `button_text` juntos começam o combobox numa escolha.
:::

<c-docs.example>
<c-combobox name="framework" selected_value="django" button_text="Django" :options="[{'value': 'next', 'label': 'Next.js'}, {'value': 'django', 'label': 'Django'}, {'value': 'rails', 'label': 'Rails'}]" />
</c-docs.example>

:::en
### Width

`width` sets the button and the list together, as a utility class.
:::pt-br
### Largura

`width` define o botão e a lista juntos, como uma classe utilitária.
:::

<c-docs.example>
<c-combobox width="w-[280px]" placeholder="Search timezone..." button_text="Select a timezone..." :options="[{'value': 'america/sao_paulo', 'label': 'America/Sao_Paulo'}, {'value': 'europe/lisbon', 'label': 'Europe/Lisbon'}, {'value': 'asia/tokyo', 'label': 'Asia/Tokyo'}]" />
</c-docs.example>

:::en
## RTL

The label sits at the start of the button and the chevron at its end, and the
search icon before the field, so under `dir="rtl"` they all change sides with
the text.

## Accessibility

The button carries `role="combobox"` and reports `aria-expanded`. Opening it
moves focus to the search field, where the up and down arrows move through the
options, Enter picks one and Escape closes the list. The options are not
announced as a listbox, so a screen reader hears them only as text.

## API reference
:::pt-br
## RTL

O rótulo fica no início do botão e o chevron no fim, e o ícone de busca antes
do campo, então sob `dir="rtl"` todos trocam de lado com o texto.

## Acessibilidade

O botão leva `role="combobox"` e informa `aria-expanded`. Abri-lo leva o foco
ao campo de busca, onde as setas para cima e para baixo percorrem as opções, o
Enter escolhe uma e o Escape fecha a lista. As opções não são anunciadas como um
listbox, então um leitor de tela as ouve só como texto.

## Referência da API
:::

<c-docs.api-reference name="combobox" />

:::en
## Notes

This is upstream's simplest combobox: one choice from a flat list. Multiple
selection with chips, groups, a clear button, custom item markup, the invalid
and disabled states, auto-highlight, the popup trigger and the input group
variant are not here. For several choices, a group of
[Checkbox]({% url 'page' slug='checkbox' %})es posts them without JavaScript.
:::pt-br
## Observações

Este é o combobox mais simples do upstream: uma escolha de uma lista plana.
Seleção múltipla com chips, grupos, um botão de limpar, markup próprio nos
itens, os estados inválido e desabilitado, o realce automático, o trigger de
popup e a variante com input group não estão aqui. Para várias escolhas, um
grupo de [Checkbox]({% url 'page' slug='checkbox' %})es as envia sem
JavaScript.
:::
