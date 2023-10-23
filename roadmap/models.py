from django.db import models
from django.utils.text import slugify


class Exam(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=100)
    online = models.BooleanField()
    free = models.BooleanField()
    link = models.URLField()

    def __str__(self):
        return self.title


class EducationEstablishment(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name


class RoadMap(models.Model):
    current_level = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=1000)
    exams = models.ManyToManyField(Exam)
    courses = models.ManyToManyField(Course)
    educationEstablishments = models.ManyToManyField(EducationEstablishment)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.current_level)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.current_level
