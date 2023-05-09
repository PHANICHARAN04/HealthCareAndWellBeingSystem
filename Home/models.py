from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_token=models.CharField(max_length=200)
    is_verified=models.BooleanField(default=False)


class Cardiology(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date=models.DateField()
    def str(self):
        return self.name
    
class Pediatrics(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date=models.DateField()
    def str(self):
        return self.name

class Gastroenterology(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date=models.DateField()
    def str(self):
        return self.name

class Psychology(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date=models.DateField()
    def str(self):
        return self.name
class Dermatology(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date=models.DateField()
    def str(self):
        return self.name


class BloodTest(models.Model):
    name=models.CharField(max_length=122)
    age=models.IntegerField()
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date=models.DateField()
    def str(self):
        return self.name


class CtScan(models.Model):
    name=models.CharField(max_length=122)
    age=models.IntegerField()
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date=models.DateField()
    def str(self):
        return self.name


class Kemotheraphy(models.Model):
    name=models.CharField(max_length=122)
    age=models.IntegerField()
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date=models.DateField()
    def str(self):
        return self.name


class XRay(models.Model):
    name=models.CharField(max_length=122)
    age=models.IntegerField()
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date=models.DateField()
    def str(self):
        return self.name

class Endoscopy(models.Model):
    name=models.CharField(max_length=122)
    age=models.IntegerField()
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date=models.DateField()
    def str(self):
        return self.name

class UrineTest(models.Model):
    name=models.CharField(max_length=122)
    age=models.IntegerField()
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date=models.DateField()
    def str(self):
        return self.name


class UltraSound(models.Model):
    name=models.CharField(max_length=122)
    age=models.IntegerField()
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date=models.DateField()
    def str(self):
        return self.name
    

class PulmonaryFuctionTest(models.Model):
    name=models.CharField(max_length=122)
    age=models.IntegerField()
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date=models.DateField()
    def str(self):
        return self.name