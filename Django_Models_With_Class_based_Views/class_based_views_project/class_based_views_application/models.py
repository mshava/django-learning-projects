from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("class_based_views_application:detail", kwargs={'pk': self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    school = models.ForeignKey(School, related_name='students')
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
