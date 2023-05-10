from django.urls import path, include
from . import views_student, views_promoter, views_faculty

app_name = 'users'

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('google/', views_student.GoogleLogin.as_view(), name='google_login'),
    
    
    path('student/list/', views_student.listDetails,name='list users'),
    
    path('student/add/', views_student.createProfile, name='create_profile'),
    path('student/details/', views_student.details, name='user_details'),
    path('student/updateDetails/', views_student.updateDetails, name='update_details'),
    path('student/deleteDetails/', views_student.deleteDetails, name='delete_details'),
    path('student/addActivity/', views_student.addActivitypts, name='add_activitypoints'),
    
    path('promoter/list/', views_promoter.listDetails,name='list users'),
    
    path('promoter/add/', views_promoter.createProfile, name='create_profile'),
    path('promoter/details/', views_promoter.details, name='user_details'),
    path('promoter/updateDetails/', views_promoter.updateDetails, name='update_details'),
    path('promoter/deleteDetails/', views_promoter.deleteDetails, name='delete_details'),
    
    
    path('faculty/list/', views_faculty.listDetails,name='list users'),
    
    path('faculty/add/', views_faculty.createProfile, name='create_profile'),
    path('faculty/details/', views_faculty.details, name='user_details'),
    path('faculty/updateDetails/', views_faculty.updateDetails, name='update_details'),
    path('faculty/deleteDetails/', views_faculty.deleteDetails, name='delete_details')
]