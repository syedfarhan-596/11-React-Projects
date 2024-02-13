from django.db import models

class Items(models.Model):
    img = models.ImageField(upload_to='media')
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} {self.id}"
