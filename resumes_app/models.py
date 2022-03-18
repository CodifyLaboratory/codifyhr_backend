from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to="images/pdf_files")
    category = models.ManyToManyField('Category')

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.surname}"


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wished_resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.wished_resume}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Partners(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="images/partners")

    def __str__(self):
        return f"{self.title}"
