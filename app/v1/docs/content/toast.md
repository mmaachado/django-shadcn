---
title: Toast
description: A succinct message that is displayed temporarily.
description.pt-br: Uma mensagem curta, exibida por alguns instantes.
description.es: Un mensaje breve, que se muestra unos instantes.
---

<c-docs.demo-section class="min-h-[350px]">
<c-button variant="outline">
<c-toast.trigger toast_target="toast-success">
Show Toast
</c-toast.trigger>
</c-button>

        <c-toast id="toast-success">
            <c-toast.content
                type="default"
                title="Success"
                description="This is a success message"
            >
                <c-button>Share</c-button>
            </c-toast.content>
        </c-toast>

</c-docs.demo-section>

<c-docs.cheat-sheet name="toast">
<c-toast.trigger toast_target="toast-success"> Show Toast </c-toast.trigger>
<c-toast id="toast-success">
  <c-toast.content description="Your message here." />
</c-toast>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add toast
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-toast.trigger toast_target="toast-success"> Show Toast </c-toast.trigger>
<c-toast id="toast-success">
  <c-toast.content description="Your message here." />
</c-toast>
```

:::en
## Examples

### Simple
:::pt-br
## Exemplos

### Simples
:::

<c-docs.example>
<c-button variant="outline">
  <c-toast.trigger toast_target='toast-simple'>
    Show Toast
  </c-toast.trigger>
</c-button>
<c-toast id='toast-simple'>
  <c-toast.content description='Your message has been sent.' />
</c-toast>
</c-docs.example>

:::en
### With title
:::pt-br
### Com título
:::

<c-docs.example>
<c-button variant="outline">
  <c-toast.trigger toast_target='toast-title'>
    Show Toast
  </c-toast.trigger>
</c-button>
<c-toast id='toast-title'>
  <c-toast.content title='Success' description='Your message has been sent.' />
</c-toast>
</c-docs.example>

:::en
### With Action
:::pt-br
### Com ação
:::

<c-docs.example>
<c-button variant="outline">
  <c-toast.trigger toast_target='toast-action'>
    Show Toast
  </c-toast.trigger>
</c-button>
<c-toast id='toast-action'>
  <c-toast.content title='Success' description='Your message has been sent.'>
    <c-button>Share</c-button>
  </c-toast.content>
</c-toast>
</c-docs.example>

:::en
### Destructive
:::pt-br
### Destructive
:::

<c-docs.example>
<c-button variant="outline">
  <c-toast.trigger toast_target='toast-fail'>
    Show Toast
  </c-toast.trigger>
</c-button>
<c-toast id='toast-fail'>
  <c-toast.content type="destructive" title='Error' description='Your message could not be sent.'>
    <c-button variant='ghost'>Retry</c-button>
  </c-toast.content>
</c-toast>
</c-docs.example>

:::en
## RTL

The toast sits in a corner of the screen, and its text and action follow the
page's direction.

## Accessibility

The toast carries `role="alert"`, so a screen reader announces it as it
appears. It goes away on its own, so keep the message short, and do not put
the only way to do something in it.

## API reference
:::pt-br
## RTL

O toast fica num canto da tela, e o texto e a ação dele seguem a direção da
página.

## Acessibilidade

O toast leva `role="alert"`, então um leitor de tela o anuncia quando ele
aparece. Ele some sozinho, então mantenha a mensagem curta, e não ponha nele o
único jeito de fazer algo.

## Referência da API
:::

<c-docs.api-reference name="toast" />
