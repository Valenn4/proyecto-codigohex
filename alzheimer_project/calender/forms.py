from django import forms
from .models import Activity, Action, Game, Music


class FormAction(forms.ModelForm):
    class Meta:
        model = Action
        fields = '__all__'

class FormMusic(forms.ModelForm):
    class Meta:
        model = Music
        fields = '__all__'

class FormGame(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

class FormActivity(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['date', 'time']