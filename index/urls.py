from django.urls import path
from index import views
urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    path('logout', views.logout, name='logout'),

]