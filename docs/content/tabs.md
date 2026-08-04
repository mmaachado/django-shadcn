---
title: Tabs
description: A set of layered sections of content—known as tab panels—that are displayed one at a time.
description.pt-br: Seções de conteúdo sobrepostas, exibidas uma de cada vez.
description.es: Secciones de contenido superpuestas, que se muestran de una en una.
---

<c-docs.demo-section class="min-h-[350px]">
<c-tabs default_value="account" class="w-[400px]">
<c-tabs.list class="grid w-[400px] grid-cols-2">
<c-tabs.trigger value="account">Account</c-tabs.trigger>
<c-tabs.trigger value="password">Password</c-tabs.trigger>
</c-tabs.list>
<c-tabs.content value="account">
<c-card>
<c-card.header>
<c-card.title>Account</c-card.title>
<c-card.description>
Make changes to your account here. Click save when you're done.
</c-card.description>
</c-card.header>
<c-card.content class="space-y-2">
<div class="space-y-1">
<c-label for="name">Name</c-label>
<c-input id="name" name="name" />
</div>
<div class="space-y-1">
<c-label for="username">Username</c-label>
<c-input id="username" name="username" />
</div>
</c-card.content>
<c-card.footer>
<c-button>Save changes</c-button>
</c-card.footer>
</c-card>
</c-tabs.content>
<c-tabs.content value="password">
<c-card>
<c-card.header>
<c-card.title>Password</c-card.title>
<c-card.description>
Change your password here. After saving, you'll be logged out.
</c-card.description>
</c-card.header>
<c-card.content class="space-y-2">
<div class="space-y-1">
<c-label for="current">Current password</c-label>
<c-input id="current" type="password" />
</div>
<div class="space-y-1">
<c-label for="new">New password</c-label>
<c-input id="new" type="password" />
</div>
</c-card.content>
<c-card.footer>
<c-button>Save password</c-button>
</c-card.footer>
</c-card>
</c-tabs.content>
</c-tabs>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add tabs
```

## Usage

```html
<c-tabs default_value="account">
  <c-tabs.list>
    <c-tabs.trigger value="account">Account</c-tabs.trigger>
    <c-tabs.trigger value="password">Password</c-tabs.trigger>
  </c-tabs.list>
  <c-tabs.content value="account"
    >Make changes to your account here.</c-tabs.content
  >
  <c-tabs.content value="password">Change your password here.</c-tabs.content>
</c-tabs>
```
