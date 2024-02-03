from django import template
from django.utils.datastructures import MultiValueDictKeyError
from Menu.models import Items


register = template.Library()


@register.inclusion_tag('Menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu):
    items = Items.objects.filter(menu__title=menu)
    items_values = items.values()
    parent_items = [item for item in items_values.filter(parent=None)]
    try:
        selected_item = items.get(id=context['request'].GET[menu])
        id_items_list = get_id_items_list(selected_item)
        for parent in parent_items:
            if parent['id'] in id_items_list:
                parent['child_items'] = get_child_items(items_values, parent['id'],  id_items_list)
        result_dict = {'items': parent_items}
    except MultiValueDictKeyError:
        result_dict = {'items': parent_items}
    result_dict['menu'] = menu
    return result_dict


def get_id_items_list(parent):
    id_items_list = []
    while parent:
        id_items_list.append(parent.id)
        parent = parent.parent
    return id_items_list


def get_child_items(item_values, current_parent_id,  id_items_list):
    current_parent_child_list = [
        item for item in item_values.filter(parent_id=current_parent_id)
    ]
    for child in current_parent_child_list:
        if child['id'] in id_items_list:
            child['child_items'] = get_child_items(
                item_values, child['id'], id_items_list)

    return current_parent_child_list

