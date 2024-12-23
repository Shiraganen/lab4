from django import forms
from .models import Athlete

class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['first_name', 'last_name', 'age', 'sport', 'country']

    def clean_age(self):
        age = self.cleaned_data['age']
        if age <= 0:
            raise forms.ValidationError("Age must be a positive number.")
        return age
