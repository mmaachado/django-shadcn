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

## Installation

```bash
uvx django_shadcn@latest add allauth
```

<p class="text-sm text-muted-foreground mt-4">
    This will install 17 templates to <c-docs.code class="text-sm">templates/account/</c-docs.code>
    along with the required UI components.
</p>
<p class="text-sm text-muted-foreground mt-4">
    You can also use these templates without django-allauth.
</p>

## All Templates

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

## Components Used

<p class="text-muted-foreground mb-4">
    The following components are automatically installed:
</p>
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

## Examples

<!-- Login -->

### Login

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

<!-- Signup -->

### Signup

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

<!-- Logout -->

### Logout

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

<!-- Password Reset -->

### Password Reset

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
