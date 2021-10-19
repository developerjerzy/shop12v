from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    """
    Создание в базе данных таблицы продуктов

    Параметры:
    Категория продуктов
    Название
    Флаг
    Фото товара
    Описание
    Цена
    Доступен или нет
    Дата создания
    Дата обновления
    """
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class Comment(models.Model):
    """
    Класс отвечает за создание в базе данных таблицы комментариев

    Пост опубликованный пост, к которому относится комментарий
    Имя того кто создал комментарий
    Емейл человека который создал комментарий
    Тело комментария
    Дата создания комментария
    Дата обновления комментария
    Дата когда комментарий был опубликован
    """
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',verbose_name=u"Пользователь")
    name = models.CharField(max_length=80,verbose_name=u"Имя")
    email = models.EmailField()
    body = models.TextField(verbose_name=u"Текст комментария")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
