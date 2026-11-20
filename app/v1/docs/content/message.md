---
title: Message
description: The row of a chat transcript: avatar, alignment, header and footer around whatever the message itself is.
description.pt-br: A linha de uma conversa: avatar, alinhamento, cabeçalho e rodapé em volta da mensagem.
description.es: La fila de una conversación: avatar, alineación, encabezado y pie alrededor del mensaje.
---

<c-docs.demo-section class="min-h-[350px]">
<c-message.group class="w-full max-w-md text-start">
<c-message>
<c-message.avatar>
<c-avatar>
<c-avatar.fallback>CN</c-avatar.fallback>
</c-avatar>
</c-message.avatar>
<c-message.content>
<c-message.header>Assistant</c-message.header>
<c-bubble variant="muted">
<c-bubble.content>The registry entry was missing, so the CLI refused the name.</c-bubble.content>
</c-bubble>
</c-message.content>
</c-message>
<c-message align="end">
<c-message.content>
<c-bubble align="end">
<c-bubble.content>That explains it. Adding the entry now.</c-bubble.content>
</c-bubble>
<c-message.footer>Sent</c-message.footer>
</c-message.content>
</c-message>
</c-message.group>
</c-docs.demo-section>

<c-docs.cheat-sheet name="message">
<c-message>
    <c-message.avatar>
        <c-avatar>
            <c-avatar.fallback>CN</c-avatar.fallback>
        </c-avatar>
    </c-message.avatar>
    <c-message.content>
        <c-message.header>Assistant</c-message.header>
        <c-bubble variant="muted">
            <c-bubble.content>How can I help?</c-bubble.content>
        </c-bubble>
        <c-message.footer>Just now</c-message.footer>
    </c-message.content>
</c-message>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add message
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-message>
    <c-message.avatar>
        <c-avatar>
            <c-avatar.fallback>CN</c-avatar.fallback>
        </c-avatar>
    </c-message.avatar>
    <c-message.content>
        <c-message.header>Assistant</c-message.header>
        <c-bubble variant="muted">
            <c-bubble.content>How can I help?</c-bubble.content>
        </c-bubble>
        <c-message.footer>Just now</c-message.footer>
    </c-message.content>
</c-message>
```

:::en
`message` is layout and nothing else. It decides which side the row sits on and
where the avatar, the header and the footer go; what fills the middle is up to
you. In a chat that is usually a [Bubble]({% url 'page' slug='bubble' %}), but a card, a table or
a plain paragraph all work.

## Examples

### Alignment

`align="end"` flips the row, and everything inside follows: the content moves to
the far side, the footer aligns with it, and the avatar changes sides.
:::pt-br
`message` é layout e mais nada. Ele decide de que lado a linha fica e onde vão o
avatar, o cabeçalho e o rodapé; o que preenche o meio fica a seu critério. Num
chat costuma ser um [Bubble]({% url 'page' slug='bubble' %}), mas um card, uma
tabela ou um parágrafo simples também funcionam.

## Exemplos

### Alinhamento

`align="end"` inverte a linha, e tudo dentro dela acompanha: o conteúdo vai para
o lado oposto, o rodapé se alinha com ele e o avatar troca de lado.
:::

<c-docs.example>
<c-message.group class="w-full max-w-md text-start">
  <c-message>
    <c-message.avatar>
      <c-avatar>
        <c-avatar.fallback>AI</c-avatar.fallback>
      </c-avatar>
    </c-message.avatar>
    <c-message.content>
      <c-bubble variant="muted">
        <c-bubble.content>Starts on the left.</c-bubble.content>
      </c-bubble>
    </c-message.content>
  </c-message>
  <c-message align="end">
    <c-message.avatar>
      <c-avatar>
        <c-avatar.fallback>ME</c-avatar.fallback>
      </c-avatar>
    </c-message.avatar>
    <c-message.content>
      <c-bubble align="end">
        <c-bubble.content>Ends on the right.</c-bubble.content>
      </c-bubble>
    </c-message.content>
  </c-message>
</c-message.group>
</c-docs.example>

:::en
### Grouped

`group` stacks a run from the same sender. Give the avatar to the last message
of the run and leave it off the others, so the run reads as one turn.
:::pt-br
### Agrupadas

O `group` empilha uma sequência do mesmo remetente. Dê o avatar à última
mensagem da sequência e deixe-o de fora das outras, para que a sequência seja
lida como uma vez só de falar.
:::

<c-docs.example>
<c-message.group class="w-full max-w-md text-start">
  <c-message align="end">
    <c-message.content>
      <c-bubble align="end">
        <c-bubble.content>Three questions, sorry.</c-bubble.content>
      </c-bubble>
    </c-message.content>
  </c-message>
  <c-message align="end">
    <c-message.content>
      <c-bubble align="end">
        <c-bubble.content>Where does the registry live?</c-bubble.content>
      </c-bubble>
    </c-message.content>
  </c-message>
  <c-message align="end">
    <c-message.avatar>
      <c-avatar>
        <c-avatar.fallback>ME</c-avatar.fallback>
      </c-avatar>
    </c-message.avatar>
    <c-message.content>
      <c-bubble align="end">
        <c-bubble.content>And does <code>add</code> read it?</c-bubble.content>
      </c-bubble>
    </c-message.content>
  </c-message>
</c-message.group>
</c-docs.example>

:::en
### Header and footer

The header names the sender and stays where the reader starts, whatever the
alignment. The footer carries status or actions and follows the message side.
When a footer is present the avatar lifts so it stays level with the message
rather than with the timestamp.
:::pt-br
### Cabeçalho e rodapé

O cabeçalho dá o nome de quem envia e fica onde o leitor começa, qualquer que
seja o alinhamento. O rodapé leva status ou ações e acompanha o lado da
mensagem. Quando há rodapé, o avatar sobe para ficar no nível da mensagem e não
no do horário.
:::

<c-docs.example>
<c-message.group class="w-full max-w-md text-start">
  <c-message>
    <c-message.avatar>
      <c-avatar>
        <c-avatar.fallback>AI</c-avatar.fallback>
      </c-avatar>
    </c-message.avatar>
    <c-message.content>
      <c-message.header>Assistant</c-message.header>
      <c-bubble variant="muted">
        <c-bubble.content>Both edges of a message are yours to fill.</c-bubble.content>
      </c-bubble>
      <c-message.footer>Delivered · 09:41</c-message.footer>
    </c-message.content>
  </c-message>
</c-message.group>
</c-docs.example>

:::en
### Avatar

The avatar sits beside the content, on the side the message comes from.
:::pt-br
### Avatar

O avatar fica ao lado do conteúdo, do lado de onde a mensagem vem.
:::

<c-docs.example>
<c-message class="max-w-md text-start">
  <c-message.avatar>
    <c-avatar><c-avatar.fallback>MM</c-avatar.fallback></c-avatar>
  </c-message.avatar>
  <c-message.content>
    <c-bubble variant="muted">
      <c-bubble.content>Is the release out?</c-bubble.content>
    </c-bubble>
  </c-message.content>
</c-message>
</c-docs.example>

:::en
### Actions

Buttons in the footer act on the message. Label the ones with only an icon.
:::pt-br
### Ações

Botões no rodapé agem sobre a mensagem. Rotule os que têm só ícone.
:::

<c-docs.example>
<c-message class="max-w-md text-start">
  <c-message.content>
    <c-bubble variant="muted">
      <c-bubble.content>Version 1.11.0 is on PyPI.</c-bubble.content>
    </c-bubble>
    <c-message.footer>
      <c-button variant="ghost" size="icon" class="size-7" aria-label="Copy message">
        <c-icon name="copy" />
      </c-button>
    </c-message.footer>
  </c-message.content>
</c-message>
</c-docs.example>

:::en
### Attachment
:::pt-br
### Anexo
:::

<c-docs.example>
<c-message align="end" class="max-w-md text-start">
  <c-message.content>
    <c-attachment size="sm">
      <c-attachment.media><c-icon name="check" /></c-attachment.media>
      <c-attachment.content>
        <c-attachment.title>report.pdf</c-attachment.title>
        <c-attachment.description>PDF · 2.1 MB</c-attachment.description>
      </c-attachment.content>
    </c-attachment>
  </c-message.content>
</c-message>
</c-docs.example>

:::en
## RTL

`align` is logical: `start` is the reader's side of the line and `end` the far
side, so under `dir="rtl"` a conversation mirrors, avatars and footers
included.

## Accessibility

**Label icon-only actions.** An action under a message with only an icon
needs an `aria-label`, such as "Copy message".

**Status updates.** "Sent" or "Read" in a footer is plain text. When it
changes after the page loads, put it in an element with `aria-live="polite"`
so the change is announced.

Who sent a message is shown by its side, which a screen reader does not hear:
put the sender's name in the header.

## API reference
:::pt-br
## RTL

O `align` é lógico: `start` é o lado do leitor na linha e `end` o lado
oposto, então sob `dir="rtl"` uma conversa espelha, avatares e rodapés
incluídos.

## Acessibilidade

**Rotule as ações só com ícone.** Uma ação embaixo de uma mensagem só com
ícone precisa de um `aria-label`, como "Copiar mensagem".

**Atualizações de status.** "Enviada" ou "Lida" num rodapé é texto simples.
Quando muda depois de a página carregar, ponha num elemento com
`aria-live="polite"` para a mudança ser anunciada.

Quem enviou uma mensagem aparece pelo lado, o que um leitor de tela não ouve:
ponha o nome de quem enviou no cabeçalho.

## Referência da API
:::

<c-docs.api-reference name="message" />
