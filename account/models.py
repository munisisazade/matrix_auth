from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to='picture/', null=True, blank=True)

    def get_image(self):
        if self.profile_picture:
            return self.profile_picture.url
        else:
            return None

    def __str__(self):
        return "{}".format(self.user.get_full_name())
