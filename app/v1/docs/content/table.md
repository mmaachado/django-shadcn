---
title: Table
description: A responsive table component.
description.pt-br: Uma tabela responsiva.
description.es: Una tabla adaptable.
---

<c-docs.demo-section class="min-h-[350px]">
<c-table>
<c-table.caption>
A list of your recent invoices.
</c-table.caption>
<c-table.header>
<c-table.row>
<c-table.head class="w-[100px]">Invoice</c-table.head>
<c-table.head>Status</c-table.head>
<c-table.head>Method</c-table.head>
<c-table.head class="text-end">Amount</c-table.head>
</c-table.row>
</c-table.header>
<c-table.body>
<c-table.row>
<c-table.cell class="font-medium">INV001</c-table.cell>
<c-table.cell>Paid</c-table.cell>
<c-table.cell>Card</c-table.cell>
<c-table.cell class="text-end">$100</c-table.cell>
</c-table.row>
<c-table.row>
<c-table.cell class="font-medium">INV002</c-table.cell>
<c-table.cell>Pending</c-table.cell>
<c-table.cell>PayPal</c-table.cell>
<c-table.cell class="text-end">$200</c-table.cell>
</c-table.row>
<c-table.row>
<c-table.cell class="font-medium">INV003</c-table.cell>
<c-table.cell>Failed</c-table.cell>
<c-table.cell>Card</c-table.cell>
<c-table.cell class="text-end">$300</c-table.cell>
</c-table.row>
</c-table.body>
</c-table>
</c-docs.demo-section>

<c-docs.cheat-sheet name="table">
<c-table>
  <c-table.caption> A list of your recent invoices. </c-table.caption>
  <c-table.header>
    <c-table.row>
      <c-table.head class="w-[100px]">Invoice</c-table.head>
      <c-table.head>Status</c-table.head>
      <c-table.head>Method</c-table.head>
      <c-table.head class="text-end">Amount</c-table.head>
    </c-table.row>
  </c-table.header>
  <c-table.body>
    <c-table.row>
      <c-table.cell class="font-medium">INV001</c-table.cell>
      <c-table.cell>Paid</c-table.cell>
      <c-table.cell>Card</c-table.cell>
      <c-table.cell class="text-end">$100</c-table.cell>
    </c-table.row>
  </c-table.body>
</c-table>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add table
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-table>
  <c-table.caption> A list of your recent invoices. </c-table.caption>
  <c-table.header>
    <c-table.row>
      <c-table.head class="w-[100px]">Invoice</c-table.head>
      <c-table.head>Status</c-table.head>
      <c-table.head>Method</c-table.head>
      <c-table.head class="text-end">Amount</c-table.head>
    </c-table.row>
  </c-table.header>
  <c-table.body>
    <c-table.row>
      <c-table.cell class="font-medium">INV001</c-table.cell>
      <c-table.cell>Paid</c-table.cell>
      <c-table.cell>Card</c-table.cell>
      <c-table.cell class="text-end">$100</c-table.cell>
    </c-table.row>
  </c-table.body>
</c-table>
```

:::en
## Examples

### Empty Table
:::pt-br
## Exemplos

### Tabela vazia
:::

<c-docs.example>
<c-table>
  <c-table.caption>
    A list of your recent invoices.
  </c-table.caption>
  <c-table.header>
    <c-table.row>
      <c-table.head>Invoice</c-table.head>
      <c-table.head>Status</c-table.head>
      <c-table.head>Method</c-table.head>
      <c-table.head>Amount</c-table.head>
    </c-table.row>
  </c-table.header>
  <c-table.body>
    <c-table.empty />
  </c-table.body>
</c-table>
</c-docs.example>

:::en
### Footer

`footer` holds totals under the body.
:::pt-br
### Rodapé

O `footer` guarda os totais embaixo do corpo.
:::

<c-docs.example>
<c-table class="max-w-md">
  <c-table.header>
    <c-table.row>
      <c-table.head>Invoice</c-table.head>
      <c-table.head class="text-end!">Amount</c-table.head>
    </c-table.row>
  </c-table.header>
  <c-table.body>
    <c-table.row>
      <c-table.cell>INV001</c-table.cell>
      <c-table.cell class="text-end tabular-nums">$250.00</c-table.cell>
    </c-table.row>
    <c-table.row>
      <c-table.cell>INV002</c-table.cell>
      <c-table.cell class="text-end tabular-nums">$150.00</c-table.cell>
    </c-table.row>
  </c-table.body>
  <c-table.footer>
    <c-table.row>
      <c-table.cell>Total</c-table.cell>
      <c-table.cell class="text-end tabular-nums">$400.00</c-table.cell>
    </c-table.row>
  </c-table.footer>
</c-table>
</c-docs.example>

:::en
### Actions

A button in the last cell acts on its row; name the row in its label.
:::pt-br
### Ações

Um botão na última célula age sobre a linha; dê o nome da linha no rótulo dele.
:::

<c-docs.example>
<c-table class="max-w-md">
  <c-table.body>
    <c-table.row>
      <c-table.cell>INV001</c-table.cell>
      <c-table.cell class="w-10">
        <c-button variant="ghost" size="icon" aria-label="Copy INV001"><c-icon name="copy" /></c-button>
      </c-table.cell>
    </c-table.row>
  </c-table.body>
</c-table>
</c-docs.example>

:::en
## RTL

The table runs with the text, so under `dir="rtl"` the first column is on the
right, and `text-end` numbers move to the left edge.

## Accessibility

It is a real `<table>` with `<th>` header cells, so a screen reader announces
the column as it moves across a row. A `caption` names the table.

## API reference
:::pt-br
## RTL

A tabela corre com o texto, então sob `dir="rtl"` a primeira coluna fica à
direita, e os números com `text-end` vão para a borda esquerda.

## Acessibilidade

É uma `<table>` de verdade com células de cabeçalho `<th>`, então um leitor de
tela anuncia a coluna ao percorrer uma linha. Um `caption` dá nome à tabela.

## Referência da API
:::

<c-docs.api-reference name="table" />
