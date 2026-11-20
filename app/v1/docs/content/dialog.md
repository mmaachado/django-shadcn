---
title: Dialog
description: A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.
description.pt-br: Uma janela sobreposta à principal, que desativa o conteúdo abaixo.
description.es: Una ventana superpuesta a la principal, que desactiva el contenido de debajo.
---

<c-docs.demo-section class="min-h-[350px]">
<c-dialog>
<c-dialog.trigger>Edit profile</c-dialog.trigger>
<c-dialog.content class="sm:max-w-[425px]">
<c-dialog.header>
<c-dialog.title>Edit profile</c-dialog.title>
<c-dialog.description>Change your name and save when you are done.</c-dialog.description>
</c-dialog.header>
<div class="grid gap-2">
<c-label for="dialog-demo-name">Name</c-label>
<c-input id="dialog-demo-name" value="Ada Carter" />
</div>
<c-dialog.footer>
<c-button>Save changes</c-button>
</c-dialog.footer>
</c-dialog.content>
</c-dialog>
</c-docs.demo-section>

<c-docs.cheat-sheet name="dialog">
<c-dialog>
  <c-dialog.trigger type="button">Open</c-dialog.trigger>
  <c-dialog.content>
    <c-dialog.header>
      <c-dialog.title>Title</c-dialog.title>
      <c-dialog.description>Description</c-dialog.description>
    </c-dialog.header>
    <c-dialog.footer>...</c-dialog.footer>
  </c-dialog.content>
</c-dialog>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add dialog
```

:::en
## Usage

The trigger opens the dialog, and the close button in its corner, Escape and a
click outside close it. It is Alpine state, so without JavaScript the dialog
never opens.

A form inside the content posts like any other, which makes the dialog a good
home for a short edit. The trigger is a `<button>` with no `type`, so give it
`type="button"` when the dialog sits inside a form of its own.
:::pt-br
## Uso

O trigger abre o diálogo, e o botão de fechar no canto, o Escape e um clique
fora o fecham. É estado do Alpine, então sem JavaScript o diálogo nunca abre.

Um formulário dentro do conteúdo envia como qualquer outro, o que faz do
diálogo um bom lugar para uma edição curta. O trigger é um `<button>` sem
`type`, então dê a ele `type="button"` quando o diálogo estiver dentro de um
formulário próprio.
:::

```html
<c-dialog>
  <c-dialog.trigger type="button">Rename</c-dialog.trigger>
  <c-dialog.content>
    <form method="post" action="{% url 'project-rename' project.pk %}">
      {% csrf_token %}
      <c-dialog.header>
        <c-dialog.title>Rename project</c-dialog.title>
      </c-dialog.header>
      <c-input name="name" value="{{ project.name }}" aria-label="Name" />
      <c-dialog.footer>
        <c-button>Save</c-button>
      </c-dialog.footer>
    </form>
  </c-dialog.content>
</c-dialog>
```

:::en
## Examples

### Custom close button

A button in the footer that calls `hideDialog()` closes it too, for a "Cancel"
next to the action.
:::pt-br
## Exemplos

### Botão de fechar personalizado

Um botão no rodapé que chama `hideDialog()` também o fecha, para um "Cancelar"
ao lado da ação.
:::

<c-docs.example>
<c-dialog>
  <c-dialog.trigger>Share link</c-dialog.trigger>
  <c-dialog.content class="sm:max-w-md">
    <c-dialog.header>
      <c-dialog.title>Share link</c-dialog.title>
      <c-dialog.description>Anyone with the link can view this page.</c-dialog.description>
    </c-dialog.header>
    <c-input value="https://example.com/s/8f3k" readonly aria-label="Link" />
    <c-dialog.footer>
      <c-button variant="outline" type="button" x-on:click="hideDialog()">Close</c-button>
    </c-dialog.footer>
  </c-dialog.content>
</c-dialog>
</c-docs.example>

:::en
### Your own trigger

`as_child="true"` makes the trigger a wrapper that opens the dialog when
anything inside it is clicked, so the trigger can be one of your buttons.
:::pt-br
### Seu próprio trigger

`as_child="true"` faz do trigger um invólucro que abre o diálogo quando algo
dentro dele é clicado, então o trigger pode ser um dos seus botões.
:::

<c-docs.example>
<c-dialog>
  <c-dialog.trigger as_child="true">
    <c-button>New project</c-button>
  </c-dialog.trigger>
  <c-dialog.content>
    <c-dialog.header>
      <c-dialog.title>New project</c-dialog.title>
      <c-dialog.description>Pick a name; you can change it later.</c-dialog.description>
    </c-dialog.header>
  </c-dialog.content>
</c-dialog>
</c-docs.example>

:::en
### Scrollable content

Long content scrolls inside the dialog while the header and the footer stay in
view: give the body a height and `overflow-y-auto`, which keeps the footer as
a sticky footer.
:::pt-br
### Conteúdo com rolagem

Um conteúdo longo rola dentro do diálogo enquanto o cabeçalho e o rodapé ficam
à vista: dê ao corpo uma altura e `overflow-y-auto`, o que mantém o rodapé fixo
embaixo.
:::

<c-docs.example>
<c-dialog>
  <c-dialog.trigger>Terms of service</c-dialog.trigger>
  <c-dialog.content class="sm:max-w-lg">
    <c-dialog.header>
      <c-dialog.title>Terms of service</c-dialog.title>
    </c-dialog.header>
    <div class="max-h-60 space-y-3 overflow-y-auto pe-2 text-sm text-muted-foreground">
      {% for n in "12345678" %}
        <p>Clause {{ n }}. A paragraph of the terms, long enough to show how the content scrolls between the header and the footer.</p>
      {% endfor %}
    </div>
    <c-dialog.footer>
      <c-button type="button" x-on:click="hideDialog()">I agree</c-button>
    </c-dialog.footer>
  </c-dialog.content>
</c-dialog>
</c-docs.example>

:::en
## RTL

The header aligns to the start of the line and the footer's buttons to its
end, and the close button sits in the end corner, so under `dir="rtl"` the
dialog mirrors with the text.

## Accessibility

The content is a `role="dialog"` with `aria-modal="true"`. Opening it moves
focus to its first focusable element, the close button, Escape and a click outside close it,
and the close button is labelled "Close". Focus is not trapped inside and the
title is not tied to the dialog with `aria-labelledby`; add an `id` to the
title and the attribute to the content when that matters.

## API reference
:::pt-br
## RTL

O cabeçalho se alinha ao início da linha e os botões do rodapé ao fim, e o
botão de fechar fica no canto do fim, então sob `dir="rtl"` o diálogo espelha
com o texto.

## Acessibilidade

O conteúdo é um `role="dialog"` com `aria-modal="true"`. Abri-lo leva o foco ao
primeiro elemento focável, o botão de fechar, o Escape e um clique fora o fecham, e o botão de
fechar tem o rótulo "Close". O foco não fica preso dentro e o título não está
ligado ao diálogo por `aria-labelledby`; acrescente um `id` ao título e o
atributo ao conteúdo quando isso importar.

## Referência da API
:::

<c-docs.api-reference name="dialog" />

:::en
## Notes

The close button in the corner is always there; upstream can leave it out with
`showCloseButton={false}`. Hide it with `[&>[data-slot=button]:first-child]:hidden` on the content when
a dialog must be answered through its own buttons.
:::pt-br
## Observações

O botão de fechar no canto está sempre ali; o upstream pode deixá-lo de fora
com `showCloseButton={false}`. Esconda-o com `[&>[data-slot=button]:first-child]:hidden` no conteúdo quando
um diálogo precisar ser respondido pelos próprios botões.
:::
