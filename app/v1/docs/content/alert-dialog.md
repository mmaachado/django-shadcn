---
title: Alert Dialog
description: A modal dialog that interrupts the user with important content and expects a response.
description.pt-br: Um diálogo modal que interrompe o usuário com algo importante e espera uma resposta.
description.es: Un diálogo modal que interrumpe al usuario con algo importante y espera una respuesta.
---

<c-docs.demo-section class="min-h-[350px]">
<c-alert-dialog>
<c-alert-dialog.trigger>
<c-button variant="outline">Delete account</c-button>
</c-alert-dialog.trigger>
<c-alert-dialog.content>
<c-alert-dialog.header>
<c-alert-dialog.title>Are you absolutely sure?</c-alert-dialog.title>
<c-alert-dialog.description>This cannot be undone. Your account and its data will be deleted.</c-alert-dialog.description>
</c-alert-dialog.header>
<c-alert-dialog.footer>
<c-alert-dialog.cancel>Cancel</c-alert-dialog.cancel>
<c-alert-dialog.action variant="destructive">Delete</c-alert-dialog.action>
</c-alert-dialog.footer>
</c-alert-dialog.content>
</c-alert-dialog>
</c-docs.demo-section>

<c-docs.cheat-sheet name="alert-dialog">
<c-alert-dialog>
  <c-alert-dialog.trigger>
    <c-button variant="outline">Delete</c-button>
  </c-alert-dialog.trigger>
  <c-alert-dialog.content>
    <c-alert-dialog.header>
      <c-alert-dialog.title>Delete this post?</c-alert-dialog.title>
    </c-alert-dialog.header>
    <c-alert-dialog.footer>
      <c-alert-dialog.cancel>Cancel</c-alert-dialog.cancel>
      <c-alert-dialog.action variant="destructive">Delete</c-alert-dialog.action>
    </c-alert-dialog.footer>
  </c-alert-dialog.content>
</c-alert-dialog>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add alert_dialog
```

:::en
## Usage

The trigger opens the dialog on click, and the cancel and action buttons close
it. It is Alpine state, so without JavaScript the trigger does nothing and the
dialog never shows.

The action is a `<button>` with no `type`, so inside a `<form>` it submits the
form as it closes the dialog. That is the usual way to confirm a destructive
action in Django: the dialog holds the form that posts it.
:::pt-br
## Uso

O trigger abre o diálogo no clique, e os botões de cancelar e de ação o fecham.
É estado do Alpine, então sem JavaScript o trigger não faz nada e o diálogo
nunca aparece.

A ação é um `<button>` sem `type`, então dentro de um `<form>` ela envia o
formulário enquanto fecha o diálogo. É o jeito comum de confirmar uma ação
destrutiva no Django: o diálogo guarda o formulário que a envia.
:::

```html
<c-alert-dialog>
  <c-alert-dialog.trigger>
    <c-button variant="destructive">Delete post</c-button>
  </c-alert-dialog.trigger>
  <c-alert-dialog.content>
    <c-alert-dialog.header>
      <c-alert-dialog.title>Delete "{{ post.title }}"?</c-alert-dialog.title>
      <c-alert-dialog.description>This cannot be undone.</c-alert-dialog.description>
    </c-alert-dialog.header>
    <form method="post" action="{% url 'post-delete' post.pk %}">
      {% csrf_token %}
      <c-alert-dialog.footer>
        <c-alert-dialog.cancel type="button">Cancel</c-alert-dialog.cancel>
        <c-alert-dialog.action variant="destructive">Delete</c-alert-dialog.action>
      </c-alert-dialog.footer>
    </form>
  </c-alert-dialog.content>
</c-alert-dialog>
```

:::en
Give the cancel button `type="button"` there, or it submits the form too.

## Examples

### Basic
:::pt-br
Dê ao botão de cancelar `type="button"` ali, senão ele envia o formulário
também.

## Exemplos

### Básico
:::

<c-docs.example>
<c-alert-dialog>
  <c-alert-dialog.trigger>
    <c-button variant="outline">Show dialog</c-button>
  </c-alert-dialog.trigger>
  <c-alert-dialog.content>
    <c-alert-dialog.header>
      <c-alert-dialog.title>Leave without saving?</c-alert-dialog.title>
      <c-alert-dialog.description>Your changes will be lost.</c-alert-dialog.description>
    </c-alert-dialog.header>
    <c-alert-dialog.footer>
      <c-alert-dialog.cancel>Stay</c-alert-dialog.cancel>
      <c-alert-dialog.action>Leave</c-alert-dialog.action>
    </c-alert-dialog.footer>
  </c-alert-dialog.content>
</c-alert-dialog>
</c-docs.example>

:::en
### Media

An icon in the header draws the eye to what the dialog is about.
:::pt-br
### Mídia

Um ícone no cabeçalho chama a atenção para o assunto do diálogo.
:::

<c-docs.example>
<c-alert-dialog>
  <c-alert-dialog.trigger>
    <c-button variant="outline">Share project</c-button>
  </c-alert-dialog.trigger>
  <c-alert-dialog.content class="max-w-sm">
    <c-alert-dialog.header>
      <div class="mb-2 flex size-10 items-center justify-center rounded-full bg-muted">
        <c-icon name="users" class="size-5" />
      </div>
      <c-alert-dialog.title>Share with your team?</c-alert-dialog.title>
      <c-alert-dialog.description>Everyone in the workspace will see this project.</c-alert-dialog.description>
    </c-alert-dialog.header>
    <c-alert-dialog.footer>
      <c-alert-dialog.cancel>Cancel</c-alert-dialog.cancel>
      <c-alert-dialog.action>Share</c-alert-dialog.action>
    </c-alert-dialog.footer>
  </c-alert-dialog.content>
</c-alert-dialog>
</c-docs.example>

:::en
### Destructive
:::pt-br
### Destructive
:::

<c-docs.example>
<c-alert-dialog>
  <c-alert-dialog.trigger>
    <c-button variant="destructive">Delete chat</c-button>
  </c-alert-dialog.trigger>
  <c-alert-dialog.content>
    <c-alert-dialog.header>
      <c-alert-dialog.title>Delete this chat?</c-alert-dialog.title>
      <c-alert-dialog.description>The messages will be deleted for everyone.</c-alert-dialog.description>
    </c-alert-dialog.header>
    <c-alert-dialog.footer>
      <c-alert-dialog.cancel>Cancel</c-alert-dialog.cancel>
      <c-alert-dialog.action variant="destructive">Delete</c-alert-dialog.action>
    </c-alert-dialog.footer>
  </c-alert-dialog.content>
</c-alert-dialog>
</c-docs.example>

:::en
## RTL

The header and the footer align to the start of the line and the buttons sit
at its end, so under `dir="rtl"` the dialog mirrors with the text.

## Accessibility

The content is a `role="dialog"` with `aria-modal="true"`. Opening it moves
focus to its first button or field, Escape closes it, and the page behind
stops scrolling. Tab and Shift+Tab cycle through what is inside and never reach the page
behind, and closing it returns focus to the element that opened it. The title is not
tied to the dialog with `aria-labelledby`: add an `id` to the title and the
attribute to the content when that matters.

## API reference
:::pt-br
## RTL

O cabeçalho e o rodapé se alinham ao início da linha e os botões ficam no fim
dela, então sob `dir="rtl"` o diálogo espelha junto com o texto.

## Acessibilidade

O conteúdo é um `role="dialog"` com `aria-modal="true"`. Abri-lo leva o foco ao
primeiro botão ou campo, o Escape o fecha, e a página de trás para de rolar.
O Tab e o Shift+Tab passam pelo que está dentro e nunca chegam à página de
trás, e fechá-lo devolve o foco ao elemento que o abriu. O título não está ligado ao
diálogo por `aria-labelledby`: acrescente um `id` ao título e o atributo ao
conteúdo quando isso importar.

## Referência da API
:::

<c-docs.api-reference name="alert-dialog" />

:::en
## Notes

Upstream's alert dialog does not close when the overlay is clicked, so the
reader has to answer it. This one does close on a click outside.

Upstream also has a `size="sm"` dialog with the buttons side by side. There is
no size here; `class="max-w-sm"` on the content makes it narrower, as in the
media example.
:::pt-br
## Observações

O alert dialog do upstream não fecha com um clique no overlay, para que o
leitor tenha de responder. Este fecha com um clique fora.

O upstream também tem um diálogo `size="sm"` com os botões lado a lado. Aqui
não há tamanho; `class="max-w-sm"` no conteúdo o deixa mais estreito, como no
exemplo com mídia.
:::
