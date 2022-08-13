from django.urls import path
from .views import home, form_producto, form_mod_producto

urlpatterns = [
    path('', home, name="home"),
    path('form-producto', form_producto, name="form_producto"),
    path('form-mod-producto/<id>', form_mod_producto, name="form_mod_producto"),
]