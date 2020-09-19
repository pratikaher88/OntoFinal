from django import forms

from .models import UserInputFormModel

CHOICES=[('YES','YES'),
        ('NO','NO')]

class UserInputForm(forms.ModelForm):

    emergency_request = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = UserInputFormModel
        fields = '__all__'
