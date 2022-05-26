from dataclasses import field
from django.forms import forms, ModelForm

from news_app.models import Articles

class ArticleForms(ModelForm):
    
    # editor = forms.CharField(att)
    
    class Meta:
        model = Articles
        fields = ('editor', 'title', 'text',)