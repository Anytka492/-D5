from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostEdit, PostDelete
from .import views

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('news/', PostList.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='news_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
]