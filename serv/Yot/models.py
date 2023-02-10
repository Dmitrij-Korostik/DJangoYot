from django.db import models
from django.urls import reverse


# Create your models here.

# from django.db import connection

# connection.queries
# просмотр sql запроса который был выполнен!

# выбераем все записи равные либо меньше 4 по Id
# tablica.objects.filter(pk__lte=4).order_by('title')
# потом сортируем по алфавиту


class tablica(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Текст Статьи') #TextField текстовый файл, blank=True параметр обозначает что поле может быть пустым!
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото') #фото будет хранить ссылку на нашу фотографию, upload_to Говорит в какой каталог и какие под каталоги будут добавлятся фото!
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания') # Время создания статьи
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения') # время последнего его редактирования
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Знаменитые люди'
        verbose_name_plural = 'Знаменитые люди'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name='Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


