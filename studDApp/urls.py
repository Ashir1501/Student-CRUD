from django.urls import path
from . import views
urlpatterns = [
    path('', views.list_view, name='list_view'),
    path('create/',views.create, name='create_new'),
    path('update/<int:pk>',views.update_info, name='update_list'),
    path('delete/<int:pk>', views.delete_info, name='delete_info'),
]