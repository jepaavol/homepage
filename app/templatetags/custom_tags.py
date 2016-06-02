from django import template

register = template.Library()

@register.filter
def to_model_name(value):
    return value._meta.object_name


@register.filter(name='lowerStrip')
def remove_whitespace_and_lower(value):
    value = value.replace(' ', '')
    return value.lower()