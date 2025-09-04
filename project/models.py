from django.db import models
class register(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    op = models.CharField(max_length=50)
    address=models.CharField(max_length=500)
    cw=models.CharField(max_length=200)
    aadhar=models.CharField(max_length=12)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    pin=models.IntegerField()
    profimage = models.ImageField(upload_to='images/')



    class Meta:
        db_table = "register"

class service(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    uservice = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    form = models.URLField()

    class Meta:
        db_table = "service"

class admin(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)

    class Meta:
        db_table = "admin"