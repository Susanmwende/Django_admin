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
    def get (self,request):
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)
         
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_CREATED)
class StudentDetailView(APIView):
    def get(self,request, id):
        student= Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def put(self,request,id):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        student=Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
class  CoursesListView(APIView):
      def get(self,request):
        courses= Courses.objects.all()
        serializer = CourseSerializer(courses,many=True)
        return Response(serializer.data)
      def post(self,request):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_CREATED)

class CoursesDetailView(APIView):
    def get(self,request, id):
        courses= Courses.objects.get(id=id)
        serializer = CoursesSerializer(courses)
        return Response(serializer.data)
    def put(self,request,id):
        courses=Courses.objects.get(id=id)
        serializer=CoursesSerializer(courses,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        courses=Courses.objects.get(id=id)
        courses.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
class TeacherListView(APIView):
    def get (self,request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_CREATED)
class TeacherDetailView(APIView):
    def get(self,request, id):
        teacher= Teacher.objects.get(id=id)
        serializer = CoursesSerializer(teacher)
        return Response(serializer.data)
    def put(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer=CoursesSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        teacher=Courses.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class  ClassesListView (APIView):
    def get (self,request):
        classes = Classes.objects.all()
        serializer =  ClassesSerializer(classes,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_CREATED)
class ClassesDetailView(APIView):
    def get(self,request, id):
        classes= Classes.objects.get(id=id)
        serializer = ClassesSerializer(classes)
        return Response(serializer.data)
    def put(self,request,id):
        classes=Classes.objects.get(id=id)
        serializer=ClassesSerializer(classes,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        classes=Classes.objects.get(id=id)
        classes.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class ClassPeriodListView(APIView):
    def get (self,request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_CREATED)
class ClassPeriodDetailView(APIView):
    def get(self,request, id):
        classperiod= ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod)
        return Response(serializer.data)
    def put(self,request,id):
        classperiod=ClassPeriod.objects.get(id=id)
        serializer=ClassPeriodSerializer(classperiod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        classperiod=ClassPeriod.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
