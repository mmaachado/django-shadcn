---
title: Questionnaire
description: A question flow that walks one step at a time and still posts as a single form.
description.pt-br: Um fluxo de perguntas que avança um passo por vez e mesmo assim envia um formulário só.
description.es: Un flujo de preguntas que avanza paso a paso y aun así envía un solo formulario.
---

<c-docs.demo-section class="min-h-[420px]">
<c-questionnaire method="get" class="mx-auto w-full max-w-lg text-left">
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

<p class="mt-4 text-sm text-muted-foreground">
    The demo above uses <code>method="get"</code>, so submitting it puts the
    answers in the address bar where you can read them. Yours will post.
</p>

## Installation

```bash
uvx django_shadcn@latest add questionnaire
```

## Usage

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

<c-docs.demo-section>
<c-questionnaire method="get" class="mx-auto w-full max-w-lg text-left">
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
</c-docs.demo-section>

```html
<c-questionnaire.item>
    <c-questionnaire.title>Pick one</c-questionnaire.title>
    <c-questionnaire.description>Optional helper text.</c-questionnaire.description>
    <c-questionnaire.choices>
        <c-questionnaire.choice name="single" value="a" required>The first</c-questionnaire.choice>
        <c-questionnaire.choice name="single" value="b" required>The second</c-questionnaire.choice>
    </c-questionnaire.choices>
    <c-questionnaire.error />
</c-questionnaire.item>
```

`title` renders the `<legend>` of the item's `<fieldset>`, so it names the
group for a screen reader without any wiring.

### Several answers

`type="checkbox"` turns the choices into a multi-select. The view reads them
with `getlist`.

```html
<c-questionnaire.choice type="checkbox" name="signals" value="progress">
    Progress
</c-questionnaire.choice>
```

### A freeform answer

`input` sits inside `choices`, alongside the fixed ones, for the answer you did
not think of.

```html
<c-questionnaire.choices>
    <c-questionnaire.choice name="direction" value="delegation">Delegation</c-questionnaire.choice>
    <c-questionnaire.input name="direction_other" aria-label="Another direction"
                           placeholder="Type another direction" />
</c-questionnaire.choices>
```

It has no visible label of its own, so give it an `aria-label`.

### A longer answer

`choices` is not required. An item can hold anything.

```html
<c-questionnaire.item>
    <c-questionnaire.title>Anything else?</c-questionnaire.title>
    <c-textarea name="notes" placeholder="Optional" />
</c-questionnaire.item>
```

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

A Django `Form` works just as well: the payload is a flat set of names, so
declare the fields and let it validate. Server-side validation is not optional
just because the page did some too — `novalidate` means a client with no
JavaScript posts everything at once, unchecked.

## Without JavaScript

Nothing is hidden until Alpine hides it, so a page with no JavaScript shows
every question at once, in one long form, and the submit button still works.
The step-by-step is an improvement on top of a form that already functions.
