from django.urls import path
from .views import main, catalogView, serviceDetailView

app_name = "main"

urlpatterns = [
    path('', main.as_view(), name="index"),
    path('Catalog/', catalogView.as_view(), name="catalog"),
    path('Service/<int:pk>', serviceDetailView.as_view(), name="service"),
]
