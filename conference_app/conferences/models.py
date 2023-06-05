from django.db import models


# Create your models here.
class Conference(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100)

    picture = models.ImageField(null = True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now_add=True)


