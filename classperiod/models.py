from django.db import models



class ClassPeriod (models.Model):
    class_starttime = models.TimeField()
    class_endtime = models.TimeField()
    class_course = models.CharField(max_length=50)
    class_classroom = models.CharField(max_length=20)
    class_dayofweek= models.CharField(max_length=20)
   

def __str__(self):
    return f"{self.class_startime} {self.class_endtime}"

# Create your mols hls here.
