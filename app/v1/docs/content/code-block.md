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

<c-docs.cheat-sheet name="code-block">
<c-code-block>
  <c-code-block.header>
    <c-code-block.title>settings.py</c-code-block.title>
    <c-code-block.actions>
      <c-code-block.copy-button />
    </c-code-block.actions>
  </c-code-block.header>
  <c-code-block.content>{{ snippet }}</c-code-block.content>
</c-code-block>
</c-docs.cheat-sheet>

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

The content is a `<pre>`, so what sits inside shows exactly as written, spaces
included. Code from a variable goes through Django's autoescaping, which turns
`<` and `&` into entities and keeps the code safe to show:
:::pt-br
## Uso

O conteúdo é um `<pre>`, então o que estiver dentro aparece exatamente como foi
escrito, espaços incluídos. Código vindo de uma variável passa pelo autoescape
do Django, que transforma `<` e `&` em entidades e mantém o código seguro para
exibir:
:::

```html
<c-code-block>
  <c-code-block.content>{{ example.source }}</c-code-block.content>
</c-code-block>
```

:::en
Upstream splits a string into lines when line numbers are on. A template
cannot, so with `line_numbers="true"` each line is a `<c-code-block.line>`; a
loop over `source.splitlines` writes them. An empty line holds a newline, so
copying a selection keeps the blank lines.

The block itself needs no JavaScript. The copy button does: it copies `value`,
or the content's lines joined by newlines, and shows a check for two seconds.
There is no syntax highlighting, as upstream ships none either.
:::pt-br
O upstream divide uma string em linhas quando os números estão ligados. Um
template não consegue, então com `line_numbers="true"` cada linha é um
`<c-code-block.line>`; um laço sobre `source.splitlines` as escreve. Uma linha
vazia guarda uma quebra de linha, para que copiar uma seleção mantenha as
linhas em branco.

O bloco em si não precisa de JavaScript. O botão de copiar precisa: ele copia o
`value`, ou as linhas do conteúdo unidas por quebras de linha, e mostra um
check por dois segundos. Não há realce de sintaxe, já que o upstream também não
traz nenhum.
:::

```html
<c-code-block.content line_numbers="true">
  {% for line in source.splitlines %}<c-code-block.line>{{ line }}</c-code-block.line>{% endfor %}
</c-code-block.content>
```

:::en
## Examples

### Basic
:::pt-br
## Exemplos

### Básico
:::

<c-docs.example>
<c-code-block class="max-w-xl">
  <c-code-block.content>uvx django_shadcn@latest add code_block</c-code-block.content>
</c-code-block>
</c-docs.example>

:::en
### Header and actions

The header holds a title and, at its end, the actions.
:::pt-br
### Cabeçalho e ações

O cabeçalho guarda um título e, no fim, as ações.
:::

<c-docs.example>
<c-code-block size="sm" class="max-w-md">
  <c-code-block.header>
    <c-code-block.title>requirements.txt</c-code-block.title>
    <c-code-block.actions>
      <c-code-block.copy-button />
    </c-code-block.actions>
  </c-code-block.header>
  <c-code-block.content>django-cotton&gt;=2.7.1</c-code-block.content>
</c-code-block>
</c-docs.example>

:::en
### Floating actions

`actions` placed straight inside the block float over its top corner, showing
on hover and on focus, and always on a touch screen.
:::pt-br
### Ações flutuantes

O `actions` posto direto dentro do bloco flutua sobre o canto de cima,
aparecendo no hover e no foco, e sempre numa tela de toque.
:::

<c-docs.example>
<c-code-block class="max-w-xl">
  <c-code-block.actions>
    <c-code-block.copy-button />
  </c-code-block.actions>
  <c-code-block.content>python manage.py migrate</c-code-block.content>
</c-code-block>
</c-docs.example>

:::en
### Line numbers and highlighted lines

`highlighted` shades a line without marking it in the gutter.
:::pt-br
### Números de linha e linhas realçadas

O `highlighted` sombreia uma linha sem marcá-la na margem.
:::

<c-docs.example>
<c-code-block class="max-w-xl">
  <c-code-block.content line_numbers="true">
    <c-code-block.line>INSTALLED_APPS = [</c-code-block.line>
    <c-code-block.line>    "django.contrib.admin",</c-code-block.line>
    <c-code-block.line variant="highlighted">    "django_cotton",</c-code-block.line>
    <c-code-block.line>]</c-code-block.line>
  </c-code-block.content>
</c-code-block>
</c-docs.example>

:::en
### Start line and diff

`start_line` sets the first number, and `added` and `removed` mark a line in
the gutter.
:::pt-br
### Linha inicial e diff

O `start_line` define o primeiro número, e `added` e `removed` marcam uma linha
na margem.
:::

<c-docs.example>
<c-code-block class="max-w-xl">
  <c-code-block.content line_numbers="true" start_line="12">
    <c-code-block.line>    'calendar': Component(depends=('button', 'icon')),</c-code-block.line>
    <c-code-block.line variant="removed">    'card': Component(),</c-code-block.line>
    <c-code-block.line variant="added">    'card': Component(depends=('separator',)),</c-code-block.line>
    <c-code-block.line>    'collapsible': Component(scripts=(COLLAPSE,)),</c-code-block.line>
  </c-code-block.content>
</c-code-block>
</c-docs.example>

:::en
### Wrap

`wrap="true"` breaks long lines instead of scrolling sideways.
:::pt-br
### Quebra de linha

`wrap="true"` quebra as linhas longas em vez de rolar para o lado.
:::

<c-docs.example>
<c-code-block class="max-w-md">
  <c-code-block.content wrap="true">DATABASE_URL=postgres://app:secret@db.internal:5432/app?sslmode=require&amp;connect_timeout=10</c-code-block.content>
</c-code-block>
</c-docs.example>

:::en
### Height

A height on the content makes it scroll inside the block.
:::pt-br
### Altura

Uma altura no conteúdo faz ele rolar dentro do bloco.
:::

<c-docs.example>
<c-code-block class="max-w-xl">
  <c-code-block.content line_numbers="true" class="max-h-32">
    <c-code-block.line>from django.db import models</c-code-block.line>
    <c-code-block.line></c-code-block.line>
    <c-code-block.line></c-code-block.line>
    <c-code-block.line>class Order(models.Model):</c-code-block.line>
    <c-code-block.line>    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)</c-code-block.line>
    <c-code-block.line>    total = models.DecimalField(max_digits=10, decimal_places=2)</c-code-block.line>
    <c-code-block.line>    created = models.DateTimeField(auto_now_add=True)</c-code-block.line>
  </c-code-block.content>
</c-code-block>
</c-docs.example>

:::en
### Size

`size="sm"` tightens the padding and the type, for a block inside a message or
a card.
:::pt-br
### Tamanho

`size="sm"` aperta o espaçamento e o texto, para um bloco dentro de uma
mensagem ou de um card.
:::

<c-docs.example>
<c-code-block size="sm" class="max-w-md">
  <c-code-block.content>pip install django-shadcn</c-code-block.content>
</c-code-block>
</c-docs.example>

:::en
### Destructive
:::pt-br
### Destructive
:::

<c-docs.example>
<c-code-block variant="destructive" class="max-w-xl">
  <c-code-block.header>
    <c-code-block.title>TemplateSyntaxError</c-code-block.title>
  </c-code-block.header>
  <c-code-block.content wrap="true">Unclosed tag on line 4: 'if'. Looking for one of: elif, else, endif.</c-code-block.content>
</c-code-block>
</c-docs.example>

:::en
### Inside a message
:::pt-br
### Dentro de uma mensagem
:::

<c-docs.example>
<c-message class="max-w-md text-start">
  <c-message.content>
    <c-bubble variant="muted">
      <c-bubble.content>Run this to apply the change:</c-bubble.content>
    </c-bubble>
    <c-code-block size="sm">
      <c-code-block.actions>
        <c-code-block.copy-button />
      </c-code-block.actions>
      <c-code-block.content>python manage.py migrate</c-code-block.content>
    </c-code-block>
  </c-message.content>
</c-message>
</c-docs.example>

:::en
## RTL

The content is always `dir="ltr"` and start-aligned, so code stays readable on
a right-to-left page, while the header, the title and the actions around it
follow the page and mirror.

## Accessibility

The content takes focus with `tabindex="0"`, so a keyboard can scroll code that
overflows, and a focus ring shows on the block. The copy button is labelled
"Copy", and "Copied" is announced through a live region after a copy; `label`
and `copied_label` translate both. The `added` and `removed` marks are drawn in
the gutter and not read out, so say what changed in the text around a diff.

## API reference
:::pt-br
## RTL

O conteúdo é sempre `dir="ltr"` e alinhado ao início, então o código continua
legível numa página da direita para a esquerda, enquanto o cabeçalho, o título
e as ações em volta seguem a página e espelham.

## Acessibilidade

O conteúdo recebe foco com `tabindex="0"`, então o teclado consegue rolar um
código que transborda, e um anel de foco aparece no bloco. O botão de copiar
tem o rótulo "Copy", e "Copied" é anunciado por uma região viva depois de
copiar; `label` e `copied_label` traduzem os dois. As marcas de `added` e
`removed` são desenhadas na margem e não são lidas, então diga o que mudou no
texto em volta de um diff.

## Referência da API
:::

<c-docs.api-reference name="code-block" />

:::en
## Notes

Upstream writes its classes as `cn-*` names resolved by a style file. The
registry the rest of this library follows has no code block, so the utilities
here come from the style closest to it.

Upstream's tabs, show-more and typeset examples, and its syntax highlighting
guide, have no counterpart: there is no highlighter, and a block of tabs is a
[Tabs]({% url 'page' slug='tabs' %}) with a code block in each panel. A code
block inside a [Trace]({% url 'page' slug='trace' %}) step works as in any
other container.
:::pt-br
## Observações

O upstream escreve as classes como nomes `cn-*` resolvidos por um arquivo de
estilo. O registry que o resto desta biblioteca segue não tem code block, então
os utilitários daqui vêm do estilo mais próximo dele.

Os exemplos de abas, de mostrar mais e de tipografia do upstream, e o guia de
realce de sintaxe, não têm equivalente: não há realce, e um bloco com abas é um
[Tabs]({% url 'page' slug='tabs' %}) com um code block em cada painel. Um code
block dentro de um passo do [Trace]({% url 'page' slug='trace' %}) funciona
como em qualquer outro contêiner.
:::
