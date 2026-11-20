---
title: Select
description: Displays a list of options for the user to pick from—triggered by a button.
description.pt-br: Uma lista de opções para o usuário escolher, aberta por um botão.
description.es: Una lista de opciones para que el usuario elija, abierta por un botón.
---

<c-docs.demo-section class="min-h-[350px]">
<c-select name="library" class="w-[180px]">
<c-select.trigger>
<c-select.value placeholder="Select a library" />
</c-select.trigger>
<c-select.content>
<c-select.item value="django">Django</c-select.item>
<c-select.item value="flask">Flask</c-select.item>
<c-select.item value="fastapi">FastAPI</c-select.item>
<c-select.item value="pyramid">Pyramid</c-select.item>
<c-select.item value="bottle">Bottle</c-select.item>
</c-select.content>
</c-select>
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add select
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-select class="w-[180px]">
  <c-select.trigger>
    <c-select.value placeholder="Theme" />
  </c-select.trigger>
  <c-select.content>
    <c-select.item value="light">Light</c-select.item>
    <c-select.item value="dark">Dark</c-select.item>
    <c-select.item value="system">System</c-select.item>
  </c-select.content>
</c-select>
</c-docs.example>

:::en
## Examples

### Disabled
:::pt-br
## Exemplos

### Desabilitado
:::

<c-docs.example>
<c-select name="library" class="w-[180px]">
  <c-select.trigger disabled>
    <c-select.value placeholder="Select a library" />
  </c-select.trigger>
</c-select>
</c-docs.example>

:::en
## API reference
:::pt-br
## Referência da API
:::

<c-docs.api-reference name="select" />
