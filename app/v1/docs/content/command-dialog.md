---
title: Command Dialog
description: Fast, composable, unstyled command menu in a dialog.
description.pt-br: Menu de comandos rápido e componível, dentro de um diálogo.
description.es: Menú de comandos rápido y componible, dentro de un diálogo.
---

<c-docs.demo-section class="min-h-[350px]">
<c-command-dialog shortcut_key="k">
<c-slot name="trigger_slot">
<p class="text-sm text-muted-foreground">
Press
<kbd
                    class="pointer-events-none inline-flex h-5 select-none items-center gap-1 rounded border bg-muted px-1.5 font-mono text-[10px] font-medium text-muted-foreground opacity-100"
                >
<span class="text-xs">⌘</span>K
</kbd>
</p>
</c-slot>

          <c-command.input placeholder="Type a command or search..." />
          <c-command.list>
            <c-command.empty>No results found.</c-command.empty>
            <c-command.group heading="Suggestions">
              <c-command.item value="calendar">Calendar</c-command.item>
              <c-command.item value="search-emoji">Search Emoji</c-command.item>
              <c-command.item value="calculator">Calculator</c-command.item>
            </c-command.group>
          </c-command.list>
        </c-command-dialog>

</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add command_dialog
```

## Usage

```html
<c-command-dialog shortcut_key="k">
  <c-slot name="trigger_slot">
    <p class="text-sm text-muted-foreground">
      Press
      <kbd
        class="pointer-events-none inline-flex h-5 select-none items-center gap-1 rounded border bg-muted px-1.5 font-mono text-[10px] font-medium text-muted-foreground opacity-100"
      >
        <span class="text-xs">⌘</span>K
      </kbd>
    </p>
  </c-slot>

  <c-command.input placeholder="Type a command or search..." />
  <c-command.list>
    <c-command.empty>No results found.</c-command.empty>
    <c-command.group heading="Suggestions">
      <c-command.item value="calendar">Calendar</c-command.item>
      <c-command.item value="search-emoji">Search Emoji</c-command.item>
      <c-command.item value="calculator">Calculator</c-command.item>
    </c-command.group>
  </c-command.list>
</c-command-dialog>
```
