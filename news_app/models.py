from django.db import models

# Create your models here.

class Articles(models.Model):
    editor = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title