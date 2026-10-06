from django.db import models

# Create your models here.


class Employee(models.Model):
    empid=models.IntegerField(unique=True)
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)

    gender_choices=[

        ('male','Male'),('female','Female')

    ]

    gender=models.CharField(max_length=20,choices=gender_choices)

    joining_date=models.DateField()

    salary=models.IntegerField()
    designation=models.CharField(max_length=20)
    image=models.ImageField(upload_to="image",null=True)

