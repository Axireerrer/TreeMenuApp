from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название меню")

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['title'])
        ]
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    objects = models.Manager()


class Items(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, verbose_name="Название меню",
                             related_name='items', blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name="Раздел меню")
    parent = models.ForeignKey('self', on_delete=models.PROTECT, verbose_name="Раздел родитель",
                               related_name='children', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['menu', 'title'])
        ]
        verbose_name = 'Разделы меню'
        verbose_name_plural = 'Разделы меню'

    objects = models.Manager()