from django import template

register = template.Library()

cens = ['хрен', 'Простофили']

@register.filter()
def change_querry(value):
    if isinstance(value, str):
        text = []
        text1 = value.split(" ")
        for i in text1:
            if i in cens:
                i = '***'
            text.append(i)
        return' '.join(text)