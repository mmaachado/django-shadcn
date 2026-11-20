---
title: Avatar
description: An image element with a fallback for representing the user.
description.pt-br: Uma imagem com fallback para representar o usuário.
description.es: Una imagen con alternativa para representar al usuario.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="flex items-center gap-4">
<c-avatar>
<c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
<c-avatar.fallback>MM</c-avatar.fallback>
</c-avatar>
<c-avatar>
<c-avatar.fallback>CN</c-avatar.fallback>
</c-avatar>
</div>
</c-docs.demo-section>

<c-docs.cheat-sheet name="avatar">
<c-avatar>
  <c-avatar.image src="{{ user.profile.photo.url }}" alt="{{ user.get_full_name }}" />
  <c-avatar.fallback>{{ user.first_name|first }}{{ user.last_name|first }}</c-avatar.fallback>
</c-avatar>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add avatar
```

:::en
## Usage

Radix hides the fallback once the image loads. Here the image is stacked on
top of the fallback instead, and removes itself on `error` so the initials show
through. Both are always in the markup, which suits a template: render the
fallback from the user's name every time, and the photo only when there is one.

The removal on `error` is one Alpine attribute on the image, with its own
`x-data`. Without Alpine the avatar still works, but a broken source leaves the
browser's broken-image glyph over the initials.
:::pt-br
## Uso

O Radix esconde o fallback quando a imagem carrega. Aqui a imagem fica
empilhada sobre o fallback, e se remove no `error` para que as iniciais
apareçam por baixo. Os dois estão sempre no markup, o que combina com um
template: renderize o fallback a partir do nome do usuário sempre, e a foto só
quando houver uma.

A remoção no `error` é um atributo do Alpine na imagem, com o próprio `x-data`.
Sem o Alpine o avatar continua funcionando, mas uma origem quebrada deixa o
ícone de imagem quebrada do navegador por cima das iniciais.
:::

```html
<c-avatar>
  {% if user.profile.photo %}
    <c-avatar.image src="{{ user.profile.photo.url }}" alt="" />
  {% endif %}
  <c-avatar.fallback>{{ user.first_name|first }}{{ user.last_name|first }}</c-avatar.fallback>
</c-avatar>
```

:::en
## Examples

### Basic
:::pt-br
## Exemplos

### Básico
:::

<c-docs.example>
<c-avatar>
  <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
  <c-avatar.fallback>MM</c-avatar.fallback>
</c-avatar>
</c-docs.example>

:::en
### Badge

`badge` is a dot on the corner, for presence or a count.
:::pt-br
### Badge

O `badge` é um ponto no canto, para presença ou para uma contagem.
:::

<c-docs.example>
<div class="flex items-center gap-4">
  <c-avatar>
    <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
    <c-avatar.fallback>MM</c-avatar.fallback>
    <c-avatar.badge class="bg-emerald-500!" />
  </c-avatar>
  <c-avatar size="lg">
    <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
    <c-avatar.fallback>MM</c-avatar.fallback>
    <c-avatar.badge class="bg-emerald-500!" />
  </c-avatar>
</div>
</c-docs.example>

:::en
### Badge with an icon

An icon inside the badge is sized to the avatar, and hidden on the small one,
where there is no room.
:::pt-br
### Badge com ícone

Um ícone dentro do badge é dimensionado conforme o avatar, e escondido no
pequeno, onde não cabe.
:::

<c-docs.example>
<c-avatar size="lg">
  <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
  <c-avatar.fallback>MM</c-avatar.fallback>
  <c-avatar.badge class="bg-emerald-500!">
    <c-icon name="check" />
  </c-avatar.badge>
</c-avatar>
</c-docs.example>

:::en
### Avatar group

`group` overlaps the avatars and rings each one in the background colour, and
`group-count` closes the row with how many more there are.
:::pt-br
### Grupo de avatares

O `group` sobrepõe os avatares e contorna cada um com a cor de fundo, e o
`group-count` fecha a fileira com quantos mais existem.
:::

<c-docs.example>
<c-avatar.group>
  <c-avatar>
    <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
    <c-avatar.fallback>MM</c-avatar.fallback>
  </c-avatar>
  <c-avatar>
    <c-avatar.image src="https://github.com/SarthakJariwala.png" alt="@SarthakJariwala" />
    <c-avatar.fallback>SJ</c-avatar.fallback>
  </c-avatar>
  <c-avatar>
    <c-avatar.image src="https://github.com/shadcn.png" alt="@shadcn" />
    <c-avatar.fallback>SH</c-avatar.fallback>
  </c-avatar>
  <c-avatar.group-count>+3</c-avatar.group-count>
</c-avatar.group>
</c-docs.example>

:::en
### Avatar group with an icon

`group-count` takes an icon instead of a number, for an "add someone" action.
:::pt-br
### Grupo com ícone

O `group-count` aceita um ícone no lugar de um número, para uma ação de
"adicionar alguém".
:::

<c-docs.example>
<c-avatar.group>
  <c-avatar>
    <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
    <c-avatar.fallback>MM</c-avatar.fallback>
  </c-avatar>
  <c-avatar>
    <c-avatar.fallback>CN</c-avatar.fallback>
  </c-avatar>
  <c-avatar.group-count>
    <c-icon name="users" />
  </c-avatar.group-count>
</c-avatar.group>
</c-docs.example>

:::en
### Sizes
:::pt-br
### Tamanhos
:::

<c-docs.example>
<div class="flex items-center gap-4">
  <c-avatar size="sm">
    <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
    <c-avatar.fallback>MM</c-avatar.fallback>
  </c-avatar>
  <c-avatar>
    <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
    <c-avatar.fallback>MM</c-avatar.fallback>
  </c-avatar>
  <c-avatar size="lg">
    <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
    <c-avatar.fallback>MM</c-avatar.fallback>
  </c-avatar>
</div>
</c-docs.example>

:::en
### Fallback

When the image fails, or there is none, the initials show.
:::pt-br
### Fallback

Quando a imagem falha, ou não existe, as iniciais aparecem.
:::

<c-docs.example>
<c-avatar>
  <c-avatar.image src="/does-not-exist.png" alt="" />
  <c-avatar.fallback>CN</c-avatar.fallback>
</c-avatar>
</c-docs.example>

:::en
### Dropdown

An avatar inside a [Dropdown Menu]({% url 'page' slug='dropdown-menu' %})
trigger opens the account menu. Put it in a button, so the trigger can take
focus.
:::pt-br
### Dropdown

Um avatar dentro do trigger de um
[Dropdown Menu]({% url 'page' slug='dropdown-menu' %}) abre o menu da conta.
Ponha-o num botão, para o trigger poder receber foco.
:::

<c-docs.example>
<c-dropdown-menu>
  <c-dropdown-menu.trigger>
    <button type="button" class="rounded-full" aria-label="Account">
      <c-avatar>
        <c-avatar.image src="https://github.com/mmaachado.png" alt="@mmaachado" />
        <c-avatar.fallback>MM</c-avatar.fallback>
      </c-avatar>
    </button>
  </c-dropdown-menu.trigger>
  <c-dropdown-menu.content class="w-40">
    <c-dropdown-menu.item>Profile</c-dropdown-menu.item>
    <c-dropdown-menu.item>Settings</c-dropdown-menu.item>
    <c-dropdown-menu.separator />
    <c-dropdown-menu.item variant="destructive">Log out</c-dropdown-menu.item>
  </c-dropdown-menu.content>
</c-dropdown-menu>
</c-docs.example>

:::en
## RTL

The badge sits on the end corner, so under `dir="rtl"` it moves to the left.
A group overlaps with logical margins, so it stacks the other way.

## Accessibility

The image keeps its `alt`. When a name sits beside the avatar, give the image
an empty `alt=""` so the name is not read twice. The fallback is text and is
read as text, so initials alone are read out letter by letter: pair the avatar
with the full name somewhere. The badge is not announced; say what it means in
words nearby.

## API reference
:::pt-br
## RTL

O badge fica no canto do fim, então sob `dir="rtl"` ele vai para a esquerda.
Um grupo se sobrepõe com margens lógicas, então se empilha para o outro lado.

## Acessibilidade

A imagem mantém o `alt`. Quando um nome fica ao lado do avatar, dê à imagem um
`alt=""` vazio para que o nome não seja lido duas vezes. O fallback é texto e é
lido como texto, então só as iniciais são lidas letra por letra: acompanhe o
avatar do nome completo em algum lugar. O badge não é anunciado; diga o que ele
significa em palavras por perto.

## Referência da API
:::

<c-docs.api-reference name="avatar" />

:::en
## Notes

The badge defaults to `bg-primary`. Colouring it takes the `!` suffix,
`bg-emerald-500!`, because two background utilities on the same element are
decided by their order in the compiled stylesheet, not by the order you wrote
them. The rule holds for any class of yours that collides with one the
component already sets, on every component here.
:::pt-br
## Observações

O badge usa `bg-primary` por padrão. Colori-lo pede o sufixo `!`,
`bg-emerald-500!`, porque dois utilitários de fundo no mesmo elemento são
decididos pela ordem na folha de estilo compilada, não pela ordem em que você
os escreveu. A regra vale para qualquer classe sua que colida com uma que o
componente já define, em todos os componentes daqui.
:::
