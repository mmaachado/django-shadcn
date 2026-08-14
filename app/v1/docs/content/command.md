---
title: Command
description: Fast, composable, unstyled command menu for Django.
description.pt-br: Menu de comandos rápido e componível para Django.
description.es: Menú de comandos rápido y componible para Django.
---

<c-docs.demo-section class="min-h-[350px]">
<c-command class="rounded-lg border shadow-md md:min-w-[450px]">
<c-command.input placeholder="Type a command or search..." />
<c-command.list>
<c-command.empty>No results found.</c-command.empty>
<c-command.group heading="Suggestions">
<c-command.item value="calendar">Calendar</c-command.item>
<c-command.item value="search-emoji">Search Emoji</c-command.item>
<c-command.item value="calculator">Calculator</c-command.item>
</c-command.group>
<c-command.separator />
<c-command.group heading="Settings">
<c-command.item value="profile">
Profile
<c-command.shortcut>⌘P</c-command.shortcut>
</c-command.item>
<c-command.item value="billing">
Billing
<c-command.shortcut>⌘B</c-command.shortcut>
</c-command.item>
<c-command.item value="settings">
Settings
<c-command.shortcut>⌘S</c-command.shortcut>
</c-command.item>
</c-command.group>
</c-command.list>
</c-command>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add command
```

## Usage

```html
<c-command class="rounded-lg border shadow-md md:min-w-[450px]">
  <c-command.input placeholder="Type a command or search..." />
  <c-command.list>
    <c-command.empty>No results found.</c-command.empty>
    <c-command.group heading="Suggestions">
      <c-command.item value="calendar">Calendar</c-command.item>
      <c-command.item value="search-emoji">Search Emoji</c-command.item>
      <c-command.item value="calculator">Calculator</c-command.item>
    </c-command.group>
    <c-command.separator />
    <c-command.group heading="Settings">
      <c-command.item value="profile">
        Profile
        <c-command.shortcut>⌘P</c-command.shortcut>
      </c-command.item>
      <c-command.item value="billing">
        Billing
        <c-command.shortcut>⌘B</c-command.shortcut>
      </c-command.item>
      <c-command.item value="settings">
        Settings
        <c-command.shortcut>⌘S</c-command.shortcut>
      </c-command.item>
    </c-command.group>
  </c-command.list>
</c-command>
```
