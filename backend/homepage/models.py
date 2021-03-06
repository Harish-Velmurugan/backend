from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User_Personal(models.Model):
    GENDER_CHOICES=[
        ('M','Male'),
        ('F','Female'),
        ('T','Other')
    ]
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,default='M',)
    dob = models.DateField(auto_now_add=True,blank=True, null=True)
    nationality=models.CharField(max_length=50)
    phone=PhoneNumberField()
    img=models.ImageField(upload_to = 'uploads/')
    pin = models.IntegerField(blank=True, null=True)

class User_Professional(models.Model):
    EXPERIENCE=[
        ('F','Fresher'),
        ('S','Student'),
        ('2','2 yr')
    ]
    qualification=models.CharField(max_length=50)
    specialization=models.CharField(max_length=50)
    domains=models.CharField(max_length=50)
    work_exp=models.CharField(max_length=2,choices=EXPERIENCE)

class bids(models.Model):
    pid = models.IntegerField()
    sid = models.IntegerField()
    uid = models.IntegerField()
    bids = models.IntegerField()

