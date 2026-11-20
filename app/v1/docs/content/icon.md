---
title: Icon
description: Lucide icons as a cotton component. Every icon used by the library goes through it.
description.pt-br: Ícones do lucide como componente cotton. Todo ícone da biblioteca passa por ele.
description.es: Iconos de lucide como componente cotton. Todo icono de la biblioteca pasa por él.
---

<c-docs.demo-section class="min-h-[350px]">

<div class="flex items-center gap-6">
            <c-icon name="search" />
            <c-icon name="check" />
            <c-icon name="chevron-down" />
            <c-icon name="x" />
        </div>
</c-docs.demo-section>

<c-docs.cheat-sheet name="icon">
<c-icon name="search" />
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add icon
```

:::en
Components that use icons pull this one in on their own, so most of the time
it is already installed.

## Usage
:::pt-br
Os componentes que usam ícones trazem este junto por conta própria, então na
maior parte das vezes ele já está instalado.

## Uso
:::

<c-docs.example>
<c-icon name="search" />
</c-docs.example>

:::en
The `name` is the icon name as it appears on <a
href="https://lucide.dev/icons" target="_blank" rel="noopener noreferrer"
class="font-medium underline underline-offset-4">lucide.dev</a>, in kebab-
case. Only the icons shipped with the library are available — see the list
below.

## Examples

### Sizing
:::pt-br
O `name` é o nome do ícone como aparece em <a
href="https://lucide.dev/icons" target="_blank" rel="noopener noreferrer"
class="font-medium underline underline-offset-4">lucide.dev</a>, em kebab-
case. Só os ícones distribuídos com a biblioteca estão disponíveis — veja a
lista abaixo.

## Exemplos

### Tamanho
:::

<c-docs.example>
<div class="flex items-end gap-4">
  <c-icon name="search" class="size-4" />
  <c-icon name="search" class="size-6" />
  <c-icon name="search" class="size-8" />
</div>
</c-docs.example>

:::en
### Color
:::pt-br
### Cor
:::

<c-docs.example>
<div class="flex items-center gap-4">
  <c-icon name="check" class="size-5 text-muted-foreground" />
  <c-icon name="check" class="size-5 text-primary" />
  <c-icon name="check" class="size-5 text-destructive" />
</div>
</c-docs.example>

:::en
### Inside a button
:::pt-br
### Dentro de um botão
:::

<c-docs.example>
<c-button variant="outline">
  <c-icon name="search" class="size-4" />
  Search
</c-button>
</c-docs.example>

:::en
### Reacting to state
:::pt-br
### Reagindo ao estado
:::

<c-docs.example>
<div x-data="{ open: false }" class="flex items-center gap-3">
  <c-button variant="outline" x-on:click="open = !open">Toggle</c-button>
  <c-icon
    name="chevron-down"
    class="size-5 transition-transform"
    x-bind:class="{ 'rotate-180': open }"
    />
</div>
</c-docs.example>

:::en
### Accessibility
:::pt-br
### Acessibilidade
:::

<c-docs.example>
<div class="flex items-center gap-4">
  <c-icon name="x" class="size-5" aria-hidden="true" />
  <c-icon name="search" class="size-5" role="img" aria-label="Search" />
</div>
</c-docs.example>

:::en
## Available icons

The library ships only the icons its components use. Each one lives in its
own file under `icon/` and is generated from lucide, never written by hand.
:::pt-br
## Ícones disponíveis

A biblioteca traz só os ícones que os componentes dela usam. Cada um mora no
próprio arquivo em `icon/` e é gerado a partir do lucide, nunca escrito à mão.
:::

<c-docs.demo-section>
<div class="grid w-full grid-cols-2 gap-4 sm:grid-cols-3 md:grid-cols-4">
{% for name in icons %}
<div class="flex flex-col items-center gap-2 rounded-md border p-4">
<c-icon name="{{ name }}" class="size-6" />
<span class="text-xs text-muted-foreground">{{ name }}</span>
</div>
{% endfor %}
</div>
</c-docs.demo-section>

:::en
## Adding an icon

Reference it in your markup with `&lt;c-icon name="..."&gt;` and run the
generator. It reads the icon names straight out of the templates, downloads
what is missing from lucide and drops whatever nothing references anymore.
:::pt-br
## Adicionando um ícone

Referencie o ícone no seu markup com `&lt;c-icon name="..."&gt;` e rode o
gerador. Ele lê os nomes dos ícones direto dos templates, baixa do lucide o que
falta e remove o que nada mais referencia.
:::

```bash
uv run python scripts/generate_icons.py
```

:::en
## License

Icons come from <a href="https://lucide.dev" target="_blank" rel="noopener
noreferrer" class="font-medium underline underline-offset-4">Lucide</a>,
under the ISC license. The full notice ships with the component, in
`icon/LICENSE`.
:::pt-br
## Licença

Os ícones vêm do <a href="https://lucide.dev" target="_blank" rel="noopener
noreferrer" class="font-medium underline underline-offset-4">Lucide</a>,
sob a licença ISC. O aviso completo vem com o componente, em `icon/LICENSE`.
:::

:::en
## API reference
:::pt-br
## Referência da API
:::

<c-docs.api-reference name="icon" />
