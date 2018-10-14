from django.db import models

class Broadcast(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    def __str__(self):
        return self.name

class SearchResults(models.Model):
    word = models.CharField('Поиск', max_length=100)
    search = models.ManyToManyField(Broadcast, verbose_name='Результаты')
    def __str__(self):
        return self.word