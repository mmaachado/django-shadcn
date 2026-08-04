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

## Installation

```bash
uvx django_shadcn@latest add toast
```

## Usage

```html
<c-toast.trigger toast_target="toast-success"> Show Toast </c-toast.trigger>
<c-toast id="toast-success">
  <c-toast.content description="Your message here." />
</c-toast>
```

## Examples

### Simple

<c-docs.demo-section>
<c-button variant="outline">
<c-toast.trigger toast_target='toast-simple'>
Show Toast
</c-toast.trigger>
</c-button>
<c-toast id='toast-simple'>
<c-toast.content description='Your message has been sent.' />
</c-toast>
</c-docs.demo-section>

```html
<c-button variant="outline">
  <c-toast.trigger toast_target="toast-simple"> Show Toast </c-toast.trigger>
</c-button>
<c-toast id="toast-simple">
  <c-toast.content description="Your message has been sent." />
</c-toast>
```

### With title

<c-docs.demo-section>
<c-button variant="outline">
<c-toast.trigger toast_target='toast-title'>
Show Toast
</c-toast.trigger>
</c-button>
<c-toast id='toast-title'>
<c-toast.content title='Success' description='Your message has been sent.' />
</c-toast>
</c-docs.demo-section>

```html
<c-button variant="outline">
  <c-toast.trigger toast_target="toast-title"> Show Toast </c-toast.trigger>
</c-button>
<c-toast id="toast-title">
  <c-toast.content title="Success" description="Your message has been sent." />
</c-toast>
```

### With Action

<c-docs.demo-section>
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
</c-docs.demo-section>

```html
<c-button variant="outline">
  <c-toast.trigger toast_target="toast-action"> Show Toast </c-toast.trigger>
</c-button>
<c-toast id="toast-action">
  <c-toast.content title="Success" description="Your message has been sent.">
    <c-button>Share</c-button>
  </c-toast.content>
</c-toast>
```

### Destructive

<c-docs.demo-section>
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
</c-docs.demo-section>

```html
<c-button variant="outline">
  <c-toast.trigger toast_target="toast-fail"> Show Toast </c-toast.trigger>
</c-button>
<c-toast id="toast-fail">
  <c-toast.content
    type="destructive"
    title="Error"
    description="Your message could not be sent."
  >
    <c-button variant="ghost">Retry</c-button>
  </c-toast.content>
</c-toast>
```
