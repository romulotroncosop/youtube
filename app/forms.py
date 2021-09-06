from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms.models import ModelForm
from .models import Search,Result

class SearchForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs= {"class":"form-control mt-5 rounded-pill","placeholder":"Search u video"}),label=False)

    class Meta:
        model = Search
        fields = '__all__'
        labels = ''

class ResultForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = '__all__'
