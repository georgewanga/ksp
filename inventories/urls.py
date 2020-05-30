from django.urls import path
from . import views


app_name = 'inventories'


urlpatterns = [
    path('create/', views.Create.as_view(), name='create'),
    path('<slug:slug>/update/', views.Update.as_view(), name='update'),
    path('<slug:slug>/delete/', views.Delete.as_view(), name='delete'),
    path('<slug:slug>/', views.Detail.as_view(), name='detail'),
    path('', views.List.as_view(), name='list'),
]
