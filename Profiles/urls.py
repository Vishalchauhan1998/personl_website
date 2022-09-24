from django.urls import path
from . import views

urlpatterns = [
    path('', views.Profile, name='pro'),
    path('Profiles/<int:id>', views.profiles, name='profile'),
    #path(r'course_details/<course_id>', views.course_details, name = 'course_details')
    #path('Project/<int:id>', views.project_details, name='project_details')
]
