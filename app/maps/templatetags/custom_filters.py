from django import template

register = template.Library()

@register.filter(name='get_alpha_code')
def get_alpha_code(dictionary, species_number):
    return dictionary.get(species_number, {}).get('alpha_code', 'Unknown species')
