from django.db import models

class Partners(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="images/partners")

    def __str__(self):
        return f"{self.title}"