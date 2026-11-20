---
title: Empty
description: Use to display an empty state, when there is nothing to show yet.
description.pt-br: Para quando ainda não há nada a mostrar.
description.es: Para cuando todavía no hay nada que mostrar.
---

<c-docs.demo-section class="min-h-[350px]">
<c-empty class="w-full border">
<c-empty.header>
<c-empty.media variant="icon">
<c-icon name="search" />
</c-empty.media>
<c-empty.title>No results found</c-empty.title>
<c-empty.description>
Try adjusting your search or filters to find what you are
looking for.
</c-empty.description>
</c-empty.header>
<c-empty.content>
<c-button variant="outline">Clear filters</c-button>
</c-empty.content>
</c-empty>
</c-docs.demo-section>

<c-docs.cheat-sheet name="empty">
<c-empty>
  <c-empty.header>
    <c-empty.media variant="icon">
      <c-icon name="search" />
    </c-empty.media>
    <c-empty.title>No results found</c-empty.title>
    <c-empty.description>Try a different search.</c-empty.description>
  </c-empty.header>
  <c-empty.content>
    <c-button variant="outline">Clear filters</c-button>
  </c-empty.content>
</c-empty>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add empty
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-empty>
  <c-empty.header>
    <c-empty.media variant="icon">
      <c-icon name="search" />
    </c-empty.media>
    <c-empty.title>No results found</c-empty.title>
    <c-empty.description>Try a different search.</c-empty.description>
  </c-empty.header>
  <c-empty.content>
    <c-button variant="outline">Clear filters</c-button>
  </c-empty.content>
</c-empty>
```

:::en
The border is dashed but no border width is applied, exactly as upstream.
Add `border` when you want the outline to show.

## Examples

### Outline
:::pt-br
A borda é tracejada, mas nenhuma largura de borda é aplicada, exatamente como no
upstream. Acrescente `border` quando quiser que o contorno apareça.

## Exemplos

### Outline
:::

<c-docs.example>
<c-empty class="w-full border">
  <c-empty.header>
    <c-empty.media variant="icon">
      <c-icon name="x" />
    </c-empty.media>
    <c-empty.title>No projects</c-empty.title>
    <c-empty.description>
      Projects you create will show up here.
    </c-empty.description>
  </c-empty.header>
  <c-empty.content>
    <c-button>Create project</c-button>
  </c-empty.content>
</c-empty>
</c-docs.example>

:::en
### Without media
:::pt-br
### Sem mídia
:::

<c-docs.example>
<c-empty class="w-full border">
  <c-empty.header>
    <c-empty.title>Nothing here yet</c-empty.title>
    <c-empty.description>
      Read the <a href="{% url 'page' slug='introduction' %}">introduction</a> to get
      started.
    </c-empty.description>
  </c-empty.header>
</c-empty>
</c-docs.example>

:::en
### Loading
:::pt-br
### Carregando
:::

<c-docs.example>
<c-empty class="w-full border">
  <c-empty.header>
    <c-empty.media>
      <c-spinner class="size-6" />
    </c-empty.media>
    <c-empty.title>Loading projects</c-empty.title>
    <c-empty.description>This will only take a moment.</c-empty.description>
  </c-empty.header>
</c-empty>
</c-docs.example>

:::en
### Background

A muted background sets the empty state apart from the page.
:::pt-br
### Fundo

Um fundo discreto separa o estado vazio da página.
:::

<c-docs.example>
<c-empty class="w-full bg-muted/50">
  <c-empty.header>
    <c-empty.title>No notifications</c-empty.title>
    <c-empty.description>You are all caught up.</c-empty.description>
  </c-empty.header>
</c-empty>
</c-docs.example>

:::en
### Avatar
:::pt-br
### Avatar
:::

<c-docs.example>
<c-empty class="w-full border">
  <c-empty.header>
    <c-empty.media>
      <c-avatar size="lg">
        <c-avatar.fallback>MM</c-avatar.fallback>
      </c-avatar>
    </c-empty.media>
    <c-empty.title>No messages from Marcelo</c-empty.title>
    <c-empty.description>Start the conversation.</c-empty.description>
  </c-empty.header>
  <c-empty.content>
    <c-button size="sm">Send a message</c-button>
  </c-empty.content>
</c-empty>
</c-docs.example>

:::en
### Input group

A search with no results keeps the search field in reach.
:::pt-br
### Input group

Uma busca sem resultados mantém o campo de busca ao alcance.
:::

<c-docs.example>
<c-empty class="w-full border">
  <c-empty.header>
    <c-empty.title>Nothing matches "invoce"</c-empty.title>
    <c-empty.description>Check the spelling, or search for something else.</c-empty.description>
  </c-empty.header>
  <c-empty.content>
    <c-input-group class="max-w-xs">
      <c-input-group.addon><c-icon name="search" /></c-input-group.addon>
      <c-input-group.input value="invoce" aria-label="Search" />
    </c-input-group>
  </c-empty.content>
</c-empty>
</c-docs.example>

:::en
## RTL

The empty state is centred, so it looks the same under `dir="rtl"`.

## Accessibility

It is plain markup: the title and the description are read in order, and an
icon in the media is decorative. Make the next step a real link or button, so
the reader has somewhere to go.

## API reference
:::pt-br
## RTL

O estado vazio é centralizado, então fica igual sob `dir="rtl"`.

## Acessibilidade

É markup simples: o título e a descrição são lidos em ordem, e um ícone na
mídia é decorativo. Faça do próximo passo um link ou botão de verdade, para o
leitor ter para onde ir.

## Referência da API
:::

<c-docs.api-reference name="empty" />
