from django import forms
from .models import Human

class NewHumanForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = '__all__'
