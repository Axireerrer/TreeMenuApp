from django.urls import path
from Menu import views

app_name = 'menu'

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
]
