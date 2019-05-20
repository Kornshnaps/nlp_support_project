from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime, date, time

class TaskPreds(models.Model):
    task = models.CharField(max_length=500)
    #answer = models.IntegerField()
    predCat = models.CharField(max_length=50,default=' ')
    date = models.DateTimeField(default = datetime.now())
    num = models.IntegerField(default=0)
    recruit = models.CharField(max_length=40,default=' ')
    #def Taskpreds(self):
     #   self.date = datetime.datetime.now()
    #def __str__(self):
     #   return self.task

    def as_json(self):
        return {'num':self.num,
            'date':self.date,
            'task':self.task,
            'predCat':self.predCat,#.encode('utf-8'),
            'recruit' :self.recruit
        }