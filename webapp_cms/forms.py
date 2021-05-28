from django import forms
from webapp.models import *

class UserRateForm(forms.ModelForm):
    class Meta:
        model = UserHourlyRate
        fields = '__all__'
        