from django import template

register = template.Library()


@register.filter(name='lookup')
def lookup(_dict, key):
    value = _dict.get(key)
    return value


register.filter('lookup', lookup)
