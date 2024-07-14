from django.urls import path
from .views import StudentListView
from .views import CoursesListView
from .views import ClassesListView
from .views import TeacherListView
from .views import ClassPeriodListView


urlpatterns =[
    path('student/',StudentListView.as_view(), name = 'student_list_view'),
    path('courses/' ,CoursesListView.as_view(), name='courses_list_view'),
    path('classes/',ClassesListView.as_view(),name='classes_list_view'),
    path('teacher/',TeacherListView.as_view(),name='teacher_list_view'),
    path('classperiod/',ClassPeriodListView.as_view(),name='classperiod_list_view')

]
