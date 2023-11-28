import django_filters
from django_filters import FilterSet, DateTimeFilter, CharFilter, ModelChoiceFilter
from .models import *
from django.forms import DateTimeInput


class PostFilter(FilterSet):
    model = Post
    fields = {'title', 'Category', 'dateCreation', 'Author'}
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Заголовок',
    )

    search_category = ModelChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Категория поста',
        empty_label='Все категории',
    )

    # search_category = Author(
    #     field_name='authorUser',
    #     queryset=Category.objects.all(),
    #     label='Автор',
    #     empty_label='Автор',
    # )
    date = django_filters.IsoDateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Дата создания',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        )
    )