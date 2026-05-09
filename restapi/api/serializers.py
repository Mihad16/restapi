from rest_framework import serializers
from .models import Book




class Bookviews(serializers.ModelSerializer):
    class Meta :
        model = Book
        fields =[ 'id','title','book', 'date']















        