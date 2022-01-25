from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import SlugField, TextField
from django.db.models.constraints import UniqueConstraint

User = get_user_model()

class Clinic(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название ветеринарного учреждения'
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Ветеринарное учреждение'
        verbose_name_plural = 'Ветеринарные учреждения'

    def __str__(self):
        return self.title


class Comment(models.Model):
    clinic = models.ForeignKey(
        Clinic,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Ветеринарное учреждение',
        help_text="Ветеринарное учреждение, к которому будет относиться комментарий."
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
        help_text="Автор комментария."
    )
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата',
        help_text="Дата комментария"
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'

    def __str__(self):
        return self.text