from django.db import models


# Create your models here.

class Services(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=20)
    malumotnoma = models.TextField()
    date = models.DateTimeField(auto_now=True)


class Type(models.Model):
    turi = models.CharField(max_length=30)

    def str(self):
        return self.turi


class Portfolio(models.Model):
    image = models.ImageField(upload_to='media')
    ism = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    client = models.CharField(max_length=20)
    date = models.DateField()
    link = models.CharField(max_length=40)


class Kasbi(models.Model):
    hodim = models.CharField(max_length=50)

    def str(self):
        return self.hodim


class Team(models.Model):
    name = models.CharField(max_length=30)
    kasb = models.ForeignKey(Kasbi, on_delete=models.CASCADE)
    malumotnoma = models.TextField()
    img = models.ImageField(upload_to="media")
    twit = models.CharField(max_length=40)
    face = models.CharField(max_length=40)
    inst = models.CharField(max_length=40)
    tele = models.CharField(max_length=40)
    date = models.DateTimeField()


class Ariza(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

class Subcrise(models.Model):
    subcrise = models.CharField(max_length=50)


class SubPort(models.Model):
    subcriseportfolio = models.CharField(max_length=50)