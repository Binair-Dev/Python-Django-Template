from django import forms
from django.forms import ModelForm
from .models import Article

class Create_article_form(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'