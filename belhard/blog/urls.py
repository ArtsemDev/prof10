from django.urls import path
from .views import *


urlpatterns = [
    path('', PostListView.as_view(), name='blog_post_list'),
    path('<slug:post_slug>/', post_detail, name='blog_post_detail'),
]
