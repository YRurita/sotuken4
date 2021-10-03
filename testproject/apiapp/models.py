from django.db import models

# 以下を追加
class GridItem(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=128,unique=True)
    picture = models.ImageField(upload_to='apiapp\static\pic_sample')

class person_in_the_room(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=128,unique=True)

class num_of_people(models.Model):
    num = models.IntegerField()
    

