from django.urls import path
from .views import StudentListView
from .views import CoursesListView
from .views import ClassesListView
from .views import TeacherListView
from .views import ClassPeriodListView
from .views import StudentDetailView
from .views import TeacherDetailView
from .views import CoursesDetailView
# from .views import ClassPeriodDetailView
from .views import ClassesDetailView
from .views import WeeklyTimetableView







urlpatterns = [
    path('student/', StudentListView.as_view(), name='student_list_view'),
    path('courses/', CoursesListView.as_view(), name='courses_list_view'),
    path('classes/', ClassesListView.as_view(), name='classes_list_view'),
    path('teacher/', TeacherListView.as_view(), name='teacher_list_view'),
    path('classperiod/', ClassPeriodListView.as_view(), name='classperiod_list_view'),
    path('student/<int:id>/', StudentDetailView.as_view(), name='student_detail_view'),
    path('teacher/<int:id>/', TeacherDetailView.as_view(), name='teacher_detail_view'),
    path('classes/<int:id>/', ClassesDetailView.as_view(), name='classes_detail_view'),
    # path('classperiod/<int:id>/', ClassPeriodDetailView.as_view(), name='classperiod_detail_view'),
    path('courses/<int:id>/', CoursesDetailView.as_view(), name='courses_detail_view'),
    path('student/<int:id>/add_to_class/', StudentDetailView.as_view(), name='add_student_to_class'),  # Add student to class
    path('teacher/<int:id>/assign/', TeacherDetailView.as_view(), name='assign_teacher'),  # Assign teacher to course and class
    path('classperiod/create/', ClassPeriodListView.as_view(), name='create_class_period'),  # Create class period
    path('timetable/', WeeklyTimetableView.as_view(), name='weekly_timetable'),  # Get weekly timetable
]