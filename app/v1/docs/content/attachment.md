---
title: Attachment
description: A file inside a message, with its preview, its metadata, its upload state and its own actions.
description.pt-br: Um arquivo dentro de uma mensagem, com prévia, metadados, estado de envio e ações próprias.
description.es: Un archivo dentro de un mensaje, con vista previa, metadatos, estado de subida y acciones propias.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="flex w-full max-w-md flex-col gap-4 text-start">
<c-attachment>
<c-attachment.media variant="image">
<img src="https://github.com/mmaachado.png" alt="">
</c-attachment.media>
<c-attachment.content>
<c-attachment.title>avatar.png</c-attachment.title>
<c-attachment.description>PNG · 84 KB</c-attachment.description>
</c-attachment.content>
<c-attachment.actions>
<c-attachment.action aria-label="Remove avatar.png">
<c-icon name="x" />
</c-attachment.action>
</c-attachment.actions>
</c-attachment>
<c-attachment state="uploading">
<c-attachment.media>
<c-icon name="loader-circle" class="animate-spin" />
</c-attachment.media>
<c-attachment.content>
<c-attachment.title>report.pdf</c-attachment.title>
<c-attachment.description>Uploading · 2.1 MB</c-attachment.description>
</c-attachment.content>
</c-attachment>
</div>
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add attachment
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-attachment>
    <c-attachment.media variant="image">
        <img src="{{ file.url }}" alt="">
    </c-attachment.media>
    <c-attachment.content>
        <c-attachment.title>{{ file.name }}</c-attachment.title>
        <c-attachment.description>{{ file.type }} · {{ file.size }}</c-attachment.description>
    </c-attachment.content>
    <c-attachment.actions>
        <c-attachment.action aria-label="Remove">
            <c-icon name="x" />
        </c-attachment.action>
    </c-attachment.actions>
</c-attachment>
```

:::en
The card is presentational. Nothing here uploads a file or tracks progress — you
set `state` from whatever already knows, and the card follows.

## States

Five, and each one changes more than a label: `idle` dashes the border,
`uploading` and `processing` shimmer the title, `error` turns the border and
the media red.
:::pt-br
O card é só apresentação. Nada aqui envia um arquivo ou acompanha o progresso —
você define `state` a partir do que já sabe disso, e o card acompanha.

## Estados

São cinco, e cada um muda mais do que um rótulo: `idle` deixa a borda
tracejada, `uploading` e `processing` fazem o título cintilar, `error` deixa a
borda e a mídia vermelhas.
:::

<c-docs.example>
<div class="flex w-full max-w-md flex-col gap-4 text-start">
  <c-attachment state="idle">
    <c-attachment.media>
      <c-icon name="circle" />
    </c-attachment.media>
    <c-attachment.content>
      <c-attachment.title>Drop a file here</c-attachment.title>
      <c-attachment.description>Nothing chosen yet</c-attachment.description>
    </c-attachment.content>
  </c-attachment>
  <c-attachment state="uploading">
    <c-attachment.media>
      <c-icon name="loader-circle" class="animate-spin" />
    </c-attachment.media>
    <c-attachment.content>
      <c-attachment.title>report.pdf</c-attachment.title>
      <c-attachment.description>Uploading · 2.1 MB</c-attachment.description>
    </c-attachment.content>
  </c-attachment>
  <c-attachment state="processing">
    <c-attachment.media>
      <c-icon name="loader-circle" class="animate-spin" />
    </c-attachment.media>
    <c-attachment.content>
      <c-attachment.title>recording.wav</c-attachment.title>
      <c-attachment.description>Transcribing</c-attachment.description>
    </c-attachment.content>
  </c-attachment>
  <c-attachment state="error">
    <c-attachment.media>
      <c-icon name="x" />
    </c-attachment.media>
    <c-attachment.content>
      <c-attachment.title>archive.zip</c-attachment.title>
      <c-attachment.description>Too large, 40 MB over the limit</c-attachment.description>
    </c-attachment.content>
  </c-attachment>
  <c-attachment state="done">
    <c-attachment.media>
      <c-icon name="check" />
    </c-attachment.media>
    <c-attachment.content>
      <c-attachment.title>notes.md</c-attachment.title>
      <c-attachment.description>Markdown · 4 KB</c-attachment.description>
    </c-attachment.content>
  </c-attachment>
</div>
</c-docs.example>

:::en
The shimmer on the title is the `shimmer` utility from `input.css`. It stops
by itself when the reader has asked for reduced motion.

## Sizes and orientation

`size` takes `default`, `sm` and `xs`. `orientation="vertical"` turns the card
into a tile, with the media on top and the actions floating over its corner.
:::pt-br
O brilho no título é o utilitário `shimmer` do `input.css`. Ele para sozinho
quando o leitor pediu menos movimento.

## Tamanhos e orientação

`size` aceita `default`, `sm` e `xs`. `orientation="vertical"` transforma o card
em um bloco, com a mídia em cima e as ações flutuando sobre o canto dela.
:::

<c-docs.example>
<div class="flex w-full max-w-md flex-col gap-4 text-start">
  <c-attachment size="sm">
    <c-attachment.media>
      <c-icon name="check" />
    </c-attachment.media>
    <c-attachment.content>
      <c-attachment.title>small.txt</c-attachment.title>
      <c-attachment.description>Text · 1 KB</c-attachment.description>
    </c-attachment.content>
  </c-attachment>
  <c-attachment size="xs">
    <c-attachment.media>
      <c-icon name="check" />
    </c-attachment.media>
    <c-attachment.content>
      <c-attachment.title>tiny.txt</c-attachment.title>
    </c-attachment.content>
  </c-attachment>
  <c-attachment orientation="vertical">
    <c-attachment.media variant="image">
      <img src="https://github.com/mmaachado.png" alt="">
    </c-attachment.media>
    <c-attachment.content>
      <c-attachment.title>avatar.png</c-attachment.title>
      <c-attachment.description>84 KB</c-attachment.description>
    </c-attachment.content>
    <c-attachment.actions>
      <c-attachment.action aria-label="Remove avatar.png">
        <c-icon name="x" />
      </c-attachment.action>
    </c-attachment.actions>
  </c-attachment>
</div>
</c-docs.example>

:::en
## Examples

### A card that opens the file

`trigger` covers the whole card, so the card itself is the target. It sits
behind the actions on purpose: the remove button keeps its own click and its
own tab stop, and neither swallows the other.
:::pt-br
## Exemplos

### Um card que abre o arquivo

O `trigger` cobre o card inteiro, então o próprio card é o alvo. Ele fica atrás
das ações de propósito: o botão de remover mantém o próprio clique e a própria
parada de tab, e nenhum dos dois engole o outro.
:::

<c-docs.example>
<div class="flex w-full max-w-md flex-col gap-4 text-start">
  <c-attachment>
    <c-attachment.media variant="image">
      <img src="https://github.com/mmaachado.png" alt="">
    </c-attachment.media>
    <c-attachment.content>
      <c-attachment.title>avatar.png</c-attachment.title>
      <c-attachment.description>PNG · 84 KB</c-attachment.description>
    </c-attachment.content>
    <c-attachment.actions>
      <c-attachment.action aria-label="Remove avatar.png">
        <c-icon name="x" />
      </c-attachment.action>
    </c-attachment.actions>
    <c-attachment.trigger tag="a" href="https://github.com/mmaachado.png" aria-label="Open avatar.png"></c-attachment.trigger>
  </c-attachment>
</div>
</c-docs.example>

:::en
The trigger has no text of its own, so it needs an `aria-label`. Without one it
is an unlabelled control covering the entire card.

Leave `tag` off and it renders a `button` with `type="button"`, for a card that
opens a preview instead of navigating.

### A row of files

`group` scrolls sideways, snaps each card into place and fades the edge you have
scrolled away from.
:::pt-br
O trigger não tem texto próprio, então precisa de um `aria-label`. Sem ele, é
um controle sem rótulo cobrindo o card inteiro.

Sem `tag`, ele renderiza um `button` com `type="button"`, para um card que abre
uma pré-visualização em vez de navegar.

### Uma fileira de arquivos

O `group` rola para o lado, encaixa cada card no lugar e esmaece a borda da qual
você rolou para longe.
:::

<c-docs.example>
<c-attachment.group class="w-full max-w-md">
  <c-attachment orientation="vertical">
    <c-attachment.media variant="image">
      <img src="https://github.com/mmaachado.png" alt="">
    </c-attachment.media>
    <c-attachment.content>
      <c-attachment.title>one.png</c-attachment.title>
    </c-attachment.content>
  </c-attachment>
  <c-attachment orientation="vertical">
    <c-attachment.media variant="image">
      <img src="https://github.com/mmaachado.png" alt="">
    </c-attachment.media>
    <c-attachment.content>
      <c-attachment.title>two.png</c-attachment.title>
    </c-attachment.content>
  </c-attachment>
  <c-attachment orientation="vertical">
    <c-attachment.media variant="image">
      <img src="https://github.com/mmaachado.png" alt="">
    </c-attachment.media>
    <c-attachment.content>
      <c-attachment.title>three.png</c-attachment.title>
    </c-attachment.content>
  </c-attachment>
  <c-attachment orientation="vertical">
    <c-attachment.media variant="image">
      <img src="https://github.com/mmaachado.png" alt="">
    </c-attachment.media>
    <c-attachment.content>
      <c-attachment.title>four.png</c-attachment.title>
    </c-attachment.content>
  </c-attachment>
</c-attachment.group>
</c-docs.example>

:::en
The scroll, the snapping and the fade are all CSS. There is no JavaScript in
this component.

### Inside a message
:::pt-br
A rolagem, o encaixe e o esmaecimento são todos CSS. Não há JavaScript neste
componente.

### Dentro de uma mensagem
:::

<c-docs.demo-section>
<c-message.group class="w-full max-w-md text-start">
<c-message align="end">
<c-message.content>
<c-attachment size="sm">
<c-attachment.media variant="image">
<img src="https://github.com/mmaachado.png" alt="">
</c-attachment.media>
<c-attachment.content>
<c-attachment.title>avatar.png</c-attachment.title>
<c-attachment.description>PNG · 84 KB</c-attachment.description>
</c-attachment.content>
</c-attachment>
<c-bubble align="end">
<c-bubble.content>Here is the file you asked for.</c-bubble.content>
</c-bubble>
</c-message.content>
</c-message>
</c-message.group>
</c-docs.demo-section>
