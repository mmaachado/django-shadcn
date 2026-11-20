---
title: Trace
description: The steps behind an answer, reasoning, tool calls and sources, as quiet lines that open into detail.
description.pt-br: Os passos por trás de uma resposta, raciocínio, chamadas de ferramenta e fontes, como linhas discretas que se abrem em detalhe.
description.es: Los pasos detrás de una respuesta, razonamiento, llamadas a herramientas y fuentes, como líneas discretas que se abren en detalle.
---

<c-docs.demo-section class="min-h-[350px]">
<c-trace class="max-w-md">
<c-trace.collapsible default_open="true">
<c-trace.collapsible-trigger>
<c-trace.line>
<c-trace.title>Thought for 4s</c-trace.title>
</c-trace.line>
</c-trace.collapsible-trigger>
<c-trace.collapsible-content>
The question is about install paths, so the registry and the CLI constants are
where to look first.
</c-trace.collapsible-content>
</c-trace.collapsible>
<c-trace.line>
<c-trace.icon><c-icon name="search" /></c-trace.icon>
<c-trace.title>Searched the registry</c-trace.title>
<c-trace.description>3 results</c-trace.description>
</c-trace.line>
<a href="#">
<c-trace.line>
<c-trace.icon><c-icon name="check" /></c-trace.icon>
<c-trace.title>Read constants.py</c-trace.title>
</c-trace.line>
</a>
<c-trace.line status="error">
<c-trace.icon><c-icon name="x" /></c-trace.icon>
<c-trace.title>Ran the test suite</c-trace.title>
<c-trace.description>1 failed</c-trace.description>
</c-trace.line>
<c-trace.line status="running">
<c-trace.icon><c-icon name="loader-circle" class="animate-spin" /></c-trace.icon>
<c-trace.title>Writing the answer</c-trace.title>
</c-trace.line>
<c-trace.line status="pending">
<c-trace.icon><c-icon name="circle" /></c-trace.icon>
<c-trace.title>Open a pull request</c-trace.title>
</c-trace.line>
</c-trace>
</c-docs.demo-section>

<c-docs.cheat-sheet name="trace">
<c-trace>
  <c-trace.line>
    <c-trace.icon><c-icon name="search" /></c-trace.icon>
    <c-trace.title>Searched the registry</c-trace.title>
    <c-trace.description>3 results</c-trace.description>
  </c-trace.line>
</c-trace>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add trace
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-trace>
  <c-trace.line>
    <c-trace.icon><c-icon name="search" /></c-trace.icon>
    <c-trace.title>Searched the registry</c-trace.title>
    <c-trace.description>3 results</c-trace.description>
  </c-trace.line>
</c-trace>
```

:::en
A trace is the column of steps that sits above an answer in a chat, next to
[Message]({% url 'page' slug='message' %}) and
[Message Scroller]({% url 'page' slug='message-scroller' %}). Each step is a
line: an icon, a title that truncates, and a description in tabular figures
for a count or a duration. The icon is decorative and hidden from a screen
reader, so the title has to say what happened.

## Status

`status` is `running`, `error` or `pending`, and a line without one is done. A
running title shimmers, an error turns the line red, and a pending one fades.
The status changes the look and nothing else: swap the icon too, as the demo
does with a spinner, a cross and an empty circle.

## A step that opens

Reasoning and a tool call's output go in a collapsible. The trigger holds a
line and adds a chevron that turns when it opens, and the content is indented
under a rule.
:::pt-br
Um trace é a coluna de passos que fica acima de uma resposta num chat, ao lado
de [Message]({% url 'page' slug='message' %}) e de
[Message Scroller]({% url 'page' slug='message-scroller' %}). Cada passo é uma
linha: um ícone, um título que trunca e uma descrição em algarismos tabulares,
para uma contagem ou uma duração. O ícone é decorativo e fica escondido de um
leitor de tela, então o título tem de dizer o que aconteceu.

## Status

`status` é `running`, `error` ou `pending`, e uma linha sem status está
concluída. Um título em andamento cintila, um erro deixa a linha vermelha e um
pendente esmaece. O status muda a aparência e mais nada: troque o ícone também,
como a demo faz com um spinner, um x e um círculo vazio.

## Um passo que se abre

O raciocínio e a saída de uma ferramenta vão num collapsible. O trigger guarda
uma linha e acrescenta um chevron que gira quando abre, e o conteúdo fica
recuado sob um traço.
:::

```html
<c-trace.collapsible>
  <c-trace.collapsible-trigger>
    <c-trace.line>
      <c-trace.title>Thought for 4s</c-trace.title>
    </c-trace.line>
  </c-trace.collapsible-trigger>
  <c-trace.collapsible-content>
    The question is about install paths, so the registry comes first.
  </c-trace.collapsible-content>
</c-trace.collapsible>
```

:::en
`default_open="true"` starts it open. The height animates through Alpine's
collapse plugin, as in [Collapsible]({% url 'page' slug='collapsible' %});
without the plugin it opens instantly.

## A step that links

Wrap a line in an `<a>` or a `<button>` to open a source or a step. The trace
styles the wrapper, rounding it and giving it a focus ring, and the line turns
to the foreground colour on hover.
:::pt-br
`default_open="true"` começa aberto. A altura anima pelo plugin collapse do
Alpine, como no [Collapsible]({% url 'page' slug='collapsible' %}); sem o
plugin ele abre na hora.

## Um passo que é link

Envolva uma linha num `<a>` ou num `<button>` para abrir uma fonte ou um passo.
O trace estiliza o elemento em volta, arredondando-o e dando a ele um anel de
foco, e a linha passa para a cor de primeiro plano no hover.
:::

```html
<a href="{{ source.url }}">
  <c-trace.line>
    <c-trace.icon><c-icon name="check" /></c-trace.icon>
    <c-trace.title>{{ source.title }}</c-trace.title>
  </c-trace.line>
</a>
```

:::en
## Anatomy

| Tag | What it is |
| --- | --- |
| `<c-trace>` | the column of steps |
| `<c-trace.line>` | one step; takes `status` |
| `<c-trace.icon>` | the step's icon, hidden from assistive technology |
| `<c-trace.title>` | what happened |
| `<c-trace.description>` | a count or a duration |
| `<c-trace.collapsible>` | a step that opens; takes `default_open` |
| `<c-trace.collapsible-trigger>` | the line that opens it, with the chevron |
| `<c-trace.collapsible-content>` | the detail, indented under a rule |
:::pt-br
## Anatomia

| Tag | O que é |
| --- | --- |
| `<c-trace>` | a coluna de passos |
| `<c-trace.line>` | um passo; aceita `status` |
| `<c-trace.icon>` | o ícone do passo, escondido das tecnologias assistivas |
| `<c-trace.title>` | o que aconteceu |
| `<c-trace.description>` | uma contagem ou uma duração |
| `<c-trace.collapsible>` | um passo que se abre; aceita `default_open` |
| `<c-trace.collapsible-trigger>` | a linha que o abre, com o chevron |
| `<c-trace.collapsible-content>` | o detalhe, recuado sob um traço |
:::

:::en
## API reference
:::pt-br
## Referência da API
:::

<c-docs.api-reference name="trace" />
