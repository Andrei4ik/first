from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=40 ,blank=False ,unique=True)
    description=models.TextField(max_length=500 ,blank=True)
    price=models.DecimalField(default=0 ,max_digits=15, decimal_places=2)
    published=models.DateField(default="1999-01-01")
    is_published=models.BooleanField(default=False)
    cover=models.ImageField(upload_to='covers/',default = "1482881197192578721.jpg")
    def __str__(self):
        return self.title
