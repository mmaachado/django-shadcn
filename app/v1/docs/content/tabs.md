---
title: Tabs
description: A set of layered sections of content—known as tab panels—that are displayed one at a time.
description.pt-br: Seções de conteúdo sobrepostas, exibidas uma de cada vez.
description.es: Secciones de contenido superpuestas, que se muestran de una en una.
---

<c-docs.demo-section class="min-h-[350px]">
<c-tabs default_value="account" class="w-[400px]">
<c-tabs.list>
<c-tabs.trigger value="account">Account</c-tabs.trigger>
<c-tabs.trigger value="password">Password</c-tabs.trigger>
</c-tabs.list>
<c-tabs.content value="account"><p class="text-sm text-muted-foreground">Make changes to your account here.</p></c-tabs.content>
<c-tabs.content value="password"><p class="text-sm text-muted-foreground">Change your password here.</p></c-tabs.content>
</c-tabs>
</c-docs.demo-section>

<c-docs.cheat-sheet name="tabs">
<c-tabs default_value="overview">
  <c-tabs.list>
    <c-tabs.trigger value="overview">Overview</c-tabs.trigger>
    <c-tabs.trigger value="activity">Activity</c-tabs.trigger>
  </c-tabs.list>
  <c-tabs.content value="overview">...</c-tabs.content>
  <c-tabs.content value="activity">...</c-tabs.content>
</c-tabs>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add tabs
```

:::en
## Usage

Each trigger and its content share a `value`, and `default_value` picks the
panel shown first. The triggers are `<button type="button">`, so tabs inside a
form never submit it, and every panel stays in the markup, so a form split
across tabs posts all its fields together.

Switching is Alpine. Without JavaScript every panel shows, one under the
other, so the content is still all there.
:::pt-br
## Uso

Cada trigger e o conteúdo dele dividem um `value`, e o `default_value` escolhe
o painel mostrado primeiro. Os triggers são `<button type="button">`, então
abas dentro de um formulário nunca o enviam, e todo painel fica no markup,
então um formulário dividido em abas envia todos os campos juntos.

Trocar de aba é Alpine. Sem JavaScript todos os painéis aparecem, um embaixo do
outro, então o conteúdo continua todo ali.
:::

:::en
## Examples

### Disabled

`disabled` on a trigger reaches its button, so that tab cannot be opened.
:::pt-br
## Exemplos

### Desabilitado

`disabled` num trigger chega ao botão dele, então aquela aba não pode ser
aberta.
:::

<c-docs.example>
<c-tabs default_value="home" class="w-[400px]">
  <c-tabs.list>
    <c-tabs.trigger value="home">Home</c-tabs.trigger>
    <c-tabs.trigger value="settings">Settings</c-tabs.trigger>
    <c-tabs.trigger value="billing" disabled>Billing</c-tabs.trigger>
  </c-tabs.list>
  <c-tabs.content value="home"><p class="text-sm text-muted-foreground">Welcome back.</p></c-tabs.content>
  <c-tabs.content value="settings"><p class="text-sm text-muted-foreground">Your preferences.</p></c-tabs.content>
</c-tabs>
</c-docs.example>

:::en
### Icons
:::pt-br
### Ícones
:::

<c-docs.example>
<c-tabs default_value="preview" class="w-[400px]">
  <c-tabs.list>
    <c-tabs.trigger value="preview"><c-icon name="search" class="me-1.5 size-4" />Preview</c-tabs.trigger>
    <c-tabs.trigger value="code"><c-icon name="copy" class="me-1.5 size-4" />Code</c-tabs.trigger>
  </c-tabs.list>
  <c-tabs.content value="preview"><p class="text-sm text-muted-foreground">The rendered result.</p></c-tabs.content>
  <c-tabs.content value="code"><p class="text-sm text-muted-foreground">The template behind it.</p></c-tabs.content>
</c-tabs>
</c-docs.example>

:::en
### A form across tabs

The panels all stay in the form, so one submit sends every field.
:::pt-br
### Um formulário em abas

Os painéis ficam todos no formulário, então um envio manda todos os campos.
:::

<c-docs.example>
<form class="w-[400px] space-y-4" onsubmit="return false">
  <c-tabs default_value="profile">
    <c-tabs.list>
      <c-tabs.trigger value="profile">Profile</c-tabs.trigger>
      <c-tabs.trigger value="contact">Contact</c-tabs.trigger>
    </c-tabs.list>
    <c-tabs.content value="profile" class="grid gap-2">
      <c-label for="tabs-name">Name</c-label>
      <c-input id="tabs-name" name="name" />
    </c-tabs.content>
    <c-tabs.content value="contact" class="grid gap-2">
      <c-label for="tabs-email">Email</c-label>
      <c-input id="tabs-email" name="email" type="email" />
    </c-tabs.content>
  </c-tabs>
  <c-button>Save</c-button>
</form>
</c-docs.example>

:::en
## RTL

The tabs run with the text, so under `dir="rtl"` the first tab is on the right,
and an icon before a label moves with it.

## Accessibility

The list is a `role="tablist"`, the triggers `role="tab"` and the panels
`role="tabpanel"`, and the hidden panels leave the reading order. The active
tab reports `aria-selected="true"`, and each tab and panel name each other
through `aria-controls` and `aria-labelledby`, with ids generated per tab set.

Only the active tab is in the Tab order, so Tab goes from the list straight
into the panel. Left and Right move to the previous and next tab and open it,
wrapping at the ends and swapping under `dir="rtl"`; Home and End go to the
first and last. Disabled tabs are skipped. Name the list with `aria-label`
when the tabs need one.

## API reference
:::pt-br
## RTL

As abas correm com o texto, então sob `dir="rtl"` a primeira aba fica à
direita, e um ícone antes de um rótulo se move junto.

## Acessibilidade

A lista é um `role="tablist"`, os triggers `role="tab"` e os painéis
`role="tabpanel"`, e os painéis escondidos saem da leitura. A aba ativa
informa `aria-selected="true"`, e cada aba e painel dão nome um ao outro com
`aria-controls` e `aria-labelledby`, com ids gerados para cada conjunto de
abas.

Só a aba ativa fica na ordem do Tab, então o Tab vai da lista direto para o
painel. As setas para a esquerda e para a direita vão para a aba anterior e a
seguinte e a abrem, dando a volta nas pontas e trocando de lado sob
`dir="rtl"`; Home e End vão para a primeira e a última. Abas desabilitadas são
puladas. Dê um nome à lista com `aria-label` quando as abas precisarem.

## Referência da API
:::

<c-docs.api-reference name="tabs" />

:::en
## Notes

Upstream's line variant and vertical tabs are not here; restyle the list and
the triggers with classes for either.
:::pt-br
## Observações

A variante line e as abas verticais do upstream não estão aqui; reestilize a
lista e os triggers com classes para qualquer uma das duas.
:::
