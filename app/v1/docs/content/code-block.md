---
title: Code Block
description: Code, terminal output and diffs, with an optional header, line numbers and a copy button.
description.pt-br: Código, saída de terminal e diffs, com cabeçalho opcional, números de linha e um botão de copiar.
description.es: Código, salida de terminal y diffs, con cabecera opcional, números de línea y un botón de copiar.
---

<c-docs.demo-section class="min-h-[350px]">
<c-code-block class="max-w-xl">
<c-code-block.header>
<c-code-block.title>views.py</c-code-block.title>
<c-code-block.actions>
<c-code-block.copy-button />
</c-code-block.actions>
</c-code-block.header>
<c-code-block.content line_numbers="true">
<c-code-block.line>from django.shortcuts import render</c-code-block.line>
<c-code-block.line></c-code-block.line>
<c-code-block.line></c-code-block.line>
<c-code-block.line>def dashboard(request):</c-code-block.line>
<c-code-block.line variant="highlighted">    orders = Order.objects.recent()[:5]</c-code-block.line>
<c-code-block.line>    return render(request, "dashboard.html", {"orders": orders})</c-code-block.line>
</c-code-block.content>
</c-code-block>
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add code_block
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-code-block>
  <c-code-block.header>
    <c-code-block.title>views.py</c-code-block.title>
    <c-code-block.actions>
      <c-code-block.copy-button />
    </c-code-block.actions>
  </c-code-block.header>
  <c-code-block.content line_numbers="true">
    <c-code-block.line>def dashboard(request):</c-code-block.line>
    <c-code-block.line>    return render(request, "dashboard.html")</c-code-block.line>
  </c-code-block.content>
</c-code-block>
```

:::en
The content is a `<pre>`, so whatever sits inside a line shows exactly as
written, spaces included. Keep each line's text flush against its tags, and
escape `<` and `&` the way any HTML needs, or pass the code through Django's
autoescaping from a variable.

There is no syntax highlighting, as upstream ships none either.

## Lines

Upstream splits a string into lines when line numbers are on. A template
cannot, so with `line_numbers="true"` each line is a `<c-code-block.line>`.
Without numbers, plain text in `<c-code-block.content>` is enough, as in the
terminal example below.

An empty `<c-code-block.line>` holds a newline, so copying a selection keeps the
blank lines. `start_line` sets the first number.

## Copying

`<c-code-block.copy-button>` copies `value` when you give it one, and otherwise
the text of the block's content, so the code is not written twice. It shows a
check for two seconds afterwards and announces "Copied" to a screen reader.
`label` and `copied_label` translate both.

Inside the header the actions sit at its end. Put
`<c-code-block.actions>` straight inside the block instead and they float over
its top corner, showing on hover and on focus, and always on a touch screen.

## Examples

### Terminal
:::pt-br
O conteúdo é um `<pre>`, então o que estiver dentro de uma linha aparece
exatamente como foi escrito, espaços incluídos. Mantenha o texto de cada linha
encostado nas tags, e escape `<` e `&` como qualquer HTML pede, ou passe o
código pelo autoescape do Django a partir de uma variável.

Não há realce de sintaxe, já que o upstream também não traz nenhum.

## Linhas

O upstream divide uma string em linhas quando os números estão ligados. Um
template não consegue, então com `line_numbers="true"` cada linha é um
`<c-code-block.line>`. Sem números, texto simples no `<c-code-block.content>`
basta, como no exemplo de terminal abaixo.

Um `<c-code-block.line>` vazio guarda uma quebra de linha, para que copiar uma
seleção mantenha as linhas em branco. `start_line` define o primeiro número.

## Copiando

O `<c-code-block.copy-button>` copia `value` quando você passa um, e senão o
texto do conteúdo do bloco, para que o código não seja escrito duas vezes.
Depois ele mostra um check por dois segundos e anuncia "Copied" a um leitor de
tela. `label` e `copied_label` traduzem os dois.

Dentro do cabeçalho as ações ficam no fim dele. Ponha o
`<c-code-block.actions>` direto dentro do bloco e elas flutuam sobre o canto de
cima, aparecendo no hover e no foco, e sempre numa tela de toque.

## Exemplos

### Terminal
:::

<c-docs.demo-section>
<c-code-block class="max-w-xl">
<c-code-block.actions>
<c-code-block.copy-button />
</c-code-block.actions>
<c-code-block.content>uvx django_shadcn@latest add code_block</c-code-block.content>
</c-code-block>
</c-docs.demo-section>

```html
<c-code-block>
  <c-code-block.actions>
    <c-code-block.copy-button />
  </c-code-block.actions>
  <c-code-block.content>uvx django_shadcn@latest add code_block</c-code-block.content>
</c-code-block>
```

:::en
### Diff

`added` and `removed` mark the line in the gutter, and `highlighted` only
shades it.
:::pt-br
### Diff

`added` e `removed` marcam a linha na margem, e `highlighted` só a sombreia.
:::

<c-docs.demo-section>
<c-code-block class="max-w-xl">
<c-code-block.content line_numbers="true" start_line="12">
<c-code-block.line>    'calendar': Component(depends=('button', 'icon')),</c-code-block.line>
<c-code-block.line variant="removed">    'card': Component(),</c-code-block.line>
<c-code-block.line variant="added">    'card': Component(depends=('separator',)),</c-code-block.line>
<c-code-block.line variant="added">    'code_block': Component(depends=('icon',)),</c-code-block.line>
<c-code-block.line>    'collapsible': Component(scripts=(COLLAPSE,)),</c-code-block.line>
</c-code-block.content>
</c-code-block>
</c-docs.demo-section>

```html
<c-code-block.content line_numbers="true" start_line="12">
  <c-code-block.line variant="removed">    'card': Component(),</c-code-block.line>
  <c-code-block.line variant="added">    'card': Component(depends=('separator',)),</c-code-block.line>
</c-code-block.content>
```

:::en
### Destructive
:::pt-br
### Destructive
:::

<c-docs.demo-section>
<c-code-block variant="destructive" class="max-w-xl">
<c-code-block.header>
<c-code-block.title>TemplateSyntaxError</c-code-block.title>
</c-code-block.header>
<c-code-block.content wrap="true">Unclosed tag on line 4: 'if'. Looking for one of: elif, else, endif.</c-code-block.content>
</c-code-block>
</c-docs.demo-section>

```html
<c-code-block variant="destructive">
  <c-code-block.header>
    <c-code-block.title>TemplateSyntaxError</c-code-block.title>
  </c-code-block.header>
  <c-code-block.content wrap="true">Unclosed tag on line 4: 'if'.</c-code-block.content>
</c-code-block>
```

:::en
`wrap="true"` breaks long lines instead of scrolling sideways.

### Small

`size="sm"` tightens the padding and the type, for a block inside a message or
a card.
:::pt-br
`wrap="true"` quebra as linhas longas em vez de rolar para o lado.

### Pequeno

`size="sm"` aperta o espaçamento e o texto, para um bloco dentro de uma
mensagem ou de um card.
:::

<c-docs.demo-section>
<c-code-block size="sm" class="max-w-md">
<c-code-block.header>
<c-code-block.title>requirements.txt</c-code-block.title>
<c-code-block.actions>
<c-code-block.copy-button />
</c-code-block.actions>
</c-code-block.header>
<c-code-block.content>django-cotton>=2.7.1</c-code-block.content>
</c-code-block>
</c-docs.demo-section>

```html
<c-code-block size="sm">...</c-code-block>
```

:::en
## Props

| Prop | Where | Default | Meaning |
| --- | --- | --- | --- |
| `variant` | `<c-code-block>` | `default` | `default` or `destructive` |
| `size` | `<c-code-block>` | `default` | `default` or `sm` |
| `line_numbers` | `.content` | `false` | number the lines; write them as `.line` parts |
| `start_line` | `.content` | `1` | the first number |
| `wrap` | `.content` | `false` | break long lines instead of scrolling |
| `variant` | `.line` | `default` | `default`, `added`, `removed` or `highlighted` |
| `value` | `.copy-button` | — | what to copy; the content's text when left out |
| `label` | `.copy-button` | `Copy` | the button's name before copying |
| `copied_label` | `.copy-button` | `Copied` | its name, and the announcement, after |

## Notes

The content is always `dir="ltr"` and start-aligned, so code stays readable on
a right-to-left page.

Upstream writes its classes as `cn-*` names resolved by a style file. The
registry the rest of this library follows has no code block, so the utilities
here come from the style closest to it.
:::pt-br
## Props

| Prop | Onde | Padrão | Significado |
| --- | --- | --- | --- |
| `variant` | `<c-code-block>` | `default` | `default` ou `destructive` |
| `size` | `<c-code-block>` | `default` | `default` ou `sm` |
| `line_numbers` | `.content` | `false` | numera as linhas; escreva-as como partes `.line` |
| `start_line` | `.content` | `1` | o primeiro número |
| `wrap` | `.content` | `false` | quebra as linhas longas em vez de rolar |
| `variant` | `.line` | `default` | `default`, `added`, `removed` ou `highlighted` |
| `value` | `.copy-button` | — | o que copiar; o texto do conteúdo quando omitido |
| `label` | `.copy-button` | `Copy` | o nome do botão antes de copiar |
| `copied_label` | `.copy-button` | `Copied` | o nome dele, e o anúncio, depois |

## Observações

O conteúdo é sempre `dir="ltr"` e alinhado ao início, então o código continua
legível numa página da direita para a esquerda.

O upstream escreve as classes como nomes `cn-*` resolvidos por um arquivo de
estilo. O registry que o resto desta biblioteca segue não tem code block, então
os utilitários daqui vêm do estilo mais próximo dele.
:::
