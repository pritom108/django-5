from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=70)
    roll=models.IntegerField()
    email=models.EmailField(max_length=255)
    city=models.CharField(max_length=70)


    def __str__(self):
        return self.name
        # return str(self.roll)

class Result(models.Model):
    stu_class= models.CharField(max_length=70)
    marks=models.IntegerField()

    def __str__(self):
        return self.stu_class

