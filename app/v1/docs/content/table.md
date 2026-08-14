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
<c-table.head class="text-right">Amount</c-table.head>
</c-table.row>
</c-table.header>
<c-table.body>
<c-table.row>
<c-table.cell class="font-medium">INV001</c-table.cell>
<c-table.cell>Paid</c-table.cell>
<c-table.cell>Card</c-table.cell>
<c-table.cell class="text-right">$100</c-table.cell>
</c-table.row>
<c-table.row>
<c-table.cell class="font-medium">INV002</c-table.cell>
<c-table.cell>Pending</c-table.cell>
<c-table.cell>PayPal</c-table.cell>
<c-table.cell class="text-right">$200</c-table.cell>
</c-table.row>
<c-table.row>
<c-table.cell class="font-medium">INV003</c-table.cell>
<c-table.cell>Failed</c-table.cell>
<c-table.cell>Card</c-table.cell>
<c-table.cell class="text-right">$300</c-table.cell>
</c-table.row>
</c-table.body>
</c-table>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add table
```

## Usage

```html
<c-table>
  <c-table.caption> A list of your recent invoices. </c-table.caption>
  <c-table.header>
    <c-table.row>
      <c-table.head class="w-[100px]">Invoice</c-table.head>
      <c-table.head>Status</c-table.head>
      <c-table.head>Method</c-table.head>
      <c-table.head class="text-right">Amount</c-table.head>
    </c-table.row>
  </c-table.header>
  <c-table.body>
    <c-table.row>
      <c-table.cell class="font-medium">INV001</c-table.cell>
      <c-table.cell>Paid</c-table.cell>
      <c-table.cell>Card</c-table.cell>
      <c-table.cell class="text-right">$100</c-table.cell>
    </c-table.row>
  </c-table.body>
</c-table>
```

## Examples

### Empty Table

<c-docs.demo-section>
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
</c-docs.demo-section>

```html
<c-table>
  <c-table.caption> A list of your recent invoices. </c-table.caption>
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
```
