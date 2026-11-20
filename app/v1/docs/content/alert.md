---
title: Alert
description: Displays a callout for user attention.
description.pt-br: Destaca um aviso para chamar a atenção do usuário.
description.es: Destaca un aviso para llamar la atención del usuario.
---

<c-docs.demo-section class="min-h-[350px]">
<c-alert class="max-w-md">
<c-icon name="check" />
<c-alert.title>Payment received</c-alert.title>
<c-alert.description>Your order is confirmed and on its way.</c-alert.description>
</c-alert>
</c-docs.demo-section>

<c-docs.cheat-sheet name="alert">
<c-alert variant="destructive">
  <c-alert.title>Something went wrong</c-alert.title>
  <c-alert.description>{{ form.non_field_errors }}</c-alert.description>
</c-alert>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add alert
```

:::en
## Usage

An alert is a bordered box with a title and a description, and an optional
icon before them. It needs no JavaScript, and it is where Django's messages and
a form's non-field errors usually go:
:::pt-br
## Uso

Um alert é uma caixa com borda, título e descrição, e um ícone opcional antes
deles. Ele não precisa de JavaScript, e é onde as mensagens do Django e os
erros de formulário que não são de um campo costumam ficar:
:::

```html
{% for message in messages %}
  <c-alert variant="{% if message.level_tag == 'error' %}destructive{% else %}default{% endif %}">
    <c-alert.description>{{ message }}</c-alert.description>
  </c-alert>
{% endfor %}
```

:::en
## Examples

### Basic
:::pt-br
## Exemplos

### Básico
:::

<c-docs.example>
<c-alert class="max-w-md">
  <c-icon name="check" />
  <c-alert.title>Account updated</c-alert.title>
  <c-alert.description>Your profile and email were saved.</c-alert.description>
</c-alert>
</c-docs.example>

:::en
### Destructive
:::pt-br
### Destructive
:::

<c-docs.example>
<c-alert variant="destructive" class="max-w-md">
  <c-icon name="x" />
  <c-alert.title>Payment failed</c-alert.title>
  <c-alert.description>The card was declined. Try another one.</c-alert.description>
</c-alert>
</c-docs.example>

:::en
### Custom colors

The colours take the `!` suffix, since the variant already sets a background,
a border and a text colour.
:::pt-br
### Cores personalizadas

As cores pedem o sufixo `!`, já que a variante define um fundo, uma borda e uma
cor de texto.
:::

<c-docs.example>
<c-alert class="max-w-md border-amber-200! bg-amber-50! text-amber-900! dark:border-amber-900! dark:bg-amber-950! dark:text-amber-100!">
  <c-icon name="trending-up" class="text-amber-600!" />
  <c-alert.title>Your plan is almost full</c-alert.title>
  <c-alert.description>You have used 90% of your storage.</c-alert.description>
</c-alert>
</c-docs.example>

:::en
## RTL

The icon is placed with `start-4` and the text after it with `ps-7`, so under
`dir="rtl"` the icon moves to the right and the text keeps clear of it.

## Accessibility

Every alert carries `role="alert"`, which a screen reader announces as soon as
the alert appears, interrupting what it was reading. That suits an error or a
message after a form posts. For a note that is simply part of the page, a
plain bordered box says the same without the interruption.

## API reference
:::pt-br
## RTL

O ícone é posicionado com `start-4` e o texto depois dele com `ps-7`, então sob
`dir="rtl"` o ícone vai para a direita e o texto continua afastado dele.

## Acessibilidade

Todo alert leva `role="alert"`, que um leitor de tela anuncia assim que o alert
aparece, interrompendo o que estava lendo. Isso combina com um erro ou com uma
mensagem depois do envio de um formulário. Para um aviso que só faz parte da
página, uma caixa com borda simples diz o mesmo sem a interrupção.

## Referência da API
:::

<c-docs.api-reference name="alert" />

:::en
## Notes

Upstream's alert has an `AlertAction` part for a button in its corner. There is
none here: put the button in the description, or beside the alert.
:::pt-br
## Observações

O alert do upstream tem uma parte `AlertAction` para um botão no canto. Aqui não
há: ponha o botão na descrição, ou ao lado do alert.
:::
