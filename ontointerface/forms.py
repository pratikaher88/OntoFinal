from django import forms

from .models import UserInputFormModel

class UserInputForm(forms.ModelForm):

    class Meta:
        model = UserInputFormModel
        fields = '__all__'