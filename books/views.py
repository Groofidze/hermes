from rest_framework import viewsets, permissions
from books.models import Books, Photos
from books.serializers import BooksSerializer, PhotosSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticated]


class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
    permission_classes = [permissions.IsAuthenticated]
