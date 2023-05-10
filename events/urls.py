from django.urls import path, include
from . import views_workshop, views_lecture, views_competition, views_points

app_name = 'events'

urlpatterns = [  
                 
    path('workshop/list/', views_workshop.list,name='list_workshop'),
    path('workshop/add/', views_workshop.create, name='create_workshop'),
    path('workshop/details/<currId>', views_workshop.details, name='user_workshop'),
    path('workshop/update/<currId>', views_workshop.update, name='update_workshop'),
    path('workshop/delete/<currId>', views_workshop.delete, name='delete_workshop'),
    path('workshop/search', views_workshop.Search.as_view(), name="search"),
    path('workshop/filter/', views_workshop.filter, name='ws_filter'),
    
    path('lecture/list/', views_lecture.list,name='list_lecture'),
    path('lecture/add/', views_lecture.create, name='create_lecture'),
    path('lecture/details/<currId>', views_lecture.details, name='user_lecture'),
    path('lecture/update/<currId>', views_lecture.update, name='update_lecture'),
    path('lecture/delete/<currId>', views_lecture.delete, name='delete_lecture'),
    path('lecture/search', views_lecture.Search.as_view(), name="search"),
    
    path('competition/list/', views_competition.list,name='list_competition'),
    path('competition/add/', views_competition.create, name='create_competition'),
    path('competition/details/<currId>', views_competition.details, name='user_competition'),
    path('competition/update/<currId>', views_competition.update, name='update_competition'),
    path('competition/delete/<currId>', views_competition.delete, name='delete_competition'),
    path('competition/search', views_competition.Search.as_view(), name="search"),
    
    # path('certificate/create', views_points.CertificateViewSet.as_view({"get": "retrieve", "post": "create", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="certificate_add")
    path('certificate/create/', views_points.pointViewSet.as_view({'get': 'list'}), name="certificate_add"),
    path('certificate/list-all/', views_points.getCertificate, name="certificates_listall")
]   