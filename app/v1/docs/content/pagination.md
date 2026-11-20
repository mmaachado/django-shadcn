---
title: Pagination
description: Navigation between pages of a list.
description.pt-br: Navegação entre páginas de uma listagem.
description.es: Navegación entre páginas de un listado.
---

<c-docs.demo-section class="min-h-[350px]">
<c-pagination>
<c-pagination.content>
<c-pagination.item><c-pagination.previous href="#" /></c-pagination.item>
<c-pagination.item><c-pagination.link href="#">1</c-pagination.link></c-pagination.item>
<c-pagination.item><c-pagination.link href="#" is_active="true">2</c-pagination.link></c-pagination.item>
<c-pagination.item><c-pagination.link href="#">3</c-pagination.link></c-pagination.item>
<c-pagination.item><c-pagination.ellipsis /></c-pagination.item>
<c-pagination.item><c-pagination.next href="#" /></c-pagination.item>
</c-pagination.content>
</c-pagination>
</c-docs.demo-section>

<c-docs.cheat-sheet name="pagination">
<c-pagination>
  <c-pagination.content>
    <c-pagination.item><c-pagination.previous href="#" /></c-pagination.item>
    <c-pagination.item><c-pagination.link href="#" is_active="true">1</c-pagination.link></c-pagination.item>
    <c-pagination.item><c-pagination.link href="#">2</c-pagination.link></c-pagination.item>
    <c-pagination.item><c-pagination.next href="#" /></c-pagination.item>
  </c-pagination.content>
</c-pagination>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add pagination
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-pagination>
  <c-pagination.content>
    <c-pagination.item><c-pagination.previous href="#" /></c-pagination.item>
    <c-pagination.item><c-pagination.link href="#" is_active="true">1</c-pagination.link></c-pagination.item>
    <c-pagination.item><c-pagination.link href="#">2</c-pagination.link></c-pagination.item>
    <c-pagination.item><c-pagination.next href="#" /></c-pagination.item>
  </c-pagination.content>
</c-pagination>
</c-docs.example>

:::en
The current page is marked with `is_active="true"`, which switches the link to
the outline look and sets `aria-current="page"`.

## Examples

### With a Django paginator
:::pt-br
A página atual é marcada com `is_active="true"`, que troca o link para o visual
outline e define `aria-current="page"`.

## Exemplos

### Com um paginator do Django
:::

```html
<c-pagination>
    <c-pagination.content>
        {% if page_obj.has_previous %}
            <c-pagination.item>
                <c-pagination.previous href="?page={{ page_obj.previous_page_number }}" />
            </c-pagination.item>
        {% endif %}

        {% for number in page_obj.paginator.page_range %}
            <c-pagination.item>
                <c-pagination.link
                    href="?page={{ number }}"
                    is_active="{% if number == page_obj.number %}true{% else %}false{% endif %}"
                >{{ number }}</c-pagination.link>
            </c-pagination.item>
        {% endfor %}

        {% if page_obj.has_next %}
            <c-pagination.item>
                <c-pagination.next href="?page={{ page_obj.next_page_number }}" />
            </c-pagination.item>
        {% endif %}
    </c-pagination.content>
</c-pagination>
```

:::en
### Custom labels
:::pt-br
### Rótulos personalizados
:::

<c-docs.example>
<c-pagination>
  <c-pagination.content>
    <c-pagination.item><c-pagination.previous href="#">Newer</c-pagination.previous></c-pagination.item>
    <c-pagination.item><c-pagination.next href="#">Older</c-pagination.next></c-pagination.item>
  </c-pagination.content>
</c-pagination>
</c-docs.example>

:::en
## Notes

The labels beside the arrows are hidden below the `sm` breakpoint, so on a
phone the controls stay as two arrows.
:::pt-br
## Observações

Os rótulos ao lado das setas ficam escondidos abaixo do breakpoint `sm`, então
num celular os controles continuam sendo duas setas.
:::

:::en
## API reference
:::pt-br
## Referência da API
:::

<c-docs.api-reference name="pagination" />
