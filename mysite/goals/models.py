from django.db import models

# Create your models here.

class Goals(models.Model):
   question_text= models.CharField(max_length=400)
   pub_date = models.DateTimeField('date goal was set')
class Choices(models.Model):
  question = models.ForeignKey(Goals, on_delete=models.CASCADE)
  choice_bool = models.BooleanField(False)

