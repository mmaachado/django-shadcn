---
title: Build your own Django component library
description: Beautiful, accessible components for Django using Tailwind CSS and Alpine.js. Open source. Open Code.
---

<div class="flex flex-wrap items-center gap-3 pb-8">
    <a href="{% url 'page' slug='installation' %}" class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors bg-primary text-primary-foreground hover:bg-primary/90 h-9 px-4 py-2">
        Get Started
    </a>
    <a href="https://github.com/mmaachado/django-shadcn" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors border border-input bg-background hover:bg-accent hover:text-accent-foreground h-9 px-4 py-2">
        GitHub
    </a>
</div>

## About

This is an unofficial Django port of [shadcn/ui](https://ui.shadcn.com/). The
project is not affiliated with [shadcn](https://twitter.com/shadcn).

Components are built with [Tailwind CSS](https://tailwindcss.com/) and
[Alpine.js](https://alpinejs.dev/), and are
[HTMX-compatible](https://htmx.org), which makes them customizable and
interactive without a build step of their own.

## Philosophy

**This is not a component library.** It is a collection of re-usable components
you add to your own Django templates through the CLI.

You do not install it as a dependency. Pick the components you need, run the
CLI, and customize them. The code is yours from that point on.

## What you get

<div class="mt-6 grid gap-4 md:grid-cols-3">
    <div class="rounded-lg border border-border bg-card p-4 transition-colors hover:bg-accent/50">
        <h3 class="mb-2 text-sm font-semibold">Tailwind CSS</h3>
        <p class="text-sm text-muted-foreground">Style your components with utility classes.</p>
    </div>
    <div class="rounded-lg border border-border bg-card p-4 transition-colors hover:bg-accent/50">
        <h3 class="mb-2 text-sm font-semibold">Alpine.js</h3>
        <p class="text-sm text-muted-foreground">Lightweight interactivity without the overhead.</p>
    </div>
    <div class="rounded-lg border border-border bg-card p-4 transition-colors hover:bg-accent/50">
        <h3 class="mb-2 text-sm font-semibold">HTMX ready</h3>
        <p class="text-sm text-muted-foreground">Works with HTMX for dynamic content.</p>
    </div>
</div>

## Credits

Designed by [shadcn](https://ui.shadcn.com). Ported to Django by
[Sarthak Jariwala](https://github.com/SarthakJariwala), whose work this fork
builds on. There is also a
[video overview](https://www.youtube.com/watch?v=HdIkm1L_lZs) by BugBytes.
