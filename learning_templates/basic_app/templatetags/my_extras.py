from django import template

register = template.Library()

@register.filter(name='cut1')
def cut1(value,arg):
    """
    This cuts out all values "arg" from string!
    """
    return value.replace(arg,'')

# druga metoda registracije umjesto dekoratora @
# register.filter('cut1',cut1)
