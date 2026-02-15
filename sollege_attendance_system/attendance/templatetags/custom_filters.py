from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Get item from dictionary by key"""
    if dictionary is None:
        return []
    return dictionary.get(key, [])

@register.filter(name='dict_lookup')
def dict_lookup(dictionary, key):
    """
    Custom filter to look up dictionary values by key in templates
    Usage: {{ my_dict|dict_lookup:key }}
    """
    if dictionary is None:
        return []
    return dictionary.get(key, [])