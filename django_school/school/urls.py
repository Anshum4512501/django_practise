from django.urls import path
from .views import (CreateSchool,SchoolList,SchoolDetailView,
CreateSchoolStudent,SchoolDeleteView,HomePage,SchoolUpdateView,SchoolStudentList,SchoolStudentDetail)

app_name = 'school'


urlpatterns = [
    path('',HomePage.as_view(),name="home"),
    path('newschool/',CreateSchool.as_view(),name="create_school"),
    path('school_list/',SchoolList.as_view(),name="school_list"),
    path('school_list/<slug:pk>',SchoolDetailView.as_view(),name="detail"),
    path('school/newstudent',CreateSchoolStudent.as_view(),name="create_student"),
     path('school/delete/<slug:pk>',SchoolDeleteView.as_view(),name="delete"),
     path('school_update/<slug:pk>',SchoolUpdateView.as_view(),name="update"),
    path('student_list/',SchoolStudentList.as_view(),name="school_student_list"),
    path('student_detail/<slug:pk>',SchoolStudentDetail.as_view(),name="student_detail"),
]