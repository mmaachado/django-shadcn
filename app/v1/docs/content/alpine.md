---
title: Alpine and JavaScript
description: The JavaScript the components rely on, the plugins some of them need, and what each one does with JavaScript off.
description.pt-br: O JavaScript de que os componentes dependem, os plugins de que alguns precisam e o que cada um faz com o JavaScript desligado.
description.es: El JavaScript del que dependen los componentes, los plugins que algunos necesitan y qué hace cada uno con JavaScript desactivado.
---

:::en
## Alpine, and nothing else

The interactive components are written with [Alpine.js](https://alpinejs.dev)
directives in the template: `x-data`, `x-show`, `@click`. There is no other
JavaScript to install, no bundle and no build step. Load Alpine once, in your
base template, with `defer`:
:::pt-br
## Alpine, e mais nada

Os componentes interativos são escritos com diretivas do
[Alpine.js](https://alpinejs.dev) no template: `x-data`, `x-show`, `@click`.
Não há outro JavaScript para instalar, nenhum bundle e nenhuma etapa de build.
Carregue o Alpine uma vez, no seu template base, com `defer`:
:::

```html
<script src="{% static 'js/alpine.min.js' %}" defer></script>
```

:::en
Serving it from your own static files keeps the page working offline and does
not trust a CDN at run time. From a CDN, pin the version instead of tracking
`latest`.

Components with no behaviour, such as a badge, a card or a table, are markup
and CSS and need no JavaScript at all.

## Plugins

Some components use an Alpine plugin that Alpine's core does not include. The
registry declares it, and `add` names it once at the end of a run:
:::pt-br
Servi-lo dos seus próprios arquivos estáticos mantém a página funcionando
offline e não confia num CDN em tempo de execução. Vindo de um CDN, fixe a
versão em vez de acompanhar a `latest`.

Componentes sem comportamento, como um badge, um card ou uma tabela, são markup
e CSS e não precisam de JavaScript nenhum.

## Plugins

Alguns componentes usam um plugin do Alpine que o núcleo do Alpine não traz. O
registry o declara, e o `add` o cita uma vez no fim de uma execução:
:::

```text
@alpinejs/collapse must be loaded before Alpine, or these components render without behaving.
```

:::en
Today there is one, `@alpinejs/collapse`, for the height animation of
`accordion`, `collapsible` and `trace`, and so of `bubble`, which brings
`collapsible` along. Load it before Alpine itself:
:::pt-br
Hoje há um, o `@alpinejs/collapse`, para a animação de altura do `accordion`,
do `collapsible` e do `trace`, e portanto do `bubble`, que traz o
`collapsible` junto. Carregue-o antes do próprio Alpine:
:::

```html
<script src="{% static 'js/collapse.min.js' %}" defer></script>
<script src="{% static 'js/alpine.min.js' %}" defer></script>
```

:::en
A missing plugin fails quietly: the component renders, nothing appears in the
console, and the panel opens and closes without its animation. That is why the
warning is worth reading.

## x-cloak

`input.css` hides anything carrying `x-cloak` until Alpine starts and removes
the attribute. That is what keeps a dialog, a menu or a closed panel from
showing open for a moment while the page loads. Keep the rule if you replace
the file.

## Swapped content

Alpine starts the components in markup added after the page loads, so a menu
or a date picker inside a fragment swapped in by htmx behaves as on first load.
See [Forms and Django]({% url 'page' slug='forms' %}) for a form swapped in
place.

## With JavaScript off

A component built on Alpine does less without it, and some do nothing. This is
what each one keeps:
:::pt-br
Um plugin que falta falha em silêncio: o componente renderiza, nada aparece no
console, e o painel abre e fecha sem a animação. É por isso que vale ler o
aviso.

## x-cloak

O `input.css` esconde tudo o que leva `x-cloak` até o Alpine começar e remover
o atributo. É isso que impede um diálogo, um menu ou um painel fechado de
aparecer aberto por um instante enquanto a página carrega. Mantenha a regra se
você substituir o arquivo.

## Conteúdo trocado

O Alpine inicia os componentes de um markup acrescentado depois de a página
carregar, então um menu ou um date picker dentro de um fragmento trocado pelo
htmx se comporta como no primeiro carregamento. Veja o
[Forms and Django]({% url 'page' slug='forms' %}) para um formulário trocado no
lugar.

## Com o JavaScript desligado

Um componente feito sobre o Alpine faz menos sem ele, e alguns não fazem nada.
Isto é o que cada um mantém:
:::

:::en
| Component | Without JavaScript |
| --- | --- |
| `questionnaire`, `tabs`, `message_scroller` | every question, panel or row shows, and the form still posts |
| `carousel` | the slides are still a scrollable list; the arrows and dots do nothing |
| `slider` | the value still moves and posts; the drawn track shows empty, with the thumb at the start |
| `input_otp` | the field still takes and posts the code; the boxes stay empty |
| `code_block` | the code shows; the copy button does nothing |
| `avatar` | the initials show; a broken image is not removed |
| `sidebar`, `resizable` | the layout shows at its default; nothing toggles or drags |
| `command` | every item shows; picking one does nothing |
| `accordion`, `collapsible`, `trace` | closed panels stay closed |
| `calendar`, `chart` | nothing is drawn |
| `select`, `combobox`, `date_picker` | nothing can be chosen or posted |
| `dialog`, `alert_dialog`, `sheet`, `drawer`, `command_dialog`, `popover`, `hover_card`, `tooltip`, `dropdown_menu`, `menubar`, `navigation_menu`, `toast` | nothing opens |
| `context_menu` | a right click opens the browser's own menu |
| `toggle`, `toggle_group`, `input_group` | they render; pressing or clicking an addon does nothing |

For a form that must work without JavaScript, the native controls are the safe
choice: [Native Select]({% url 'page' slug='native-select' %}),
[Checkbox]({% url 'page' slug='checkbox' %}),
[Radio Group]({% url 'page' slug='radio-group' %}),
[Switch]({% url 'page' slug='switch' %}) and
[Input]({% url 'page' slug='input' %}).
:::pt-br
| Componente | Sem JavaScript |
| --- | --- |
| `questionnaire`, `tabs`, `message_scroller` | toda pergunta, painel ou linha aparece, e o formulário continua enviando |
| `carousel` | os slides continuam uma lista rolável; as setas e os pontos não fazem nada |
| `slider` | o valor continua mudando e sendo enviado; a trilha desenhada aparece vazia, com o puxador no início |
| `input_otp` | o campo continua recebendo e enviando o código; as caixas ficam vazias |
| `code_block` | o código aparece; o botão de copiar não faz nada |
| `avatar` | as iniciais aparecem; uma imagem quebrada não é removida |
| `sidebar`, `resizable` | o layout aparece no padrão; nada alterna nem arrasta |
| `command` | todo item aparece; escolher um não faz nada |
| `accordion`, `collapsible`, `trace` | os painéis fechados continuam fechados |
| `calendar`, `chart` | nada é desenhado |
| `select`, `combobox`, `date_picker` | nada pode ser escolhido nem enviado |
| `dialog`, `alert_dialog`, `sheet`, `drawer`, `command_dialog`, `popover`, `hover_card`, `tooltip`, `dropdown_menu`, `menubar`, `navigation_menu`, `toast` | nada abre |
| `context_menu` | um clique com o botão direito abre o menu do próprio navegador |
| `toggle`, `toggle_group`, `input_group` | renderizam; pressionar ou clicar num addon não faz nada |

Para um formulário que precisa funcionar sem JavaScript, os controles nativos
são a escolha segura: [Native Select]({% url 'page' slug='native-select' %}),
[Checkbox]({% url 'page' slug='checkbox' %}),
[Radio Group]({% url 'page' slug='radio-group' %}),
[Switch]({% url 'page' slug='switch' %}) e
[Input]({% url 'page' slug='input' %}).
:::
