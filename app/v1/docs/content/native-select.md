---
title: Native Select
description: The browser's own select element, styled to match the library.
description.pt-br: O select nativo do navegador, estilizado como o resto da biblioteca.
description.es: El select nativo del navegador, estilizado como el resto de la biblioteca.
---

<c-docs.demo-section class="min-h-[350px]">
<c-native-select>
<c-native-select.option value="light">Light</c-native-select.option>
<c-native-select.option value="dark">Dark</c-native-select.option>
<c-native-select.option value="system">System</c-native-select.option>
</c-native-select>
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add native_select
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-native-select name="theme">
  <c-native-select.option value="light">Light</c-native-select.option>
  <c-native-select.option value="dark">Dark</c-native-select.option>
</c-native-select>
```

:::en
A real `&lt;select&gt;`, so it submits with the form, works without
JavaScript and opens the platform picker on mobile. Reach for <a
href="{% url 'page' slug='select' %}" class="font-medium underline underline-offset-4">Select</a>
when you need custom option markup.

## Examples

### Small
:::pt-br
Um `&lt;select&gt;` de verdade, então ele é enviado com o formulário, funciona
sem JavaScript e abre o seletor da plataforma no celular. Recorra ao <a
href="{% url 'page' slug='select' %}" class="font-medium underline underline-offset-4">Select</a>
quando precisar de markup próprio nas opções.

## Exemplos

### Pequeno
:::

<c-docs.demo-section>
<c-native-select size="sm">
<c-native-select.option value="10">10 per page</c-native-select.option>
<c-native-select.option value="25">25 per page</c-native-select.option>
<c-native-select.option value="50">50 per page</c-native-select.option>
</c-native-select>
</c-docs.demo-section>

```html
<c-native-select size="sm">...</c-native-select>
```

:::en
### Grouped options
:::pt-br
### Opções agrupadas
:::

<c-docs.demo-section>
<c-native-select>
<c-native-select.optgroup label="Fruits">
<c-native-select.option value="apple">Apple</c-native-select.option>
<c-native-select.option value="banana">Banana</c-native-select.option>
</c-native-select.optgroup>
<c-native-select.optgroup label="Vegetables">
<c-native-select.option value="carrot">Carrot</c-native-select.option>
</c-native-select.optgroup>
</c-native-select>
</c-docs.demo-section>

```html
<c-native-select>
  <c-native-select.optgroup label="Fruits">
    <c-native-select.option value="apple">Apple</c-native-select.option>
  </c-native-select.optgroup>
</c-native-select>
```

:::en
### Disabled
:::pt-br
### Desabilitado
:::

<c-docs.demo-section>
<c-native-select disabled>
<c-native-select.option value="locked">Not available</c-native-select.option>
</c-native-select>
</c-docs.demo-section>

```html
<c-native-select disabled>...</c-native-select>
```

:::en
### Invalid
:::pt-br
### Inválido
:::

<c-docs.demo-section>
<c-native-select aria-invalid="true">
<c-native-select.option value="">Pick one</c-native-select.option>
<c-native-select.option value="a">Option A</c-native-select.option>
</c-native-select>
</c-docs.demo-section>

```html
<c-native-select aria-invalid="true">...</c-native-select>
```

:::en
### From a Django form
:::pt-br
### A partir de um formulário Django
:::

<c-docs.demo-section>
<c-native-select name="country">
{% for value, label in countries %}
<c-native-select.option value="{{ value }}">{{ label }}</c-native-select.option>
{% endfor %}
</c-native-select>
</c-docs.demo-section>

```html
<c-native-select name="country">
  {% for value, label in form.country.field.choices %}
  <c-native-select.option value="{{ value }}"
    >{{ label }}</c-native-select.option
  >
  {% endfor %}
</c-native-select>
```
