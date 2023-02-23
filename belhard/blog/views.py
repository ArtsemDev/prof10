from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView
from slugify import slugify

from .models import Post
from .forms import PostModelForm


class PostListView(ListView):
    model = Post
    # template_name = 'blog/post_list.html'
    http_method_names = ('get', 'post')
    # context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data()
        context['post_form'] = PostModelForm()
        return context

    def post(self, request: HttpRequest):
        data = request.POST.dict()
        data.update(slug=slugify(request.POST.get('title')))
        form = PostModelForm(data)
        # if form.is_valid():
        #   form.save()
        return self.get(request=request)

    # def get(self, request, *args, **kwargs):
    #     posts = self.get_queryset()
    #     text = ''
    #     for post in posts:
    #         text += f'<a href="{post.get_absolute_url()}">{post.title}</a></br>'
    #     return HttpResponse(text)


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    # slug_field = 'slug'

    http_method_names = ('get', )

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)
        return get_object_or_404(self.model, Q(slug=slug) & Q(is_published=True))

    def get(self, *args, **kwargs):
        obj = self.get_object()
        text = f'<b>{obj.title}</b></br><b>{obj.body}</b>'
        return HttpResponse(text)

# @require_GET
# def post_list(request: HttpRequest):
#     posts = Post.objects.all()
#     text = ''
#     for post in posts:
#         text += f'<a href="{post.get_absolute_url()}">{post.title}</a></br>'
#     return HttpResponse(text)


# @require_GET
# def post_detail(request: HttpRequest, post_slug: str):
#     post = get_object_or_404(Post, slug=post_slug)
#     # post = Post.objects.get(slug=post_slug)
#     text = f'<b>{post.title}</b></br><b>{post.body}</b>'
#     return HttpResponse(text)


def error(request, exception):
    print(exception)
    return HttpResponse(f'<b>{exception}</b>')
