from django.db import models


# # Create your models here.
class Workers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return "{}".format(self.get_full_name())

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
