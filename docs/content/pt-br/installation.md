---
title: Instalação
description: Configure Tailwind, Alpine e django-cotton, e comece a adicionar componentes.
---

## Requisitos

- Python 3.12 ou mais novo
- Django 5.1 ou mais novo
- [django-cotton](https://django-cotton.com), que fornece a sintaxe `<c-...>`
  em que todo componente é escrito
- Tailwind CSS v4
- Alpine.js, para os componentes interativos

## Preparar o projeto

Instale o django-cotton e adicione às configurações:

```python
INSTALLED_APPS = [
    ...
    "django_cotton",
]
```

Depois inicialize o tema. Isso cria `templates/cotton/` e traz um `input.css`
com a paleta, os tokens de design e as fontes Geist em que todo componente se
apoia:

```bash
uvx django_shadcn@latest init
```

Aponte o Tailwind para esse arquivo e deixe ele observando seus templates:

```bash
npx @tailwindcss/cli -i input.css -o static/css/output.css --watch
```

Por fim, carregue a folha de estilo e o Alpine no seu template base:

```html
<link rel="stylesheet" href="{% static 'css/output.css' %}" />
<script src="{% static 'js/alpine.min.js' %}" defer></script>
```

Servir o Alpine dos seus próprios arquivos estáticos mantém a página
funcionando offline e evita depender de um CDN em tempo de execução. Se
preferir um CDN, fixe a versão em vez de acompanhar a `latest`.

## Adicionar um componente

```bash
uvx django_shadcn@latest add button
```

Os componentes vão para `templates/cotton/<nome>/`, e as dependências deles vêm
junto automaticamente. Você pode pedir vários de uma vez:

```bash
uvx django_shadcn@latest add button card input
```

Use como qualquer outro componente cotton:

```html
<c-button variant="outline">Clique aqui</c-button>
```

## Seus arquivos continuam seus

O `add` nunca sobrescreve o que já está no disco. Rodar de novo reporta os
arquivos que pulou e deixa suas edições intactas — os componentes passam a ser
seus assim que chegam.

Duas flags mudam isso, de propósito:

| Flag          | Arquivo existente | Apaga alguma coisa      |
| ------------- | ----------------- | ----------------------- |
| _(padrão)_    | pulado            | nunca                   |
| `--overwrite` | substituído       | nunca                   |
| `--sync`      | substituído       | sim, espelha a origem   |

O `--sync` lista o que vai apagar e pergunta antes. Passe `--yes` para dispensar
a confirmação em um script.

## Ver o que existe

```bash
uvx django_shadcn@latest list
```

Os componentes já instalados aparecem marcados, então dá para saber de relance
o que o projeto já usa.
