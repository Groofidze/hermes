from django.contrib import admin
from books.models import Books, ChapterBooks, Photos


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ['author', 'name', 'chapter', 'price', 'management', 'from_made_in', 'made_in', 'year', 'status',
              'date_active', 'comment']
    ordering = ['name']

    def get_queryset(self, request):
        return Books.objects.select_related("chapter").all()


@admin.register(ChapterBooks)
class ChapterBooksAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ['name', 'tag_alib']
    ordering = ['name']


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('book',)
    fields = ['book', 'photo']
    ordering = ['book']

    def get_queryset(self, request):
        return Books.objects.select_related("book").all()
