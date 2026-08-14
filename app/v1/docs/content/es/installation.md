---
title: Instalación
description: Configura Tailwind, Alpine y django-cotton, y empieza a añadir componentes.
---

## Requisitos

- Python 3.12 o superior
- Django 4.2 o superior
- [django-cotton](https://django-cotton.com) 2.7.1 o superior, que aporta la
  sintaxis `<c-...>` en la que está escrito cada componente
- Tailwind CSS v4
- Alpine.js, para los componentes interactivos

### Qué django-cotton

Tu versión de Django lo decide por ti, así que conviene saberlo antes de elegir:

| django-cotton | Funciona con      |
| ------------- | ----------------- |
| 1.x           | Django 4.2 a 5.1  |
| 2.x           | Django 4.2 a 6.x  |

**En Django 5.2 o superior, la 2.x es la única línea que se instala.** Y las
versiones por debajo de 2.7.1 arrastran una corrección que conviene tener: un
atributo dinámico con comillas podía escapar del atributo e inyectar otros
arbitrariamente. Fija el suelo:

```
django-cotton>=2.7.1
```

Los componentes funcionan en ambas líneas — cada uno se renderiza contra la 1.6
y contra la 2.7 en cada cambio — así que un proyecto antiguo sigue funcionando.
El suelo es por la corrección de la inyección, no por el markup.

## Preparar el proyecto

Instala django-cotton y añádelo a la configuración:

```python
INSTALLED_APPS = [
    ...
    "django_cotton",
]
```

Después inicializa el tema. Esto crea `templates/cotton/` y deja un `input.css`
con la paleta, los tokens de diseño y las fuentes Geist sobre los que se apoya
cada componente:

```bash
uvx django_shadcn@latest init
```

Apunta Tailwind a ese archivo y deja que observe tus plantillas:

```bash
npx @tailwindcss/cli -i input.css -o static/css/output.css --watch
```

Por último, carga la hoja de estilo y Alpine desde tu plantilla base:

```html
<link rel="stylesheet" href="{% static 'css/output.css' %}" />
<script src="{% static 'js/alpine.min.js' %}" defer></script>
```

Servir Alpine desde tus propios archivos estáticos mantiene la página
funcionando sin conexión y evita depender de un CDN en tiempo de ejecución. Si
prefieres usar uno, fija la versión en lugar de seguir a `latest`.

## Añadir un componente

```bash
uvx django_shadcn@latest add button
```

Los componentes llegan a `templates/cotton/<nombre>/`, y sus dependencias
vienen incluidas. Puedes pedir varios a la vez:

```bash
uvx django_shadcn@latest add button card input
```

Úsalo como cualquier otro componente cotton:

```html
<c-button variant="outline">Haz clic</c-button>
```

## Tus archivos siguen siendo tuyos

`add` nunca sobrescribe lo que ya está en disco. Ejecutarlo otra vez informa de
los archivos que omitió y deja tus cambios intactos: los componentes son tuyos
en cuanto llegan.

Dos flags cambian eso, a propósito:

| Flag          | Archivo existente | Borra algo             |
| ------------- | ----------------- | ---------------------- |
| _(por defecto)_ | omitido         | nunca                  |
| `--overwrite` | reemplazado       | nunca                  |
| `--sync`      | reemplazado       | sí, refleja el origen  |

`--sync` enumera lo que va a borrar y pregunta antes de hacerlo. Pasa `--yes`
para omitir la confirmación en un script.

## Ver qué hay disponible

```bash
uvx django_shadcn@latest list
```

Los componentes ya instalados aparecen marcados, así se ve de un vistazo qué
usa el proyecto.
