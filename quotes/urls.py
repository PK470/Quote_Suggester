from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quotes import views


router = DefaultRouter()
router.register('quote',  views.QuoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

