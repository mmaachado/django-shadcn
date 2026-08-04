---
title: Monte sua própria biblioteca de componentes Django
description: Componentes acessíveis e bonitos para Django, com Tailwind CSS e Alpine.js. Código aberto, código seu.
---

<div class="flex flex-wrap items-center gap-3 pb-8">
    <a href="{% url 'page' slug='installation' %}" class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors bg-primary text-primary-foreground hover:bg-primary/90 h-9 px-4 py-2">
        Começar
    </a>
    <a href="https://github.com/mmaachado/django-shadcn" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors border border-input bg-background hover:bg-accent hover:text-accent-foreground h-9 px-4 py-2">
        GitHub
    </a>
</div>

## Sobre

Este é um port não oficial do [shadcn/ui](https://ui.shadcn.com/) para Django.
O projeto não tem vínculo com o [shadcn](https://twitter.com/shadcn).

Os componentes são feitos com [Tailwind CSS](https://tailwindcss.com/) e
[Alpine.js](https://alpinejs.dev/), e são compatíveis com
[HTMX](https://htmx.org). Isso os deixa customizáveis e interativos sem exigir
um passo de build próprio.

## Filosofia

**Isto não é uma biblioteca de componentes.** É um conjunto de componentes
reutilizáveis que você adiciona aos seus próprios templates Django pela CLI.

Você não instala como dependência. Escolhe os componentes que precisa, roda a
CLI e customiza. A partir daí, o código é seu.

## O que você leva

<div class="mt-6 grid gap-4 md:grid-cols-3">
    <div class="rounded-lg border border-border bg-card p-4 transition-colors hover:bg-accent/50">
        <h3 class="mb-2 text-sm font-semibold">Tailwind CSS</h3>
        <p class="text-sm text-muted-foreground">Estilize os componentes com classes utilitárias.</p>
    </div>
    <div class="rounded-lg border border-border bg-card p-4 transition-colors hover:bg-accent/50">
        <h3 class="mb-2 text-sm font-semibold">Alpine.js</h3>
        <p class="text-sm text-muted-foreground">Interatividade leve, sem peso extra.</p>
    </div>
    <div class="rounded-lg border border-border bg-card p-4 transition-colors hover:bg-accent/50">
        <h3 class="mb-2 text-sm font-semibold">Pronto para HTMX</h3>
        <p class="text-sm text-muted-foreground">Funciona com HTMX para conteúdo dinâmico.</p>
    </div>
</div>

## Créditos

Design do [shadcn](https://ui.shadcn.com). Portado para Django por
[Sarthak Jariwala](https://github.com/SarthakJariwala), cujo trabalho este fork
continua. Há também um
[vídeo de visão geral](https://www.youtube.com/watch?v=HdIkm1L_lZs) feito pelo
BugBytes.
