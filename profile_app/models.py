from django.db import models
from resumes_app.models import Resume
from django.contrib.auth.models import User


class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    wished_resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"