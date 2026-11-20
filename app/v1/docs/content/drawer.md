---
title: Drawer
description: A panel that slides in from an edge and can be dragged shut.
description.pt-br: Um painel que entra por uma borda e pode ser arrastado para fechar.
description.es: Un panel que entra desde un borde y se puede arrastrar para cerrar.
---

<c-docs.demo-section class="min-h-[350px]">
<c-drawer>
<c-drawer.trigger>
<c-button variant="outline">Open drawer</c-button>
</c-drawer.trigger>
<c-drawer.overlay />
<c-drawer.content>
<c-drawer.header>
<c-drawer.title>Move to folder</c-drawer.title>
<c-drawer.description>Pick where this should live.</c-drawer.description>
</c-drawer.header>
<div class="px-4 pb-2 text-sm text-muted-foreground">
Drag the handle down to dismiss, or press Escape.
</div>
<c-drawer.footer>
<c-button>Move</c-button>
<c-drawer.close>
<c-button variant="outline" class="w-full">Cancel</c-button>
</c-drawer.close>
</c-drawer.footer>
</c-drawer.content>
</c-drawer>
</c-docs.demo-section>

<c-docs.cheat-sheet name="drawer">
<c-drawer>
    <c-drawer.trigger>
        <c-button variant="outline">Open drawer</c-button>
    </c-drawer.trigger>
    <c-drawer.overlay />
    <c-drawer.content>
        <c-drawer.header>
            <c-drawer.title>Move to folder</c-drawer.title>
            <c-drawer.description>Pick where this should live.</c-drawer.description>
        </c-drawer.header>
        <c-drawer.footer>
            <c-button>Move</c-button>
            <c-drawer.close>
                <c-button variant="outline" class="w-full">Cancel</c-button>
            </c-drawer.close>
        </c-drawer.footer>
    </c-drawer.content>
</c-drawer>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add drawer
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-drawer>
    <c-drawer.trigger>
        <c-button variant="outline">Open drawer</c-button>
    </c-drawer.trigger>
    <c-drawer.overlay />
    <c-drawer.content>
        <c-drawer.header>
            <c-drawer.title>Move to folder</c-drawer.title>
            <c-drawer.description>Pick where this should live.</c-drawer.description>
        </c-drawer.header>
        <c-drawer.footer>
            <c-button>Move</c-button>
            <c-drawer.close>
                <c-button variant="outline" class="w-full">Cancel</c-button>
            </c-drawer.close>
        </c-drawer.footer>
    </c-drawer.content>
</c-drawer>
```

:::en
The grab handle at the top follows your pointer. Let go past about four tenths
of the panel's height and it closes; let go short of that and it springs back.
Escape and a click on the overlay close it too.

The overlay is a separate element, so you can leave it out for a drawer that
does not dim the page.

## Examples

### Direction
:::pt-br
A alça no topo acompanha o seu ponteiro. Solte depois de uns quatro décimos da
altura do painel e ele fecha; solte antes disso e ele volta. O Escape e um
clique no overlay também o fecham.

O overlay é um elemento à parte, então você pode deixá-lo de fora para um
drawer que não escurece a página.

## Exemplos

### Direção
:::

<c-docs.example>
<div class="flex items-center gap-3">
  <c-drawer direction="right">
    <c-drawer.trigger><c-button variant="outline" size="sm">Right</c-button></c-drawer.trigger>
    <c-drawer.overlay />
    <c-drawer.content>
      <c-drawer.header>
        <c-drawer.title>From the right</c-drawer.title>
        <c-drawer.description>No handle on this one.</c-drawer.description>
      </c-drawer.header>
    </c-drawer.content>
  </c-drawer>
  <c-drawer direction="top">
    <c-drawer.trigger><c-button variant="outline" size="sm">Top</c-button></c-drawer.trigger>
    <c-drawer.overlay />
    <c-drawer.content>
      <c-drawer.header>
        <c-drawer.title>From the top</c-drawer.title>
        <c-drawer.description>Useful for a notification tray.</c-drawer.description>
      </c-drawer.header>
    </c-drawer.content>
  </c-drawer>
</div>
</c-docs.example>

:::en
### Without the overlay
:::pt-br
### Sem o overlay
:::

<c-docs.example>
<c-drawer>
  <c-drawer.trigger><c-button variant="outline">No dimming</c-button></c-drawer.trigger>
  <c-drawer.content>
    <c-drawer.header>
      <c-drawer.title>The page stays lit</c-drawer.title>
      <c-drawer.description>Drop the overlay when the drawer is not modal.</c-drawer.description>
    </c-drawer.header>
    <c-drawer.footer>
      <c-drawer.close><c-button variant="outline" class="w-full">Close</c-button></c-drawer.close>
    </c-drawer.footer>
  </c-drawer.content>
</c-drawer>
</c-docs.example>

:::en
### Scrollable content

Long content scrolls inside the drawer while the header stays put: give the
body a height and `overflow-y-auto`.
:::pt-br
### Conteúdo com rolagem

Um conteúdo longo rola dentro do drawer enquanto o cabeçalho fica no lugar:
dê ao corpo uma altura e `overflow-y-auto`.
:::

<c-docs.example>
<c-drawer>
  <c-drawer.trigger><c-button variant="outline">Release notes</c-button></c-drawer.trigger>
  <c-drawer.overlay />
  <c-drawer.content>
    <c-drawer.header>
      <c-drawer.title>What changed in 1.11</c-drawer.title>
    </c-drawer.header>
    <div class="max-h-60 space-y-3 overflow-y-auto px-4 pb-4 text-sm text-muted-foreground">
      {% for n in "123456" %}
        <p>A change worth reading about, number {{ n }}, with a sentence on what it means for your templates.</p>
      {% endfor %}
    </div>
  </c-drawer.content>
</c-drawer>
</c-docs.example>

:::en
## RTL

`direction` names a side of the screen, so a drawer from the left stays on
the left under `dir="rtl"`, and its border with it. The contents follow the
text.

## Accessibility

The content is a `role="dialog"` with `aria-modal="true"`, and Escape closes
it. Focus is not moved into the drawer or trapped there, so put the first
thing to do near its top, and dragging the handle is a pointer gesture only:
keep a close button for the keyboard.

## API reference
:::pt-br
## RTL

`direction` nomeia um lado da tela, então um drawer da esquerda continua à
esquerda sob `dir="rtl"`, e a borda dele também. O conteúdo acompanha o
texto.

## Acessibilidade

O conteúdo é um `role="dialog"` com `aria-modal="true"`, e o Escape o fecha.
O foco não é levado para dentro do drawer nem preso ali, então ponha a primeira
coisa a fazer perto do topo dele, e arrastar a alça é um gesto só de ponteiro:
mantenha um botão de fechar para o teclado.

## Referência da API
:::

<c-docs.api-reference name="drawer" />

:::en
## Notes

Upstream builds on `vaul`, which adds momentum, snap points that let the panel
rest at intermediate heights, and a scaling effect on the page behind. None of
that is reproduced. What is here is the part people actually use: a panel from
the edge, a handle, and drag to dismiss.

**Dragging works on the bottom drawer only** — the handle appears there and
nowhere else, which is upstream's own arrangement. The other directions open
and close by click, Escape and the overlay.

If you only need a panel from an edge, [Sheet]({% url 'page' slug='sheet' %})
covers that with less machinery. Reach for the drawer when the drag matters.

The directional classes come from the registry, with `data-vaul-drawer-direction`
renamed to `data-direction` — carrying a library name for a library we do not
ship would be misleading.
:::pt-br
## Observações

O upstream se apoia no `vaul`, que acrescenta embalo, pontos de parada que
deixam o painel descansar em alturas intermediárias e um efeito de escala na
página de trás. Nada disso é reproduzido. O que está aqui é a parte que as
pessoas realmente usam: um painel vindo da borda, uma alça e arrastar para
fechar.

**Arrastar só funciona no drawer de baixo** — a alça aparece ali e em nenhum
outro lugar, que é o arranjo do próprio upstream. As outras direções abrem e
fecham com clique, Escape e o overlay.

Se você só precisa de um painel vindo de uma borda, o
[Sheet]({% url 'page' slug='sheet' %}) resolve isso com menos maquinário. Use o
drawer quando o arrastar importar.

As classes de direção vêm do registry, com `data-vaul-drawer-direction`
renomeado para `data-direction` — levar o nome de uma biblioteca que não
distribuímos seria enganoso.
:::
