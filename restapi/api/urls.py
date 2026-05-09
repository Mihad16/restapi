from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Booksetviews



router = DefaultRouter()
router.register('books', Booksetviews)

urlpatterns = [
    path('', include(router.urls)),
]