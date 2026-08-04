dependencies = {
    'a': [],
    'accordion': ['icon'],
    'alert': [],
    'alert_dialog': ['button'],
    'allauth': [
        'card',
        'button',
        'input',
        'label',
        'checkbox',
        'alert',
        'badge',
        'separator',
    ],
    'aspect_ratio': [],
    'avatar': [],
    'badge': [],
    'breadcrumb': ['icon'],
    'button': [],
    'button_group': ['button', 'separator'],
    'card': [],
    'combobox': ['button', 'popover', 'icon'],
    'collapsible': [],
    'command': ['icon'],
    'command_dialog': ['command'],
    'dialog': ['button', 'icon'],
    'checkbox': [],
    'dropdown_menu': [],
    'empty': [],
    'field': ['label', 'separator'],
    'form': ['label'],
    'hover_card': [],
    'icon': [],
    'input': [],
    'input_group': ['button', 'input', 'textarea'],
    'item': ['separator'],
    'kbd': [],
    'label': [],
    'native_select': ['icon'],
    'navigation_menu': ['icon'],
    'pagination': ['icon'],
    'popover': [],
    'progress': [],
    'radio_group': [],
    'scroll_area': [],
    'select': ['icon'],
    'sheet': ['button', 'icon'],
    'separator': [],
    'skeleton': [],
    'spinner': ['icon'],
    'slider': [],
    'switch': [],
    'table': [],
    'tabs': [],
    'toast': ['icon'],
    'textarea': [],
    'toggle': [],
    'toggle_group': [],
    'tooltip': [],
    'typography': [],
}


def canonical(name: str) -> str:
    """Accept the cotton tag spelling as well as the directory name.

    The tag is <c-toggle-group> while the directory has to be toggle_group,
    so both reach the CLI and both should work.
    """
    if name in dependencies:
        return name

    return name.replace('-', '_')
