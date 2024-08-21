from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from  courses.models import Courses
from  classes.models import Classes
from teacher.models import Teacher
from classperiod.models import ClassPeriod
from .serializers import StudentSerializer
from .serializers import ClassesSerializer
from .serializers import CoursesSerializer
from .serializers import TeacherSerializer
from .serializers import ClassPeriodSerializer
from rest_framework.response import Response
from rest_framework.views import status

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        country = request.query_params.get("country")

        if first_name:
            students = students.filter(first_name=first_name)
        if country:
            students = students.filter(country=country)

        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id):
        student = Student.objects.get(id=id)
        class_id = request.data.get("class_id")
        self.add_student_to_class(student, class_id)
        return Response(status=status.HTTP_202_ACCEPTED)

    def add_student_to_class(self, student, class_id):
        class_instance = Classes.objects.get(id=class_id)
        student.classes.add(class_instance)

class CoursesListView(APIView):
    def get(self, request):
        courses = Courses.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CoursesDetailView(APIView):
    def get(self, request, id):
        course = Courses.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, id):
        course = Courses.objects.get(id=id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = Courses.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        course_id = request.data.get("course_id")
        class_id = request.data.get("class_id")
        self.assign_teacher_to_course(teacher, course_id)
        self.assign_teacher_to_class(teacher, class_id)
        return Response(status=status.HTTP_202_ACCEPTED)

    def assign_teacher_to_course(self, teacher, course_id):
        course = Courses.objects.get(id=course_id)
        teacher.courses.add(course)

    def assign_teacher_to_class(self, teacher, class_id):
        class_instance = Classes.objects.get(id=class_id)
        teacher.classes.add(class_instance)

class ClassesListView(APIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassesDetailView(APIView):
    def get(self, request, id):
        class_instance = Classes.objects.get(id=id)
        serializer = ClassesSerializer(class_instance)
        return Response(serializer.data)

    def put(self, request, id):
        class_instance = Classes.objects.get(id=id)
        serializer = ClassesSerializer(class_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        class_instance = Classes.objects.get(id=id)
        class_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClassPeriodListView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        teacher_id = request.data.get("teacher_id")
        course_id = request.data.get("course_id")
        day = request.data.get("day")
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")
        self.create_class_period(teacher_id, course_id, day, start_time, end_time)
        return Response(status=status.HTTP_202_ACCEPTED)

    def create_class_period(self, teacher_id, course_id, day, start_time, end_time):
        teacher = Teacher.objects.get(id=teacher_id)
        course = Courses.objects.get(id=course_id)
        class_period = ClassPeriod.objects.create(teacher=teacher, course=course, day=day, start_time=start_time, end_time=end_time)
        class_period.save()

class WeeklyTimetableView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data)