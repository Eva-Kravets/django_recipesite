from django.db import models
from django.urls import reverse


class Dish(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")
    steps = models.TextField(blank=True, verbose_name="Шаги приготовления")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        ordering = ['cat', 'title', 'id']
        verbose_name = 'блюдо'
        verbose_name_plural = 'Блюда'

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'prod_id': self.pk})

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'

class Amount(models.Model):
    amount = models.CharField(max_length=100, db_index=True, verbose_name="Количество")

    def __str__(self):
        return self.amount

    def get_absolute_url(self):
        return reverse('amount', kwargs={'am_id': self.pk})

    class Meta:
        verbose_name = 'Количество'
        verbose_name_plural = 'Количество'

class Ingredients(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    am = models.ForeignKey('Amount', on_delete=models.PROTECT, verbose_name="Количество")
    prod = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name="Продукт")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredients', kwargs={'ingred_id': self.pk})

    class Meta:
        verbose_name = 'Ингредиенты'
        verbose_name_plural = 'Ингредиенты'



#class Step(models.Model):
#   name = models.CharField(max_length=100, db_index=True, verbose_name="Номер шага")
#   content = models.TextField(blank=True, verbose_name="Описание")
#   dis = models.ForeignKey('Dish', on_delete=models.PROTECT, verbose_name="Блюдо")

#    def __str__(self):
#       return self.name

#   def get_absolute_url(self):
#       return reverse('step', kwargs={'step_slug': self.slug})

#   class Meta:
#       verbose_name = 'Этапы'
#       verbose_name_plural = 'Этапы'
#       ordering = ['id', 'dis', 'name']

class Advice(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    content = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('advice', kwargs={'advice_id': self.pk})

    class Meta:
        verbose_name = 'Советы'
        verbose_name_plural = 'Советы'

class Instruments(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    content = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('instruments', kwargs={'instruments_id': self.pk})

    class Meta:
        verbose_name = 'Инструменты'
        verbose_name_plural = 'Инструменты'

class Serving(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    content = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('serving', kwargs={'serving_id': self.pk})

    class Meta:
        verbose_name = 'Идеи подачи'
        verbose_name_plural = 'Идеи подачи'
