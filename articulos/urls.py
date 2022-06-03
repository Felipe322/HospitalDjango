from django.urls import path
from .views import Lista, comprar

app_name = 'articulos'

urlpatterns = [
    path('lista/', Lista.as_view(), name='lista'),
    path('comprar/<int:pk>', comprar, name='comprar'),

]
