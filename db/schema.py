from django.db import models

class usr(models.Model):
  e_mail = models.EmailField(max_length=64)
  password = models.CharField(max_length=64)
  status = models.IntegerField()
  picture = models.CharField(max_length=256)

class associaton(models.Model):
  name = models.CharField(max_length=64)
  e_mail = models.CharField(max_length=64)
  website = models.CharField(max_length=256)
  president = models.ForeignKey(usr, on_delete = models.CASCADE)
  usr = models.ManyToManyField(usr)

class meetings(models.Model):
  schedule = models.TimeField()
  place = models.CharField(max_length=256)
  private = models.IntegerField()
