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

## Installation

```bash
uvx django_shadcn@latest add pagination
```

## Usage

<c-docs.demo-section>
<c-pagination>
<c-pagination.content>
<c-pagination.item><c-pagination.previous href="#" /></c-pagination.item>
<c-pagination.item><c-pagination.link href="#" is_active="true">1</c-pagination.link></c-pagination.item>
<c-pagination.item><c-pagination.link href="#">2</c-pagination.link></c-pagination.item>
<c-pagination.item><c-pagination.next href="#" /></c-pagination.item>
</c-pagination.content>
</c-pagination>
</c-docs.demo-section>

```html
<c-pagination>
    <c-pagination.content>
        <c-pagination.item><c-pagination.previous href="#" /></c-pagination.item>
        <c-pagination.item>
            <c-pagination.link href="#" is_active="true">1</c-pagination.link>
        </c-pagination.item>
        <c-pagination.item><c-pagination.link href="#">2</c-pagination.link></c-pagination.item>
        <c-pagination.item><c-pagination.next href="#" /></c-pagination.item>
    </c-pagination.content>
</c-pagination>
```

The current page is marked with `is_active="true"`, which switches the link to
the outline look and sets `aria-current="page"`.

## Examples

### With a Django paginator

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

### Custom labels

<c-docs.demo-section>
<c-pagination>
<c-pagination.content>
<c-pagination.item><c-pagination.previous href="#">Newer</c-pagination.previous></c-pagination.item>
<c-pagination.item><c-pagination.next href="#">Older</c-pagination.next></c-pagination.item>
</c-pagination.content>
</c-pagination>
</c-docs.demo-section>

```html
<c-pagination.previous href="#">Newer</c-pagination.previous>
<c-pagination.next href="#">Older</c-pagination.next>
```

## Notes

The labels beside the arrows are hidden below the `sm` breakpoint, so on a
phone the controls stay as two arrows.
