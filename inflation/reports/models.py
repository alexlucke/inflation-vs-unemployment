from django.db import models
from datetime import datetime

# Create your models here.
class Inflation(models.Model):
  rate = models.FloatField(null=True)
  date = models.DateField()
  
  def __str__(self):
    return "{} on {}".format(self.rate, self.date)
  
  def get_absolute_url(self):
    return "/inflation/{}/{}/".format( datetime.strftime(self.date, "%Y/%m"))


class Unemployment(models.Model):
  rate = models.FloatField(null=True)
  date = models.DateField()
  
  def __str__(self):
    return "{} on {}".format(self.rate, self.date)
  
  def get_absolute_url(self):
    return "/unemployment/{}".format(self.date)

class Interest(models.Model):
  rate = models.FloatField(null=True)
  date = models.DateField()
  
  def __str__(self):
    return "{} on {}".format(self.rate, self.date)
  
  def get_absolute_url(self):
    return "/interest/{}".format(self.date)