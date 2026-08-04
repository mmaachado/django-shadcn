---
title: Checkbox
description: A control that allows the user to toggle between checked and not checked.
description.pt-br: Um controle que o usuário alterna entre marcado e desmarcado.
description.es: Un control que el usuario alterna entre marcado y sin marcar.
---

<c-docs.demo-section class="min-h-[350px]">

<div class="flex items-center space-x-2">
            <c-checkbox id="terms" />
            <label
                for="terms"
                class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
            >
                Accept terms and conditions
            </label>
        </div>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add checkbox
```

## Usage

```html
<c-checkbox id="terms" />
```

## Examples

### With text

<c-docs.demo-section>

<div class="items-top flex space-x-2">
    <c-checkbox id="terms" />
    <div class="grid gap-1.5 leading-none">
        <label
            for="terms"
            class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
        >
            Accept terms and conditions
        </label>
        <p class="text-sm text-muted-foreground">
            You agree to our Terms of Service and Privacy Policy.
        </p>
    </div>
</div>
</c-docs.demo-section>

```html
<div class="items-top flex space-x-2">
  <c-checkbox id="terms" />
  <div class="grid gap-1.5 leading-none">
    <label
      for="terms"
      class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
    >
      Accept terms and conditions
    </label>
    <p class="text-sm text-muted-foreground">
      You agree to our Terms of Service and Privacy Policy.
    </p>
  </div>
</div>
```

### Disabled

<c-docs.demo-section>
<c-checkbox id='terms' disabled />
</c-docs.demo-section>

```html
<c-checkbox id="terms" disabled />
```
