from django.urls import path
from .views import home, form_producto

urlpatterns = [
    path('', home, name="home"),
    path('form-producto', form_producto, name="form_producto")
]