---
title: Theming
description: The tokens in input.css, what each one colours, and how to change the palette, the radius and dark mode.
description.pt-br: Os tokens do input.css, o que cada um colore e como mudar a paleta, o raio e o modo escuro.
description.es: Los tokens de input.css, qué colorea cada uno y cómo cambiar la paleta, el radio y el modo oscuro.
---

:::en
## Where the theme lives

`init` copies one file into your project, `input.css`, and every component
reads its colours and its radius from it. Nothing in the components is a fixed
colour: `bg-primary`, `border-input` or `text-muted-foreground` are names, and
the file decides what they are. Change a value there and every component
follows, with no template to touch.

The file has three parts. `:root` holds the light values, `.dark` the dark
ones, and `@theme inline` turns each variable into a Tailwind colour, so
`--primary` becomes the `bg-primary`, `text-primary` and `border-primary`
utilities.
:::pt-br
## Onde o tema mora

O `init` copia um arquivo para o seu projeto, o `input.css`, e todo componente
lê as cores e o raio dele. Nada nos componentes é uma cor fixa: `bg-primary`,
`border-input` ou `text-muted-foreground` são nomes, e o arquivo decide o que
eles são. Mude um valor ali e todo componente acompanha, sem mexer em nenhum
template.

O arquivo tem três partes. O `:root` guarda os valores claros, o `.dark` os
escuros, e o `@theme inline` transforma cada variável numa cor do Tailwind,
então `--primary` vira os utilitários `bg-primary`, `text-primary` e
`border-primary`.
:::

```css
:root {
  --primary: oklch(0.205 0 0);
  --primary-foreground: oklch(0.985 0 0);
}

.dark {
  --primary: oklch(0.985 0 0);
  --primary-foreground: oklch(0.205 0 0);
}
```

:::en
## The tokens

Colours come in pairs: the surface, and `-foreground` for the text on it.

| Token | What it colours |
| --- | --- |
| `background`, `foreground` | the page and its text |
| `card`, `card-foreground` | cards |
| `popover`, `popover-foreground` | menus, popovers, tooltips |
| `primary`, `primary-foreground` | the default button, the checked checkbox and switch, the active badge |
| `secondary`, `secondary-foreground` | secondary buttons and badges |
| `muted`, `muted-foreground` | quiet surfaces, and descriptions and placeholders |
| `accent`, `accent-foreground` | hovered and highlighted items in menus and lists |
| `destructive`, `destructive-foreground` | errors and destructive actions |
| `border` | borders and separators |
| `input` | the border of fields |
| `ring` | focus rings |
| `chart-1` to `chart-5` | the series of a chart, in order |
| `sidebar` and its own set | the sidebar, which can differ from the page |

`--radius` is the corner of a card, and `rounded-sm`, `rounded-md` and
`rounded-lg` are worked out from it, so one value rounds or squares the whole
library.
:::pt-br
## Os tokens

As cores vêm em pares: a superfície, e `-foreground` para o texto sobre ela.

| Token | O que ele colore |
| --- | --- |
| `background`, `foreground` | a página e o texto dela |
| `card`, `card-foreground` | os cards |
| `popover`, `popover-foreground` | menus, popovers, tooltips |
| `primary`, `primary-foreground` | o botão padrão, o checkbox e o switch marcados, o badge ativo |
| `secondary`, `secondary-foreground` | botões e badges secundários |
| `muted`, `muted-foreground` | superfícies discretas, e descrições e placeholders |
| `accent`, `accent-foreground` | itens com hover e realçados em menus e listas |
| `destructive`, `destructive-foreground` | erros e ações destrutivas |
| `border` | bordas e separadores |
| `input` | a borda dos campos |
| `ring` | os anéis de foco |
| `chart-1` a `chart-5` | as séries de um gráfico, em ordem |
| `sidebar` e o conjunto dele | a sidebar, que pode ser diferente da página |

O `--radius` é o canto de um card, e `rounded-sm`, `rounded-md` e `rounded-lg`
são calculados a partir dele, então um valor só arredonda ou deixa quadrada a
biblioteca inteira.
:::

:::en
## Changing the palette

Edit the values in place, in both `:root` and `.dark`. They are `oklch()`,
lightness, chroma and hue, which keeps a colour's lightness steady as you move
its hue; hex and `hsl()` work too. A blue primary:
:::pt-br
## Mudando a paleta

Edite os valores no lugar, tanto no `:root` quanto no `.dark`. Eles são
`oklch()`, luminosidade, croma e matiz, o que mantém a luminosidade de uma cor
estável enquanto você muda a matiz; hex e `hsl()` também funcionam. Um primary
azul:
:::

```css
:root {
  --primary: oklch(0.546 0.245 262.881);
  --primary-foreground: oklch(0.985 0 0);
  --ring: oklch(0.546 0.245 262.881);
}
```

:::en
Keep each foreground readable on its surface: when a surface gets darker, its
foreground gets lighter. And rebuild the stylesheet afterwards, since the
values are compiled into it.

`init` never overwrites the file you have changed, and says so when it finds
one. `init --force` puts the shipped one back.

## Dark mode

The dark values apply under the `dark` class, on any ancestor: put it on
`<html>`. Choosing when is yours. This snippet follows the visitor's system and
remembers a choice, and runs in the `<head>`, before the first paint, so the
page never flashes the wrong theme:
:::pt-br
Mantenha cada foreground legível sobre a superfície dele: quando uma superfície
escurece, o foreground clareia. E recompile a folha de estilo depois, já que os
valores são compilados nela.

O `init` nunca sobrescreve o arquivo que você mudou, e avisa quando encontra
um. O `init --force` traz de volta o que vem com a biblioteca.

## Modo escuro

Os valores escuros valem sob a classe `dark`, em qualquer ancestral: ponha-a no
`<html>`. Escolher quando é com você. Este trecho segue o sistema de quem visita
e lembra uma escolha, e roda no `<head>`, antes da primeira pintura, para a
página nunca piscar no tema errado:
:::

```html
<script>
  (function () {
    var stored = localStorage.getItem('theme');
    var dark = stored ? stored === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
    document.documentElement.classList.toggle('dark', dark);
  })();
</script>
```

:::en
A button that toggles the class and stores the choice completes it:
:::pt-br
Um botão que alterna a classe e guarda a escolha completa o trabalho:
:::

```html
<c-button variant="ghost" size="icon" aria-label="Toggle theme"
  x-data x-on:click="localStorage.setItem('theme', document.documentElement.classList.toggle('dark') ? 'dark' : 'light')">
  <c-icon name="circle" />
</c-button>
```

:::en
## Charts

A chart's series take `--chart-1` to `--chart-5` in order, unless its config
names a colour. They are defined for light and dark, so a chart changes with
the theme without any JavaScript running again, and a project that themes the
tokens themes its charts too. See [Chart]({% url 'page' slug='chart' %}).

## The sidebar

The sidebar has its own set of tokens, `--sidebar`, `--sidebar-primary`,
`--sidebar-accent`, `--sidebar-border` and the rest, so the panel can sit on a
different surface from the page. Restyle it there rather than with classes on
each part.
:::pt-br
## Gráficos

As séries de um gráfico usam `--chart-1` a `--chart-5` em ordem, a menos que o
config dele nomeie uma cor. Eles são definidos para o claro e o escuro, então
um gráfico muda com o tema sem nenhum JavaScript rodar de novo, e um projeto
que personaliza os tokens personaliza os gráficos também. Veja o
[Chart]({% url 'page' slug='chart' %}).

## A sidebar

A sidebar tem o próprio conjunto de tokens, `--sidebar`, `--sidebar-primary`,
`--sidebar-accent`, `--sidebar-border` e o resto, para que o painel possa ficar
sobre uma superfície diferente da página. Mude o estilo dele ali, e não com
classes em cada parte.
:::
