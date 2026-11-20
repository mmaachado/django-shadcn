---
title: django-allauth
description: Beautiful, pre-styled authentication templates for django-allauth.
description.pt-br: Telas de autenticação prontas e estilizadas para o django-allauth.
description.es: Pantallas de autenticación listas y estilizadas para django-allauth.
---

<c-docs.demo-section class="min-h-[350px]">
<c-card class='w-[400px]'>
                <c-card.header>
                    <c-card.title>Sign In</c-card.title>
                    <c-card.description>
                        Please sign in with your email address and password.
                    </c-card.description>
                </c-card.header>

<c-card.content class='space-y-4'>
    <div class='space-y-2'>
        <c-label for="login-email">Email</c-label>
        <c-input
            type="email"
            id="login-email"
            placeholder="Enter your email"
        />
    </div>

<div class='space-y-2'>
    <c-label for="login-password">Password</c-label>
    <c-input
        type="password"
        id="login-password"
        placeholder="Enter your password"
    />
</div>

    <div class="flex items-center space-x-2">
        <c-checkbox id="remember" />
        <c-label for="remember" class="text-sm font-normal">Remember me</c-label>
    </div>
</c-card.content>

<c-card.footer class='flex flex-col space-y-3'>
    <c-button type="button" class="w-full">Sign In</c-button>

<div class="text-center text-sm text-muted-foreground">
    <a href="#" class="text-primary hover:underline">Forgot Password?</a>
</div>

                    <div class="text-center text-sm text-muted-foreground">
                        Don't have an account?
                        <a href="#" class="text-primary hover:underline">Sign up</a>
                    </div>
                </c-card.footer>
            </c-card>
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add allauth
```

:::en
This is a block, not a component. It installs 17 templates to
`templates/account/`, under the names django-allauth looks for, and the
components they use to `templates/cotton/`: Card, Button, Input, Label,
Checkbox, Alert, Badge and Separator.

## Usage

django-allauth renders its own templates unless a project template of the same
name comes first. Django checks the directories in `DIRS` before the apps, so
with `templates/` in `DIRS` these replace allauth's as soon as they are on
disk. There is nothing to wire up beyond allauth itself.

Each page extends your `base.html` and fills its
`{% verbatim %}{% block content %}{% endverbatim %}`, the contract the other
blocks use too. The forms are rendered field by field from allauth's own form,
so a bound value and its errors come back after a failed post, with the
`csrf_token` in place. They are plain forms and work without JavaScript.

The pages open with `{% verbatim %}{% load account %}{% endverbatim %}`, which
comes from django-allauth. Without allauth installed, take the markup and point
the forms at your own views.

## All templates
:::pt-br
Isto é um bloco, não um componente. Ele instala 17 templates em
`templates/account/`, com os nomes que o django-allauth procura, e os
componentes que eles usam em `templates/cotton/`: Card, Button, Input, Label,
Checkbox, Alert, Badge e Separator.

## Uso

O django-allauth renderiza os próprios templates, a menos que um template do
projeto com o mesmo nome venha antes. O Django confere os diretórios de `DIRS`
antes dos apps, então com `templates/` em `DIRS` estes substituem os do allauth
assim que estiverem no disco. Não há nada para ligar além do próprio allauth.

Cada página estende o seu `base.html` e preenche o
`{% verbatim %}{% block content %}{% endverbatim %}` dele, o contrato que os
outros blocos também usam. Os formulários são renderizados campo a campo a
partir do formulário do próprio allauth, então um valor preenchido e os erros
voltam depois de um envio com falha, com o `csrf_token` no lugar. São
formulários comuns e funcionam sem JavaScript.

As páginas abrem com `{% verbatim %}{% load account %}{% endverbatim %}`, que
vem do django-allauth. Sem o allauth instalado, aproveite o markup e aponte os
formulários para as suas próprias views.

## Todos os templates
:::

:::en
<div class="grid gap-2 text-sm">
    <div class="grid grid-cols-2 gap-4">
        <div class="space-y-2">
            <h4 class="font-medium">Authentication</h4>
            <ul class="space-y-1 text-muted-foreground">
                <li><c-docs.code class="text-xs">login.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">signup.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">logout.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">reauthenticate.html</c-docs.code></li>
            </ul>
        </div>
        <div class="space-y-2">
            <h4 class="font-medium">Password</h4>
            <ul class="space-y-1 text-muted-foreground">
                <li><c-docs.code class="text-xs">password_change.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">password_set.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">password_reset.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">password_reset_done.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">password_reset_from_key.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">password_reset_from_key_done.html</c-docs.code></li>
            </ul>
        </div>
        <div class="space-y-2">
            <h4 class="font-medium">Email</h4>
            <ul class="space-y-1 text-muted-foreground">
                <li><c-docs.code class="text-xs">email.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">email_change.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">email_confirm.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">verification_sent.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">verified_email_required.html</c-docs.code></li>
            </ul>
        </div>
        <div class="space-y-2">
            <h4 class="font-medium">Status</h4>
            <ul class="space-y-1 text-muted-foreground">
                <li><c-docs.code class="text-xs">account_inactive.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">signup_closed.html</c-docs.code></li>
            </ul>
        </div>
    </div>
</div>
:::pt-br
<div class="grid gap-2 text-sm">
    <div class="grid grid-cols-2 gap-4">
        <div class="space-y-2">
            <h4 class="font-medium">Autenticação</h4>
            <ul class="space-y-1 text-muted-foreground">
                <li><c-docs.code class="text-xs">login.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">signup.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">logout.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">reauthenticate.html</c-docs.code></li>
            </ul>
        </div>
        <div class="space-y-2">
            <h4 class="font-medium">Senha</h4>
            <ul class="space-y-1 text-muted-foreground">
                <li><c-docs.code class="text-xs">password_change.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">password_set.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">password_reset.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">password_reset_done.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">password_reset_from_key.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">password_reset_from_key_done.html</c-docs.code></li>
            </ul>
        </div>
        <div class="space-y-2">
            <h4 class="font-medium">E-mail</h4>
            <ul class="space-y-1 text-muted-foreground">
                <li><c-docs.code class="text-xs">email.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">email_change.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">email_confirm.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">verification_sent.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">verified_email_required.html</c-docs.code></li>
            </ul>
        </div>
        <div class="space-y-2">
            <h4 class="font-medium">Status</h4>
            <ul class="space-y-1 text-muted-foreground">
                <li><c-docs.code class="text-xs">account_inactive.html</c-docs.code></li>
                <li><c-docs.code class="text-xs">signup_closed.html</c-docs.code></li>
            </ul>
        </div>
    </div>
</div>
:::

<div class="flex flex-wrap gap-2">
    <a href="{% url 'page' slug='card' %}"><c-badge variant="outline">Card</c-badge></a>
    <a href="{% url 'page' slug='button' %}"><c-badge variant="outline">Button</c-badge></a>
    <a href="{% url 'page' slug='input' %}"><c-badge variant="outline">Input</c-badge></a>
    <a href="{% url 'page' slug='label' %}"><c-badge variant="outline">Label</c-badge></a>
    <a href="{% url 'page' slug='checkbox' %}"><c-badge variant="outline">Checkbox</c-badge></a>
    <a href="{% url 'page' slug='alert' %}"><c-badge variant="outline">Alert</c-badge></a>
    <a href="{% url 'page' slug='badge' %}"><c-badge variant="outline">Badge</c-badge></a>
    <a href="{% url 'page' slug='separator' %}"><c-badge variant="outline">Separator</c-badge></a>
</div>

:::en
## Examples

The previews below show the pages' markup with sample text, outside allauth.

### Login
:::pt-br
## Exemplos

As prévias abaixo mostram o markup das páginas com texto de exemplo, fora do
allauth.

### Login
:::

<c-docs.demo-section>
<c-card class='w-[400px]'>
    <c-card.header>
        <c-card.title>Sign In</c-card.title>
        <c-card.description>
            Please sign in with your email address and password.
        </c-card.description>
    </c-card.header>

<c-card.content class='space-y-4'>
    <div class='space-y-2'>
        <c-label for="login-email">Email</c-label>
        <c-input
            type="email"
            id="login-email"
            placeholder="Enter your email"
        />
    </div>

<div class='space-y-2'>
    <c-label for="login-password">Password</c-label>
    <c-input
        type="password"
        id="login-password"
        placeholder="Enter your password"
    />
</div>

    <div class="flex items-center space-x-2">
        <c-checkbox id="remember" />
        <c-label for="remember" class="text-sm font-normal">Remember me</c-label>
    </div>
</c-card.content>

<c-card.footer class='flex flex-col space-y-3'>
    <c-button type="button" class="w-full">Sign In</c-button>

<div class="text-center text-sm text-muted-foreground">
    <a href="#" class="text-primary hover:underline">Forgot Password?</a>
</div>

        <div class="text-center text-sm text-muted-foreground">
            Don't have an account?
            <a href="#" class="text-primary hover:underline">Sign up</a>
        </div>
    </c-card.footer>
</c-card>
</c-docs.demo-section>

:::en
### Sign up
:::pt-br
### Cadastro
:::

<c-docs.demo-section>
<c-card class='w-[400px]'>
    <c-card.header>
        <c-card.title>Sign Up</c-card.title>
        <c-card.description>
            Create your account to get started.
        </c-card.description>
    </c-card.header>

<c-card.content class='space-y-4'>
    <div class='space-y-2'>
        <c-label for="signup-email">Email</c-label>
        <c-input
            type="email"
            id="signup-email"
            placeholder="Enter your email"
        />
    </div>

<div class='space-y-2'>
    <c-label for="signup-password">Password</c-label>
    <c-input
        type="password"
        id="signup-password"
        placeholder="Create a password"
    />
</div>

    <div class='space-y-2'>
        <c-label for="signup-password2">Confirm Password</c-label>
        <c-input
            type="password"
            id="signup-password2"
            placeholder="Confirm your password"
        />
    </div>
</c-card.content>

<c-card.footer class='flex flex-col space-y-3'>
    <c-button type="button" class="w-full">Sign Up</c-button>

        <div class="text-center text-sm text-muted-foreground">
            Already have an account?
            <a href="#" class="text-primary hover:underline">Sign in</a>
        </div>
    </c-card.footer>
</c-card>
</c-docs.demo-section>

:::en
### Logout
:::pt-br
### Logout
:::

<c-docs.demo-section>
<c-card class='w-[400px]'>
    <c-card.header>
        <c-card.title>Sign Out</c-card.title>
        <c-card.description>
            Are you sure you want to sign out?
        </c-card.description>
    </c-card.header>

    <c-card.footer class='flex gap-2'>
        <c-button variant="outline" class="flex-1">Cancel</c-button>
        <c-button class="flex-1">Sign Out</c-button>
    </c-card.footer>
</c-card>
</c-docs.demo-section>

:::en
### Password reset
:::pt-br
### Redefinição de senha
:::

<c-docs.demo-section>
<c-card class='w-[400px]'>
    <c-card.header>
        <c-card.title>Reset Password</c-card.title>
        <c-card.description>
            Enter your email address and we'll send you a link to reset your password.
        </c-card.description>
    </c-card.header>

<c-card.content class='space-y-4'>
    <div class='space-y-2'>
        <c-label for="reset-email">Email</c-label>
        <c-input
            type="email"
            id="reset-email"
            placeholder="Enter your email"
        />
    </div>
</c-card.content>

<c-card.footer class='flex flex-col space-y-3'>
    <c-button type="button" class="w-full">Reset Password</c-button>

        <div class="text-center text-sm text-muted-foreground">
            Remember your password?
            <a href="#" class="text-primary hover:underline">Sign in</a>
        </div>
    </c-card.footer>
</c-card>
</c-docs.demo-section>

:::en
## RTL

The pages are built from logical utilities, so under `dir="rtl"` the forms and
the cards mirror with the text. allauth translates its labels and messages, so
a right-to-left language gets its own words as well as its direction.

## Accessibility

Every field has a `<c-label>` tied to it through `for` and the field's id, and
required fields carry `required`. Errors are written under their field in red,
which a screen reader reads in order but does not tie to the input: add
`aria-describedby` pointing at the error when that matters.

## Notes

The [Login and Sign Up]({% url 'page' slug='login' %}) block is the same idea
as a split-screen design with a plain form, for a project that handles accounts
itself or wants that layout for allauth's forms.
:::pt-br
## RTL

As páginas são feitas de utilitários lógicos, então sob `dir="rtl"` os
formulários e os cards espelham junto com o texto. O allauth traduz os rótulos
e as mensagens, então um idioma da direita para a esquerda ganha as próprias
palavras além da direção.

## Acessibilidade

Todo campo tem um `<c-label>` ligado a ele pelo `for` e pelo id do campo, e os
campos obrigatórios levam `required`. Os erros ficam escritos embaixo do campo
em vermelho, o que um leitor de tela lê em ordem mas não liga ao input:
acrescente um `aria-describedby` apontando para o erro quando isso importar.

## Observações

O bloco [Login and Sign Up]({% url 'page' slug='login' %}) é a mesma ideia como
um design em tela dividida com um formulário simples, para um projeto que cuida
das contas por conta própria ou que quer esse layout para os formulários do
allauth.
:::
