---
title: Sidebar
description: A composable, collapsible sidebar that remembers whether it was open.
description.pt-br: Uma sidebar composta e recolhível que lembra se estava aberta.
description.es: Una barra lateral componible y plegable que recuerda si estaba abierta.
---

<c-docs.demo-section>
<div class="relative h-[420px] w-full transform-gpu overflow-hidden rounded-lg border">
<c-sidebar.provider class="min-h-full!">
<c-sidebar class="h-full!">
<c-sidebar.header>
<c-sidebar.input placeholder="Search" />
</c-sidebar.header>
<c-sidebar.content>
<c-sidebar.group>
<c-sidebar.group-label>Workspace</c-sidebar.group-label>
<c-sidebar.group-content>
<c-sidebar.menu>
<c-sidebar.menu-item>
<c-sidebar.menu-button is_active="true" tooltip="Search">
<c-icon name="search" />
<span>Search</span>
</c-sidebar.menu-button>
</c-sidebar.menu-item>
<c-sidebar.menu-item>
<c-sidebar.menu-button tooltip="Drafts">
<c-icon name="circle" />
<span>Drafts</span>
</c-sidebar.menu-button>
<c-sidebar.menu-badge>7</c-sidebar.menu-badge>
</c-sidebar.menu-item>
<c-sidebar.menu-item>
<c-sidebar.menu-button tooltip="Done">
<c-icon name="check" />
<span>Done</span>
</c-sidebar.menu-button>
<c-sidebar.menu-action><c-icon name="ellipsis" /></c-sidebar.menu-action>
</c-sidebar.menu-item>
</c-sidebar.menu>
</c-sidebar.group-content>
</c-sidebar.group>
</c-sidebar.content>
<c-sidebar.footer>
<c-sidebar.menu>
<c-sidebar.menu-item>
<c-sidebar.menu-button tooltip="Account">
<c-icon name="circle" />
<span>Account</span>
</c-sidebar.menu-button>
</c-sidebar.menu-item>
</c-sidebar.menu>
</c-sidebar.footer>
<c-sidebar.rail />
</c-sidebar>
<c-sidebar.inset>
<header class="flex h-12 shrink-0 items-center gap-2 border-b px-4">
<c-sidebar.trigger />
<span class="text-sm font-medium">Inbox</span>
</header>
<div class="p-4 text-sm text-muted-foreground">
Toggle with the button, the rail on the panel's edge, or <c-kbd>⌘</c-kbd> <c-kbd>B</c-kbd>.
</div>
</c-sidebar.inset>
</c-sidebar.provider>
</div>
</c-docs.demo-section>

<c-docs.cheat-sheet name="sidebar">
<c-sidebar.provider>
    <c-sidebar>
        <c-sidebar.header>...</c-sidebar.header>
        <c-sidebar.content>
            <c-sidebar.group>
                <c-sidebar.group-label>Workspace</c-sidebar.group-label>
                <c-sidebar.group-content>
                    <c-sidebar.menu>
                        <c-sidebar.menu-item>
                            <c-sidebar.menu-button href="/inbox/" tooltip="Inbox">
                                <c-icon name="search" />
                                <span>Inbox</span>
                            </c-sidebar.menu-button>
                        </c-sidebar.menu-item>
                    </c-sidebar.menu>
                </c-sidebar.group-content>
            </c-sidebar.group>
        </c-sidebar.content>
        <c-sidebar.footer>...</c-sidebar.footer>
        <c-sidebar.rail />
    </c-sidebar>
    <c-sidebar.inset>
        <c-sidebar.trigger />
        {{ content }}
    </c-sidebar.inset>
</c-sidebar.provider>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add sidebar
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-sidebar.provider>
    <c-sidebar>
        <c-sidebar.header>...</c-sidebar.header>
        <c-sidebar.content>
            <c-sidebar.group>
                <c-sidebar.group-label>Workspace</c-sidebar.group-label>
                <c-sidebar.group-content>
                    <c-sidebar.menu>
                        <c-sidebar.menu-item>
                            <c-sidebar.menu-button href="/inbox/" tooltip="Inbox">
                                <c-icon name="search" />
                                <span>Inbox</span>
                            </c-sidebar.menu-button>
                        </c-sidebar.menu-item>
                    </c-sidebar.menu>
                </c-sidebar.group-content>
            </c-sidebar.group>
        </c-sidebar.content>
        <c-sidebar.footer>...</c-sidebar.footer>
        <c-sidebar.rail />
    </c-sidebar>
    <c-sidebar.inset>
        <c-sidebar.trigger />
        {{ content }}
    </c-sidebar.inset>
</c-sidebar.provider>
```

:::en
`<c-sidebar.provider>` holds the open state and has to wrap both the panel and
the page. Put it in your base template, around everything.

`<c-sidebar.inset>` is where the page goes. It must be a sibling that comes
after `<c-sidebar>` — the `inset` variant styles it from there.

A `<c-sidebar.menu-button>` with an `href` renders an `<a>`; without one it
renders a `<button>`. Mark the current page with `is_active="true"`.

## Remembering the state

Toggling writes a `sidebar_state` cookie. Read it back in the view so the
server renders the panel in the shape the visitor left it, instead of drawing
it expanded and letting it snap shut once Alpine boots:
:::pt-br
O `<c-sidebar.provider>` guarda o estado de aberto e precisa envolver tanto o
painel quanto a página. Ponha-o no seu template base, em volta de tudo.

O `<c-sidebar.inset>` é onde a página vai. Ele precisa ser um irmão que vem
depois do `<c-sidebar>` — a variante `inset` o estiliza a partir dali.

Um `<c-sidebar.menu-button>` com `href` renderiza um `<a>`; sem ele, renderiza
um `<button>`. Marque a página atual com `is_active="true"`.

## Lembrando o estado

Abrir e fechar grava um cookie `sidebar_state`. Leia-o de volta na view para que
o servidor renderize o painel do jeito que o visitante o deixou, em vez de
desenhá-lo aberto e deixá-lo fechar de repente quando o Alpine iniciar:
:::

```python
def dashboard(request):
    return render(request, "dashboard.html", {
        "sidebar_open": request.COOKIES.get("sidebar_state", "true"),
    })
```

```html
<c-sidebar.provider default_open="{{ sidebar_open }}">
```

:::en
## Examples

### Collapse to icons

`collapsible="icon"` keeps a rail of icons instead of sliding the whole panel
away. Labels, badges and sub-menus hide themselves; the `tooltip` on each
button takes over as the label.
:::pt-br
## Exemplos

### Recolher para ícones

`collapsible="icon"` mantém uma faixa de ícones em vez de deslizar o painel
inteiro para fora. Rótulos, badges e submenus se escondem sozinhos; o `tooltip`
de cada botão assume o papel de rótulo.
:::

<c-docs.example>
<div class="relative h-[300px] w-full transform-gpu overflow-hidden rounded-lg border">
  <c-sidebar.provider class="min-h-full!">
    <c-sidebar collapsible="icon" class="h-full!">
      <c-sidebar.content>
        <c-sidebar.group>
          <c-sidebar.group-label>Workspace</c-sidebar.group-label>
          <c-sidebar.group-content>
            <c-sidebar.menu>
              <c-sidebar.menu-item>
                <c-sidebar.menu-button tooltip="Search">
                  <c-icon name="search" />
                  <span>Search</span>
                </c-sidebar.menu-button>
              </c-sidebar.menu-item>
              <c-sidebar.menu-item>
                <c-sidebar.menu-button tooltip="Drafts">
                  <c-icon name="circle" />
                  <span>Drafts</span>
                </c-sidebar.menu-button>
              </c-sidebar.menu-item>
              <c-sidebar.menu-item>
                <c-sidebar.menu-button tooltip="Done">
                  <c-icon name="check" />
                  <span>Done</span>
                </c-sidebar.menu-button>
              </c-sidebar.menu-item>
            </c-sidebar.menu>
          </c-sidebar.group-content>
        </c-sidebar.group>
      </c-sidebar.content>
      <c-sidebar.rail />
    </c-sidebar>
    <c-sidebar.inset>
      <header class="flex h-12 shrink-0 items-center gap-2 border-b px-4">
        <c-sidebar.trigger />
        <span class="text-sm font-medium">Collapse me</span>
      </header>
    </c-sidebar.inset>
  </c-sidebar.provider>
</div>
</c-docs.example>

:::en
### Variants and side
:::pt-br
### Variantes e lado
:::

```html
<c-sidebar variant="floating">...</c-sidebar>
<c-sidebar variant="inset">...</c-sidebar>
<c-sidebar side="right">...</c-sidebar>
<c-sidebar collapsible="none">...</c-sidebar>
```

:::en
`floating` detaches the panel with a border and a radius. `inset` does the same
to the page instead, and needs the provider to sit on the sidebar background —
`has-data-[variant=inset]:bg-sidebar` already handles that. `none` drops the
toggle entirely and leaves a panel that is always there.

### Nested items
:::pt-br
`floating` destaca o painel com uma borda e um raio. `inset` faz o mesmo com a
página, e precisa que o provider fique sobre o fundo da sidebar —
`has-data-[variant=inset]:bg-sidebar` já cuida disso. `none` tira o botão de
alternar por completo e deixa um painel que está sempre ali.

### Itens aninhados
:::

```html
<c-sidebar.menu-item>
    <c-sidebar.menu-button>
        <span>Settings</span>
    </c-sidebar.menu-button>
    <c-sidebar.menu-sub>
        <c-sidebar.menu-sub-item>
            <c-sidebar.menu-sub-button href="/settings/team/" is_active="true">
                <span>Team</span>
            </c-sidebar.menu-sub-button>
        </c-sidebar.menu-sub-item>
    </c-sidebar.menu-sub>
</c-sidebar.menu-item>
```

:::en
Wrap the sub-menu in a [Collapsible]({% url 'page' slug='collapsible' %}) if
you want it to fold.

### Actions and badges
:::pt-br
Envolva o submenu num [Collapsible]({% url 'page' slug='collapsible' %}) se
quiser que ele se recolha.

### Ações e badges
:::

```html
<c-sidebar.menu-item>
    <c-sidebar.menu-button>
        <span>Done</span>
    </c-sidebar.menu-button>
    <c-sidebar.menu-action show_on_hover="true">
        <c-icon name="ellipsis" />
    </c-sidebar.menu-action>
</c-sidebar.menu-item>
```

:::en
Both the action and the badge sit on top of the button, so they go after it,
inside the same `<c-sidebar.menu-item>`. Only one of the two per item — they
claim the same corner.

### Loading placeholder
:::pt-br
Tanto a ação quanto o badge ficam sobre o botão, então vão depois dele, dentro
do mesmo `<c-sidebar.menu-item>`. Só um dos dois por item — eles disputam o
mesmo canto.

### Placeholder de carregamento
:::

<c-docs.example>
<div class="w-[240px] rounded-lg bg-sidebar p-2">
  <c-sidebar.menu>
    <c-sidebar.menu-item><c-sidebar.menu-skeleton show_icon="true" width="60%" /></c-sidebar.menu-item>
    <c-sidebar.menu-item><c-sidebar.menu-skeleton show_icon="true" width="85%" /></c-sidebar.menu-item>
    <c-sidebar.menu-item><c-sidebar.menu-skeleton show_icon="true" width="70%" /></c-sidebar.menu-item>
  </c-sidebar.menu>
</div>
</c-docs.example>


```html
<c-sidebar.provider style="--sidebar-width: 20rem">
```

:::en
`<c-sidebar.menu-button>` renders its `tooltip` as a plain sibling label
instead of composing [Tooltip]({% url 'page' slug='tooltip' %}), because the
badge and action rules position themselves against the button as a sibling and
a wrapper would break them.

The sidebar's own colour tokens — `--sidebar`, `--sidebar-accent`,
`--sidebar-border` and the rest — live in `input.css`. Restyle the panel there,
not with utility classes on each part.
:::pt-br
O `<c-sidebar.menu-button>` renderiza o `tooltip` como um rótulo irmão simples
em vez de compor o [Tooltip]({% url 'page' slug='tooltip' %}), porque as regras
do badge e da ação se posicionam em relação ao botão como irmão, e um elemento
em volta as quebraria.

Os tokens de cor da própria sidebar — `--sidebar`, `--sidebar-accent`,
`--sidebar-border` e o resto — moram no `input.css`. Mude o estilo do painel lá,
não com classes utilitárias em cada parte.
:::

:::en
## RTL

`side` names a side of the screen, so a sidebar on the left stays there under
`dir="rtl"`; pass `side="right"` for one at the start of an RTL page. The
menus inside follow the text.

## Accessibility

The menu is a list of links and buttons, so it is tabbed through like any
navigation, and `is_active="true"` marks the current page. <c-kbd>⌘</c-kbd> or
<c-kbd>Ctrl</c-kbd> with <c-kbd>B</c-kbd> toggles the panel, and Escape closes
it on a phone. In the icon rail, each button's `tooltip` names it.

## API reference
:::pt-br
## RTL

O `side` nomeia um lado da tela, então uma sidebar à esquerda fica ali sob
`dir="rtl"`; passe `side="right"` para uma no início de uma página RTL. Os
menus dentro acompanham o texto.

## Acessibilidade

O menu é uma lista de links e botões, então é percorrido pelo Tab como
qualquer navegação, e `is_active="true"` marca a página atual.
<c-kbd>⌘</c-kbd> ou <c-kbd>Ctrl</c-kbd> com <c-kbd>B</c-kbd> alterna o painel,
e o Escape o fecha num celular. Na faixa de ícones, o `tooltip` de cada botão
dá nome a ele.

## Referência da API
:::

<c-docs.api-reference name="sidebar" />

:::en
## Notes

Below `md` the panel slides in over a backdrop rather than becoming a
[Sheet]({% url 'page' slug='sheet' %}) as upstream does. One tree serves both
widths, so the menu is written once and there are no duplicate ids in the page.

The width comes from `--sidebar-width` and `--sidebar-width-icon`, set on the
provider. Override them with an inline style, which beats the defaults:
:::pt-br
## Observações

Abaixo de `md` o painel desliza por cima de um fundo escurecido em vez de virar
um [Sheet]({% url 'page' slug='sheet' %}) como faz o upstream. Uma árvore só
atende às duas larguras, então o menu é escrito uma vez e não há ids duplicados
na página.

A largura vem de `--sidebar-width` e `--sidebar-width-icon`, definidos no
provider. Sobrescreva-os com um estilo inline, que vence os padrões:
:::
