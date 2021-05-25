from django import template
register = template.Library()

@register.filter
def exclaim(value,arg):
    """
    This cuts out all values of "arg" and replaces with "!"
    """
    return value.replace(arg,'!')
