from django.db import models

class Books(models.Model):
    author = models.CharField(verbose_name="Автор", max_length=128)
    name = models.CharField(verbose_name="Название книги", max_length=128)
    made_in = models.CharField(verbose_name="Издательство", max_length=64, blank=True, null=True)
    year = models.PositiveIntegerField(verbose_name="Год выпуска", blank=True, null=True)
    management = models.PositiveIntegerField(verbose_name="Номер коробки, где лежит книга")

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
