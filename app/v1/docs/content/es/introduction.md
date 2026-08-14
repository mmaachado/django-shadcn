---
title: Construye tu propia biblioteca de componentes Django
description: Componentes accesibles y cuidados para Django, con Tailwind CSS y Alpine.js. Código abierto, código tuyo.
---

<div class="flex flex-wrap items-center gap-3 pb-8">
    <a href="{% url 'page' slug='installation' %}" class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors bg-primary text-primary-foreground hover:bg-primary/90 h-9 px-4 py-2">
        Empezar
    </a>
    <a href="https://github.com/mmaachado/django-shadcn" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors border border-input bg-background hover:bg-accent hover:text-accent-foreground h-9 px-4 py-2">
        GitHub
    </a>
</div>

## Acerca de

Este es un port no oficial de [shadcn/ui](https://ui.shadcn.com/) para Django.
El proyecto no está afiliado a [shadcn](https://twitter.com/shadcn).

Los componentes están hechos con [Tailwind CSS](https://tailwindcss.com/) y
[Alpine.js](https://alpinejs.dev/), y son compatibles con
[HTMX](https://htmx.org), lo que los hace personalizables e interactivos sin
necesitar un paso de compilación propio.

## Filosofía

**Esto no es una biblioteca de componentes.** Es un conjunto de componentes
reutilizables que añades a tus propias plantillas de Django mediante la CLI.

No se instala como dependencia. Eliges los componentes que necesitas, ejecutas
la CLI y los personalizas. A partir de ahí, el código es tuyo.

## Qué obtienes

<div class="mt-6 grid gap-4 md:grid-cols-3">
    <div class="rounded-lg border border-border bg-card p-4 transition-colors hover:bg-accent/50">
        <h3 class="mb-2 text-sm font-semibold">Tailwind CSS</h3>
        <p class="text-sm text-muted-foreground">Da estilo a los componentes con clases utilitarias.</p>
    </div>
    <div class="rounded-lg border border-border bg-card p-4 transition-colors hover:bg-accent/50">
        <h3 class="mb-2 text-sm font-semibold">Alpine.js</h3>
        <p class="text-sm text-muted-foreground">Interactividad ligera, sin sobrecarga.</p>
    </div>
    <div class="rounded-lg border border-border bg-card p-4 transition-colors hover:bg-accent/50">
        <h3 class="mb-2 text-sm font-semibold">Listo para HTMX</h3>
        <p class="text-sm text-muted-foreground">Funciona con HTMX para contenido dinámico.</p>
    </div>
</div>

## Créditos

Diseñado por [shadcn](https://ui.shadcn.com). Adaptado a Django por
[Sarthak Jariwala](https://github.com/SarthakJariwala), cuyo trabajo continúa
este fork. También hay un
[vídeo de introducción](https://www.youtube.com/watch?v=HdIkm1L_lZs) de
BugBytes.
