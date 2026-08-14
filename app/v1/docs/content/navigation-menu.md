---
title: Navigation Menu
description: A collection of links for navigating websites.
description.pt-br: Um conjunto de links para navegar pelo site.
description.es: Un conjunto de enlaces para navegar por el sitio.
---

<c-docs.demo-section class="min-h-[350px]">
<c-navigation-menu>
<c-navigation-menu.list>
<c-navigation-menu.item>
<c-navigation-menu.trigger index="0">Getting started</c-navigation-menu.trigger>
<c-navigation-menu.content index="0">
<div class="md:w-[200px]">
<c-navigation-menu.link href="/introduction">
Introduction
<c-navigation-menu.link_details>
A quick tutorial to get you started.
</c-navigation-menu.link_details>
</c-navigation-menu.link>
<c-navigation-menu.link href="/installation">
Installation
<c-navigation-menu.link_details>
Install and set up your project.
</c-navigation-menu.link_details>
</c-navigation-menu.link>
</div>
</c-navigation-menu.content>
</c-navigation-menu.item>

<c-navigation-menu.item>
<c-navigation-menu.trigger index="1">Components</c-navigation-menu.trigger>
<c-navigation-menu.content index="1">
<div class="md:w-[150px]">
<c-navigation-menu.link href="/accordion">Accordion</c-navigation-menu.link>
<c-navigation-menu.link href="/button">Button</c-navigation-menu.link>
<c-navigation-menu.link href="/card">Card</c-navigation-menu.link>
<c-navigation-menu.link href="/checkbox">Checkbox</c-navigation-menu.link>
<c-navigation-menu.link href="/dropdown-menu">Dropdown Menu</c-navigation-menu.link>
<c-navigation-menu.link href="/form">Form</c-navigation-menu.link>
<c-navigation-menu.link href="/input">Input</c-navigation-menu.link>
<c-navigation-menu.link href="/progress">Progress</c-navigation-menu.link>
<c-navigation-menu.link href="/select">Select</c-navigation-menu.link>
<c-navigation-menu.link href="/tabs">Tabs</c-navigation-menu.link>
<c-navigation-menu.link href="/toast">Toast</c-navigation-menu.link>
</div>
</c-navigation-menu.content>
</c-navigation-menu.item>

                <c-navigation-menu.item>
                    <c-navigation-menu.link href="https://shadcn-django.com/">Documentation</c-navigation-menu.link>
                </c-navigation-menu.item>
            </c-navigation-menu.list>
        </c-navigation-menu>

</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add navigation_menu
```

## Usage

```html
<c-navigation-menu>
  <c-navigation-menu.list>
    <c-navigation-menu.item>
      <c-navigation-menu.trigger index="0"
        >Getting started</c-navigation-menu.trigger
      >
      <c-navigation-menu.content index="0">
        <c-navigation-menu.link href="/introduction"
          >Introduction</c-navigation-menu.link
        >
        <c-navigation-menu.link href="/installation"
          >Installation</c-navigation-menu.link
        >
      </c-navigation-menu.content>
    </c-navigation-menu.item>

    <c-navigation-menu.item>
      <c-navigation-menu.trigger index="1"
        >Components</c-navigation-menu.trigger
      >
      <c-navigation-menu.content index="1">
        <div class="md:w-[150px]">
          <c-navigation-menu.link href="/accordion"
            >Accordion</c-navigation-menu.link
          >
          <c-navigation-menu.link href="/button">Button</c-navigation-menu.link>
          <c-navigation-menu.link href="/card">Card</c-navigation-menu.link>
        </div>
      </c-navigation-menu.content>
    </c-navigation-menu.item>

    <c-navigation-menu.item>
      <c-navigation-menu.trigger index="2">Utilities</c-navigation-menu.trigger>
      <c-navigation-menu.content index="2">
        <div class="md:w-[150px]">
          <c-navigation-menu.link href="/typography"
            >Typography</c-navigation-menu.link
          >
          <c-navigation-menu.link href="/icons">Icons</c-navigation-menu.link>
          <c-navigation-menu.link href="/colors">Colors</c-navigation-menu.link>
        </div>
      </c-navigation-menu.content>
    </c-navigation-menu.item>

    <c-navigation-menu.item>
      <c-navigation-menu.link href="https://shadcn-django.com/"
        >Documentation</c-navigation-menu.link
      >
    </c-navigation-menu.item>
  </c-navigation-menu.list>
</c-navigation-menu>
```

## Examples

###

<c-docs.demo-section>
<c-card class="w-[380px]">
<c-card.header>
<c-card.title>Create Project</c-card.title>
<c-card.description>Deploy your new project in one-click.</c-card.description>
</c-card.header>
<c-card.content class="space-y-2">
<div class="flex flex-col space-y-1">
<c-label for="name">Name</c-label>
<c-input id="name" placeholder="Name of your project" />
</div>
</c-card.content>
<c-card.footer class="flex justify-between">
<c-button variant="outline">Cancel</c-button>
<c-button>Submit</c-button>
</c-card.footer>
</c-card>
</c-docs.demo-section>

```html
<c-card class="w-[380px]">
  <c-card.header>
    <c-card.title>Create Project</c-card.title>
    <c-card.description
      >Deploy your new project in one-click.</c-card.description
    >
  </c-card.header>
  <c-card.content class="space-y-2">
    <div class="flex flex-col space-y-1">
      <c-label for="name">Name</c-label>
      <c-input id="name" placeholder="Name of your project" />
    </div>
  </c-card.content>
  <c-card.footer class="flex justify-between">
    <c-button variant="outline">Cancel</c-button>
    <c-button>Submit</c-button>
  </c-card.footer>
</c-card>
```
