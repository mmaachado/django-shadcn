---
title: Button
description: Displays a button or a component that looks like a button.
description.pt-br: Exibe um botão, ou um componente com cara de botão.
description.es: Muestra un botón, o un componente con aspecto de botón.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="flex flex-wrap items-center justify-center gap-2">
<c-button>Button</c-button>
<c-button variant="outline">Outline</c-button>
<c-button variant="ghost">Ghost</c-button>
<c-button variant="outline" size="icon" aria-label="Next"><c-icon name="arrow-right" /></c-button>
</div>
</c-docs.demo-section>

<c-docs.cheat-sheet name="button">
<c-button variant="outline" type="button">Button</c-button>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add button
```

:::en
## Usage

`<c-button>` renders a `<button>` element, and every attribute you set lands on
it. It needs no JavaScript and no Alpine.

Inside a `<form>`, a button with no `type` submits the form: that is the HTML
default, and the component does not change it. Pass `type="button"` to a
button that only opens or toggles something.

A submit button's `name` and `value` reach `request.POST` when it is the one
that was pressed, which is how one form gets more than one action:
:::pt-br
## Uso

O `<c-button>` renderiza um elemento `<button>`, e todo atributo que você define
cai nele. Ele não precisa de JavaScript nem de Alpine.

Dentro de um `<form>`, um botão sem `type` envia o formulário: é o padrão do
HTML, e o componente não muda isso. Passe `type="button"` a um botão que só
abre ou alterna alguma coisa.

O `name` e o `value` de um botão de envio chegam ao `request.POST` quando é ele
que foi apertado, e é assim que um formulário ganha mais de uma ação:
:::

```html
<form method="post">
  {% csrf_token %}
  <c-button name="action" value="publish">Publish</c-button>
  <c-button name="action" value="draft" variant="outline">Save draft</c-button>
</form>
```

```python
if request.POST.get("action") == "publish":
    post.publish()
```

:::en
## Examples

### Size

`size` takes `xs`, `sm`, `default` and `lg`, and `icon` for a square button that
holds only an icon.
:::pt-br
## Exemplos

### Tamanho

`size` aceita `xs`, `sm`, `default` e `lg`, e `icon` para um botão quadrado que
guarda só um ícone.
:::

<c-docs.example>
<div class="flex flex-wrap items-center gap-2">
  <c-button size="xs">Extra small</c-button>
  <c-button size="sm">Small</c-button>
  <c-button>Default</c-button>
  <c-button size="lg">Large</c-button>
  <c-button size="icon" aria-label="Next"><c-icon name="arrow-right" /></c-button>
</div>
</c-docs.example>

:::en
### Default
:::pt-br
### Default
:::

<c-docs.example>
<c-button>Button</c-button>
</c-docs.example>

:::en
### Outline
:::pt-br
### Outline
:::

<c-docs.example>
<c-button variant="outline">Button</c-button>
</c-docs.example>

:::en
### Secondary
:::pt-br
### Secondary
:::

<c-docs.example>
<c-button variant="secondary">Button</c-button>
</c-docs.example>

:::en
### Ghost
:::pt-br
### Ghost
:::

<c-docs.example>
<c-button variant="ghost">Button</c-button>
</c-docs.example>

:::en
### Destructive
:::pt-br
### Destructive
:::

<c-docs.example>
<c-button variant="destructive">Delete</c-button>
</c-docs.example>

:::en
### Link

The link variant still renders a `<button>`. For a real link that looks like
one, use [Link]({% url 'page' slug='a' %}).
:::pt-br
### Link

A variante link continua renderizando um `<button>`. Para um link de verdade com
essa aparência, use o [Link]({% url 'page' slug='a' %}).
:::

<c-docs.example>
<c-button variant="link">Button</c-button>
</c-docs.example>

:::en
### Icon

A button with only an icon has no text for a screen reader to read, so give
it an `aria-label`.
:::pt-br
### Ícone

Um botão só com ícone não tem texto para um leitor de tela ler, então dê a ele
um `aria-label`.
:::

<c-docs.example>
<c-button variant="outline" size="icon" aria-label="Next">
  <c-icon name="chevron-right" />
</c-button>
</c-docs.example>

:::en
### With an icon

Put the icon beside the text; the button spaces and sizes it.
:::pt-br
### Com ícone

Ponha o ícone ao lado do texto; o botão cuida do espaço e do tamanho.
:::

<c-docs.example>
<c-button variant="outline">
  Continue
  <c-icon name="arrow-right" />
</c-button>
</c-docs.example>

:::en
### Rounded

The button's corners come from `rounded-md`, so a rounder one needs the `!`
suffix: two utilities for the same property are settled by the compiled
stylesheet, not by the order you write them.
:::pt-br
### Arredondado

Os cantos do botão vêm de `rounded-md`, então um mais redondo precisa do sufixo
`!`: dois utilitários para a mesma propriedade são decididos pela folha de
estilo compilada, não pela ordem em que você os escreve.
:::

<c-docs.example>
<c-button variant="outline" size="icon" class="rounded-full!" aria-label="Next">
  <c-icon name="arrow-right" />
</c-button>
</c-docs.example>

:::en
### Spinner

A [Spinner]({% url 'page' slug='spinner' %}) inside the button shows a pending
state. Disable the button while it lasts, so the form is not sent twice.
:::pt-br
### Spinner

Um [Spinner]({% url 'page' slug='spinner' %}) dentro do botão mostra um estado
de espera. Desabilite o botão enquanto ele dura, para o formulário não ser
enviado duas vezes.
:::

<c-docs.example>
<c-button disabled>
  <c-spinner />
  Saving
</c-button>
</c-docs.example>

:::en
### Button group

[Button Group]({% url 'page' slug='button-group' %}) joins buttons into one
outlined row.
:::pt-br
### Grupo de botões

O [Button Group]({% url 'page' slug='button-group' %}) junta botões numa fileira
com um contorno só.
:::

<c-docs.example>
<c-button-group>
  <c-button variant="outline">Archive</c-button>
  <c-button variant="outline">Report</c-button>
  <c-button variant="outline">Snooze</c-button>
</c-button-group>
</c-docs.example>

:::en
## RTL

The button has no side of its own: the gap between an icon and the text is the
same either way, and the icon stays where you wrote it in the markup, which
under `dir="rtl"` is the other side. An arrow does not turn around by itself;
add `rtl:rotate-180` to one that means "next", as the
[Direction]({% url 'page' slug='direction' %}) page explains.

## Accessibility

It is a native `<button>`, so it takes focus, answers to Enter and Space, and
is announced as a button. `disabled` takes it out of the tab order and the
form. The focus ring shows only for the keyboard.

## API reference
:::pt-br
## RTL

O botão não tem um lado próprio: o espaço entre um ícone e o texto é o mesmo
nas duas direções, e o ícone fica onde você o escreveu no markup, o que sob
`dir="rtl"` é o outro lado. Uma seta não se vira sozinha; acrescente
`rtl:rotate-180` a uma que signifique "próximo", como explica a página de
[Direction]({% url 'page' slug='direction' %}).

## Acessibilidade

É um `<button>` nativo, então recebe foco, responde ao Enter e ao Espaço e é
anunciado como botão. `disabled` o tira da ordem de tab e do formulário. O anel
de foco só aparece para o teclado.

## Referência da API
:::

<c-docs.api-reference name="button" />

:::en
## Notes

**Cursor.** Tailwind v4 gives buttons the default arrow cursor instead of the
pointer, and so does this one. For the pointer everywhere, add this to your
`input.css`:
:::pt-br
## Observações

**Cursor.** O Tailwind v4 dá aos botões o cursor de seta padrão em vez da
mãozinha, e este também. Para a mãozinha em todo lugar, acrescente isto ao seu
`input.css`:
:::

```css
@layer base {
  button:not(:disabled),
  [role="button"]:not(:disabled) {
    cursor: pointer;
  }
}
```

:::en
**As a link.** Upstream's `asChild` hands the button's look to another element,
such as a link. A template has no equivalent: `<c-button>` always renders a
`<button>`, and an `href` on it does nothing. For a link in the link variant's
style, use [Link]({% url 'page' slug='a' %}). For a link that looks like a solid
button, put the button's classes on an `<a>`: they are in
`templates/cotton/button/index.html`, yours to copy.
:::pt-br
**Como link.** O `asChild` do upstream passa a aparência do botão para outro
elemento, como um link. Um template não tem equivalente: o `<c-button>` sempre
renderiza um `<button>`, e um `href` nele não faz nada. Para um link no estilo
da variante link, use o [Link]({% url 'page' slug='a' %}). Para um link com
cara de botão sólido, ponha as classes do botão num `<a>`: elas estão em
`templates/cotton/button/index.html`, à sua disposição para copiar.
:::
