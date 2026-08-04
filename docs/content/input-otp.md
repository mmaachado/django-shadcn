---
title: Input OTP
description: A one-time code field with a box per character.
description.pt-br: Um campo de código de uso único, com uma caixa por caractere.
description.es: Un campo de código de un solo uso, con una casilla por carácter.
---

<c-docs.demo-section class="min-h-[350px]">
<c-input-otp maxlength="6" name="code">
<c-input-otp.group>
<c-input-otp.slot index="0" />
<c-input-otp.slot index="1" />
<c-input-otp.slot index="2" />
</c-input-otp.group>
<c-input-otp.separator />
<c-input-otp.group>
<c-input-otp.slot index="3" />
<c-input-otp.slot index="4" />
<c-input-otp.slot index="5" />
</c-input-otp.group>
</c-input-otp>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add input_otp
```

## Usage

<c-docs.demo-section>
<c-input-otp maxlength="4" name="pin">
<c-input-otp.group>
<c-input-otp.slot index="0" />
<c-input-otp.slot index="1" />
<c-input-otp.slot index="2" />
<c-input-otp.slot index="3" />
</c-input-otp.group>
</c-input-otp>
</c-docs.demo-section>

```html
<c-input-otp maxlength="4" name="pin">
    <c-input-otp.group>
        <c-input-otp.slot index="0" />
        <c-input-otp.slot index="1" />
        <c-input-otp.slot index="2" />
        <c-input-otp.slot index="3" />
    </c-input-otp.group>
</c-input-otp>
```

One real input sits transparent over the boxes and holds the whole code, so
pasting works, the browser can autofill it from an SMS, and phones show the
number pad. The boxes below only draw what that input contains. `name` reaches
the input, so the field submits like any other.

Each slot carries its own `index`, the same way it does upstream.

## Examples

### Split into groups

<c-docs.demo-section>
<c-input-otp maxlength="6" name="split">
<c-input-otp.group>
<c-input-otp.slot index="0" />
<c-input-otp.slot index="1" />
<c-input-otp.slot index="2" />
</c-input-otp.group>
<c-input-otp.separator />
<c-input-otp.group>
<c-input-otp.slot index="3" />
<c-input-otp.slot index="4" />
<c-input-otp.slot index="5" />
</c-input-otp.group>
</c-input-otp>
</c-docs.demo-section>

```html
<c-input-otp maxlength="6" name="code">
    <c-input-otp.group>
        <c-input-otp.slot index="0" />
        <c-input-otp.slot index="1" />
        <c-input-otp.slot index="2" />
    </c-input-otp.group>
    <c-input-otp.separator />
    <c-input-otp.group>
        <c-input-otp.slot index="3" />
        <c-input-otp.slot index="4" />
        <c-input-otp.slot index="5" />
    </c-input-otp.group>
</c-input-otp>
```

### Disabled

<c-docs.demo-section>
<c-input-otp maxlength="4" disabled>
<c-input-otp.group>
<c-input-otp.slot index="0" />
<c-input-otp.slot index="1" />
<c-input-otp.slot index="2" />
<c-input-otp.slot index="3" />
</c-input-otp.group>
</c-input-otp>
</c-docs.demo-section>

```html
<c-input-otp maxlength="4" disabled>
    ...
</c-input-otp>
```

### In a Django form

```html
<c-field>
    <c-field.label for="{{ form.code.id_for_label }}">Verification code</c-field.label>
    <c-input-otp maxlength="6" name="{{ form.code.html_name }}" id="{{ form.code.id_for_label }}">
        <c-input-otp.group>
            <c-input-otp.slot index="0" />
            <c-input-otp.slot index="1" />
            <c-input-otp.slot index="2" />
            <c-input-otp.slot index="3" />
            <c-input-otp.slot index="4" />
            <c-input-otp.slot index="5" />
        </c-input-otp.group>
    </c-input-otp>
    <c-field.error :errors="form.code.errors" />
</c-field>
```

## Notes

The blinking caret sits on the box the next character will land in, which is
the slot at the current length. It is drawn, not real — the actual caret
belongs to the transparent input and is hidden.

Upstream restricts the accepted characters through a pattern prop. Here the
field takes whatever the input takes; `inputmode="numeric"` asks phones for the
number pad but does not enforce digits, so validate on the server as you would
with any other field.
