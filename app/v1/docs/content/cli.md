---
title: CLI
description: init, add, list and their flags, how dependencies come along, and what happens to a file that already exists.
description.pt-br: init, add, list e as flags deles, como as dependências vêm junto e o que acontece com um arquivo que já existe.
description.es: init, add, list y sus flags, cómo llegan las dependencias y qué pasa con un archivo que ya existe.
---

:::en
## Running it

The CLI ships in the package, so `uvx` runs it without installing anything
into your project:
:::pt-br
## Executando

A CLI vem no pacote, então o `uvx` a executa sem instalar nada no seu projeto:
:::

```bash
uvx django_shadcn@latest add button
```

:::en
Run it from the root of your project. `init` and `add` write relative to the
current directory: `templates/cotton/`, `templates/blocks/`, `templates/account/`
and `input.css` all land there.

`--version`, or `-V`, prints the installed version.

## init

Creates `templates/cotton/` and copies `input.css`, the palette and the tokens
every component reads, into the current directory. See
[Theming]({% url 'page' slug='theming' %}) for what is in it.
:::pt-br
Execute a partir da raiz do seu projeto. O `init` e o `add` escrevem em relação
ao diretório atual: `templates/cotton/`, `templates/blocks/`,
`templates/account/` e o `input.css` caem todos ali.

O `--version`, ou `-V`, imprime a versão instalada.

## init

Cria `templates/cotton/` e copia o `input.css`, a paleta e os tokens que todo
componente lê, para o diretório atual. Veja
[Theming]({% url 'page' slug='theming' %}) para o que está nele.
:::

```bash
uvx django_shadcn@latest init
uvx django_shadcn@latest init --force
```

:::en
Running it again keeps the `input.css` you have, and says so: your palette is
never replaced without you asking. `--force` puts the shipped one back.

## add

Copies one or more components, and everything they depend on, into the
project:
:::pt-br
Rodar de novo mantém o `input.css` que você tem, e avisa: a sua paleta nunca é
substituída sem você pedir. O `--force` traz de volta o que vem com a
biblioteca.

## add

Copia um ou mais componentes, e tudo de que eles dependem, para o projeto:
:::

```bash
uvx django_shadcn@latest add button card input
```

:::en
A name can be written as the directory, `toggle_group`, or as the tag,
`toggle-group`, in any case. An unknown name stops the run before anything is
written, with the closest names suggested.

**Dependencies.** A component that uses another brings it along: `add
date_picker` also adds `calendar`, `popover`, `button` and `icon`. Each lands
in its own directory.

**Where files go.** A component goes to `templates/cotton/<name>/`, a block to
`templates/blocks/<name>/`, and `allauth` to `templates/account/`, under the
template names django-allauth looks for.

**Existing files.** `add` never overwrites what is already on disk. A second
run reports the files it skipped and leaves your edits alone, so a component is
yours to change once it lands. Two flags change that:
:::pt-br
Um nome pode ser escrito como o diretório, `toggle_group`, ou como a tag,
`toggle-group`, em maiúsculas ou minúsculas. Um nome desconhecido interrompe a
execução antes de qualquer escrita, com os nomes mais próximos sugeridos.

**Dependências.** Um componente que usa outro o traz junto: `add date_picker`
também acrescenta `calendar`, `popover`, `button` e `icon`. Cada um cai no
próprio diretório.

**Para onde vão os arquivos.** Um componente vai para
`templates/cotton/<nome>/`, um bloco para `templates/blocks/<nome>/`, e o
`allauth` para `templates/account/`, com os nomes de template que o
django-allauth procura.

**Arquivos existentes.** O `add` nunca sobrescreve o que já está no disco. Uma
segunda execução informa os arquivos que pulou e deixa suas edições em paz,
então um componente é seu para mudar assim que chega. Duas flags mudam isso:
:::

:::en
| Flag | An existing file | Removes anything |
| --- | --- | --- |
| _(default)_ | skipped | never |
| `--overwrite` | replaced | never |
| `--sync` | replaced | yes, files the component no longer ships |

`--sync` mirrors only the components you name; their dependencies are still
added the safe way, so syncing `allauth` does not wipe what you changed in
`button`. It lists what it is about to delete and asks first; `--yes`, or
`-y`, skips the question in a script.

`--dry-run` works with any of them and writes nothing. It prints the same
report, file by file, that the real run would, and never asks, so it is worth
the habit before `--sync`.

A run that would put a file where a directory is, or the other way round,
stops before the first write rather than halfway through. So does a symlink
anywhere in a component's directory: writing through it would change a file
outside the project.

**Plugins.** Some components need an Alpine plugin that Alpine's core does not
include. `add` names it once at the end of the run, for everything it added;
[Alpine and JavaScript]({% url 'page' slug='alpine' %}) lists which.
:::pt-br
| Flag | Um arquivo existente | Apaga alguma coisa |
| --- | --- | --- |
| _(padrão)_ | pulado | nunca |
| `--overwrite` | substituído | nunca |
| `--sync` | substituído | sim, os arquivos que o componente não traz mais |

O `--sync` espelha só os componentes que você nomeia; as dependências deles
continuam sendo acrescentadas do jeito seguro, então sincronizar o `allauth`
não apaga o que você mudou no `button`. Ele lista o que vai apagar e pergunta
antes; o `--yes`, ou `-y`, dispensa a pergunta num script.

O `--dry-run` funciona com qualquer um deles e não grava nada. Ele imprime o
mesmo relatório, arquivo por arquivo, que a execução de verdade, e nunca
pergunta, então vale o hábito antes do `--sync`.

Uma execução que poria um arquivo onde há um diretório, ou o contrário, para
antes da primeira escrita, e não no meio do caminho. O mesmo vale para um link
simbólico em qualquer ponto do diretório de um componente: escrever através
dele mudaria um arquivo fora do projeto.

**Plugins.** Alguns componentes precisam de um plugin do Alpine que o núcleo do
Alpine não traz. O `add` o cita uma vez no fim da execução, para tudo o que
acrescentou; o [Alpine and JavaScript]({% url 'page' slug='alpine' %}) lista
quais.
:::

```bash
uvx django_shadcn@latest add allauth --sync --dry-run
```

:::en
## list

Prints every component and every block, in two panels, and marks the ones the
project already holds with `*`. A component counts as installed only when every
file it ships is on disk, so a project that wrote its own `login.html` is not
mistaken for one with `allauth`.
:::pt-br
## list

Imprime todos os componentes e todos os blocos, em dois painéis, e marca com
`*` os que o projeto já tem. Um componente só conta como instalado quando todo
arquivo que ele traz está no disco, então um projeto que escreveu o próprio
`login.html` não é confundido com um que tem o `allauth`.
:::

```bash
uvx django_shadcn@latest list
```
