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

## Installation

```bash
uvx django_shadcn@latest add native_select
```

## Usage

```html
<c-native-select name="theme">
  <c-native-select.option value="light">Light</c-native-select.option>
  <c-native-select.option value="dark">Dark</c-native-select.option>
</c-native-select>
```

A real `&lt;select&gt;`, so it submits with the form, works without
JavaScript and opens the platform picker on mobile. Reach for <a
href="{% url 'page' slug='select' %}" class="font-medium underline underline-offset-4">Select</a>
when you need custom option markup.

## Examples

### Small

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

### Grouped options

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

### Disabled

<c-docs.demo-section>
<c-native-select disabled>
<c-native-select.option value="locked">Not available</c-native-select.option>
</c-native-select>
</c-docs.demo-section>

```html
<c-native-select disabled>...</c-native-select>
```

### Invalid

<c-docs.demo-section>
<c-native-select aria-invalid="true">
<c-native-select.option value="">Pick one</c-native-select.option>
<c-native-select.option value="a">Option A</c-native-select.option>
</c-native-select>
</c-docs.demo-section>

```html
<c-native-select aria-invalid="true">...</c-native-select>
```

### From a Django form

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
