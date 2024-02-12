from .models import *
from modeltranslation.translator import register, TranslationOptions  # импортируем декоратор для перевода и класс настроек, от которого будем наследоваться


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)  # указываем, какие именно поля надо переводить в виде кортежа


@register(Post)
class MyModelTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


@register(Comment)
class MyModelTranslationOptions(TranslationOptions):
    fields = ('text',)