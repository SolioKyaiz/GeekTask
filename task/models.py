from django.db import models
from django.db import models

class Task(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )

    description = models.TextField(
        verbose_name='Описание'
    )

    completed = models.BooleanField(
        default=False,
        verbose_name = 'Завершенные'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )