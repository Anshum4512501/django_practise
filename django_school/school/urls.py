from django.urls import path
from .views import CreateSchool,SchoolList,SchoolDetailView,CreateSchoolStudent

app_name = 'school'


urlpatterns = [
    path('',CreateSchool.as_view(),name="create_school"),
    path('school_list/',SchoolList.as_view(),name="school_list"),
    path('school_list/<slug:pk>',SchoolDetailView.as_view(),name="detail"),
     path('school/newstudent',CreateSchoolStudent.as_view(),name="create_student"),
]