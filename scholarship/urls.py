from django.urls import path
from . import views

app_name = 'scholarship'

urlpatterns = [  
    path('list/', views.list,name='list events'),
    path('add/', views.create, name='create_profile'),
    path('details/<currId>', views.details, name='user_details'),
    path('update/<currId>', views.update, name='update_details'),
    path('delete/<currId>', views.delete, name='delete_details')
]