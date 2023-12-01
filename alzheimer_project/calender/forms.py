from django import forms
from .models import Activity, Object, Action, Game, Music


class FormObject(forms.ModelForm):
    class Meta:
        model = Object
        fields = '__all__'

class FormAction(forms.ModelForm):
    class Meta:
        model = Action
        fields = '__all__'

class FormMusic(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['name_music', 'id_music', 'category_music']

class FormGame(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

class FormActivity(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['date', 'time']
