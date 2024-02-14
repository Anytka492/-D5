from django import template
import string

register = template.Library()

forbidden_words = ['хрен', 'Простофили']

@register.filter()
def censor(value):
    words = value.split()
    result = []
    for word in words:
        if word in forbidden_words:
            result.append(word[0] + "*"*(len(word)-2) + word[-1])
        else:
            result.append(word)
    return " ".join(result)
