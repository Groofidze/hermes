from django.contrib import admin
from books.models import Books, Photos


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ['author', 'name', 'management', 'made_in', 'year']
    ordering = ['name']


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('book',)
    fields = ['book', 'photo']
    ordering = ['book']

    def get_queryset(self, request):
        return Photos.objects.select_related("book").all()
