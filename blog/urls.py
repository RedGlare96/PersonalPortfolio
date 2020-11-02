from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('readblog/<int:blog_id>/', views.blogmain, name='blogmain')
]
