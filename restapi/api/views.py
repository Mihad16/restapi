from rest_framework import viewsets
from .models import Book

from .serializers import Bookviews


# Create your views here.

class Booksetviews(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Bookviews