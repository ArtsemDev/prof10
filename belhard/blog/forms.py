from django.forms import ModelForm, TextInput, Textarea, Select

from .models import Post


class PostModelForm(ModelForm):

    class Meta:
        model = Post
        # fields = ('__all__', )
        fields = ('title', 'body', 'category', 'author', 'slug')
        widgets = {
            'title': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'title',
                    'placeholder': 'Enter Post Title'
                }
            ),
            'body': Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'body',
                    'placeholder': 'Enter Post Body'
                }
            ),
            'author': Select(
                attrs={
                    'class': 'form-control',
                    'id': 'author'
                }
            ),
            'category': Select(
                attrs={
                    'class': 'form-control',
                    'id': 'category'
                }
            ),
            'slug': TextInput(
                attrs={
                    'id': 'slug',
                    'value': 'slug'
                }
            )
        }
