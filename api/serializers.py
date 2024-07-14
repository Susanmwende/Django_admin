from rest_framework import serializers
from student.models import Student
from courses.models import Courses
from  teacher.models import Teacher
from classes.models import Classes
from classperiod.models import ClassPeriod

class StudentSerializer (serializers.ModelSerializer):
        class Meta:
              model= Student
              fields ="__all__"
class CoursesSerializer(serializers.ModelSerializer):
      class Meta:
            model = Courses
            fields = "_all_"
class  TeacherSerializer(serializers.ModelSerializer):
      class Meta:
            model= Teacher
            fields = "_all_"

class ClassesSerializer(serializers.ModelSerializer):
      class Meta:
            model = Classes
            fields = "_all_"
class ClassPeriodSerializer(serializers.ModelSerializer):
      class Meta:
            model = ClassPeriod
            fields = "_all_"