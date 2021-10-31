from django.db import models

# Create your models here.
class Advisor(models.Model):
    # def nameFile(instance, filename):
    #     return '/'.join(['images', str(instance.adName), filename])
    adID = models.AutoField(primary_key=True)
    adName = models.CharField(max_length=20)
    adPhoto = models.ImageField(upload_to='advisor', default='')

    class Meta:
        db_table = "Advisor"

class User(models.Model):
    usrID = models.AutoField(primary_key=True)
    usrName = models.CharField(max_length=20)
    usrEmail = models.CharField(max_length=20)
    usrPassword = models.CharField(max_length=20)

    class Meta:
        db_table = "User"

class Booking(models.Model):
    bookID = models.AutoField(primary_key=True)
    bookAdID = models.IntegerField()
    bookUsrID = models.IntegerField(default=0)
    bookAdName = models.CharField(max_length=20)
    bookAdPhoto = models.ImageField(upload_to='booking', default='')
    bookTime = models.DateTimeField()

    class Meta:
        db_table = "Booking"

