from django.db import models


class ChapterBooks(models.Model):
    name = models.CharField(verbose_name="Название жанра", max_length=128)
    tag_alib = models.CharField(verbose_name="Тег алиба", max_length=128)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Books(models.Model):
    author = models.CharField(verbose_name="Автор", max_length=128)
    name = models.CharField(verbose_name="Название книги", max_length=128)
    chapter = models.ForeignKey(ChapterBooks, on_delete=models.CASCADE, verbose_name="Жанр", default=1)
    price = models.PositiveIntegerField(verbose_name="Цена")
    management = models.PositiveIntegerField(verbose_name="Номер коробки, где лежит книга")
    from_made_in = models.CharField(verbose_name="Место издательство", max_length=64, blank=True, null=True)
    made_in = models.CharField(verbose_name="Издательство", max_length=64, blank=True, null=True)
    year = models.PositiveIntegerField(verbose_name="Год выпуска", blank=True, null=True)
    pages = models.PositiveIntegerField(verbose_name="Сколько страниц?", blank=True, null=True)
    status = models.CharField(verbose_name="Состояние книги", max_length=32, blank=True, null=True)
    date_active = models.DateField(verbose_name="День рекламы", blank=True, null=True)
    comment = models.CharField(verbose_name="Комментарий", max_length=256, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"


class Photos(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name="Книга")
    photo = models.ImageField(verbose_name="Картинка книги", blank=True, null=True)

    def __str__(self):
        return f"{self.book.name}"

    class Meta:
        ordering = ["book"]
        verbose_name = "Фотографию книги"
        verbose_name_plural = "Фотографии книг"
