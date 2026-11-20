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

<c-docs.cheat-sheet name="attachment">
<c-attachment>
  <c-attachment.media>
    <c-icon name="check" />
  </c-attachment.media>
  <c-attachment.content>
    <c-attachment.title>{{ document.file.name }}</c-attachment.title>
    <c-attachment.description>{{ document.file.size|filesizeformat }}</c-attachment.description>
  </c-attachment.content>
</c-attachment>
</c-docs.cheat-sheet>

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

The card is presentational. Nothing here uploads a file or tracks progress:
you set `state` from whatever already knows, and the card follows. With a
`FileField`, the name, the URL and the size are all on the field. The card is
markup and CSS only, so it renders the same without JavaScript.
:::pt-br
## Uso

O card é só apresentação. Nada aqui envia um arquivo ou acompanha o progresso:
você define `state` a partir do que já sabe disso, e o card acompanha. Com um
`FileField`, o nome, a URL e o tamanho estão todos no campo. O card é só markup
e CSS, então renderiza igual sem JavaScript.
:::

```html
{% for document in message.documents.all %}
  <c-attachment state="{{ document.state }}">
    <c-attachment.media>
      <c-icon name="check" />
    </c-attachment.media>
    <c-attachment.content>
      <c-attachment.title>{{ document.file.name }}</c-attachment.title>
      <c-attachment.description>{{ document.file.size|filesizeformat }}</c-attachment.description>
    </c-attachment.content>
    <c-attachment.trigger tag="a" href="{{ document.file.url }}" aria-label="Open {{ document.file.name }}"></c-attachment.trigger>
  </c-attachment>
{% endfor %}
```

:::en
## Examples

### Image

`media` holds an icon by default. `variant="image"` fits a picture to the
square instead, and dims it until the upload is done.
:::pt-br
## Exemplos

### Imagem

O `media` guarda um ícone por padrão. `variant="image"` encaixa uma imagem no
quadrado, e a esmaece até o envio terminar.
:::

<c-docs.example>
<c-attachment class="max-w-md text-start">
  <c-attachment.media variant="image">
    <img src="https://github.com/mmaachado.png" alt="">
  </c-attachment.media>
  <c-attachment.content>
    <c-attachment.title>avatar.png</c-attachment.title>
    <c-attachment.description>PNG · 84 KB</c-attachment.description>
  </c-attachment.content>
</c-attachment>
</c-docs.example>

:::en
### States

Five, and each changes more than a label: `idle` dashes the border, `uploading`
and `processing` shimmer the title, `error` turns the border and the media red,
and `done` is the default.
:::pt-br
### Estados

São cinco, e cada um muda mais do que um rótulo: `idle` deixa a borda
tracejada, `uploading` e `processing` fazem o título cintilar, `error` deixa a
borda e a mídia vermelhas, e `done` é o padrão.
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
The shimmer is the `shimmer` utility from `input.css`, and it stops by itself
when the reader has asked for reduced motion.

### Sizes

`size` takes `default`, `sm` and `xs`. `orientation="vertical"` turns the card
into a tile, with the media on top and the actions floating over its corner.
:::pt-br
O brilho é o utilitário `shimmer` do `input.css`, e ele para sozinho quando o
leitor pediu menos movimento.

### Tamanhos

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
### Group

`group` scrolls sideways, snaps each card into place and fades the edge you
have scrolled away from, all in CSS.
:::pt-br
### Grupo

O `group` rola para o lado, encaixa cada card no lugar e esmaece a borda da
qual você rolou para longe, tudo em CSS.
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
### Trigger

`trigger` covers the whole card, so the card itself is the target. It sits
behind the actions on purpose: the remove button keeps its own click and its
own tab stop. Leave `tag` off for a `button` with `type="button"`, to open a
preview instead of navigating.
:::pt-br
### Trigger

O `trigger` cobre o card inteiro, então o próprio card é o alvo. Ele fica atrás
das ações de propósito: o botão de remover mantém o próprio clique e a própria
parada de tab. Sem `tag`, ele é um `button` com `type="button"`, para abrir uma
pré-visualização em vez de navegar.
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
### Inside a message
:::pt-br
### Dentro de uma mensagem
:::

<c-docs.example>
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
</c-docs.example>

:::en
## RTL

The media sits at the start of the card and the actions at its end, so under
`dir="rtl"` they change sides with the text. A group scrolls the other way, and
its fade follows the edge you scroll away from.

## Accessibility

**Label icon-only actions.** An action that holds only an icon needs an
`aria-label` that names the file too, such as "Remove avatar.png", so a list of
them is not a row of identical "Remove" buttons.

**Label the trigger.** The trigger has no text of its own. Without an
`aria-label` it is an unlabelled control covering the whole card.

**Keyboard scrolling.** A group hides its scrollbar and is not focusable, so
when its cards hold nothing focusable a keyboard cannot scroll it. Give it
`tabindex="0"`, `role="region"` and an `aria-label` then.

**Meaning beyond colour.** The red of `error` and the dashed `idle` border are
not read out. Put the state in the description too, as the examples do.

## API reference
:::pt-br
## RTL

A mídia fica no início do card e as ações no fim, então sob `dir="rtl"` elas
trocam de lado com o texto. Um grupo rola para o outro lado, e o esmaecimento
acompanha a borda da qual você rola para longe.

## Acessibilidade

**Rotule as ações só com ícone.** Uma ação que guarda só um ícone precisa de um
`aria-label` que também dê o nome do arquivo, como "Remove avatar.png", para que
uma lista delas não vire uma fileira de botões "Remove" iguais.

**Rotule o trigger.** O trigger não tem texto próprio. Sem um `aria-label`, ele
é um controle sem rótulo cobrindo o card inteiro.

**Rolagem pelo teclado.** Um grupo esconde a barra de rolagem e não recebe
foco, então quando os cards não têm nada focável o teclado não consegue rolá-lo.
Dê a ele `tabindex="0"`, `role="region"` e um `aria-label` nesse caso.

**Significado além da cor.** O vermelho de `error` e a borda tracejada de
`idle` não são lidos. Ponha o estado na descrição também, como fazem os
exemplos.

## Referência da API
:::

<c-docs.api-reference name="attachment" />
