from dataclasses import dataclass


@dataclass(frozen=True)
class Component:
    """What `add` has to know about a component besides its files.

    `scripts` names JavaScript the markup needs and Alpine's core does not
    provide. A component that declares one renders without erroring and
    without behaving, so `add` has to say so.
    """

    depends: tuple[str, ...] = ()
    scripts: tuple[str, ...] = ()


COLLAPSE = '@alpinejs/collapse'

registry: dict[str, Component] = {
    'a': Component(),
    'accordion': Component(depends=('icon',), scripts=(COLLAPSE,)),
    'alert': Component(),
    'alert_dialog': Component(depends=('button',)),
    'allauth': Component(
        depends=(
            'card',
            'button',
            'input',
            'label',
            'checkbox',
            'alert',
            'badge',
            'separator',
        )
    ),
    'aspect_ratio': Component(),
    'attachment': Component(depends=('button', 'icon')),
    'avatar': Component(),
    'badge': Component(),
    'breadcrumb': Component(depends=('icon',)),
    'bubble': Component(depends=('collapsible',)),
    'button': Component(),
    'button_group': Component(depends=('button', 'separator')),
    'card': Component(),
    'combobox': Component(depends=('button', 'popover', 'icon')),
    'collapsible': Component(scripts=(COLLAPSE,)),
    'context_menu': Component(depends=('icon',)),
    'command': Component(depends=('icon',)),
    'command_dialog': Component(depends=('command',)),
    'dialog': Component(depends=('button', 'icon')),
    'checkbox': Component(),
    'drawer': Component(),
    'dropdown_menu': Component(depends=('icon',)),
    'empty': Component(),
    'field': Component(depends=('label', 'separator')),
    'form': Component(depends=('label',)),
    'hover_card': Component(),
    'icon': Component(),
    'input': Component(),
    'input_otp': Component(depends=('icon',)),
    'input_group': Component(depends=('button', 'input', 'textarea')),
    'item': Component(depends=('separator',)),
    'kbd': Component(),
    'label': Component(),
    'marker': Component(depends=('icon',)),
    'menubar': Component(depends=('icon',)),
    'message': Component(depends=('avatar',)),
    'message_scroller': Component(depends=('icon',)),
    'native_select': Component(depends=('icon',)),
    'navigation_menu': Component(depends=('icon',)),
    'pagination': Component(depends=('icon',)),
    'popover': Component(),
    'progress': Component(),
    'questionnaire': Component(depends=('icon',)),
    'radio_group': Component(),
    'resizable': Component(depends=('icon',)),
    'scroll_area': Component(),
    'select': Component(depends=('icon',)),
    'sheet': Component(depends=('button', 'icon')),
    'separator': Component(),
    'sidebar': Component(depends=('icon',)),
    'skeleton': Component(),
    'spinner': Component(depends=('icon',)),
    'slider': Component(),
    'switch': Component(),
    'table': Component(),
    'tabs': Component(),
    'toast': Component(depends=('icon',)),
    'textarea': Component(),
    'toggle': Component(),
    'toggle_group': Component(),
    'tooltip': Component(),
    'typography': Component(),
}


def canonical(name: str) -> str:
    """Accept the cotton tag spelling as well as the directory name.

    The tag is <c-toggle-group> while the directory has to be toggle_group,
    so both reach the CLI and both should work. Case and surrounding space
    are what a shell and a copied doc line leave behind, not a different
    component.
    """
    if name in registry:
        return name

    return name.strip().lower().replace('-', '_')
