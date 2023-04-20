from django.db import models

# Create your models here.
class Student(models.model):
    Firstname=models.CharField(max_length=200)
    Lastname=models.CharField(max_length=200)
    contact=models.CharField(max_length=20)
    Nin=models.CharField(max_length=30)
    Photo=models.Imagefield(upload_to ="uploads/")
    GENDER_CHOICES =[('MALE',"MALE"),
    ("FEMALE", "FEMALE"),]
    GENDER =models.CharField (
        max_length=6,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    DOB = models.DateField()
