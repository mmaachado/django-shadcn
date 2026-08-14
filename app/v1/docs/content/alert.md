---
title: Alert
description: Displays a callout for user attention.
description.pt-br: Destaca um aviso para chamar a atenção do usuário.
description.es: Destaca un aviso para llamar la atención del usuario.
---

<c-docs.demo-section class="min-h-[350px]">
<c-alert variant="default">
          <!-- Include the terminal icon -->
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="h-4 w-4"
          >
            <polyline points="4 17 10 11 4 5"></polyline>
            <line x1="12" y1="19" x2="20" y2="19"></line>
          </svg>
          <c-alert.title>Heads up!</c-alert.title>
          <c-alert.description>
            You can add components to your app using the cli.
          </c-alert.description>
        </c-alert>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add alert
```

## Usage

```html
<c-alert variant='default'>
    <c-alert.title>Heads up!</c-alert.title>
    <c-alert.description>
    You can add components to your app using the cli.
    </c-alert.description>
</c-alert>
```
