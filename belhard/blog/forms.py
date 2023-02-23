from django.forms import ModelForm

from .models import Post


class PostModelForm(ModelForm):
    class Meta:
        model = Post
        # fields = ('__all__', )
        fields = ('title', 'body', 'category', 'author')
