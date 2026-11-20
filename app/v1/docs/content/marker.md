---
title: Marker
description: The rows in a transcript that are not messages: status, system notes, tool activity and date breaks.
description.pt-br: As linhas de uma conversa que não são mensagens: status, avisos do sistema, atividade de ferramentas e quebras de data.
description.es: Las filas de una conversación que no son mensajes: estado, avisos del sistema, actividad de herramientas y cortes de fecha.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="flex w-full max-w-md flex-col gap-4 text-start">
<c-marker>
<c-marker.icon>
<c-icon name="check" />
</c-marker.icon>
<c-marker.content>Explored 4 files</c-marker.content>
</c-marker>
<c-marker variant="separator">
<c-marker.content>Today</c-marker.content>
</c-marker>
<c-marker role="status">
<c-marker.icon>
<c-icon name="loader-circle" class="animate-spin" />
</c-marker.icon>
<c-marker.content class="shimmer">Compacting conversation</c-marker.content>
</c-marker>
</div>
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add marker
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-marker>
    <c-marker.icon>
        <c-icon name="check" />
    </c-marker.icon>
    <c-marker.content>Explored 4 files</c-marker.content>
</c-marker>
```

:::en
The icon slot is decorative and hidden from assistive technology, so the content
has to carry the whole meaning on its own. Nothing here is stateful.

## Variants
:::pt-br
O espaço do ícone é decorativo e fica escondido das tecnologias assistivas,
então o conteúdo tem de carregar sozinho todo o significado. Nada aqui tem
estado.

## Variantes
:::

<c-docs.example>
<div class="flex w-full max-w-md flex-col gap-6 text-start">
  <c-marker>
    <c-marker.icon>
      <c-icon name="check" />
    </c-marker.icon>
    <c-marker.content>Default, an inline row</c-marker.content>
  </c-marker>
  <c-marker variant="border">
    <c-marker.icon>
      <c-icon name="check" />
    </c-marker.icon>
    <c-marker.content>Border, with a rule underneath</c-marker.content>
  </c-marker>
  <c-marker variant="separator">
    <c-marker.content>Separator, centred between two rules</c-marker.content>
  </c-marker>
</div>
</c-docs.example>

:::en
`separator` draws its rules with `before` and `after`, so an icon inside it
lands between the label and the left rule rather than at the start of the row.
Date breaks usually read better without one.

## Examples

### Announcing a change

A marker that reports work in progress should be announced, not just drawn.
`role="status"` reaches the root through the attributes, and the shimmer marks
the text as live.
:::pt-br
`separator` desenha os traços com `before` e `after`, então um ícone dentro dele
cai entre o rótulo e o traço da esquerda, e não no início da linha. Quebras de
data costumam ficar melhores sem ícone.

## Exemplos

### Anunciando uma mudança

Um marker que informa um trabalho em andamento deve ser anunciado, não só
desenhado. `role="status"` chega à raiz pelos atributos, e o brilho marca o
texto como vivo.
:::

<c-docs.example>
<div class="flex w-full max-w-md flex-col gap-4 text-start">
  <c-marker role="status">
    <c-marker.icon>
      <c-icon name="loader-circle" class="animate-spin" />
    </c-marker.icon>
    <c-marker.content class="shimmer">Thinking</c-marker.content>
  </c-marker>
</div>
</c-docs.example>

:::en
`shimmer` is a utility in `input.css`, not part of the component. It works on
any text element and turns itself off when the reader has asked for reduced
motion.

### Linking out

A marker can point somewhere. Put the link in the content rather than on the
root, so only the words are clickable and the row keeps its layout.
:::pt-br
`shimmer` é um utilitário do `input.css`, não faz parte do componente. Ele
funciona em qualquer elemento de texto e se desliga sozinho quando o leitor
pediu menos movimento.

### Apontando para fora

Um marker pode apontar para algum lugar. Ponha o link no conteúdo e não na raiz,
para que só as palavras sejam clicáveis e a linha mantenha o layout.
:::

<c-docs.example>
<div class="flex w-full max-w-md flex-col gap-4 text-start">
  <c-marker>
    <c-marker.icon>
      <c-icon name="check" />
    </c-marker.icon>
    <c-marker.content>
      <a href="{% url 'page' slug='installation' %}">Opened the installation guide</a>
    </c-marker.content>
  </c-marker>
</div>
</c-docs.example>

:::en
### In a transcript

Between messages, a marker is the line that explains a gap.
:::pt-br
### Numa transcrição

Entre mensagens, um marker é a linha que explica uma lacuna.
:::

<c-docs.demo-section>
<c-message.group class="w-full max-w-md text-start">
<c-message>
<c-message.content>
<c-bubble variant="muted">
<c-bubble.content>Give me a moment, I am reading the registry.</c-bubble.content>
</c-bubble>
</c-message.content>
</c-message>
<c-marker>
<c-marker.icon>
<c-icon name="search" />
</c-marker.icon>
<c-marker.content>Explored 4 files</c-marker.content>
</c-marker>
<c-message>
<c-message.content>
<c-bubble variant="muted">
<c-bubble.content>Found it. The entry was never added.</c-bubble.content>
</c-bubble>
</c-message.content>
</c-message>
</c-message.group>
</c-docs.demo-section>
