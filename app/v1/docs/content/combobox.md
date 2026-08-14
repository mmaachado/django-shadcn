---
title: Combobox
description: Autocomplete input and command palette with a list of suggestions.
description.pt-br: Campo com autocompletar e paleta de comandos, com lista de sugestões.
description.es: Campo con autocompletado y paleta de comandos, con lista de sugerencias.
---

<c-docs.demo-section class="min-h-[350px]">
<c-combobox
          :options="[
            {'value': 'django', 'label': 'Django'},
            {'value': 'tailwind', 'label': 'Tailwind'},
            {'value': 'alpine.js', 'label': 'Alpine.js'},
            {'value': 'htmx', 'label': 'HTMX'},
          ]"
          placeholder="Search framework..."
          button_text="Select framework..."
          width="w-[200px]"
        />
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add combobox
```

## Usage

```html
<c-combobox
  :options="[]"
  placeholder="Search framework..."
  button_text="Select framework..."
  width="w-[200px]"
/>
<!-- Options can be a list of dicts with values and labels -->
<!-- options=[
    {'value': 'django', 'label': 'Django'},
    {'value': 'tailwind', 'label': 'Tailwind'},
    {'value': 'alpine.js', 'label': 'Alpine.js'},
    {'value': 'htmx', 'label': 'HTMX'},
]-->
```
