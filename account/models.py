from django.db import models
import random
from django.utils import timezone


def generate_salary():
    return random.randint(500, 1500)


class Todo(models.Model):
    name = models.TextField()

    def __str__(self):
        return "{}".format(self.name)


class Tester(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)


# # Create your models here.
class Workers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField()
    tester_list = models.ManyToManyField('Tester')
    description = models.TextField()
    salary = models.IntegerField(default=generate_salary)
    slug = models.SlugField(null=True, blank=True)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}".format(self.get_full_name())

    # def save(self, *args, **kwargs):
    #     super(Workers, self).save(*args, **kwargs)
    #     if not self.slug:
    #         self.slug = slugify("{} {} {}".format(
    #             self.first_name,
    #             self.last_name,
    #             self.company.name
    #         ))
    #     super(Workers, self).save(*args, **kwargs)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class Company(models.Model):
    name = models.CharField(max_length=255)
    job = models.ForeignKey('Job', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Job(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)


class Picture(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image/")

    def __str__(self):
        return "{}".format(self.image.name)


class Article(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)
