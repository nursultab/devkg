from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logos/')
    description = models.TextField()
    telegram = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='Jobs')
    position = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

class Event(models.Model):
    job= models.ForeignKey(Job, on_delete=models.CASCADE,related_name='Events')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateTimeField()
    website = models.URLField()
    registration = models.URLField()
    description = models.TextField()
    image = models.ImageField()

class Video(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE,related_name='Videos')
    date = models.DateTimeField()
    image = models.ImageField()
    video = models.FileField()