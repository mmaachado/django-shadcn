---
title: Data Table
description: Sorting, filtering and pagination built on the queryset, not on the client.
description.pt-br: Ordenação, filtro e paginação sobre o queryset, e não no cliente.
description.es: Ordenación, filtrado y paginación sobre el queryset, no en el cliente.
---

<c-docs.demo-section>
<div class="w-full">
<div class="flex items-center gap-2 pb-4">
<c-input placeholder="Filter emails..." class="max-w-sm" />
<c-button variant="outline" size="sm" class="ml-auto">Columns <c-icon name="chevron-down" /></c-button>
</div>
<div class="rounded-md border">
<c-table>
<c-table.header>
<c-table.row>
<c-table.head class="w-10"><c-checkbox /></c-table.head>
<c-table.head>Status</c-table.head>
<c-table.head><span class="inline-flex items-center gap-1 font-medium text-foreground">Email <c-icon name="chevron-down" class="size-4 rotate-180" /></span></c-table.head>
<c-table.head class="text-right">Amount</c-table.head>
</c-table.row>
</c-table.header>
<c-table.body>
<c-table.row>
<c-table.cell><c-checkbox /></c-table.cell>
<c-table.cell><c-badge variant="secondary">Success</c-badge></c-table.cell>
<c-table.cell>abe45@example.com</c-table.cell>
<c-table.cell class="text-right tabular-nums">$242.00</c-table.cell>
</c-table.row>
<c-table.row data-state="selected">
<c-table.cell><c-checkbox checked="checked" /></c-table.cell>
<c-table.cell><c-badge variant="outline">Processing</c-badge></c-table.cell>
<c-table.cell>carmella@example.com</c-table.cell>
<c-table.cell class="text-right tabular-nums">$721.00</c-table.cell>
</c-table.row>
<c-table.row>
<c-table.cell><c-checkbox /></c-table.cell>
<c-table.cell><c-badge variant="destructive">Failed</c-badge></c-table.cell>
<c-table.cell>monserrat@example.com</c-table.cell>
<c-table.cell class="text-right tabular-nums">$836.00</c-table.cell>
</c-table.row>
<c-table.row>
<c-table.cell><c-checkbox /></c-table.cell>
<c-table.cell><c-badge variant="secondary">Success</c-badge></c-table.cell>
<c-table.cell>silas22@example.com</c-table.cell>
<c-table.cell class="text-right tabular-nums">$174.00</c-table.cell>
</c-table.row>
</c-table.body>
</c-table>
</div>
<div class="flex items-center justify-between pt-4">
<span class="shrink-0 text-sm text-muted-foreground">1 of 4 row(s) selected.</span>
<c-pagination class="mx-0 w-auto justify-end">
<c-pagination.content>
<c-pagination.item><c-pagination.previous href="#" /></c-pagination.item>
<c-pagination.item><c-pagination.link href="#" is_active="true">1</c-pagination.link></c-pagination.item>
<c-pagination.item><c-pagination.link href="#">2</c-pagination.link></c-pagination.item>
<c-pagination.item><c-pagination.ellipsis /></c-pagination.item>
<c-pagination.item><c-pagination.link href="#">9</c-pagination.link></c-pagination.item>
<c-pagination.item><c-pagination.next href="#" /></c-pagination.item>
</c-pagination.content>
</c-pagination>
</div>
</div>
</c-docs.demo-section>

There is nothing to install called `data-table`. Upstream ships one because React has no
idea how to sort a list of rows — TanStack Table does the sorting, filtering and
paging in the browser, and the component wires it to the markup.

Django already has that engine. `order_by`, `filter` and `Paginator` do the work,
the answer arrives already sorted and already sliced, and the page is a table
plus a few links. What follows is that wiring.

## Installation

```bash
uvx django_shadcn@latest add table pagination input checkbox button badge dropdown_menu
```

## The view

One view reads three query parameters and hands back a page of rows.

```python
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

COLUMNS = [("status", "Status"), ("email", "Email"), ("amount", "Amount")]
SORTABLE = {name for name, _ in COLUMNS}


def columns_for(sort):
    """Each column, plus the ordering its header should ask for next."""
    for name, label in COLUMNS:
        active = sort.lstrip("-") == name
        descending = active and sort.startswith("-")
        yield {
            "label": label,
            "next": f"-{name}" if active and not descending else name,
            "direction": "desc" if descending else "asc" if active else "",
        }


def invoices(request):
    query = request.GET.get("q", "")
    sort = request.GET.get("sort", "email")

    rows = Invoice.objects.all()
    if query:
        rows = rows.filter(Q(email__icontains=query))
    if sort.lstrip("-") in SORTABLE:
        rows = rows.order_by(sort)

    page = Paginator(rows, 10).get_page(request.GET.get("page"))

    return render(request, "invoices.html", {
        "page": page,
        "query": query,
        "columns": columns_for(sort),
        "page_range": page.paginator.get_elided_page_range(page.number),
    })
```

`SORTABLE` is not decoration. `order_by` takes whatever string you give it,
including one that walks a relation — `?sort=author__user__password` is a
`FieldError` at best and a disclosure at worst. Sort only by names you wrote
down yourself.

## The template

```html
<form method="get" class="flex items-center gap-2 pb-4">
    <c-input name="q" value="{{ query }}" placeholder="Filter emails..." class="max-w-sm" />
</form>

<div class="rounded-md border">
    <c-table>
        <c-table.header>
            <c-table.row>
                {% for column in columns %}
                <c-table.head>
                    <a href="{% querystring sort=column.next page=None %}"
                       class="inline-flex items-center gap-1 hover:text-foreground">
                        {{ column.label }}
                        {% if column.direction == "asc" %}
                        <c-icon name="chevron-down" class="size-4 rotate-180" />
                        {% elif column.direction == "desc" %}
                        <c-icon name="chevron-down" class="size-4" />
                        {% else %}
                        <c-icon name="chevrons-up-down" class="size-4 opacity-50" />
                        {% endif %}
                    </a>
                </c-table.head>
                {% endfor %}
            </c-table.row>
        </c-table.header>
        <c-table.body>
            {% for invoice in page %}
            <c-table.row>
                <c-table.cell>{{ invoice.status }}</c-table.cell>
                <c-table.cell>{{ invoice.email }}</c-table.cell>
                <c-table.cell class="text-right tabular-nums">{{ invoice.amount }}</c-table.cell>
            </c-table.row>
            {% empty %}
            <c-table.empty>No results.</c-table.empty>
            {% endfor %}
        </c-table.body>
    </c-table>
</div>
```

The filter form has no submit button because Enter submits it. Everything the
table needs travels in the query string, so a page is a URL you can bookmark
and send to someone.

## Pagination

`{% verbatim %}{% querystring %}{% endverbatim %}` rewrites one parameter and
keeps the rest, which is what makes the filter survive a page change. It landed
in Django 5.1, and it reads the request off the context — if you have trimmed
`django.template.context_processors.request` out of your settings, put it back.

```html
<c-pagination class="mx-0 w-auto justify-end">
    <c-pagination.content>
        {% if page.has_previous %}
        <c-pagination.item>
            <c-pagination.previous href="{% querystring page=page.previous_page_number %}" />
        </c-pagination.item>
        {% endif %}

        {% for number in page_range %}
        <c-pagination.item>
            {% if number == page.paginator.ELLIPSIS %}
            <c-pagination.ellipsis />
            {% elif number == page.number %}
            <c-pagination.link href="{% querystring page=number %}" is_active="true">{{ number }}</c-pagination.link>
            {% else %}
            <c-pagination.link href="{% querystring page=number %}">{{ number }}</c-pagination.link>
            {% endif %}
        </c-pagination.item>
        {% endfor %}

        {% if page.has_next %}
        <c-pagination.item>
            <c-pagination.next href="{% querystring page=page.next_page_number %}" />
        </c-pagination.item>
        {% endif %}
    </c-pagination.content>
</c-pagination>
```

`get_elided_page_range` yields page numbers with `Paginator.ELLIPSIS` standing
in for the gaps, which is exactly the shape
[Pagination]({% url 'page' slug='pagination' %}) draws. Ten thousand pages
render as seven links.

`is_active` cannot be worked out inside the tag — Django templates have no
inline comparison — so the current page is a separate branch.

## Row selection

Wrap the table in a form and give the checkboxes one name. The selection is a
list of ids in `request.POST`, which is all a bulk action needs.

```html
<form method="post">
    {% csrf_token %}
    <c-table>
        <c-table.body>
            {% for invoice in page %}
            <c-table.row x-data="{ selected: false }" :data-state="selected ? 'selected' : ''">
                <c-table.cell>
                    <c-checkbox name="selected" value="{{ invoice.pk }}" x-model="selected" />
                </c-table.cell>
                <c-table.cell>{{ invoice.email }}</c-table.cell>
            </c-table.row>
            {% endfor %}
        </c-table.body>
    </c-table>
    <c-button type="submit" name="action" value="archive" variant="outline" size="sm">
        Archive selected
    </c-button>
</form>
```

`<c-table.row>` already paints `data-[state=selected]:bg-muted`; the two lines
of Alpine only exist so the row highlights before the round trip.

## Column visibility

Nothing server-side to do here — the rows are already in the page.

```html
<div x-data="{ shown: { status: true, email: true, amount: true } }">
    <c-dropdown-menu>
        <c-dropdown-menu.trigger>
            <c-button variant="outline" size="sm">Columns <c-icon name="chevron-down" /></c-button>
        </c-dropdown-menu.trigger>
        <c-dropdown-menu.content>
            <template x-for="name in Object.keys(shown)" :key="name">
                <c-dropdown-menu.item @click.stop>
                    <label class="flex items-center gap-2 capitalize">
                        <c-checkbox x-model="shown[name]" />
                        <span x-text="name"></span>
                    </label>
                </c-dropdown-menu.item>
            </template>
        </c-dropdown-menu.content>
    </c-dropdown-menu>

    <c-table>
        <c-table.header>
            <c-table.row>
                <c-table.head x-show="shown.status">Status</c-table.head>
                <c-table.head x-show="shown.email">Email</c-table.head>
            </c-table.row>
        </c-table.header>
    </c-table>
</div>
```

Every `<th>` and its `<td>` need the same `x-show`. Two places per column, and
no way around it without a column loop in the body as well.

## Notes

Sorting happens in the database, so it sorts the whole table and not the ten
rows you can see. That is the difference people usually miss when they move a
client-side table to the server: with TanStack, clicking a header reorders the
current page; here it reorders everything and gives you the first page of the
new order.

Nothing on this page needs JavaScript except the two optional pieces —
selection highlighting and column visibility. The table works with it turned
off.

For a filter that reacts as you type, keep the form and let
[htmx](https://htmx.org) swap the table body on `keyup changed delay:300ms`.
The view does not change: it is the same query parameters, and the response is
the same markup.
