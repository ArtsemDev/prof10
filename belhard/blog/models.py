from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='название',
        unique=True,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Post(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='заголовок',
        null=False,
        blank=False
    )
    body = models.TextField(
        verbose_name='пост',
        null=False,
        blank=False
    )
    slug = models.SlugField(
        verbose_name='URL',
        null=False,
        blank=False,
        unique=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name='категория'
    )
    date_created = models.DateTimeField(
        verbose_name='дата создания',
        default=now
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор'
    )
    is_published = models.BooleanField(default=False, verbose_name='публикация')

    @property
    def date(self):
        return self.date_created.strftime('%a %d %b %Y %H:%M')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post_detail', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
