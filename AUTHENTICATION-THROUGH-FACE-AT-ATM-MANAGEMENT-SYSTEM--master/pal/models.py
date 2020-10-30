from django.db import models

# Create your models here.
class users(models.Model):
    username=models.CharField(max_length=100, primary_key=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    gender=(
        ('M','MALE'),
        ('F','FEMALE'),
    )
    pin=models.IntegerField()
    Gender=models.CharField(max_length=1,choices=gender)
    img= models.ImageField(upload_to='pics')
    phone=models.IntegerField()
    mail=models.CharField(max_length=100)
    add=models.CharField(max_length=100)
    dob=models.DateField()
    

class amount(models.Model):
    username=models.ForeignKey(users, on_delete=models.CASCADE)
    balance=models.IntegerField()