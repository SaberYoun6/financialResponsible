from django.db import models

import datetime 

from django.utils import timezone 

# Create your models here.

class Goals(models.Model):
   question_text= models.CharField(max_length=400)
   pub_date = models.DateTimeField('date goal was set')
   def  was_published_recently(self):
      return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
   def __str__(self):
      return self.question_text
class Choices(models.Model):
  question = models.ForeignKey(Goals, on_delete=models.CASCADE)
  budget   = models.FloatField(default=1000)
  hal      = models.BooleanField(False) 
  
  
  def __str__(self):
      return self.budget

