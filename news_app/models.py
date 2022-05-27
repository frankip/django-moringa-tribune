from django.db import models

from django.shortcuts import get_object_or_404

# Create your models here.

class Articles(models.Model):
    editor = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    @classmethod
    def fetch_single_article(cls, article_id):
        return get_object_or_404(cls, id=article_id)