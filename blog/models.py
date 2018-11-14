from django.db import models
# Create your models here.
from django import forms

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('timestamp',)
class Employee(models.Model):
    name = models.CharField(max_length=20)
#class BlogPostForm(forms.Form):
#    title = forms.CharField(max_length = 150)
#    body = forms.CharField(
#        widget=forms.Textarea(attrs = {'rows':3,'col':60})
#    )
#    timestamp = forms.DateTimeField()