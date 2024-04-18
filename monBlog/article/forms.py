from django import forms
from django.forms import ModelForm
from .models import Article, Author

class Create_article_form(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class Create_author_form(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'