from django.urls import path
from .views import *
from .views import CategoryListView
from .import views

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('news/', PostList.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='news_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),

    path('article/', ArticleList.as_view(), name='article_list'),
    path('article/<int:id>/', ArticleDetail.as_view(), name='article_detail'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/update/', ArticleEdit.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
]
