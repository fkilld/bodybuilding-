from django.db import models
from tinymce import HTMLField
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.fields import DateField


# Create your models here.
class Category(models.Model):
    TYPE = (
        ('Body Building', 'Body Building'),
        ('Aerobic', 'Aerobic'),
        ('Weight Lifting', 'Weight Lifting'),
        ('Yoga', 'Yoga'),
    )
    category = models.CharField(max_length=100, choices=TYPE)

    def __str__(self):
        return self.category


class Exercise(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = HTMLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exercise_detail', kwargs={
            'exercise_id': self.id
        })


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, null=True, upload_to='images')

    def __str__(self):
        return self.user.username


class Workout(models.Model):
    name = models.CharField(max_length=100)
    STATUS = (
        ('In progress', 'In progress'),
        ('Finished', 'Finished')
    )

    member = models.ForeignKey(Member, null=True, blank=True, on_delete=models.CASCADE)
    date_of_working = models.DateField()
    exercise = models.ManyToManyField(Exercise)
    status = models.CharField(max_length=50, null=True, blank=True, choices=STATUS)

    def __str__(self):
        return self.name
