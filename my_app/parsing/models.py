from django.db import models


class Job(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    page_link = models.URLField(
        'URL'
    )
    xp_level = models.CharField(
        max_length=100,
        verbose_name='Досвід роботи'
    )
    requirements = models.CharField(
        max_length=255,
        verbose_name='Вимоги'
    )
    time_publish = models.DateTimeField(
        'Дата публікації оголошення'
    )

    class Meta:
        verbose_name = 'Обява'
        verbose_name_plural = 'Обяви'
