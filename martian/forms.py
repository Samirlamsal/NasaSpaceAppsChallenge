from .models import entry
from django import forms
from django.forms import ModelForm


class detail(ModelForm):
    class Meta:
        model = entry
        fields=['Name','Age','Country','Email','Destination','Purpose']
