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

<c-docs.cheat-sheet name="input-otp">
<c-input-otp maxlength="4" name="pin">
  <c-input-otp.group>
    <c-input-otp.slot index="0" />
    <c-input-otp.slot index="1" />
    <c-input-otp.slot index="2" />
    <c-input-otp.slot index="3" />
  </c-input-otp.group>
</c-input-otp>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add input_otp
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-input-otp maxlength="4" name="pin">
  <c-input-otp.group>
    <c-input-otp.slot index="0" />
    <c-input-otp.slot index="1" />
    <c-input-otp.slot index="2" />
    <c-input-otp.slot index="3" />
  </c-input-otp.group>
</c-input-otp>
</c-docs.example>

:::en
One real input sits transparent over the boxes and holds the whole code, so
pasting works, the browser can autofill it from an SMS, and phones show the
number pad. The boxes below only draw what that input contains. `name` reaches
the input, so the field submits like any other.

Each slot carries its own `index`, the same way it does upstream.

## Examples

### Split into groups
:::pt-br
Um input de verdade fica transparente sobre as caixas e guarda o código
inteiro, então colar funciona, o navegador pode preenchê-lo a partir de um SMS e
os celulares mostram o teclado numérico. As caixas de baixo só desenham o que
esse input contém. O `name` chega ao input, então o campo é enviado como
qualquer outro.

Cada slot leva o próprio `index`, do mesmo jeito que no upstream.

## Exemplos

### Dividido em grupos
:::

<c-docs.example>
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
</c-docs.example>

:::en
### Disabled
:::pt-br
### Desabilitado
:::

<c-docs.example>
<c-input-otp maxlength="4" disabled>
  <c-input-otp.group>
    <c-input-otp.slot index="0" />
    <c-input-otp.slot index="1" />
    <c-input-otp.slot index="2" />
    <c-input-otp.slot index="3" />
  </c-input-otp.group>
</c-input-otp>
</c-docs.example>

:::en
### In a Django form
:::pt-br
### Num formulário Django
:::

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

:::en
### Four digits

`maxlength` sets the length, and the slots follow it.
:::pt-br
### Quatro dígitos

O `maxlength` define o tamanho, e os slots o acompanham.
:::

<c-docs.example>
<c-input-otp maxlength="4" aria-label="PIN">
  <c-input-otp.group>
    <c-input-otp.slot index="0" />
    <c-input-otp.slot index="1" />
    <c-input-otp.slot index="2" />
    <c-input-otp.slot index="3" />
  </c-input-otp.group>
</c-input-otp>
</c-docs.example>

:::en
## RTL

The code reads left to right in every language, so the slots keep their
order under `dir="rtl"`, as a one-time code is typed.

## Accessibility

One real input holds the whole code, so a screen reader hears a single
field, and it carries `autocomplete="one-time-code"`, so the browser can fill it
from an SMS. Give it a label. The boxes draw its value as text and are not
hidden, so a screen reader can read the digits there too.

## API reference
:::pt-br
## RTL

O código é lido da esquerda para a direita em qualquer idioma, então os slots
mantêm a ordem sob `dir="rtl"`, como um código de uso único é digitado.

## Acessibilidade

Um input de verdade guarda o código inteiro, então um leitor de tela ouve um
campo só, e ele leva `autocomplete="one-time-code"`, então o navegador pode
preenchê-lo a partir de um SMS. Dê um rótulo a ele. As caixas desenham o valor
como texto e não ficam escondidas, então um leitor de tela também pode ler os
dígitos ali.

## Referência da API
:::

<c-docs.api-reference name="input-otp" />

:::en
## Notes

The blinking caret sits on the box the next character will land in, which is
the slot at the current length. It is drawn, not real — the actual caret
belongs to the transparent input and is hidden.

Upstream restricts the accepted characters through a pattern prop. Here the
field takes whatever the input takes; `inputmode="numeric"` asks phones for the
number pad but does not enforce digits, so validate on the server as you would
with any other field.
:::pt-br
## Observações

O cursor piscando fica na caixa em que o próximo caractere vai cair, que é o
slot no comprimento atual. Ele é desenhado, não é de verdade — o cursor real
pertence ao input transparente e fica escondido.

O upstream restringe os caracteres aceitos com uma prop de padrão. Aqui o campo
aceita o que o input aceitar; `inputmode="numeric"` pede aos celulares o teclado
numérico mas não obriga a digitar só números, então valide no servidor como
faria com qualquer outro campo.
:::
