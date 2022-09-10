from rest_framework import serializers

from books.models import Books, ChapterBooks, Photos


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ["author", "name", "chapter", "price", "management", "from_made_in", "made_in", "year", "pages",
                  "status", "date_active", "comment"]


class ChapterBooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChapterBooks
        fields = ["name", "tag_alib"]


class PhotosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photos
        fields = ["book", "photo"]
