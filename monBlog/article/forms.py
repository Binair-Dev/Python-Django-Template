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

class Update_article_form(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'content']

class SearchForm(forms.Form):
    query = forms.CharField(label='Recherche', max_length=100)