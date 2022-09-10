from rest_framework import viewsets, permissions
from books.models import Books, ChapterBooks, Photos
from books.serializers import BooksSerializer, ChapterBooksSerializer, PhotosSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChapterBooksViewSet(viewsets.ModelViewSet):
    queryset = ChapterBooks.objects.all()
    serializer_class = ChapterBooksSerializer
    permission_classes = [permissions.IsAuthenticated]


class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
    permission_classes = [permissions.IsAuthenticated]
