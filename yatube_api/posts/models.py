from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        'Название', max_length=200,
        help_text='Название группы'
    )
    slug = models.SlugField(unique=True)
    description = models.TextField(
        'Описание', blank=True,
        help_text='Описание группы'
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField('Текст поста')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        help_text='Дата первой публикации поста'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts', verbose_name='Автор',
        help_text='Автор поста'
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='posts', verbose_name='Группа',
        help_text='Группа, которой принадлежит пост'
    )
    image = models.ImageField(
        'Иллюстрация поста',
        upload_to='posts/',
        blank=True, null=True,
        help_text='Картинка, характеризующая данный пост'
    )

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментарий',
        help_text='Ваш комментарий к посту'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    created = models.DateTimeField(
        'Дата создания комментария',
        auto_now_add=True,
        help_text='Дата создания комментария или его последнего изменения'
    )
    text = models.TextField('Текст комментария')

    class Meta:
        ordering = ['-created']


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='followers',
        verbose_name='На кого подписан'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'], name='follow_record'
            )
        ]
