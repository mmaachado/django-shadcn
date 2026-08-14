---
title: Alert Dialog
description: A modal dialog that interrupts the user with important content and expects a response.
description.pt-br: Um diálogo modal que interrompe o usuário com algo importante e espera uma resposta.
description.es: Un diálogo modal que interrumpe al usuario con algo importante y espera una respuesta.
---

<c-docs.demo-section class="min-h-[350px]">
<c-alert-dialog>
            <c-button variant="outline">
                <c-alert-dialog.trigger>Open Dialog</c-alert-dialog.trigger>
            </c-button>

            <c-alert-dialog.content>
                <c-alert-dialog.header>
                    <c-alert-dialog.title>Are you absolutely sure?</c-alert-dialog.title>
                    <c-alert-dialog.description>
                    This action cannot be undone. This will permanently delete your account
                    and remove your data from our servers.
                    </c-alert-dialog.description>
                </c-alert-dialog.header>
                <c-alert-dialog.footer>
                    <c-alert-dialog.cancel>Cancel</c-alert-dialog.cancel>
                    <c-alert-dialog.action>Continue</c-alert-dialog.action>
                </c-alert-dialog.footer>
            </c-alert-dialog.content>
        </c-alert-dialog>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add alert_dialog
```

## Usage

```html
<c-alert-dialog>
    <c-button variant='outline'>
        <c-alert-dialog.trigger>Open Dialog</c-alert-dialog.trigger>
    </c-button>

    <c-alert-dialog.content>

        <c-alert-dialog.header>
            <c-alert-dialog.title>Are you absolutely sure?</c-alert-dialog.title>
            <c-alert-dialog.description>
            This action cannot be undone. This will permanently delete your account
            and remove your data from our servers.
            </c-alert-dialog.description>
        </c-alert-dialog.header>

        <c-alert-dialog.footer>
            <c-alert-dialog.cancel>Cancel</c-alert-dialog.cancel>
            <c-alert-dialog.action>Continue</c-alert-dialog.action>
        </c-alert-dialog.footer>
    </c-alert-dialog.content>

</c-alert-dialog>
```
