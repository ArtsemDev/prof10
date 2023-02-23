from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import View
from django.views.decorators.http import require_GET
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

    def get(self, request, *args, **kwargs):
        posts = self.get_queryset()
        text = ''
        for post in posts:
            text += f'<a href="{post.get_absolute_url()}">{post.title}</a></br>'
        return HttpResponse(text)


# @require_GET
# def post_list(request: HttpRequest):
#     posts = Post.objects.all()
#     text = ''
#     for post in posts:
#         text += f'<a href="{post.get_absolute_url()}">{post.title}</a></br>'
#     return HttpResponse(text)


@require_GET
def post_detail(request: HttpRequest, post_slug: str):
    post = get_object_or_404(Post, slug=post_slug)
    # post = Post.objects.get(slug=post_slug)
    text = f'<b>{post.title}</b></br><b>{post.body}</b>'
    return HttpResponse(text)


def error(request, exception):
    print(exception)
    return HttpResponse(f'<b>{exception}</b>')
