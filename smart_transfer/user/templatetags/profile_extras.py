from django import template

register = template.Library()

@register.filter
def capitalize_field(value):
    return value.capitalize() if isinstance(value, str) else value
