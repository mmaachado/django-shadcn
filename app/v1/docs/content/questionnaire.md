---
title: Questionnaire
description: A question flow that walks one step at a time and still posts as a single form.
description.pt-br: Um fluxo de perguntas que avança um passo por vez e mesmo assim envia um formulário só.
description.es: Un flujo de preguntas que avanza paso a paso y aun así envía un solo formulario.
---

<c-docs.demo-section class="min-h-[420px]">
<c-questionnaire method="get" class="mx-auto w-full max-w-lg text-start">
<c-questionnaire.progress />

<c-questionnaire.item>
<c-questionnaire.title>What should we prototype next?</c-questionnaire.title>
<c-questionnaire.description>Choose one direction, or write another.</c-questionnaire.description>
<c-questionnaire.choices>
<c-questionnaire.choice name="direction" value="delegation" required>
<span class="font-medium">Sub-agent delegation</span>
<c-questionnaire.choice_description>Show when work is delegated and what comes back.</c-questionnaire.choice_description>
</c-questionnaire.choice>
<c-questionnaire.choice name="direction" value="questions" required>
<span class="font-medium">Question prompts</span>
<c-questionnaire.choice_description>Show choices while the agent waits for input.</c-questionnaire.choice_description>
</c-questionnaire.choice>
<c-questionnaire.input name="direction_other" aria-label="Another direction" placeholder="Type another direction" />
</c-questionnaire.choices>
<c-questionnaire.error />
</c-questionnaire.item>

<c-questionnaire.item>
<c-questionnaire.title>What should every update include?</c-questionnaire.title>
<c-questionnaire.description>Select all that apply, or skip this question.</c-questionnaire.description>
<c-questionnaire.choices>
<c-questionnaire.choice type="checkbox" name="signals" value="progress">Progress</c-questionnaire.choice>
<c-questionnaire.choice type="checkbox" name="signals" value="decisions">Decisions</c-questionnaire.choice>
<c-questionnaire.choice type="checkbox" name="signals" value="risks">Risks</c-questionnaire.choice>
</c-questionnaire.choices>
<c-questionnaire.error />
</c-questionnaire.item>

<c-questionnaire.item>
<c-questionnaire.title>When should this be revisited?</c-questionnaire.title>
<c-questionnaire.choices>
<c-questionnaire.choice name="timing" value="week" required>This week</c-questionnaire.choice>
<c-questionnaire.choice name="timing" value="later" required>Revisit later</c-questionnaire.choice>
</c-questionnaire.choices>
<c-questionnaire.error />
</c-questionnaire.item>

<c-questionnaire.actions>
<c-questionnaire.previous />
<c-questionnaire.skip />
<c-questionnaire.next />
<c-questionnaire.submit>Save answers</c-questionnaire.submit>
</c-questionnaire.actions>
</c-questionnaire>
</c-docs.demo-section>

<c-docs.cheat-sheet name="questionnaire">
<c-questionnaire action="{% url 'onboarding' %}" method="post">
    {% csrf_token %}
    <c-questionnaire.progress />

    <c-questionnaire.item>
        <c-questionnaire.title>What should we prototype next?</c-questionnaire.title>
        <c-questionnaire.choices>
            <c-questionnaire.choice name="direction" value="delegation" required>
                Sub-agent delegation
            </c-questionnaire.choice>
            <c-questionnaire.choice name="direction" value="questions" required>
                Question prompts
            </c-questionnaire.choice>
        </c-questionnaire.choices>
        <c-questionnaire.error />
    </c-questionnaire.item>

    <c-questionnaire.actions>
        <c-questionnaire.previous />
        <c-questionnaire.skip />
        <c-questionnaire.next />
        <c-questionnaire.submit />
    </c-questionnaire.actions>
</c-questionnaire>
</c-docs.cheat-sheet>

:::en
<p class="mt-4 text-sm text-muted-foreground">
    The demo above uses <code>method="get"</code>, so submitting it puts the
    answers in the address bar where you can read them. Yours will post.
</p>

## Installation
:::pt-br
<p class="mt-4 text-sm text-muted-foreground">
    A demo acima usa <code>method="get"</code>, então enviá-la põe as respostas
    na barra de endereço, onde você pode lê-las. O seu vai usar POST.
</p>

## Instalação
:::

```bash
uvx django_shadcn@latest add questionnaire
```

:::en
## Usage
:::pt-br
## Uso
:::

```html
<c-questionnaire action="{% url 'onboarding' %}" method="post">
    {% csrf_token %}
    <c-questionnaire.progress />

    <c-questionnaire.item>
        <c-questionnaire.title>What should we prototype next?</c-questionnaire.title>
        <c-questionnaire.choices>
            <c-questionnaire.choice name="direction" value="delegation" required>
                Sub-agent delegation
            </c-questionnaire.choice>
            <c-questionnaire.choice name="direction" value="questions" required>
                Question prompts
            </c-questionnaire.choice>
        </c-questionnaire.choices>
        <c-questionnaire.error />
    </c-questionnaire.item>

    <c-questionnaire.actions>
        <c-questionnaire.previous />
        <c-questionnaire.skip />
        <c-questionnaire.next />
        <c-questionnaire.submit />
    </c-questionnaire.actions>
</c-questionnaire>
```

:::en
## One form, every question

The questions are not swapped in and out. All of them are rendered, inside one
`<form>`, and Alpine hides the ones that are not the current step.

That is the whole design, and two things follow from it:

- **The final POST carries every answer**, including the ones given five steps
  ago. There is nothing to stash, no hidden mirror of the state, no session to
  keep in step with the page.
- **Radio and checkbox groups keep their native behaviour** — arrow keys,
  grouping by `name`, and `required` meaning what it means everywhere else.

An inactive question is `hidden` and `inert`, so neither the tab order nor a
screen reader reaches it. A control inside it still posts: only `disabled`
would drop a value, and nothing here is disabled.

## Questions

Each question is an item. Give the controls a `name` and the view reads them
back under that name — the component adds nothing of its own to the payload.
:::pt-br
## Um formulário, todas as perguntas

As perguntas não são trocadas umas pelas outras. Todas são renderizadas, dentro
de um único `<form>`, e o Alpine esconde as que não são a etapa atual.

Esse é o design inteiro, e duas coisas decorrem dele:

- **O POST final leva todas as respostas**, inclusive as dadas cinco etapas
  atrás. Não há nada a guardar, nenhum espelho escondido do estado, nenhuma
  sessão para manter em sincronia com a página.
- **Os grupos de radio e de checkbox mantêm o comportamento nativo** — as setas
  do teclado, o agrupamento por `name` e `required` significando o que significa
  em todo outro lugar.

Uma pergunta inativa é `hidden` e `inert`, então nem a ordem de tab nem um
leitor de tela chegam a ela. Um controle dentro dela continua sendo enviado: só
`disabled` descartaria um valor, e nada aqui está desabilitado.

## Perguntas

Cada pergunta é um item. Dê um `name` aos controles e a view os lê de volta com
esse nome — o componente não acrescenta nada próprio ao que é enviado.
:::

<c-docs.example>
<c-questionnaire method="get" class="mx-auto w-full max-w-lg text-start">
  <c-questionnaire.progress />
  <c-questionnaire.item>
    <c-questionnaire.title>Pick one</c-questionnaire.title>
    <c-questionnaire.choices>
      <c-questionnaire.choice name="single" value="a" required>The first</c-questionnaire.choice>
      <c-questionnaire.choice name="single" value="b" required>The second</c-questionnaire.choice>
    </c-questionnaire.choices>
    <c-questionnaire.error />
  </c-questionnaire.item>
  <c-questionnaire.actions>
    <c-questionnaire.previous />
    <c-questionnaire.skip />
    <c-questionnaire.next />
    <c-questionnaire.submit />
  </c-questionnaire.actions>
</c-questionnaire>
</c-docs.example>

:::en
`title` renders the `<legend>` of the item's `<fieldset>`, so it names the
group for a screen reader without any wiring.

### Several answers

`type="checkbox"` turns the choices into a multi-select. The view reads them
with `getlist`.
:::pt-br
`title` renderiza o `<legend>` do `<fieldset>` do item, então ele dá nome ao
grupo para um leitor de tela sem nenhuma ligação extra.

### Várias respostas

`type="checkbox"` transforma as opções numa seleção múltipla. A view as lê com
`getlist`.
:::

```html
<c-questionnaire.choice type="checkbox" name="signals" value="progress">
    Progress
</c-questionnaire.choice>
```

:::en
### A freeform answer

`input` sits inside `choices`, alongside the fixed ones, for the answer you did
not think of.
:::pt-br
### Uma resposta livre

O `input` fica dentro de `choices`, ao lado das opções fixas, para a resposta em
que você não pensou.
:::

```html
<c-questionnaire.choices>
    <c-questionnaire.choice name="direction" value="delegation">Delegation</c-questionnaire.choice>
    <c-questionnaire.input name="direction_other" aria-label="Another direction"
                           placeholder="Type another direction" />
</c-questionnaire.choices>
```

:::en
It has no visible label of its own, so give it an `aria-label`.

### A longer answer

`choices` is not required. An item can hold anything.
:::pt-br
Ele não tem um rótulo visível próprio, então dê a ele um `aria-label`.

### Uma resposta mais longa

`choices` não é obrigatório. Um item pode conter qualquer coisa.
:::

```html
<c-questionnaire.item>
    <c-questionnaire.title>Anything else?</c-questionnaire.title>
    <c-textarea name="notes" placeholder="Optional" />
</c-questionnaire.item>
```

:::en
## Required, and skipping

Put `required` on the controls, not on the item. The browser is what decides
whether an answer counts, and `next` simply refuses to move while the current
question has a control the browser calls invalid — moving focus there and
showing its message.

`skip` appears only when the current question has no required control, so an
optional question can be passed over and a required one cannot.

For a radio group, `required` on the choices means *one of them* must be
chosen, which is what you want. **A checkbox group is different:** `required`
on a checkbox means that one box must be ticked, so there is no way to say
"at least one of these" in HTML. Leave those optional and check them in the
view.

### Why the form is `novalidate`

Left alone, the browser refuses to submit an invalid form and tries to focus
the offending control. Here that control is usually inside a question that is
hidden, so the focus fails and the browser reports nothing at all — the form
would look broken while doing exactly what it was told.

So the form carries `novalidate` and the checking is driven from the
component: on `next` for the current question, and on submit for every
question, jumping back to the first one that fails. The messages are still the
browser's own.

## Reading the answers

An ordinary view, and nothing else:
:::pt-br
## Obrigatório, e pular

Ponha `required` nos controles, não no item. Quem decide se uma resposta vale é
o navegador, e o `next` simplesmente se recusa a avançar enquanto a pergunta
atual tiver um controle que o navegador considera inválido — levando o foco até
ele e mostrando a mensagem dele.

O `skip` só aparece quando a pergunta atual não tem nenhum controle obrigatório,
então uma pergunta opcional pode ser pulada e uma obrigatória não.

Num grupo de radio, `required` nas opções quer dizer que *uma delas* tem de ser
escolhida, que é o que você quer. **Um grupo de checkbox é diferente:**
`required` num checkbox quer dizer que aquela caixa tem de ser marcada, então
não há como dizer "pelo menos uma destas" em HTML. Deixe essas opcionais e
confira na view.

### Por que o formulário é `novalidate`

Por conta própria, o navegador se recusa a enviar um formulário inválido e tenta
dar foco ao controle problemático. Aqui esse controle costuma estar dentro de
uma pergunta escondida, então o foco falha e o navegador não informa nada — o
formulário pareceria quebrado enquanto faz exatamente o que lhe mandaram.

Por isso o formulário leva `novalidate` e a verificação é conduzida pelo
componente: no `next`, para a pergunta atual, e no envio, para todas as
perguntas, voltando à primeira que falhar. As mensagens continuam sendo as do
próprio navegador.

## Lendo as respostas

Uma view comum, e mais nada:
:::

```python
def onboarding(request):
    if request.method == 'POST':
        answers = {
            'direction': request.POST.get('direction'),
            'direction_other': request.POST.get('direction_other', ''),
            'signals': request.POST.getlist('signals'),
            'timing': request.POST.get('timing'),
        }
        ...
```

:::en
A Django `Form` works just as well: the payload is a flat set of names, so
declare the fields and let it validate. Server-side validation is not optional
just because the page did some too — `novalidate` means a client with no
JavaScript posts everything at once, unchecked.

## Without JavaScript

Nothing is hidden until Alpine hides it, so a page with no JavaScript shows
every question at once, in one long form, and the submit button still works.
The step-by-step is an improvement on top of a form that already functions.
:::pt-br
Um `Form` do Django funciona igualmente bem: o que é enviado é um conjunto plano
de nomes, então declare os campos e deixe-o validar. A validação no servidor não
é opcional só porque a página também fez alguma — `novalidate` quer dizer que um
cliente sem JavaScript envia tudo de uma vez, sem verificação.

## Sem JavaScript

Nada fica escondido até o Alpine esconder, então uma página sem JavaScript
mostra todas as perguntas de uma vez, num formulário longo, e o botão de enviar
continua funcionando. O passo a passo é uma melhoria por cima de um formulário
que já funciona.
:::

:::en
## RTL

The questions, the choices and the buttons follow the text, so under
`dir="rtl"` the form mirrors, with next and back changing sides.

## Accessibility

Each question is a `<fieldset>` whose `<legend>` is the title, so a group of
radios is announced by its question. Inactive questions are `hidden` and
`inert`, out of the tab order and the reading order. The progress is a
`role="progressbar"` with the step in `aria-valuetext`, and moving between
steps moves focus to the new question.

## API reference
:::pt-br
## RTL

As perguntas, as opções e os botões acompanham o texto, então sob
`dir="rtl"` o formulário espelha, com avançar e voltar trocando de lado.

## Acessibilidade

Cada pergunta é um `<fieldset>` cuja `<legend>` é o título, então um grupo de
radios é anunciado pela pergunta. As perguntas inativas são `hidden` e `inert`,
fora da ordem de tab e da leitura. O progresso é um `role="progressbar"` com a
etapa em `aria-valuetext`, e passar de uma etapa para outra leva o foco à nova
pergunta.

## Referência da API
:::

<c-docs.api-reference name="questionnaire" />
