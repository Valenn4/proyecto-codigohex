from django import forms
from .models import DetectObject

class FormObject(forms.ModelForm):
    class Meta:
        model = DetectObject
        fields = ['imagen']