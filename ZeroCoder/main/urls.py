from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='first'),
    path('test', views.test, name='second'),
    path('page', views.page, name='third'),
    path('leaf', views.leaf, name='fourth')
]