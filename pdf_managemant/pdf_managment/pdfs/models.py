from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PDF(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='pdfs/')
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    