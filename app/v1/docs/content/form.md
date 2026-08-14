---
title: Form
description: Displays well-designed HTML forms.
description.pt-br: Formulários HTML bem apresentados.
description.es: Formularios HTML bien presentados.
---

<c-docs.demo-section class="min-h-[350px]">

<form class="w-2/3 space-y-4">
            <c-form.field>
                <c-form.label for="email">Email</c-form.label>
                <c-input id="email" type="email" placeholder="Email"></c-input>
                <c-form.description>
                    This will be your username.
                </c-form.description>
            </c-form.field>
            <c-form.field>
                <c-form.label for="password">Password</c-form.label>
                <c-input id="password" type="password" placeholder="Password"></c-input>
            </c-form.field>
            <c-button type="submit">
                Sign in
            </c-button>
        </form>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add form
```

## Usage

```html
<form class="w-2/3 space-y-4">
  <c-form.field>
    <c-form.label for="email">Email</c-form.label>
    <c-input id="email" type="email" placeholder="Email"></c-input>
    <c-form.description> This will be your username. </c-form.description>
  </c-form.field>

  <c-form.field>
    <c-form.label for="password">Password</c-form.label>
    <c-input id="password" type="password" placeholder="Password"></c-input>
  </c-form.field>

  <c-button type="submit">Sign in</c-button>
</form>
```

## Examples

###

<c-docs.demo-section>

<form class="w-2/3 space-y-4">
    <c-form.field>
        <c-form.label for="username" error="true">Username</c-form.label>
        <c-input id="username" type="text" placeholder="Username"></c-input>
        <c-form.error>
            Username already taken.
        </c-form.error>
    </c-form.field>
    <c-button type="submit">
        Submit
    </c-button>
</form>
</c-docs.demo-section>

```html
<form class="w-2/3 space-y-4">
  <c-form.field>
    <c-form.label for="username" error="true">Username</c-form.label>
    <c-input id="username" type="text" placeholder="Username"></c-input>
    <c-form.error> Username already taken. </c-form.error>
  </c-form.field>
  <c-button type="submit"> Submit </c-button>
</form>
```
