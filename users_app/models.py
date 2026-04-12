from django.db import models

# Sirf User ka data yahan rahega
class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email