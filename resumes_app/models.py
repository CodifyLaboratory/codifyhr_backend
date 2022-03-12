from django.db import models

class Resume(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    image =  models.ImageField(null=True, blank=True, upload_to="images/resumes_image")
    comment = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    category = models.ManyToManyField('categories_app.Category')

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.surname}"
